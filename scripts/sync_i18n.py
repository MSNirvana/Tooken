#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
EN_DIR = DOCS_DIR / "en"
JA_DIR = DOCS_DIR / "ja"
KO_DIR = DOCS_DIR / "ko"
GLOSSARY_PATH = ROOT / "scripts" / "i18n_glossary.json"

# Chinese source pages currently maintained by authors.
ZH_PAGES = [
    "index.mdx",
    "module-1-platform-overview.mdx",
    "module-2-quickstart.mdx",
    "module-3-models-routing.mdx",
    "module-4-payment-settlement.mdx",
    "module-5-agent-economy.mdx",
    "module-5-agent-wallet-identity.mdx",
    "module-5-agent-routing-budget.mdx",
    "module-5-erc8183-roadmap.mdx",
    "module-5-multi-agent-economy.mdx",
    "module-5-web4-vision.mdx",
    "api-reference.mdx",
    "api-authentication.mdx",
    "api-chat-completions.mdx",
    "api-messages.mdx",
    "api-routing.mdx",
    "api-errors-rate-limits.mdx",
    "api-openapi.mdx",
    "changelog.mdx",
    "faq-troubleshooting.mdx",
    "brand-assets.mdx",
    "translation-quality.mdx",
]

TITLE_MAP = {
    "Tooken 平台文档": "Tooken Documentation",
    "模块一：平台简介": "Module 1: Platform Overview",
    "模块二：快速上手": "Module 2: Quick Start",
    "模块三：模型与路由": "Module 3: Models and Routing",
    "模块四：支付与结算": "Module 4: Payment and Settlement",
    "模块五：Agent 经济层 · AGI × Web4": "Module 5: Agent Economy · AGI x Web4",
    "5.1 Agent 钱包与身份": "5.1 Agent Wallet and Identity",
    "5.2 Agent 自动路由购买 Token": "5.2 Agent Auto-routing and Token Budgeting",
    "5.3 ERC-8183 合约层（路线图）": "5.3 ERC-8183 Contract Layer (Roadmap)",
    "5.4 多 Agent 协作经济": "5.4 Multi-Agent Collaborative Economy",
    "5.5 AGI 出现在 Web4 的愿景": "5.5 Vision: AGI in Web4",
    "API 参考总览": "API Reference Overview",
    "6.1 认证": "6.1 Authentication",
    "6.2 Chat Completions（OpenAI 兼容）": "6.2 Chat Completions (OpenAI Compatible)",
    "6.3 Messages（Claude 兼容）": "6.3 Messages (Claude Compatible)",
    "6.4 路由 API（Auto 模式）": "6.4 Routing API (Auto Mode)",
    "6.5 错误码与限流说明": "6.5 Errors and Rate Limits",
    "OpenAPI 说明": "OpenAPI Guide",
    "更新日志": "Changelog",
    "常见问题与排查": "FAQ and Troubleshooting",
    "品牌与资源": "Brand and Assets",
}

LOCALE_TITLE_MAP = {
    "en": TITLE_MAP,
    "ja": {
        "Tooken 平台文档": "Tooken ドキュメント",
    },
    "ko": {
        "Tooken 平台文档": "Tooken 문서",
    },
}

DEFAULT_TERMS_TO_PRESERVE = [
    "Tooken",
    "x402",
    "Agent",
    "AGI",
    "Web4",
    "ERC-8183",
    "OpenAPI",
    "Credits",
    "API",
    "DID",
]


def run_git_changed_files(since_ref: str, until_ref: str):
    cmd = [
        "git",
        "diff",
        "--name-only",
        since_ref,
        until_ref,
        "--",
        "docs/*.mdx",
    ]
    out = subprocess.check_output(cmd, cwd=ROOT, text=True).strip()
    return [line.strip() for line in out.splitlines() if line.strip()]


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw, body = parts
    fm_lines = raw.splitlines()[1:]
    fm = {}
    for line in fm_lines:
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body


def normalize_scalar(value: str):
    """
    Best-effort unquote/unescape for previously over-escaped frontmatter values.
    """
    s = value.strip()
    # Repeatedly try JSON decode for values like "\"\\\"Title\\\"\"".
    for _ in range(4):
        if len(s) >= 2 and ((s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'")):
            try:
                # json expects double-quoted strings; for single quotes, fallback strip.
                if s[0] == "'":
                    s = s[1:-1]
                else:
                    s = json.loads(s)
            except Exception:
                s = s[1:-1]
        else:
            break
    return s


def strip_fallback_banner(body: str):
    """
    Remove stacked fallback notices at the beginning of locale files.
    """
    lines = body.splitlines()
    i = 0
    n = len(lines)

    # Skip leading blank lines
    while i < n and not lines[i].strip():
        i += 1

    removed_any = False
    while i + 1 < n:
        l1 = lines[i].strip()
        l2 = lines[i + 1].strip()
        if l1.startswith("> This page is synced automatically from the Chinese source and awaits full ") and \
           l1.endswith(" translation.") and \
           l2 == "> To enable AI translation, configure `OPENAI_API_KEY` in GitHub repository secrets.":
            removed_any = True
            i += 2
            while i < n and not lines[i].strip():
                i += 1
            continue
        break

    if removed_any:
        remaining = lines[i:]
        return ("\n".join(remaining)).lstrip("\n")
    return body


def split_sections(body: str):
    """
    Split markdown body into sections by heading boundaries.
    Returns list[(heading_or_preamble, content)].
    """
    lines = body.splitlines(keepends=True)
    sections = []
    current_key = "__preamble__"
    current_lines = []
    heading_re = re.compile(r"^\s{0,3}#{1,6}\s+")

    for line in lines:
        if heading_re.match(line) and current_lines:
            sections.append((current_key, "".join(current_lines)))
            current_key = line.strip()
            current_lines = [line]
        elif heading_re.match(line) and not current_lines:
            current_key = line.strip()
            current_lines.append(line)
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_key, "".join(current_lines)))
    return sections


def sections_to_body(sections):
    return "".join(content for _, content in sections)


def build_frontmatter(fm: dict):
    lines = ["---"]
    for k, v in fm.items():
        value = normalize_scalar(str(v))
        # Quote scalar values to keep YAML safe for colons and symbols.
        lines.append(f"{k}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def load_glossary():
    if not GLOSSARY_PATH.exists():
        return {
            "preserve_terms": DEFAULT_TERMS_TO_PRESERVE,
            "locale_style": {},
        }
    try:
        return json.loads(GLOSSARY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {
            "preserve_terms": DEFAULT_TERMS_TO_PRESERVE,
            "locale_style": {},
        }


def translate_with_openai(
    content: str,
    api_key: str,
    model: str,
    target_language: str,
    base_url: str,
    terms_to_preserve,
    locale_style_prompt: str,
):
    lang_name = {
        "en": "English",
        "ja": "Japanese",
        "ko": "Korean",
    }.get(target_language, "English")
    terms = ", ".join(terms_to_preserve)
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    f"You are a technical translator. Translate Simplified Chinese markdown/MDX into natural {lang_name}. "
                    "Preserve links, code blocks, table structure, frontmatter keys, inline code, and file paths exactly. "
                    "Do not add or remove sections. Keep heading hierarchy exactly the same. "
                    f"Never translate these terms: {terms}."
                    f" {locale_style_prompt}".strip()
                ),
            },
            {"role": "user", "content": content},
        ],
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body["choices"][0]["message"]["content"]


def apply_locale_term_map(text: str, locale: str, locale_term_map: dict):
    mappings = locale_term_map.get(locale, {}) if isinstance(locale_term_map, dict) else {}
    if not mappings:
        return text
    # Replace longer keys first to avoid partial overlaps.
    for src, dst in sorted(mappings.items(), key=lambda kv: len(kv[0]), reverse=True):
        text = text.replace(src, dst)
    return text


def fallback_sync(content: str, target_language: str):
    language_hint = {
        "en": "English",
        "ja": "Japanese",
        "ko": "Korean",
    }.get(target_language, target_language)
    banner = (
        f"> This page is synced automatically from the Chinese source and awaits full {language_hint} translation.\n"
        "> To enable AI translation, configure `OPENAI_API_KEY` in GitHub repository secrets.\n\n"
    )
    return banner + content


def normalize_title(title: str, locale: str):
    return LOCALE_TITLE_MAP.get(locale, {}).get(title, title)


def map_to_locale_path(zh_rel: str, locale: str):
    return str(Path("docs") / locale / Path(zh_rel).name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since-ref", default="")
    parser.add_argument("--until-ref", default="HEAD")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--model", default="gpt-4.1-mini")
    parser.add_argument("--locales", default="en,ja,ko")
    parser.add_argument("--force-fallback", action="store_true")
    parser.add_argument("--sanitize-only", action="store_true")
    parser.add_argument("--require-api-key", action="store_true")
    args = parser.parse_args()
    locales = [x.strip() for x in args.locales.split(",") if x.strip()]

    # Supports OpenAI-compatible providers via base_url override.
    api_key = (
        os.getenv("TRANSLATION_API_KEY", "").strip()
        or os.getenv("OPENAI_API_KEY", "").strip()
    )
    base_url = (
        os.getenv("TRANSLATION_BASE_URL", "").strip()
        or os.getenv("OPENAI_BASE_URL", "").strip()
        or "https://api.openai.com/v1"
    )
    glossary = load_glossary()
    terms_to_preserve = glossary.get("preserve_terms", DEFAULT_TERMS_TO_PRESERVE)
    locale_style = glossary.get("locale_style", {})
    locale_term_map = glossary.get("locale_term_map", {})
    changed = set()
    if args.require_api_key and not api_key and not args.sanitize_only:
        raise SystemExit(
            "Missing translation API key. Set TRANSLATION_API_KEY or OPENAI_API_KEY before syncing."
        )
    if args.all or not args.since_ref:
        changed = {str(Path("docs") / p) for p in ZH_PAGES}
    else:
        for f in run_git_changed_files(args.since_ref, args.until_ref):
            if Path(f).name in ZH_PAGES:
                changed.add(f)

    EN_DIR.mkdir(parents=True, exist_ok=True)
    JA_DIR.mkdir(parents=True, exist_ok=True)
    KO_DIR.mkdir(parents=True, exist_ok=True)
    updated = []

    for zh_rel in sorted(changed):
        zh_path = ROOT / zh_rel
        if not zh_path.exists():
            continue
        text = zh_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        body = strip_fallback_banner(body)
        zh_sections = split_sections(body)
        for locale in locales:
            locale_fm = dict(fm)
            if "title" in locale_fm:
                locale_fm["title"] = normalize_title(locale_fm["title"], locale)

            locale_style_prompt = locale_style.get(locale, "")
            locale_path = ROOT / map_to_locale_path(zh_rel, locale)
            existing_sections = {}
            if locale_path.exists():
                old_text = locale_path.read_text(encoding="utf-8")
                _old_fm, old_body = parse_frontmatter(old_text)
                if args.sanitize_only:
                    clean_old = strip_fallback_banner(old_body)
                    # Normalize title/frontmatter escaping artifacts only.
                    out_text = build_frontmatter(locale_fm) + "\n\n" + clean_old
                    locale_path.write_text(out_text, encoding="utf-8")
                    updated.append(str(locale_path.relative_to(ROOT)))
                    continue
                old_body = strip_fallback_banner(old_body)
                existing_sections = {k: v for k, v in split_sections(old_body)}

            if api_key and not args.force_fallback:
                try:
                    # Phase-2 quality optimization: translate only changed sections.
                    translated_sections = []
                    for sec_key, zh_content in zh_sections:
                        old_content = existing_sections.get(sec_key)
                        # Reuse only when section is already translated.
                        # If old content equals Chinese source, it's untranslated and must be translated.
                        if old_content is not None and old_content.strip() != zh_content.strip():
                            translated_sections.append((sec_key, old_content))
                            continue
                        translated = translate_with_openai(
                            zh_content,
                            api_key,
                            args.model,
                            locale,
                            base_url,
                            terms_to_preserve,
                            locale_style_prompt,
                        )
                        translated = apply_locale_term_map(translated, locale, locale_term_map)
                        translated_sections.append((sec_key, translated))
                    new_body = sections_to_body(translated_sections)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
                    new_body = fallback_sync(body, locale)
            else:
                # Quality guard: without translation key, do not overwrite existing locale files.
                if locale_path.exists() and not args.force_fallback:
                    continue
                new_body = fallback_sync(body, locale)
            new_body = apply_locale_term_map(new_body, locale, locale_term_map)

            out_text = build_frontmatter(locale_fm) + "\n\n" + new_body
            locale_path.write_text(out_text, encoding="utf-8")
            updated.append(str(locale_path.relative_to(ROOT)))

    if updated:
        print("Updated locale files:")
        for p in updated:
            print(f"- {p}")
    else:
        print("No English files updated.")


if __name__ == "__main__":
    main()

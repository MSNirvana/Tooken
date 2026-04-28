#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
EN_DIR = DOCS_DIR / "en"
JA_DIR = DOCS_DIR / "ja"
KO_DIR = DOCS_DIR / "ko"

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

TERMS_TO_PRESERVE = [
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


def build_frontmatter(fm: dict):
    lines = ["---"]
    for k, v in fm.items():
        value = str(v)
        # Quote scalar values to keep YAML safe for colons and symbols.
        lines.append(f"{k}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def translate_with_openai(content: str, api_key: str, model: str, target_language: str):
    lang_name = {
        "en": "English",
        "ja": "Japanese",
        "ko": "Korean",
    }.get(target_language, "English")
    terms = ", ".join(TERMS_TO_PRESERVE)
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    f"You are a technical translator. Translate Simplified Chinese markdown/MDX into natural {lang_name}. "
                    "Preserve links, code blocks, frontmatter keys, inline code, and file paths exactly. "
                    f"Never translate these terms: {terms}."
                ),
            },
            {"role": "user", "content": content},
        ],
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
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
    args = parser.parse_args()
    locales = [x.strip() for x in args.locales.split(",") if x.strip()]

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    changed = set()
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
        for locale in locales:
            locale_fm = dict(fm)
            if "title" in locale_fm:
                locale_fm["title"] = normalize_title(locale_fm["title"], locale)

            if api_key:
                try:
                    new_body = translate_with_openai(body, api_key, args.model, locale)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
                    new_body = fallback_sync(body, locale)
            else:
                new_body = fallback_sync(body, locale)

            out_text = build_frontmatter(locale_fm) + "\n\n" + new_body
            locale_path = ROOT / map_to_locale_path(zh_rel, locale)
            locale_path.write_text(out_text, encoding="utf-8")
            updated.append(str(locale_path.relative_to(ROOT)))

    if updated:
        print("Updated English files:")
        for p in updated:
            print(f"- {p}")
    else:
        print("No English files updated.")


if __name__ == "__main__":
    main()

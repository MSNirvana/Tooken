# Tooken平台建设文档

日期: 2026年4月23日 18:33 (GMT+8)
领域: 项目推进 (https://www.notion.so/336e6e4ce15f80ad8044fbd03f416dbd?pvs=21)

# **Tooken平台文档**

> **AGI 基础设施 · 智能路由 · Web4 原生结算层**
> 
> 
> 让 AGI 出现在 Web4 上——我们不只是 API 聚合器，我们是机器经济体系的底层基础设施。
> 
> Bringing AGI to Web4.
> 

---

## **目录**

- [模块一：平台简介](/docs/module-1-platform-overview)
- [模块二：快速上手](/docs/module-2-quickstart)
- [模块三：模型与路由](/docs/module-3-models-routing)
- [模块四：支付与结算](/docs/module-4-payment-settlement)
- [模块五：Agent 经济层 · AGI × Web4](/docs/module-5-agent-economy)
- [模块六：API 参考](/docs/module-6-api-reference)

---

# **模块一：平台简介**

## **1.1 什么是Tooken？**

**Tooken**是一个面向企业与 AI Agent 的新一代 AGI 基础设施平台，由三个核心能力层构成：

```
多模型聚合 & 智能路由层
         ↓
  x402 Web4 原生支付结算层
         ↓
  AGI Agent 经济自治层
```

我们不是另一个"API 中转站"。

我们是第一个将 **AGI 能力接入** 与 **机器原生支付** 原生融合的基础设施平台——让 AI Agent 像人一样拥有账户、预算、决策权与结算能力，同时让企业用最低成本调用全球最优模型。

### **核心定位**

| **维度** | **传统 API 聚合器** | **Tooken** |
| --- | --- | --- |
| 用户对象 | 开发者（人） | 开发者 + AI Agent（机器） |
| 支付方式 | 法币订阅、预充值 | 链上微支付 + x402 流式结算 |
| 模型选择 | 手动指定 | Auto 智能路由，自动最优 |
| 故障处理 | 人工干预 | 账号池动态调度，秒级切换 |
| 未来方向 | API 工具 | AGI 经济基础设施 |

---

## **1.2 核心能力全景**

### **多模型聚合**

整合全球主流大语言模型，一个 API Key 调用所有模型：

- **国际顶级**：GPT-5 / Claude Opus / Gemini Ultra
- **高性价比**：Claude Sonnet / GPT-4o-mini / Gemini Flash
- **国产优选**：Kimi（月之暗面）/ Minimax / DeepSeek / Qwen
- **开源部署**：Llama 3 / Mistral / Yi 系列

### **Auto 智能路由**

平台核心差异化能力。声明任务类型，系统自动匹配最优模型：

- 文本处理 → 高性价比国产模型（Kimi / Minimax）
- 代码生成 → Claude Opus / GPT-5
- 多模态分析 → Gemini Ultra
- 高并发轻任务 → DeepSeek / Qwen

**结果：平均降低 60–80% Token 成本，无需人工维护模型切换逻辑。**

### **x402 原生支付**

AI 请求即触发支付，流式结算，无需预充值账户体系：

- 机器原生：Agent 自主发起支付，无需人工干预
- 微支付级别：按 Token 粒度结算
- 链上透明：所有交易可验证，防跑路、防超卖

### **Agent 经济自治**

为 AI Agent 分配钱包、预算与决策权：

- Agent 自主决定调用哪个模型
- Agent 自主控制成本支出
- Agent 之间可建立可编程商业合同（ERC-8183，路线图）

---

## **1.3 为什么是 Web4？**

> *"法币体系是为人设计的，Token 正在变成为机器设计的货币。"*
> 

### **Web1 → Web4 的演进**

| **时代** | **核心主体** | **经济模式** | **支付体系** |
| --- | --- | --- | --- |
| Web1 | 网站 | 信息消费 | 无 |
| Web2 | 平台 | 注意力经济 | 法币 / 信用卡 |
| Web3 | 用户 | 所有权经济 | 加密货币 |
| **Web4** | **AGI Agent** | **机器经济** | **x402 · Token 原生支付** |

### **Web4 的本质**

Web4 不是 Web3 的升级版，而是一次范式转移：

**经济主体从"人"扩展到"机器"。**

当 AI Agent 拥有：

- **钱包**（持有与支配数字资产）
- **权限**（访问 API、数据、工具）
- **身份**（链上可验证的 Agent DID）
- **持续运行能力**（7×24 小时自主执行）

它就不再是工具，而是一个**经济参与者**。

### **四个核心问题**

当 AI 需要花钱时，回到四个问题：

1. **你是谁？** → Agent 身份（DID / 钱包地址）
2. **你有什么钱？** → Agent 钱包余额与授权额度
3. **你如何付钱？** → x402 协议，机器原生支付
4. **谁控制你花钱？** → 人类设定的预算上限与策略规则

**Tooken**是第一个将这四个问题完整回答的基础设施平台。

### **我们的使命**

> 我们不是在建一个更便宜的 API 中转站。
> 
> 
> 我们在建设 **AGI 时代的经济基础设施**——让每一个 AI Agent 都能在 Web4 世界中独立生存、自主交易、创造价值。
> 

---

## **1.4 架构总览**

```
┌─────────────────────────────────────────────────────────────┐
│                        用户 / Agent                          │
│              （开发者 · 企业系统 · AI Agent）                  │
└───────────────────────────┬─────────────────────────────────┘
                            │ API 请求
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      智能网关层                               │
│   鉴权 → 限流 → 任务分析 → Auto 路由决策 → 排队调度             │
└─────────┬──────────────────┬───────────────┬────────────────┘
          │                  │               │
          ▼                  ▼               ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  国际模型层  │    │  国产模型层  │    │  私有模型层  │
│ GPT / Claude│    │Kimi/Minimax │    │  企业私有化  │
│  Gemini 等  │    │ DeepSeek 等 │    │   部署模型   │
└─────────┬───┘    └──────┬──────┘    └──────┬──────┘
          └───────────────┴───────────────────┘
                            │ 响应
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      结算层                                   │
│   Token 计量 → Credits 扣减 → x402 链上结算 → ROI 记录         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   数据与监控层                                 │
│   用量统计 · 成本分析 · ROI 面板 · 健康检测 · 审计日志           │
└─────────────────────────────────────────────────────────────┘
```

---

# **模块二：快速上手**

## **2.1 5 分钟跑通第一个请求**

### **第一步：注册账户**

访问 **Tooken.ai**，支持以下方式注册：

- **Web3 钱包**（MetaMask / OKX Wallet / Phantom）
- **Google 账号** — 快速登录
- **邮箱注册** — 传统方式

> **推荐 Web3 钱包登录**：无需填写任何个人信息，即连即用，无需许可，最适合 AI Agent 身份绑定。
> 

### **第二步：获取 API Key**

1. 登录后进入控制台 → **API Keys**
2. 点击 **创建新 Key**
3. 设置 Key 名称（如 `my-agent-001`）
4. 可选：设置该 Key 的月消费上限（用于 Agent 预算控制）
5. 复制 Key，格式为 `sk-xxx...`

> **安全提示**：API Key 等同于账户密码，请勿泄露。建议为不同 Agent / 项目创建独立的 Key，便于成本分摊与权限管理。
> 

### **第三步：发送第一个请求**

平台完全兼容 OpenAI 接口格式，任何已接入 OpenAI 的项目，只需修改 `base_url` 即可切换：

```
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-api-key",
    base_url="https://api.tooken.ai/v1"
)

response = client.chat.completions.create(
    model="auto",        # 使用 Auto 路由，平台自动选最优模型
    messages=[
        {"role": "system", "content": "你是一个专业的 AI 助手。"},
        {"role": "user", "content": "用 Python 写一个快速排序算法"}
    ]
)

print(response.choices[0].message.content)
```

```
# 或使用 curl
curl https://api.tooken.ai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto",
    "messages": [
      {"role": "user", "content": "Hello, 你好！"}
    ]
  }'
```

### **第四步：查看用量**

进入控制台 → **用量监控**，可查看：

- 实时 Token 消耗
- 各模型调用次数
- 成本明细
- ROI 分析面板

---

## **2.2 登录与身份验证**

### **Web3 钱包登录（推荐）**

适合追求隐私、无国界使用、AI Agent 身份绑定场景。

**支持的钱包：**

| **钱包** | **平台** | **说明** |
| --- | --- | --- |
| MetaMask | 浏览器插件 / Mobile | 以太坊生态首选 |
| OKX Wallet | 浏览器插件 / Mobile | 多链支持，国内用户友好 |
| Phantom | 浏览器插件 / Mobile | Solana 生态 |
| WalletConnect | 协议 | 兼容 400+ 钱包 |

**登录步骤：**

1. 点击 **Connect Wallet**
2. 选择你的钱包类型
3. 在钱包中确认签名（此签名不消耗 Gas，仅用于身份验证）
4. 登录成功，钱包地址即为你的账户 ID

> **注意**：签名验证不会产生任何链上交易，不消耗 Gas 费用。
> 

### **中心化账户登录**

适合企业用户、团队协作场景。

- Google 账号一键登录
- 邮箱 + 密码注册
- 企业 SSO（联系商务）

## **2.3 Credits 充值与管理**

### **Credits 是什么？**

Credits 是平台的计费单位，**1 Credit = 0.001 USD**。

所有模型调用均消耗 Credits，消耗量取决于：

- 所用模型的单价
- 输入 Token 数量
- 输出 Token 数量
- 是否命中缓存

### **充值方式**

**链上充值（主推）：**

| **网络** | **代币** | **最低充值** | **到账时间** |
| --- | --- | --- | --- |
| Ethereum | USDT / USDC | 10 USD | 约 2 分钟 |
| Base | USDT / USDC | 1 USD | 约 10 秒 |
| Solana | USDC | 1 USD | 约 5 秒 |
| BNB Chain | USDT | 5 USD | 约 1 分钟 |

> **推荐使用 Base 网络**：手续费极低（< $0.01），到账速度快，最适合高频小额充值。
> 

**法币充值（企业）：**

- 支付宝 / 微信支付（国内企业）
- Stripe 信用卡（海外用户）
- 银行电汇（大额企业采购，联系商务）

### **企业额度管理**

企业账户支持多级额度管理：

```
企业主账户（总额度）
    ├── 部门 A 子账户（分配额度上限：5000 Credits/月）
    │     ├── API Key 1（营销 Agent）
    │     └── API Key 2（客服 Agent）
    ├── 部门 B 子账户（分配额度上限：3000 Credits/月）
    └── 个人 Key（研发测试）
```

---

## **2.4 OpenClaw / Claude Code 接入**

### **OpenClaw 一键接入**

如果你使用 OpenClaw，可以通过以下方式将 Tooken 设为默认 API 后端：

```
# 一键配置脚本
curl -fsSL https://tooken.ai/install/openclaw.sh | bash
```

脚本会自动：

1. 检测你的 OpenClaw 配置文件位置
2. 将 API Base URL 替换为平台地址
3. 引导你填入 API Key
4. 验证连接是否成功

**手动配置：**

在 OpenClaw 设置中找到 API 配置项：

```
{
  "apiBaseUrl": "https://api.tooken.ai/v1",
  "apiKey": "sk-your-api-key",
  "defaultModel": "auto"
}
```

### **Claude Code 接入**

```
# 设置环境变量
export ANTHROPIC_BASE_URL="https://api.tooken.ai"
export ANTHROPIC_API_KEY="sk-your-api-key"

# 启动 Claude Code
claude
```

或写入 `~/.bashrc` / `~/.zshrc` 永久生效：

```
echo 'export ANTHROPIC_BASE_URL="https://api.tooken.ai"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY="sk-your-api-key"' >> ~/.zshrc
source ~/.zshrc
```

---

# **模块三：模型与路由**

## **3.1 支持的模型列表**

### **国际顶级模型**

| **模型 ID** | **提供商** | **上下文窗口** | **特点** | **Credits/1K Token** |
| --- | --- | --- | --- | --- |
| `gpt-5` | OpenAI | 128K | 综合最强，推理顶尖 | 15 |
| `gpt-5-mini` | OpenAI | 128K | 性价比，速度快 | 0.6 |
| `claude-opus-4` | Anthropic | 200K | 代码 + 长文最强 | 15 |
| `claude-sonnet-4` | Anthropic | 200K | 均衡首选 | 3 |
| `claude-haiku-4` | Anthropic | 200K | 极速，低成本 | 0.25 |
| `gemini-ultra` | Google | 1M | 多模态顶级 | 10 |
| `gemini-flash` | Google | 1M | 超快速，多模态 | 0.3 |

### **国产优选模型**

| **模型 ID** | **提供商** | **上下文窗口** | **特点** | **Credits/1K Token** |
| --- | --- | --- | --- | --- |
| `kimi-k2` | 月之暗面 | 128K | 中文最强，长文理解 | 0.5 |
| `deepseek-v3` | DeepSeek | 64K | 代码极强，开源最优 | 0.2 |
| `minimax-text` | MiniMax | 245K | 超长上下文，国产性价比 | 0.3 |
| `qwen-max` | 阿里云 | 128K | 工具调用优秀 | 0.6 |
| `doubao-pro` | 字节跳动 | 128K | 中文创意写作 | 0.4 |

### **Auto 路由模型**

| **模型 ID** | **说明** |
| --- | --- |
| `auto` | 全自动路由，综合成本与质量最优 |
| `auto-fast` | 优先速度，适合实时交互场景 |
| `auto-cheap` | 优先成本，适合批量处理场景 |
| `auto-quality` | 优先质量，适合高要求输出场景 |

---

## **3.2 Auto 智能路由**

Auto 路由是平台的核心差异化能力，**让平台代替你做模型选择决策**。

### **工作原理**

```
输入请求
    ↓
任务类型分析（延迟 < 5ms）
    ├── 代码生成？→ Claude Opus / DeepSeek-v3
    ├── 中文写作？→ Kimi / Doubao-pro
    ├── 数学推理？→ GPT-5 / Claude Opus（思考模式）
    ├── 图片理解？→ Gemini Ultra / GPT-5
    ├── 简单问答？→ Claude Haiku / Gemini Flash
    └── 长文处理？→ MiniMax / Gemini Flash（1M 上下文）
    ↓
综合评分（质量权重 × 成本权重 × 当前延迟）
    ↓
选定模型 → 发送请求
```

### **路由策略配置**

通过请求头或请求体参数自定义路由策略：

```
response = client.chat.completions.create(
    model="auto",
    messages=[...],
    extra_body={
        "route_strategy": {
            "cost_weight": 0.8,       # 成本权重（0-1，越高越省钱）
            "quality_weight": 0.2,    # 质量权重
            "max_cost_per_1k": 5,     # 单次请求最高成本上限（Credits/1K Token）
            "preferred_regions": ["cn"],  # 优先国内模型
            "exclude_models": ["gpt-5"]   # 排除特定模型
        }
    }
)
```

### **路由透明度**

每次响应都会在 Headers 中返回实际使用的模型：

```
X-Routed-Model: kimi-k2
X-Route-Reason: chinese-text-optimized
X-Cost-Saved: 0.87          # 相比默认模型节省的 Credits
```

---

## **3.3 模型能力对比矩阵**

| **能力维度** | **GPT-5** | **Claude Opus** | **Gemini Ultra** | **Kimi K2** | **DeepSeek V3** |
| --- | --- | --- | --- | --- | --- |
| 通用推理 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| 代码生成 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| 中文理解 | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★★★ |
| 长文处理 | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★☆☆ |
| 多模态 | ★★★★★ | ★★★☆☆ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| 工具调用 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| 响应速度 | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★★ |
| 成本效率 | ★★☆☆☆ | ★★☆☆☆ | ★★★☆☆ | ★★★★★ | ★★★★★ |

---

## **3.4 故障自愈与秒级切换**

### **问题背景**

传统 API 中转站的致命缺陷：

- 单账号封禁 → 全平台不可用
- 上游节点故障 → 用户请求失败
- 限速触发 → 响应变慢甚至超时
- 没有重试机制 → 错误直接暴露给用户

### **我们的解决方案：账号池动态路由**

```
请求进入
    ↓
账号池调度器（实时监控所有账号健康状态）
    ├── 按地区调度：选择最低延迟节点
    ├── 按余额调度：优先余额充足账号
    ├── 健康度调度：降低频繁报错账号权重
    └── 模型调度：匹配支持该模型的账号
    ↓
主账号发送请求
    ├── 成功 → 返回结果
    └── 失败（封号 / 限速 / 超时）
            ↓
        秒级切换备用账号
            └── 对用户完全透明，无感知
```

### **监控指标**

| **指标** | **正常范围** | **告警阈值** |
| --- | --- | --- |
| 账号可用率 | > 99% | < 95% |
| 平均响应时间 | < 2s | > 5s |
| 封号检测延迟 | < 30s | > 60s |
| 切换成功率 | > 99.9% | < 99% |

---

## **3.5 ROI 监测面板**

> **核心洞察：企业不是在买 Token，他们在买业务结果。**
> 

ROI 面板帮助企业量化 AI 投入的实际回报：

### **内置 ROI 模型**

**客服场景：**

```
今日消耗：200,000 Token（成本：¥5）
成功处理咨询：1,200 条
平均每条成本：¥0.004
人工替代成本（按 ¥30/小时，每条 5 分钟）：¥3,000
ROI = 3000 / 5 = 600x
```

**内容生产场景：**

```
本周消耗：1,000,000 Token（成本：¥25）
生产文章：500 篇
每篇成本：¥0.05
人工写作成本（按 ¥200/篇）：¥100,000
ROI = 100000 / 25 = 4000x
```

### **自定义 ROI 指标**

通过 API 上报业务事件，平台自动关联 Token 成本：

```
# 在你的业务代码中上报成果事件
import requests

requests.post("https://api.tooken.ai/v1/roi/event",
    headers={"Authorization": "Bearer sk-your-api-key"},
    json={
        "session_id": "chat-session-001",   # 关联到具体对话
        "event_type": "order_saved",         # 挽回订单
        "value": 299.00,                     # 业务价值（元）
        "currency": "CNY"
    }
)
```

---

# **模块四：支付与结算**

## **4.1 Credits 计费体系**

### **计费单位**

- **1 Credit = 0.001 USD ≈ 0.007 RMB**（汇率实时浮动）
- 所有模型调用按 **实际消耗 Token 数 × 模型单价** 扣减
- 输入 Token 与输出 Token 分别计费（输出通常更贵）

### **定价示例**

以一次典型的客服对话为例（输入 500 Token + 输出 200 Token）：

| **模型** | **输入成本** | **输出成本** | **总成本** |
| --- | --- | --- | --- |
| claude-opus-4 | 7.5 Credits | 15 Credits | 22.5 Credits (≈¥0.16) |
| claude-sonnet-4 | 1.5 Credits | 6 Credits | 7.5 Credits (≈¥0.05) |
| kimi-k2 | 0.25 Credits | 1 Credits | 1.25 Credits (≈¥0.009) |
| **auto（推荐）** | **自动选最优** | — | **↓ 平均节省 70%** |

### **企业套餐**

| **套餐** | **月费** | **赠送 Credits** | **折扣** | **适合场景** |
| --- | --- | --- | --- | --- |
| 入门版 | ¥199 | 50,000 | 9折 | 小团队测试 |
| 专业版 | ¥999 | 300,000 | 8折 | 中小企业日常 |
| 企业版 | ¥4,999 | 2,000,000 | 7折 | 规模化业务 |
| 旗舰版 | 联系商务 | 无上限 | 6折起 | 大型部署 |

> **用量越大，折扣越深。** 所有套餐均支持子账号分配、用量监控与合规发票。
> 

---

## **4.2 链上支付（USDT / USDC）**

### **为什么选择链上支付？**

| **传统支付** | **链上支付** |
| --- | --- |
| 需要银行账户 / 信用卡 | 只需加密钱包 |
| 跨境付款费率高、周期长 | 全球即时到账，手续费极低 |
| 平台可冻结账户 | 资产自主控制 |
| 不支持 Agent 自动化 | 完美支持程序化付款 |
| 付款记录可被追溯关联 | 钱包地址匿名 |

### **充值流程**

1. 进入控制台 → **充值**
2. 选择充值网络（推荐 Base，手续费 < $0.01）
3. 复制平台收款地址
4. 从你的钱包向该地址转账 USDT / USDC
5. 链上确认后（约 10 秒 - 2 分钟），Credits 自动到账

**Base 网络充值示例（Solidity 调用）：**

```
// 使用 ethers.js 从 Agent 钱包自动充值
const { ethers } = require("ethers");

const USDC_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"; // Base USDC
const PLATFORM_ADDRESS = "0x...your-platform-address";
const AMOUNT = ethers.parseUnits("10", 6); // 充值 10 USDC

const usdcContract = new ethers.Contract(USDC_ADDRESS, ERC20_ABI, agentWallet);
await usdcContract.transfer(PLATFORM_ADDRESS, AMOUNT);
```

---

## **4.3 x402 协议集成**

> **x402 是什么：HTTP 状态码 402（Payment Required）的机器原生实现。**
> 
> 
> 过去，API 付费依赖账户、订阅、密钥、人工开通；x402 把这些压缩成一个机器可理解的协议动作。
> 

### **工作原理**

```
Agent 发送 API 请求
        ↓
服务端返回 402 Payment Required
        + 支付要求（金额、接受的 Token、支付地址）
        ↓
Agent 解析支付要求
        ↓
Agent 自动完成链上支付
        ↓
Agent 携带支付证明重新发送请求
        ↓
服务端验证支付 → 返回 AI 响应
```

### **对开发者意味着什么**

**传统方式：**

1. 开发者注册账户 ✗
2. 绑定信用卡 ✗
3. 设置充值 ✗
4. 获取 API Key ✗
5. 在代码中硬编码 Key ✗
6. 监控余额，手动续费 ✗

**x402 方式：**

1. Agent 持有钱包 ✓
2. 请求 → 自动付款 → 获得响应 ✓

### **接入 x402**

```
# 平台原生支持 x402，无需额外配置
# 只需为 Agent 提供一个已授权的钱包

from platform_sdk import AgentClient

client = AgentClient(
    wallet_private_key="0x...",     # Agent 的钱包私钥
    wallet_budget_usdc=100,          # 最大授权额度：100 USDC
    payment_network="base"           # 使用 Base 网络支付
)

# Agent 自动处理所有支付逻辑
response = client.chat("分析这份财务报告的风险点")
print(response.content)
print(f"本次消耗：{response.cost_usdc} USDC")
```

### **流式计费**

x402 支持真正的流式结算——AI 每输出一段内容，对应的微支付同步发生：

```
AI 输出 "The" → 支付 0.000001 USDC
AI 输出 "quick" → 支付 0.000001 USDC
AI 输出 "brown" → 支付 0.000001 USDC
...
```

**优势：**

- 不再需要预充值押金
- Agent 实际用多少付多少
- 杜绝平台跑路风险（未收到付款就不提供服务）

---

## **4.4 企业账单与发票合规**

### **合规通道**

平台与以下机构建立官方合作，为企业提供 100% 合规的采购路径：

- **亚马逊 AWS** — AWS Marketplace 上架，企业可走 AWS 采购合同
- **腾讯云** — 腾讯云市场合规销售，支持腾讯云账单
- **阿里云** — 阿里云市场合规销售

> 大型企业、政府项目建议通过官方合规通道采购，可获得正规增值税专用发票、合同与技术支持 SLA。
> 

### **发票申请**

1. 进入控制台 → **账单** → **申请发票**
2. 选择发票类型（增值税普通发票 / 增值税专用发票）
3. 填写企业信息
4. 3 个工作日内邮寄纸质发票，或提供电子发票

### **数据安全合规**

| **合规要求** | **状态** |
| --- | --- |
| 数据不出境（国内模型） | ✅ 支持 |
| API 网关 IP 白名单 | ✅ 支持 |
| 操作审计日志（180天留存） | ✅ 支持 |
| 私有化部署 | ✅ 支持（企业版） |
| SOC 2 Type II | 🔄 认证中 |

---

## **4.5 微支付与实时流式计费（路线图）**

> **当前状态：规划阶段，预计 2026 Q3 上线**
> 

### **愿景**

传统的 Credits 预充值体系仍然是"先买后用"的人类付款模式。我们正在构建真正的**机器原生微支付**基础设施：

- **每 Token 对应一次价值转移**，精确到 0.000001 USDC 粒度
- **无需账户余额**，Agent 持有链上资产即可直接使用
- **双向流动**，未来支持 Agent 提供服务并收取费用

### **技术路径**

```
阶段 1（当前）：Credits 预充值 + 链上批量结算
阶段 2（2026 Q3）：x402 按请求实时结算
阶段 3（2027）：Token 级流式结算 + Agent 自主收款
```

---

# **模块五：Agent 经济层 · AGI × Web4**

## **5.1 Agent 钱包与身份**

### **为什么 Agent 需要钱包？**

传统 AI Agent 是"无产者"——它没有资产，没有账户，所有资源都依赖人类托管。这带来几个根本性问题：

1. **依赖人工充值**：Agent 余额不足时必须人工干预
2. **无法自主决策**：Agent 不知道自己能"花多少钱"
3. **无法 Agent 间交易**：A Agent 无法直接向 B Agent 购买服务
4. **身份不可验证**：调用来自 Agent 还是人类，无法链上证明

**Agent 钱包解决这一切。**

### **为 Agent 创建钱包**

```
from platform_sdk import AgentWallet

# 创建 Agent 钱包
wallet = AgentWallet.create(
    agent_id="customer-service-agent-001",
    budget_policy={
        "monthly_limit_usdc": 500,        # 月预算上限
        "per_request_limit_usdc": 0.1,    # 单次请求上限
        "auto_refill": True,               # 余额不足时自动从主账户补充
        "auto_refill_threshold": 10,       # 余额低于 10 USDC 时触发补充
        "auto_refill_amount": 50           # 每次补充 50 USDC
    }
)

print(f"Agent 钱包地址:{wallet.address}")
print(f"初始余额:{wallet.balance_usdc} USDC")
```

### **Agent 身份（DID）**

每个 Agent 钱包自动生成一个去中心化身份标识符（DID）：

```
did:platform:0x1a2b3c4d5e6f...
```

DID 包含：

- Agent 的链上地址（可验证）
- Agent 的能力声明（调用了哪些模型、执行了哪些任务）
- Agent 的信誉分数（由历史执行质量决定）
- Agent 的授权范围（被允许花费的资源上限）

---

## **5.2 Agent 自动路由购买 Token**

> **这是我们认为最重要的 Web4 创新之一：让 AI 自己决定用什么模型、花多少钱。**
> 

### **核心思想**

人类购买模型服务时，需要：

- 研究各模型能力
- 对比价格
- 手动配置
- 定期维护

**Agent 不需要这些。**

Agent 知道自己的任务类型，平台知道每个模型的实时能力和价格——让平台帮 Agent 做决策，Agent 只需声明目标和预算。

### **工作流示例**

```
# 给 Agent 100 USDC 的月预算，让它自主决定如何分配

agent = Agent(
    wallet=AgentWallet(budget_usdc=100),
    routing_policy={
        "optimize_for": "cost_quality_balance",
        "task_model_mapping": {
            "text_processing": "auto-cheap",    # 文本处理用便宜模型
            "code_generation": "auto-quality",  # 代码生成用高质量模型
            "quick_qa": "auto-fast",            # 快问快答用快速模型
            "analysis": "claude-opus-4"         # 分析任务指定 Opus
        }
    }
)

# Agent 自主完成一系列任务
results = agent.run_pipeline([
    {"task": "summarize_emails", "type": "text_processing"},     # → Kimi（便宜）
    {"task": "write_python_script", "type": "code_generation"},  # → Claude Opus（高质量）
    {"task": "answer_customer", "type": "quick_qa"},             # → Haiku（极快）
    {"task": "analyze_financials", "type": "analysis"},          # → Claude Opus（指定）
])

# 查看 Agent 的花费明细
print(agent.wallet.spending_report())
# 输出：
# text_processing: 0.02 USDC (5 tasks)
# code_generation: 0.45 USDC (3 tasks)
# quick_qa: 0.01 USDC (8 tasks)
# analysis: 0.38 USDC (2 tasks)
# 总计: 0.86 USDC / 月预算 100 USDC
```

### **为什么这很重要？**

这不只是工程便利性问题，这是**经济效率的根本性提升**：

- 人类需要花时间研究、配置、维护模型选择逻辑
- Agent 可以在毫秒内完成这些决策
- Agent 可以根据实时价格、质量和延迟动态调整
- **最终结果：AI 比人类更擅长管理 AI 的成本**

---

## **5.3 ERC-8183 合约层（路线图）**

> **当前状态：技术预研阶段，预计 2027 上线**
> 

### **背景：Agent 之间的商业关系**

当两个 Agent 需要合作时，如何建立信任？

**问题场景：**

Agent A 需要分析一份法律文件，它决定委托专门的"法律 Agent B"来完成，并支付 5 USDC。

但：

- Agent A 如何确保 Agent B 真的完成了工作？
- Agent B 如何确保 Agent A 真的会付款？
- 如果 Agent B 的结果质量不达标，谁来仲裁？

### **ERC-8183：Agent 之间的可编程合同**

```
┌─────────────────────────────────────────────────────┐
│                  ERC-8183 执行流程                    │
│                                                      │
│  Agent A（客户）                                      │
│      ↓ 发起任务 + 锁定资金（5 USDC → 托管合约）         │
│  Agent B（服务提供方）                                 │
│      ↓ 接受任务，开始执行                               │
│      ↓ 完成后提交结果 + 执行证明                         │
│  Evaluator（评估方，可以是人类或另一个 Agent）            │
│      ↓ 验证结果质量                                    │
│  托管合约                                             │
│      ├── 质量达标 → 释放 5 USDC 给 Agent B ✓           │
│      └── 质量不达标 → 退还 5 USDC 给 Agent A ✗         │
└─────────────────────────────────────────────────────┘
```

### **这构建了什么？**

**Agent 经济市场（Agent Economy）：**

- Agent 可以作为"服务提供方"上架能力，收取费用
- Agent 可以作为"客户"购买其他 Agent 的服务
- 信誉系统记录每个 Agent 的历史完成率和质量分
- 形成"发现 → 交易 → 结算 → 信誉"的完整市场闭环

这是 Web4 的核心愿景：**一个由 AGI 驱动的自组织经济网络。**

---

## **5.4 多 Agent 协作经济**

### **A2A 协议（Agent to Agent）**

A2A 协议定义了 Agent 之间通信和协作的标准：

```
Agent 发现层（类似 DNS）
    ↓
Agent 能力描述（类似 OpenAPI Spec）
    ↓
Agent 谈判与定价（自动化）
    ↓
任务执行 + ERC-8183 结算
    ↓
信誉更新
```

**平台角色：**

Tooken 提供 A2A 协议的基础设施层：

- **Agent 注册表**：发布你的 Agent 能力，供其他 Agent 发现
- **定价引擎**：设置你的 Agent 服务价格（按 Token / 按任务 / 按结果）
- **结算层**：自动完成 Agent 间的 x402 支付
- **信誉系统**：链上记录每个 Agent 的执行历史

### **实际场景：自动化投研流水线**

```
主 Agent（投研负责人）
    ↓ 分配子任务
    ├── 数据收集 Agent → 抓取财报、新闻、公告
    │       ↓ 支付 0.1 USDC
    ├── 分析 Agent → Claude Opus 深度分析
    │       ↓ 支付 0.5 USDC
    ├── 校验 Agent → 交叉验证数据
    │       ↓ 支付 0.1 USDC
    └── 报告 Agent → 生成 PDF 研报
            ↓ 支付 0.05 USDC
总成本：0.75 USDC
人工成本替代：¥2,000+（1名分析师1天工作量）
```

---

## **5.5 AGI 出现在 Web4 的愿景**

> *"当 AI 拥有钱包、权限、接口、环境和持续运行能力后，它会越来越自然地卷入经济活动。"*
> 

### **三个历史性转变**

**第一个转变：AI 从工具变成经济主体**

工具没有账户，没有预算，没有决策权。
经济主体拥有资产、做出交易、承担责任。

当 Agent 拥有了钱包，这个转变就发生了。

**第二个转变：支付从人类设计变成机器设计**

信用卡、银行账户、法币支付体系——这一切都是为人类设计的。
x402、链上微支付、可编程结算——这是为机器设计的。

当 Agent 可以自主完成支付，无需人类干预，Web4 就真正到来了。

**第三个转变：经济网络从中心化变成 AGI 驱动**

Web2 的经济网络由平台驱动（亚马逊、淘宝、Uber）。
Web3 的经济网络由协议驱动（DeFi、NFT、DAO）。
Web4 的经济网络由 AGI 驱动——Agent 自主发现需求、协商价格、执行任务、完成结算。

### **我们在建设什么？**

Tooken 不是终点，是起点。

我们正在建设的，是 AGI 时代的**经济基础设施底层**：

```
今天：让人类更便宜地使用 AI 模型
明天：让 Agent 自主管理自己的 AI 成本
后天：让 Agent 在经济网络中自由交易与创造价值
```

**加入我们，成为 Web4 时代的建设者。**

---

# **模块六：API 参考**

## **6.1 认证**

### **Bearer Token（OpenAI 兼容）**

```
Authorization: Bearer sk-your-api-key
```

### **API Key Header（Claude 兼容）**

```
x-api-key: sk-your-api-key
```

### **钱包签名认证（Agent 专用）**

```
X-Agent-Address: 0x1a2b3c4d5e6f...
X-Agent-Signature: 0xabcdef...
X-Agent-Timestamp: 1719000000
```

---

## **6.2 Chat Completions（OpenAI 兼容）**

**端点：** `POST /v1/chat/completions`

**Base URL：** `https://api.tooken.ai`

### **请求参数**

| **参数** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| `model` | string | 是 | 模型 ID，或 `auto` / `auto-fast` / `auto-cheap` |
| `messages` | array | 是 | 对话消息列表 |
| `stream` | boolean | 否 | 是否流式返回，默认 `false` |
| `max_tokens` | integer | 否 | 最大输出 Token 数 |
| `temperature` | number | 否 | 随机性，0-2，默认 1 |
| `tools` | array | 否 | 工具定义列表 |
| `tool_choice` | string/object | 否 | 工具选择策略 |

**平台扩展参数：**

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| `route_strategy` | object | Auto 路由策略配置 |
| `budget_limit` | number | 本次请求最大 Credits 上限 |
| `agent_wallet` | string | Agent 钱包地址（用于 x402 结算） |

### **请求示例**

```
curl https://api.tooken.ai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto",
    "messages": [
      {"role": "system", "content": "你是一个专业的财务分析师。"},
      {"role": "user", "content": "分析这家公司的盈利能力"}
    ],
    "stream": false,
    "route_strategy": {
      "cost_weight": 0.6,
      "quality_weight": 0.4
    }
  }'
```

### **响应（非流式）**

```
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1719000000,
  "model": "kimi-k2",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "从财务指标来看..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 800,
    "total_tokens": 950
  },
  "platform": {
    "routed_model": "kimi-k2",
    "route_reason": "chinese-analysis-optimized",
    "credits_consumed": 0.475,
    "cost_saved_credits": 13.525
  }
}
```

### **流式响应（SSE）**

```
curl https://api.tooken.ai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"model": "auto", "messages": [...], "stream": true}'
```

```
data: {"id":"chatcmpl-abc","object":"chat.completion.chunk","choices":[{"delta":{"content":"从"},"index":0}]}
data: {"id":"chatcmpl-abc","object":"chat.completion.chunk","choices":[{"delta":{"content":"财务"},"index":0}]}
...
data: {"id":"chatcmpl-abc","object":"chat.completion.chunk","choices":[{"delta":{},"finish_reason":"stop","index":0}]}
data: [DONE]
```

---

## **6.3 Messages（Claude 兼容）**

**端点：** `POST /v1/messages`

### **请求示例**

```
import anthropic

client = anthropic.Anthropic(
    api_key="sk-your-api-key",
    base_url="https://api.tooken.ai"
)

message = client.messages.create(
    model="claude-opus-4",
    max_tokens=2048,
    system="你是一个资深的商业顾问。",
    messages=[
        {"role": "user", "content": "帮我分析这个商业计划的可行性"}
    ]
)

print(message.content[0].text)
```

### **扩展思考模式**

```
message = client.messages.create(
    model="claude-opus-4",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # 允许最多 10000 Token 用于思考
    },
    messages=[
        {"role": "user", "content": "这道数学题：..."}
    ]
)

# 获取思考过程
for block in message.content:
    if block.type == "thinking":
        print("思考过程：", block.thinking)
    elif block.type == "text":
        print("最终答案：", block.text)
```

---

## **6.4 路由 API（Auto 模式）**

**端点：** `POST /v1/route`

专用路由查询接口，在发送实际请求前先查询平台推荐的模型（不消耗实际 Token）：

```
curl https://api.tooken.ai/v1/route \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "code_generation",
    "estimated_input_tokens": 2000,
    "constraints": {
      "max_cost_credits": 50,
      "max_latency_ms": 5000,
      "required_languages": ["python", "javascript"]
    }
  }'
```

**响应：**

```
{
  "recommended_model": "claude-opus-4",
  "reasoning": "代码生成任务，Claude Opus 在 Python/JavaScript 综合表现最佳",
  "estimated_cost_credits": 38.5,
  "estimated_latency_ms": 3200,
  "alternatives": [
    {
      "model": "deepseek-v3",
      "estimated_cost_credits": 5.5,
      "quality_trade_off": "代码质量约 85% 水平，成本降低 86%"
    }
  ]
}
```

---

## **6.5 错误码与限流说明**

### **HTTP 状态码**

| **状态码** | **含义** | **处理建议** |
| --- | --- | --- |
| 200 | 成功 | — |
| 400 | 请求参数错误 | 检查请求体格式 |
| 401 | 认证失败 | 检查 API Key 是否正确 |
| 402 | 余额不足 | 充值 Credits 或配置 x402 钱包 |
| 403 | 无权限 | 检查 Key 的模型访问权限 |
| 429 | 超出限流 | 降低请求频率，或联系商务升级限额 |
| 500 | 服务内部错误 | 重试，或联系技术支持 |
| 502 | 上游服务错误 | 平台正在自动切换节点，稍后重试 |
| 503 | 服务不可用 | 流量高峰，系统正在扩容，稍后重试 |

### **限流规则**

| **账户类型** | **请求/分钟** | **Token/分钟** | **并发请求** |
| --- | --- | --- | --- |
| 免费 | 10 | 40,000 | 2 |
| 入门版 | 60 | 200,000 | 5 |
| 专业版 | 300 | 1,000,000 | 20 |
| 企业版 | 2,000 | 10,000,000 | 100 |
| 旗舰版 | 自定义 | 自定义 | 自定义 |

### **推荐重试策略**

```
import time
import random

def call_with_retry(client, max_retries=3, **kwargs):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
        except Exception as e:
            if "429" in str(e):
                # 指数退避 + 随机抖动
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"限流，{wait_time:.1f}秒后重试...")
                time.sleep(wait_time)
            elif "502" in str(e) or "503" in str(e):
                # 上游故障，快速重试
                time.sleep(1)
            else:
                raise e
    raise Exception("超过最大重试次数")
```

---

## **附录**

### **常见问题**

**Q：Auto 路由会不会不稳定，每次用不同模型导致结果不一致？**

A：Auto 路由会根据任务类型选择同一档次的模型，对于需要严格一致性的场景，建议指定具体模型。

**Q：链上支付是否需要 KYC？**

A：使用加密钱包登录和链上支付无需 KYC。仅企业采购需要提供营业执照用于开票。

**Q：Agent 钱包的私钥如何安全存储？**

A：推荐使用 AWS KMS / HashiCorp Vault 等密钥管理服务存储，避免明文写入代码或配置文件。

**Q：x402 支付协议支持哪些区块链？**

A：当前支持 Ethereum、Base、Solana。计划中：Arbitrum、Polygon、BNB Chain。

**Q：如果平台故障，我的资产安全吗？**

A：链上支付的资产由智能合约托管，平台无法单方面挪用。Credits 余额对应的稳定币由多签钱包管理，定期审计。

---

### **更新日志**

| **版本** | **日期** | **主要更新** |
| --- | --- | --- |
| v1.0.0 | 2026-04 | 平台上线，多模型聚合 + Auto 路由 + 链上支付 |
| v1.1.0 | 2026 Q3（计划） | x402 实时结算上线 |
| v2.0.0 | 2027（计划） | Agent 钱包 + ERC-8183 合约层 + A2A 协议 |
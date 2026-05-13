# Tooken 文档中心

> 链上金融 x AI 的明亮科技文档中心
>
> 浅色底、深色字、轻科技质感。面向开发者与产品团队，快速理解 Tooken 的模型路由、链上结算与 Agent 经济能力。

---

## 文档导航

- [平台概览](#平台概览)
- [快速开始](#快速开始)
- [模型与路由](#模型与路由)
- [支付与结算](#支付与结算)
- [Agent 经济能力](#agent-经济能力)
- [API 参考](#api-参考)
- [合规与隐私](#合规与隐私)
- [常见问题](#常见问题)

---

## 平台概览

### Tooken 是什么

`Tooken` 是面向开发者、产品团队与 AI Agent 的基础设施平台，核心提供三层能力：

```text
多模型聚合与智能路由
        ↓
链上支付与结算（x402）
        ↓
Agent 预算与经济自治能力
```

平台目标是让企业更高效地用好模型，同时让 Agent 拥有可治理、可结算、可审计的执行能力。

### 核心能力

- **多模型聚合**：一个 API Key 调用多家主流模型能力。
- **Auto 智能路由**：按质量、成本、时延自动选择模型。
- **链上结算**：支持 USDT/USDC 充值与请求级支付。
- **Agent 预算治理**：可为不同 Agent 配置独立预算与访问策略。

### 适用场景

- 多模型统一接入与成本优化
- 海内外业务统一结算
- 需要可观测、可治理的 Agent 工作流
- 企业级 AI 应用的权限与预算隔离

---

## 快速开始

### 1) 注册并获取 API Key

1. 进入 Tooken 控制台并完成注册或登录
2. 打开 `API Keys` 页面创建 Key
3. 按项目或 Agent 维度拆分 Key，便于权限与成本管理

> 安全建议：将 API Key 存放在密钥管理服务中，不要写入代码仓库。

### 2) 发起第一个请求（OpenAI 兼容）

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-api-key",
    base_url="https://api.tooken.ai/v1",
)

resp = client.chat.completions.create(
    model="auto",
    messages=[
        {"role": "system", "content": "你是专业助手"},
        {"role": "user", "content": "用 Python 写一个快速排序"},
    ],
)

print(resp.choices[0].message.content)
```

```bash
curl https://api.tooken.ai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto",
    "messages": [{"role":"user","content":"Hello, 你好"}]
  }'
```

### 3) 查看成本与用量

在控制台查看：

- Token 消耗
- 各模型调用分布
- 请求成功率与时延
- 费用明细与预算告警

---

## 模型与路由

### 支持模型类型

- 国际主流模型（如 GPT、Claude、Gemini 系列）
- 国产优选模型（如 Kimi、DeepSeek、Qwen、Minimax 系列）
- 企业私有部署模型（按接入方案）

### Auto 路由模式

- `auto`：综合效果优先（默认）
- `auto-fast`：低时延优先
- `auto-cheap`：低成本优先

路由会综合任务类型、预算约束与模型健康状态，选择当前最合适执行路径。

### 路由策略示例

```python
resp = client.chat.completions.create(
    model="auto",
    messages=[{"role": "user", "content": "生成接口文档"}],
    route_strategy={
        "cost_weight": 0.5,
        "quality_weight": 0.3,
        "latency_weight": 0.2,
        "max_budget_credits": 20
    },
)
```

---

## 支付与结算

### Credits 计费说明

- 输入和输出 Token 按模型档位计费
- 可按请求维度追踪费用
- 支持预算上限和超限告警

### 链上支付（USDT / USDC）

支持链上充值并自动入账，适合全球化团队与 Agent 自动支付场景。

```text
控制台发起充值
  ↓
选择链与币种
  ↓
转账到账确认
  ↓
Credits 自动入账
```

### x402 支付集成

平台支持请求级支付语义，可用于机器自治结算：

```python
resp = client.chat.completions.create(
    model="auto",
    messages=[{"role": "user", "content": "总结这份报告"}],
    extra_headers={
        "X-Agent-Address": "0x1234...",
        "X-Agent-Signature": "...",
        "X-Agent-Timestamp": "1719000000",
    },
)
```

---

## Agent 经济能力

### Agent 钱包与身份

为 Agent 绑定钱包后，可实现：

- 预算内自主调用模型
- 请求级支付与账单追踪
- 多 Agent 任务分工与成本拆分

### Agent 预算治理

建议按“团队 -> 项目 -> Agent”三级管理预算与权限：

- 团队级总预算
- 项目级成本中心
- Agent 级调用白名单和额度上限

### 多 Agent 协作

在工作流中，主 Agent 可以把子任务分发给不同能力 Agent，实现并行执行与分账管理，适用于投研、客服、运营自动化等场景。

---

## API 参考

### 认证方式

**Bearer Token（OpenAI 兼容）**

```text
Authorization: Bearer sk-your-api-key
```

**API Key Header（Claude 兼容）**

```text
x-api-key: sk-your-api-key
```

**钱包签名认证（Agent 场景）**

```text
X-Agent-Address: 0x1a2b3c4d5e6f...
X-Agent-Signature: 0xabcdef...
X-Agent-Timestamp: 1719000000
```

### Chat Completions

- **Endpoint**: `POST /v1/chat/completions`
- **Base URL**: `https://api.tooken.ai`

请求参数（核心）：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `model` | string | 是 | 模型 ID 或 `auto` 系列 |
| `messages` | array | 是 | 消息数组 |
| `stream` | boolean | 否 | 是否流式返回 |
| `max_tokens` | integer | 否 | 最大输出长度 |
| `temperature` | number | 否 | 采样温度 |

平台扩展参数：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `route_strategy` | object | 路由权重和约束 |
| `budget_limit` | number | 本次请求预算上限 |
| `agent_wallet` | string | Agent 钱包地址 |

### Messages（Claude 兼容）

- **Endpoint**: `POST /v1/messages`
- 支持通过 `base_url` 直接对接 Tooken 服务

### 路由查询接口

- **Endpoint**: `POST /v1/route`
- 用于请求前的模型推荐评估（不执行实际生成）

### 错误码与限流

| 状态码 | 含义 | 建议处理 |
| --- | --- | --- |
| 400 | 参数错误 | 检查请求体格式 |
| 401 | 认证失败 | 检查 API Key |
| 402 | 余额不足 | 充值或调整预算 |
| 429 | 超出限流 | 指数退避重试 |
| 500/502/503 | 服务异常 | 稍后重试并保留重试策略 |

推荐在 SDK 或网关侧启用指数退避与抖动重试机制。

---

## 合规与隐私

### 上游渠道

Tooken 所接入的全部 AI 模型，均来自具备完整商业授权的企业级上游渠道。我们不接入任何非官方、来源不明的模型接口，确保您的每一次调用都建立在可信的服务基础之上。

---

### 隐私承诺

我们对用户隐私的承诺简单且明确：

> **不读取、不存储您的任何对话内容，更不会将其用于模型训练或任何商业目的。**

您通过 API 传输的消息内容，在平台内部不做任何解析、缓存或落库。我们只记录必要的请求元数据（时间、模型、Token 数量）用于计费，仅此而已。

您的数据属于您，我们没有理由碰它，也不会碰它。

---

### 关于上游原厂

作为接入层，Tooken 保护的是数据在平台内部的隐私。但请您注意：**您在使用特定模型时，仍受该模型原厂（如 OpenAI、Anthropic、Google 等）使用协议的约束。**

建议您同步了解所使用模型原厂各自的隐私政策，以做出符合您业务需求的选择。

如有任何隐私相关问题，欢迎联系：**privacy@tooken.ai**

---

## 常见问题

**Q: Auto 路由会不会导致输出不稳定？**

A: 对强一致场景建议固定模型；对成本和速度敏感场景可使用 Auto 模式。

**Q: 链上支付是否必须 KYC？**

A: 常规链上支付无需额外 KYC；企业开票流程按本地合规要求执行。

**Q: Agent 私钥如何存储更安全？**

A: 建议使用 KMS 或 Vault 管理密钥，不要明文保存在代码与环境共享文件中。

**Q: 平台故障时资产是否安全？**

A: 链上资产以链上状态为准，建议结合最小授权、分层钱包与审计策略降低风险。

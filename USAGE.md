# 🔗 UTM Link Generator — 测试与使用手册

> 版本: 1.0 | 最后更新: 2026-07-11
> 仓库: [github.com/shuishouac/utm-link-generator](https://github.com/shuishouac/utm-link-generator)
> 参考模板: [飞书多维表格](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)

---

## 📋 目录

1. [UTM 参数规范速查](#1-utm-参数规范速查)
2. [5 种触发方式](#2-5-种触发方式)
3. [推断逻辑详解](#3-推断逻辑详解)
4. [测试用例（全场景覆盖）](#4-测试用例全场景覆盖)
5. [常见问题](#5-常见问题)

---

## 1. UTM 参数规范速查

### 核心格式

```
https://example.com/?&utm_campaign={campaign}&utm_medium={medium}&utm_source={source}&utm_content={content}&utm_term={term}
```

### 全局规则

| 规则 | 要求 | 示例 |
|------|------|------|
| 大小写 | **全部小写** | `Black Friday` → `black-friday` |
| 语言 | **英文** | `春季大促` → `spring-sale` |
| 空格 | **自动转为 `-`** | `Summer Sale 2026` → `summer-sale-2026` |
| 分隔符 | **仅用 `-`**，不用 `_` 或空格 | 不要 `summer_sale` |
| 中文 | **不允许** | ❌ `black-星期五` |
| 日期 | 仅放 utm_term，不放 campaign | ❌ `black-friday-2026` |

### 参数一览

| 参数 | 顺序 | 必填 | 格式说明 | 示例 |
|------|------|------|---------|------|
| `utm_campaign` | **①** | ✅ | 用户自定义固定名称 | `black-friday` |
| `utm_medium` | **②** | ✅ | 标准媒介选项 | `influencer` |
| `utm_source` | **③** | ✅ | 标准来源选项 | `instagram` |
| `utm_content` | **④** | 可选 | 达人/素材标识 | `creator-jessica` |
| `utm_term` | **⑤** | ✅（自动） | `YYYYMMDDlaunch` | `20260711launch` |

---

## 2. 5 种触发方式

### 方式一：一句话全信息触发（推荐）

一次性说完整，Agent 直接生成。

> **你**：生成utm链接，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://shuishouac.com/products/bag，7月11日发布
>
> **Agent**：🔗 直接生成完整链接

📌 **适用场景**：你清楚所有信息，想一步到位。

---

### 方式二：分段对话 + 关键词触发

先聊活动方案，再触发生成，Agent 从对话历史中提取参数。

> **你**：下周黑色星期五我们和 Jessica 合作推新品包包，在 Instagram 上发帖，链接到 https://shuishouac.com/products/bag，7月11号上线
>
> **Agent**：收到，黑五 + Instagram + Jessica
>
> **你**：生成utm链接
>
> **Agent**：🔗（从上文提取全部参数直接生成，**不会重复问**）

📌 **适用场景**：你已经在和 Agent 讨论活动方案，最后需要出链接。

---

### 方式三：只说关键词 + 逐步补充（缺失才问）

> **你**：生成utm链接
>
> **Agent**：好的，请告诉我：
> 1️⃣ 目标链接是什么？
> 2️⃣ 这是什么活动？
> ...
>
> **你**：https://shuishouac.com/sale，黑色星期五，Jessica 在 Instagram 发帖
>
> **Agent**：🔗 已收到全部信息，生成完整链接

📌 **适用场景**：你还没想好所有细节，想边聊边补充。

---

### 方式四：批量生成多个链接

> **你**：帮我生成这周两个 UTM 链接：
> 1. 周三发春季大促邮件 → https://shuishouac.com/sale
> 2. 周五发 Instagram 达人推广新品 → https://shuishouac.com/new
> 都是7月这周，今天7月11号
>
> **Agent**：🔗🔗 一次性生成两个链接

📌 **适用场景**：同时有多个活动需要出链接。

---

### 方式五：基于上次生成修改 / 复用

> **你**：刚才那个链接，目标链接改成 https://shuishouac.com/spring2026，其他不变
>
> **Agent**：🔗（复用上次所有参数，只替换 URL）

或者：

> **你**：再帮我生成一个，还是春季大促，这次是在 Facebook 投广告
>
> **Agent**：🔗（复用 campaign/term，只改 source/medium/content）

📌 **适用场景**：同一活动不同渠道，或多个类似链接。

---

## 3. 推断逻辑详解

### 核心原则

1. **优先从上下文提取** → 不会问已经知道的信息
2. **缺失才反问** → 只问缺少的部分，不问全部
3. **自动规范化** → 空格→`-`、大写→小写、中→英
4. **确认 campaign 名称** → 确保一致性

### 参数提取优先级

| 参数 | 从哪里提取 | 如果缺失 |
|------|-----------|---------|
| `url` | 用户显式提供 / 上文提到的链接 | 必须反问 |
| `campaign` | 用户自定义 / 上下文活动类型 | 反问"这是什么活动？" |
| `medium` | 用户说的触达方式 | 反问"什么方式触达？" |
| `source` | 用户说的平台/渠道 | 反问"哪个平台？" |
| `content` | 达人名字/素材描述 | 可留空或反问 |
| `term` | 用户指定日期 / 默认当天 | 用当天日期 |

### 命名规范化流程

```
用户输入: Summer Sale 2026
    ↓ 小写
summer sale 2026
    ↓ 空格 → -
summer-sale-2026
    ↓ 确认
"campaign 使用 summer-sale-2026，之后同一活动请保持统一，可以吗？"
```

---

## 4. 测试用例（全场景覆盖）

### 测试 1️⃣：标准单句触发（全信息）

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 生成utm链接，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://shuishouac.com/products/bag，7月11日发布 |
| **期望结果** | ✅ 直接生成，无需反问 |
| **验证点** | campaign=black-friday, medium=influencer, source=instagram, content=creator-jessica, term=20260711launch |

**期望输出：**
```text
🔗 UTM 链接

https://shuishouac.com/products/bag?&utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260711launch

📋 参数解析
| 参数 | 值 | 说明 |
|------|-----|------|
| utm_campaign | black-friday | ⚠️ 后续同一活动请保持统一 |
| utm_medium | influencer | 达人营销 |
| utm_source | instagram | Instagram 平台 |
| utm_content | creator-jessica | 达人 Jessica |
| utm_term | 20260711launch | 7月11日发布 |
```

---

### 测试 2️⃣：分段对话触发

| 测试项 | 内容 |
|--------|------|
| **用户第一步** | 下周返校季和 Carry 合作，他在 Instagram 发帖推广 https://shuishouac.com/，7月9号发 |
| **Agent 回应** | 收到，返校季 + Instagram + Carry |
| **用户第二步** | 生成utm链接 |
| **期望结果** | ✅ 直接从上下文提取，**不问任何问题** |
| **验证点** | campaign=backtoschool, medium=influencer, source=instagram, content=creator-carry, term=20260709launch |

---

### 测试 3️⃣：用户自定义 campaign 名称 + 空格转连字符

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 生成utm链接，我们的 Summer Sale 2026 活动，在 Facebook 投广告推 https://shuishouac.com/summer，明天发 |
| **处理过程** | `Summer Sale 2026` → `summer-sale-2026` |
| **期望结果** | ✅ 生成 + **确认 campaign 名称** |
| **验证点** | Agent 问："campaign 使用 `summer-sale-2026`，之后统一使用这个名称可以吗？" |

---

### 测试 4️⃣：信息不完整（只反问缺失项）

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 帮我生成utm链接，黑色星期五活动，目标链接 https://shuishouac.com/sale |
| **期望结果** | ✅ Agent 只问缺失的 2 项（方式+平台），**不问 URL 和活动** |
| **验证点** | "已记录：✅URL ✅活动。还需要补充：①方式？②平台？" |

---

### 测试 5️⃣：批量生成

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 帮我生成这周两个UTM链接：1. 周三发春季大促邮件 → https://shuishouac.com/sale 2. 周五发 Instagram 达人合作推新品 → https://shuishouac.com/new，今天7月11号 |
| **期望结果** | ✅ 生成 2 个链接，campaign 统一为 spring-sale |

---

### 测试 6️⃣：覆盖同一活动的不同渠道

| 测试项 | 内容 |
|--------|------|
| **用户第一步** | 生成utm链接，春季大促，在 Instagram 发帖推 https://shuishouac.com/sale，7月11号 |
| **用户第二步** | 再帮我生成一个，还是春季大促，这次在 Facebook 投广告 |
| **期望结果** | ✅ 复用 campaign=spring-sale, term=20260711launch，只改 source 和 medium |

---

### 测试 7️⃣：修改已有链接

| 测试项 | 内容 |
|--------|------|
| **先决条件** | Agent 刚生成过一个链接 |
| **用户输入** | 刚才那个链接，目标链接改成 https://shuishouac.com/spring2026，其他不变 |
| **期望结果** | ✅ 只替换 URL，其他参数不变 |

---

### 测试 8️⃣：中文活动名（应提示并处理）

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 生成utm链接，「春季大促」活动，在抖音发帖推 https://shuishouac.com/sale |
| **期望结果** | Agent 应问清楚英文 campaign 名称（"春季大促"的英文名称是什么？） |
| **验证点** | campaign 不能含中文 |

---

### 测试 9️⃣：Campaign 名称一致性确认

| 测试项 | 内容 |
|--------|------|
| **用户输入** | 生成utm链接，做黑五活动，... |
| **期望结果** | ✅ 生成后附带提醒"后续同一活动请保持统一" |
| **验证点** | 用户后续用 `bf-2026` 时，Agent 应提示"上次黑五活动用的 `black-friday`，这次用 `bf-2026` 是不同的名称，确认要换吗？" |

---

### 测试 🔟：CLI 交互模式（需 Python 环境）

| 测试项 | 内容 |
|--------|------|
| **命令** | `python scripts/utm_generator.py --interactive` |
| **步骤** | 按提示依次输入 URL / campaign / medium / source / content / term |
| **期望结果** | ✅ campaign 输入后有确认步骤："campaign 确认使用「xxx」？(Y/n)" |
| **验证点** | 输入 n 可重新输入，输入 y 继续 |

---

## 5. 常见问题

### Q: 我忘了之前活动用的 campaign 名称怎么办？

A: 直接问 Agent"上次黑色星期五活动用的什么 campaign 名称？"，Agent 会从对话历史中找到。如果跨会话了，可以自己查 UTM 链接中的 `utm_campaign` 参数。

### Q: 同一活动多个渠道，campaign 要一样吗？

A: **是的。** campaign 标识"什么活动"，而不是"什么渠道"。同一活动（如春季大促）不管在 Instagram/TikTok/邮件发，campaign 都应该用 `spring-sale`。通过 medium 和 source 区分渠道。

### Q: 如果不小心用了不同的名称怎么办？

A: 数据会分散在两个名称下，无法统一分析。Agent 生成时会提醒一致性，如果发现用户用了不同名称，会主动提示上次的 campaign 名称。

### Q: 空格怎么处理？

A: **自动转为 `-`**。你输入 `Summer Sale`、`summer_sale`、`SummerSale` 都会被处理成 `summer-sale`。不用刻意改格式。

### Q: 日期不传会怎样？

A: 默认用**当天日期 + launch**。比如今天（2026-07-11）不指定 term，自动用 `20260711launch`。

### Q: 可以批量生成吗？

A: 可以。直接说"帮我生成这周两个 UTM 链接：……" 或分别触发多次。

### Q: 我能用中文 campaign 名称吗？

A: **不可以。** 全部参数必须用英文小写。中文活动名称 Agent 会问你对应的英文名称。

---

## 附录：文件

| 资源 | 链接 |
|------|------|
| 主仓库 | [github.com/shuishouac/utm-link-generator](https://github.com/shuishouac/utm-link-generator) |
| 飞书模板 | [水手阿C UTM链接生成器](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink) |
| CLI 工具 | `scripts/utm_generator.py`（需 Python 环境） |
| 配置文件 | `scripts/utm_config.json`（自定义 source/medium/campaign 列表） |

---

*Generated by UTM Link Generator v1.0*

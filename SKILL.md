# 🔗 UTM Link Generator — 标准化 UTM 链接生成器

标准化 UTM 链接生成工具。根据上下文信息自动生成符合团队规范的 UTM 跟踪链接。

- **参考模板**: [飞书多维表格 - 水手阿C UTM链接生成器模板](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)
- **触发关键词**: `生成utm链接` / `utm` / `生成链接` / `帮我生成UTM` / `帮我生成链接` / `出个链接`
- **Campaign 一致性**: 每个活动使用固定统一的 campaign 名称，生成时会向您确认

---

## 🔴 强制执行规则（Agent 必须遵守）

以下规则在每次生成 UTM 链接时**必须严格执行**，不允许例外：

```
https://example.com/?utm_campaign={campaign}&utm_medium={medium}&utm_source={source}&utm_content={content}&utm_term={term}
```

### 规则 1：参数顺序固定
URL 中参数必须按 **campaign → medium → source → content → term** 的顺序排列。
> ✅ `?utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260713`
> ❌ `?utm_source=instagram&utm_medium=influencer&utm_campaign=bf2026&utm_content=jessica`

### 规则 2：campaign 必须用标准名称或用户确认
- 优先使用参考列表中已有的固定名称（如 `black-friday`, `spring-sale`）
- 如果用户自定义名称，必须确认一致性：**"campaign 名称使用 `xxx`，后续同活动请保持统一，可以吗？"**
- 禁止使用缩写、变体或临时名称（如 `bf2026`、`bf-sale` 应统一为 `black-friday`）

### 规则 3：content 只标识达人/素材本身，不重复场景
- 达人合作（medium=influencer）：**必须**使用 `creator-{达人名}` 格式
  - ✅ `creator-jessica`（只标识达人，场景放 term 后缀）
  - ❌ `creator-jessica-story`（场景已放 term 后缀，content 不应重复）
  - ❌ `jessica`、`jessica_story`（缺 creator- 前缀）
- 广告素材：使用 `ad-{描述}`（如 `ad-hero-banner`）
- 邮件：使用 `email-{名称}`（如 `email-welcome-series`）

> 💡 **区分原则**：content 回答"谁/什么素材"，term 回答"什么发布形式"。两者各司其职，不重复。

### 规则 4：term 始终生成 + 日期优先 + 场景后缀（无硬编码）
utm_term 是**必填参数**，永远不允许省略。
- 先让用户选择日期 → 自动生成 `YYYYMMDD`
- 再让用户自定义场景后缀（如 `ig-story`、`ig-post`、`bio`）
  - 如果加了后缀 → `20260713ig-story`
  - 如果没加后缀 → 仅 `20260713`
- **不硬编码任何默认后缀**，用户有场景需求才加
- content 已标识的维度，term 不重复；反之亦然

---

## 总原则

生成 UTM 链接前，先理解用户提供的上下文（渠道、内容、活动类型等），然后按以下规范拼装完整的 UTM URL。

### 核心格式

```
https://example.com/?utm_campaign={campaign}&utm_medium={medium}&utm_source={source}&utm_content={content}&utm_term={term}
```

> 参数顺序固定：**utm_campaign → utm_medium → utm_source → utm_content → utm_term**，与模板表格列顺序一致。

### 全局规范

| 规则 | 要求 |
|------|------|
| 大小写 | **全部小写** |
| 语言 | **英文** |
| 分隔符 | 使用 `-`（连字符），不用 `_`、空格或其他符号 |
| 中文 | **不使用中文** |
| 日期 | campaign 名称里不使用日期（日期放 utm_term） |
| 空格 | **不使用空格**（用 `-` 替代） |

---

## 参数详解

### utm_campaign（营销活动名称）

**格式**：使用你团队**自己定义的固定统一名称**。每次为同一活动生成链接时，campaign 名称必须保持一致，方便后续汇总分析。

> ⚠️ **重要原则**：每个活动应该使用唯一且固定的 campaign 名称，不要同一活动这次写 `black-friday`、下次写 `bf-sale`。**一致性比命名本身更重要。**

**参考建议**：以下是常见的 campaign 命名参考，你可以直接使用，也可以自定义团队名称。关键是一个活动只用一个名字，持久不变。

#### ① Holiday（节日营销）
围绕国内外节日、购物节、季节性节点开展的营销活动。

| 名称 | 适用场景 |
|------|---------|
| `black-friday` | 黑五 |
| `cyber-monday` | 网络星期一 |
| `prime-day` | Amazon Prime Day |
| `christmas` | 圣诞节 |
| `new-year` | 新年 |
| `valentines-day` | 情人节 |
| `mothers-day` | 母亲节 |
| `fathers-day` | 父亲节 |
| `easter` | 复活节 |
| `halloween` | 万圣节 |
| `backtoschool` | 返校季 |

#### ② Promotion（促销活动）
品牌自主发起的促销活动，不依赖具体节日。

| 名称 | 适用场景 |
|------|---------|
| `spring-sale` | 春季大促 |
| `summer-sale` | 夏季促销 |
| `autumn-sale` | 秋季促销 |
| `winter-sale` | 冬季促销 |
| `flash-sale` | 限时闪购 |
| `weekend-sale` | 周末促销 |
| `sitewide-sale` | 全场折扣 |
| `free-shipping` | 包邮活动 |
| `buy-more-save-more` | 多买多省 |
| `buy2-get1` | 买二送一 |
| `gift-with-purchase` | 买赠活动 |
| `new-arrival` | 新品到货 |

#### ③ Launch（新品发布）
新品、系列、版本或补货上线。

| 名称 | 适用场景 |
|------|---------|
| `new-product` | 新品发布 |
| `new-collection` | 新系列上线 |
| `limited-edition` | 限量款 |
| `restock` | 补货通知 |
| `product-refresh` | 产品更新 |
| `seasonal-collection` | 季节系列 |

#### ④ Member（会员活动）
针对会员、VIP 用户的专属营销。

| 名称 | 适用场景 |
|------|---------|
| `member-day` | 会员日 |
| `vip-sale` | VIP 专享 |
| `birthday-event` | 生日活动 |
| `double-points` | 双倍积分 |
| `member-exclusive` | 会员专属 |
| `referral` | 推荐奖励 |

#### ⑤ Clearance（清仓活动）
库存清理、季末清仓。

| 名称 | 适用场景 |
|------|---------|
| `end-of-season` | 季末清仓 |
| `inventory-clearance` | 库存清理 |
| `warehouse-sale` | 仓库清仓 |
| `last-chance` | 最后机会 |
| `final-sale` | 最终清仓 |

#### ⑥ Brand（品牌营销）
以提升品牌认知为目标，非直接促销。

| 名称 | 适用场景 |
|------|---------|
| `brand-awareness` | 品牌认知 |
| `brand-story` | 品牌故事 |
| `brand-anniversary` | 品牌周年庆 |
| `ugc-campaign` | 用户生成内容活动 |
| `creator-program` | 创作者招募 |

#### ⑦ Retention（老客运营）
针对已有客户，提高复购率和 LTV。

| 名称 | 适用场景 |
|------|---------|
| `reorder` | 复购提醒 |
| `win-back` | 老客召回 |
| `subscription` | 订阅续费 |
| `loyalty` | 忠诚度计划 |
| `cross-sell` | 交叉销售 |
| `upsell` | 升级销售 |

#### ⑧ Acquisition（拉新获客）
以获取新用户为主要目标。

| 名称 | 适用场景 |
|------|---------|
| `first-order` | 首单优惠 |
| `new-customer` | 新客专享 |
| `welcome-offer` | 欢迎优惠 |
| `free-trial` | 免费试用 |
| `lead-generation` | 线索收集 |

---

### utm_medium（营销媒介）

流量通过什么方式触达。根据上下文推断：

| 媒介 | 适用场景 | 判断依据 |
|------|---------|---------|
| `cpc` | 付费点击广告 | 提到广告投放、PPC、竞价、SEM |
| `paid-social` | 付费社交广告 | 提到社交平台广告投流（FB Ads、IG Ads、TikTok Ads） |
| `organic-social` | 自然社交内容 | 提到社媒内容、自然流量、发帖 |
| `email` | 邮件营销 | 提到邮件发送、EDM |
| `display` | 展示广告/横幅广告 | 提到展示广告、banner、display |
| `influencer` | 达人营销 | 提到达人、KOL、红人合作 |
| `affiliate` | 联盟营销 | 提到联盟伙伴、佣金推广 |
| `sms` | 短信 | 提到短信、SMS |
| `qr` | 二维码 | 提到二维码 |
| `video` | 视频广告 | 提到视频广告 |
| `banner` | 横幅广告 | 提到 banner 广告 |
| `audio` | 音频广告/播客 | 提到播客、音频广告 |
| `app` | App 内广告 | 提到 App 内投放 |
| `ppc` | 按点击付费 | 提到 PPC |
| `retargeting` | 再营销/重定向 | 提到再营销、retarget、重定向 |
| `paid` | 综合付费 | 泛指付费渠道 |
| `expandable` | 可展开广告 | 富媒体广告 |
| `interstitial` | 插屏广告 | 插屏/全屏广告 |
| `cpm` | 按展示付费 | 提到 CPM、千次展示 |
| `referral` | 推荐/转介绍 | 提到用户推荐 |
| `mobile` | 移动渠道 | 提到移动端推广 |

---

### utm_source（流量来源）

流量从哪个平台/渠道来。根据上下文推断：

| 来源 | 适用场景 | 判断依据 |
|------|---------|---------|
| `google` | Google 搜索/购物/展示 | 提到 Google、谷歌、搜索广告 |
| `tiktok` | TikTok | 提到 TikTok、抖音海外 |
| `facebook` | Facebook / Meta | 提到 Facebook、Meta、FB |
| `youtube` | YouTube | 提到 YouTube |
| `instagram` | Instagram | 提到 Instagram、IG、ins |
| `linkedin` | LinkedIn | 提到 LinkedIn、领英 |
| `qr` | 二维码 | 提到二维码、QR code |
| `klaviyo` | Klaviyo 邮件 | 提到 Klaviyo |
| `x` | Twitter/X | 提到 Twitter、X（平台） |
| `reddit` | Reddit | 提到 Reddit |
| `discord` | Discord | 提到 Discord |
| `email` | 邮件 | 提到邮件、Email |
| `sms` | 短信 | 提到短信 |
| `firebase` | Firebase | 提到 Firebase |

---

### utm_content（内容标识）

标识具体的素材或创作者。**只标识"谁/什么"本身，不重复场景区分。**

**格式规则**：
- 达人合作：`creator-{达人名字/账号}`（全部小写，用 `-` 连接）
  - ✅ 正确：`creator-jessica`、`creator-carry`
  - ❌ 错误：`creator-jessica-story`（场景应放 term 后缀）
- 广告素材：`ad-{素材描述}`（全部小写，用 `-` 连接）
  - 例如：`ad-hero-banner-v1`、`ad-square-image`
- 博客文章：`post-{文章slug}`
  - 例如：`post-utm-guide`
- 邮件：`email-{邮件名称}`
  - 例如：`email-welcome-series`

> 💡 **content vs term 分工**：content 回答"谁/什么素材"，term 回答"什么发布形式/场景"。两者各司其职，信息不重复。

---

### utm_term（时间标识）

**格式**: `YYYYMMDD` 或 `YYYYMMDD{场景后缀}`

**生成逻辑（优先级从上到下）**：

1. 用户自定义完整 term → 直接使用
2. 用户指定日期 + 场景后缀 → `20260713ig-story`
3. 用户指定日期（无后缀）→ `20260713`
4. 都没指定 → 仅当天日期（`20260713`）

**规则**：
- 日期部分：8 位数字（如 `20260713`）
- 后缀部分：**按需添加，不硬编码默认后缀**
  - 有场景区分需求才加后缀（如 `ig-story`、`ig-post`、`bio`、`fb-ad`）
  - 无场景区分只用日期
- 全部小写，无空格
- **content 已标识的信息，term 不重复；term 已标识的信息，content 不重复**

**示例**：
- 2026年7月13日发布，无场景区分 → `20260713`
- 2026年7月13日 IG Story → `20260713ig-story`
- 2026年7月13日 IG Post → `20260713ig-post`
- 2026年7月13日 Bio 链接 → `20260713bio`
- 用户完全自定义 → `q3-launch-2026`

---

## 触发方式

通过以下任一方式即可触发 UTM 链接生成：

### 方式一：一句话包含所有信息（推荐）

在当前对话中一次性提供所有参数，Agent 自动提取生成，无需反问。

> "生成utm链接，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://myshop.com/products/bag，7月11日发布"

### 方式二：对话中分段提供信息

先聊活动方案，然后发送触发词，Agent 从上文提取参数。

> **你**：下周黑色星期五我们和 Jessica 合作推新品包包，在 Instagram 上发帖，链接到 https://myshop.com/products/bag，7月11号上线
> **Agent**：收到，记下了
> **你**：生成utm链接
> **Agent**：（从上文提取全部参数直接生成，无需再问）

### 方式三：只说触发词 + 逐步补充

> **你**：生成utm链接
> **Agent**：好的，请告诉我：
> 1️⃣ 目标链接是什么？
> 2️⃣ 这是什么活动？
> 3️⃣ 通过什么方式触达？...
>
> **你**：https://myshop.com/sale，黑色星期五，Jessica 在 Instagram 发帖
> **Agent**：（生成完整链接）

### 方式四：批量生成多个链接

> "帮我生成这周的 UTM 链接，周三发春季大促的邮件推 https://myshop.com/sale，周五发 Instagram 达人合作推 https://myshop.com/new"

### 方式五：修改已有链接 / 基于上次生成

> "刚才那个链接换一下目标 URL，改成 https://myshop.com/spring，其他不变"

或：
> "再帮我生成一个，还是春季大促，这次是在 Facebook 投广告"

---

## 推断流程

### 核心原则：从上下文提取，不问多余问题

当用户触发 UTM 生成时，按以下优先级处理：

**第一步：扫描当前会话上下文**

如果当前对话中已经包含了必要的信息（URL、活动类型、渠道、日期等），直接提取，**不需要重新向用户确认**。

**第二步：参数提取**

对每一项参数，按优先级从以下来源提取：

| 参数 | 提取优先级 |
|------|-----------|
| `url` | ①用户显式提供 ②上文中用户提到的链接 |
| `campaign` | ①用户自定义名称 ②上下文推断活动类型 ③反问用户 |
| `medium` | ①上下文触达方式 ②反问用户 |
| `source` | ①上下文平台/渠道 ②反问用户 |
| `content` | ①上下文达人/素材名 ②视情况留空 |
| `term` | ①用户指定日期 ②默认当天 |

**第三步：仅信息缺失时反问**

如果扫描上下文后发现某参数缺失，**只针对缺失项提问**，不重复问已有信息。

> ✅ 正确做法：
> 用户: 帮我生成黑色星期五的utm链接 https://myshop.com/sale
> Agent: 收到！黑五活动。是通过什么方式触达？哪个平台？

> ❌ 错误做法：
> 用户: 帮我生成黑色星期五的utm链接 https://myshop.com/sale
> Agent: 目标链接是什么？什么活动？什么方式？...
> （用户刚说过，不应重复问）

**第四步：生成后确认 campaign 名称一致性**

每次生成后，主动确认 campaign 名称：

> "这次使用的 campaign 名称是 `black-friday`，后续为同一活动生成链接时请保持统一，方便数据汇总。"

如果 campaign 是用户自定义的，确认格式：

> "活动名称我理解为 `2026-summer-promo`，这个名称后续这个活动都会统一使用，可以吗？"

### 交互流程完整示例

```
场景 A：上下文已包含全部信息

用户: 下周黑色星期五和 Jessica 合作推包包 → 链接 https://shuishouac.com/bag，7月11号在 Ins 发

Agent: 记下了，黑五 + Instagram + Jessica。

用户: 生成utm链接

Agent:
🔗 UTM 链接

https://shuishouac.com/bag?utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260711

📋 参数解析
| 参数 | 值 | 说明 |
|------|-----|------|
| utm_campaign | black-friday | ⚠️ 后续同一活动请保持此名称 |
| ... | ... | ... |

---

场景 B：信息不足，只问缺失项

用户: 帮我生成utm链接，黑色星期五活动，目标链接 https://shuishouac.com/sale

Agent: 收到！已知道：
✅ 目标链接: https://shuishouac.com/sale
✅ 活动: black-friday

还有两个信息需要补充：
1️⃣ 通过什么方式触达？（邮件/达人/广告/社媒...）
2️⃣ 在哪个平台？（Instagram/TikTok/Google/邮件...）
```

---

## 输出格式

生成后以以下格式输出：

```
🔗 UTM 链接

{完整 UTM URL}

---

📋 参数解析

| 参数 | 值 | 说明 |
|------|-----|------|
| utm_campaign | {campaign} | 活动名称 — ⚠️ 后续同一活动请保持统一 |
| utm_medium | {medium} | 营销媒介 |
| utm_source | {source} | 流量来源 |
| utm_content | {content} | 内容标识 |
| utm_term | {term} | 时间标识 |
```

> 每次生成后附带 campaign 名称一致性提醒，确保用户知道后续同活动要用同一个名称。

---

## 使用示例

### 示例 1：达人合作（全信息单句触发）

**用户输入**：
> 生成utm链接，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://myshop.com/products/bag，7月11日发布

**生成结果**：
```
🔗 UTM 链接

https://myshop.com/products/bag?utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260711

---

📋 参数解析
| 参数 | 值 | 说明 |
|------|-----|------|
| utm_campaign | black-friday | ⚠️ 后续同一活动请保持统一 |
| utm_medium | influencer | 达人营销 |
| utm_source | instagram | Instagram 平台 |
| utm_content | creator-jessica | 达人 Jessica |
| utm_term | 20260711 | 7月11日发布 |
```

### 示例 2：邮件营销（全信息单句触发）

**用户输入**：
> 生成utm链接，给会员发一封双倍积分的邮件，链接到 https://myshop.com/member，7月9日发布

**生成结果**：
```
https://myshop.com/member?utm_campaign=double-points&utm_medium=email&utm_source=email&utm_content=email-double-points&utm_term=20260709
```

### 示例 3：社媒广告（全信息单句触发）

**用户输入**：
> 生成utm链接，TikTok 上投春季大促广告，主打新款连衣裙 https://myshop.com/collections/dresses，今天发

**生成结果**：
```
https://myshop.com/collections/dresses?utm_campaign=spring-sale&utm_medium=paid-social&utm_source=tiktok&utm_content=ad-spring-dresses&utm_term=20260711
```

### 示例 4：分段对话触发（从上下文提取）

**对话**：
```
你: 下周返校季和 Carry 合作，他在 Instagram 发帖推广 https://shuishouac.com/，7月9号发
Agent: 好的，返校季活动 + Instagram + Carry。

你: 生成utm链接
Agent:
🔗 UTM 链接

https://shuishouac.com/?utm_campaign=backtoschool&utm_medium=influencer&utm_source=instagram&utm_content=creator-carry&utm_term=20260709

📋 参数解析
| utm_campaign | backtoschool | ⚠️ 后续同一活动请保持统一 |
| utm_medium | influencer | 达人营销 |
| utm_source | instagram | Instagram |
| utm_content | creator-carry | 达人 Carry |
| utm_term | 20260709launch | 7月9日发布 |
```

### 示例 5：用户自定义 campaign 名称 + 空格转连字符

**用户输入**：
> 生成utm链接，我们的 Summer Sale 2026 活动，在 Facebook 投广告推 https://shuishouac.com/summer，明天发

**处理过程**：
- `Summer Sale 2026` → `summer-sale-2026`（空格转连字符，大写转小写）
- 生成后确认：**"campaign 名称使用 `summer-sale-2026`，后续同活动请保持统一，可以吗？"**

**生成结果**：
```
https://shuishouac.com/summer?utm_campaign=summer-sale-2026&utm_medium=paid-social&utm_source=facebook&utm_content=ad-summer-sale&utm_term=20260712
```

### 示例 6：信息不完整（仅反问缺失项）

**用户输入**：
> 帮我生成utm链接，黑色星期五活动，目标链接 https://shuishouac.com/sale

**Agent 回复**：
> 已记录：
> ✅ 目标链接: https://shuishouac.com/sale
> ✅ 活动: black-friday
>
> 还需要补充 2 项：
> 1️⃣ 通过什么方式触达？（广告/邮件/达人/社媒...）
> 2️⃣ 在哪个平台/渠道？（Instagram/TikTok/Google/邮件...）

**用户补充**：
> Instagram 达人

**Agent 生成**：
```
🔗 UTM 链接

https://shuishouac.com/sale?utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260713
```

### 示例 7：批量生成多个链接

**用户输入**：
> 帮我生成这周两个UTM链接：
> 1. 周三发春季大促邮件 → https://shuishouac.com/sale
> 2. 周五发 Instagram 达人合作推新品 → https://shuishouac.com/new
> 这两个都是7月这周，今天7月11号

**生成结果**：
```
1️⃣ 邮件（7月11日）
https://shuishouac.com/sale?utm_campaign=spring-sale&utm_medium=email&utm_source=email&utm_content=email-spring-sale&utm_term=20260711

2️⃣ 达人合作（7月11日）
https://shuishouac.com/new?utm_campaign=spring-sale&utm_medium=influencer&utm_source=instagram&utm_content=creator-unknown&utm_term=20260711

⚠️ 两个链接都使用 campaign 名称 spring-sale，方便统一分析。
```

### 示例 8：基于上次生成修改

**用户输入**：
> 刚才那个链接，目标链接改成 https://shuishouac.com/spring2026，其他的不变

**生成结果**（复用上次参数，只变 URL）：
```
https://shuishouac.com/spring2026?utm_campaign=spring-sale&utm_medium=email&utm_source=email&utm_content=email-spring-sale&utm_term=20260711
```

---

## 自定义配置

如果团队有自己的域名、默认 source/medium 映射或 campaign 分类，可在安装后修改以下文件：

- `scripts/utm_config.json` — 参数映射表和域名配置
- `SKILL.md` — 规则说明
- 参考模板：[飞书多维表格](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)

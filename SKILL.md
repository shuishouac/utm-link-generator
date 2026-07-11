# 🔗 UTM Link Generator — 标准化 UTM 链接生成器

标准化 UTM 链接生成工具。根据上下文信息自动生成符合团队规范的 UTM 跟踪链接。

- **参考模板**: [飞书多维表格 - 水手阿C UTM链接生成器模板](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)
- **触发关键词**: `生成utm链接` / `utm` / `生成链接` / `帮我生成UTM`

---

## 总原则

生成 UTM 链接前，先理解用户提供的上下文（渠道、内容、活动类型等），然后按以下规范拼装完整的 UTM URL。

### 核心格式

```
https://example.com/?&utm_campaign={campaign}&utm_medium={medium}&utm_source={source}&utm_content={content}&utm_term={term}
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

标识具体的素材、创作者或内容变体。

**格式规则**：
- 达人合作：`creator-{达人名字/账号}`（全部小写，用 `-` 连接）
  - 例如：`creator-jessica`、`creator-carry`
- 广告素材：`ad-{素材描述}`（全部小写，用 `-` 连接）
  - 例如：`ad-hero-banner-v1`、`ad-square-image`
- 博客文章：`post-{文章slug}`
  - 例如：`post-utm-guide`
- 邮件：`email-{邮件名称}`
  - 例如：`email-welcome-series`

如果无法明确归类，用具体描述性关键词，全部小写并用 `-` 连接。

---

### utm_term（时间标识）

固定格式：**发布日期 + launch**

**格式**：`YYYYMMDDlaunch`

- 全部小写，字母数字连写
- 固定后缀 `launch`（无其他时段选项）

**示例**：
- 2026年7月9日发布 → `20260709launch`
- 2026年7月11日发布 → `20260711launch`

如果用户未提供发布日期，默认使用 **当前日期 + launch**。

---

## 推断流程

当用户说"生成utm链接"并提供上下文时，按以下顺序推断：

1. **确认目标 URL** → 如果用户未提供，要求用户提供
2. **识别活动类型** → 匹配 campaign 分类中最近似的标准化名称
3. **识别营销媒介** → 从触达方式匹配 utm_medium
4. **识别流量来源** → 从上下文提到的渠道匹配 utm_source
5. **识别内容标识** → 达人名字、素材描述等填入 utm_content
6. **确认日期** → 填入 utm_term（默认当天），固定后缀 `launch`

### 交互流程

```
用户: 生成utm链接

Agent 反问（如缺少信息）：
1. 目标链接是什么？
2. 这是什么活动？（节日/促销/新品/会员/清仓/品牌/老客/拉新）
3. 通过什么方式触达？（广告/社媒/邮件/达人/联盟/二维码等）
4. 流量从哪个平台/渠道来？
5. 具体素材或达人名字是什么？
6. 发布日期是什么时候？

Agent 生成后展示完整 UTM 链接并逐项确认。
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
| utm_campaign | {campaign} | 活动名称 |
| utm_medium | {medium} | 营销媒介 |
| utm_source | {source} | 流量来源 |
| utm_content | {content} | 内容标识 |
| utm_term | {term} | 时间标识 |
```

---

## 使用示例

### 示例 1：达人合作

**用户输入**：
> 生成utm链接，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://myshop.com/products/bag，7月11日发布

**生成结果**：
```
https://myshop.com/products/bag?&utm_campaign=black-friday&utm_medium=influencer&utm_source=instagram&utm_content=creator-jessica&utm_term=20260711launch
```

### 示例 2：邮件营销

**用户输入**：
> 生成utm链接，给会员发一封双倍积分的邮件，链接到 https://myshop.com/member，7月9日发布

**生成结果**：
```
https://myshop.com/member?&utm_campaign=double-points&utm_medium=email&utm_source=email&utm_content=email-double-points&utm_term=20260709launch
```

### 示例 3：社媒广告

**用户输入**：
> 生成utm链接，TikTok 上投春季大促广告，主打新款连衣裙 https://myshop.com/collections/dresses，今天发

**生成结果**：
```
https://myshop.com/collections/dresses?&utm_campaign=spring-sale&utm_medium=paid-social&utm_source=tiktok&utm_content=ad-spring-dresses&utm_term=20260711launch
```

### 示例 4：返校季达人

**用户输入**：
> 生成utm链接，和 Carry 合作返校季活动，他在 Instagram 发帖推广 https://shuishouac.com/，7月9日

**生成结果**：
```
https://shuishouac.com/?&utm_campaign=backtoschool&utm_medium=influencer&utm_source=instagram&utm_content=creator-carry&utm_term=20260709launch
```

---

## 自定义配置

如果团队有自己的域名、默认 source/medium 映射或 campaign 分类，可在安装后修改以下文件：

- `scripts/utm_config.json` — 参数映射表和域名配置
- `SKILL.md` — 规则说明
- 参考模板：[飞书多维表格](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)

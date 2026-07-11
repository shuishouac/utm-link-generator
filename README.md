# 🔗 UTM Link Generator — 标准化 UTM 链接生成器

根据上下文信息自动生成符合团队规范的 UTM 跟踪链接。

## 参考模板

本 Skill 的 UTM 参数规范基于飞书多维表格模板：

> [📊 水手阿C UTM链接生成器模板](https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog?from=from_copylink)

该模板定义了：
- 参数顺序：`utm_campaign → utm_medium → utm_source → utm_content → utm_term`
- 8 类 Campaign 标准化命名（节日/促销/新品/会员/清仓/品牌/老客/拉新）
- utm_source 和 utm_medium 的标准下拉选项
- utm_term 格式：`YYYYMMDDlaunch`
- 全局规范：全部小写、英文、连字符分隔

## 安装

```bash
git clone https://github.com/shuishouac/utm-link-generator.git
cd utm-link-generator
pip install -r requirements.txt
```

## 使用方式

### AI 对话触发

在支持的 AI 工具中，直接输入：

> **生成utm链接**，我们在黑色星期五和一个叫 Jessica 的 Instagram 达人合作推广新品包包，目标链接 https://myshop.com/products/bag，7月11日发布

### 命令行工具

```bash
# 交互模式
python skills/utm-link-generator/scripts/utm_generator.py --interactive

# 命令行模式
python skills/utm-link-generator/scripts/utm_generator.py \
  --url https://myshop.com/sale \
  --campaign black-friday \
  --medium influencer \
  --source instagram \
  --content creator-jessica \
  --term 20260711launch
```

## UTM 参数规范速查

| 参数 | 位置 | 格式 | 示例 |
|------|------|------|------|
| utm_campaign | 1 | 标准化活动名称 | `black-friday`, `spring-sale`, `backtoschool` |
| utm_medium | 2 | 标准媒介选项 | `influencer`, `cpc`, `email`, `paid-social` |
| utm_source | 3 | 标准来源选项 | `instagram`, `google`, `tiktok`, `facebook` |
| utm_content | 4 | `creator-{名字}` / `ad-{描述}` | `creator-jessica` |
| utm_term | 5 | `YYYYMMDDlaunch` | `20260711launch` |

## 文件结构

```
skills/utm-link-generator/
├── SKILL.md                       # Skill 定义（完整 UTM 规范）
├── install.sh                     # 安装脚本
├── README.md                      # 本文件
└── scripts/
    ├── utm_generator.py           # CLI 生成工具
    └── utm_config.json            # 可自定义的配置
```

## 自定义

编辑 `scripts/utm_config.json` 可自定义：
- source/medium 的选项列表
- campaign 分类和名称
- 默认域名

## 开源协议

MIT

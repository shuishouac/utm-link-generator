#!/usr/bin/env python3
"""
UTM Link Generator — 标准化 UTM 链接生成工具

用法：
  python utm_generator.py [options]

选项：
  --url URL              目标链接（必填）
  --campaign CAMPAIGN    活动名称（utm_campaign，必填）
  --medium MEDIUM        营销媒介（utm_medium，必填）
  --source SOURCE        流量来源（utm_source，必填）
  --content CONTENT      内容标识（utm_content，可选）
  --term TERM            完整自定义 utm_term（覆盖日期+后缀自动生成）
  --term-date TERM_DATE  日期部分（8位数字，如 20260713）
  --term-suffix SUFFIX   场景后缀（如 ig-story, fb-ad, bio），不带则仅日期
  --interactive          交互模式，逐步引导输入

参数顺序固定：campaign → medium → source → content → term

示例：
  python utm_generator.py --url https://myshop.com/sale --campaign black-friday --medium influencer --source instagram --content creator-jessica --term 20260711launch
  python utm_generator.py --url https://myshop.com/sale --campaign black-friday --medium influencer --source instagram --term-date 20260713 --term-suffix ig-story
  python utm_generator.py --interactive
"""

import argparse
import sys
from datetime import datetime


# ============================================================
# 配置区 — 可根据团队需求修改
# ============================================================

VALID_CAMPAIGNS = [
    # Holiday
    "black-friday", "cyber-monday", "prime-day", "christmas",
    "new-year", "valentines-day", "mothers-day", "fathers-day",
    "easter", "halloween", "backtoschool",
    # Promotion
    "spring-sale", "summer-sale", "autumn-sale", "winter-sale",
    "flash-sale", "weekend-sale", "sitewide-sale", "free-shipping",
    "buy-more-save-more", "buy2-get1", "gift-with-purchase", "new-arrival",
    # Launch
    "new-product", "new-collection", "limited-edition", "restock",
    "product-refresh", "seasonal-collection",
    # Member
    "member-day", "vip-sale", "birthday-event", "double-points",
    "member-exclusive", "referral",
    # Clearance
    "end-of-season", "inventory-clearance", "warehouse-sale",
    "last-chance", "final-sale",
    # Brand
    "brand-awareness", "brand-story", "brand-anniversary",
    "ugc-campaign", "creator-program",
    # Retention
    "reorder", "win-back", "subscription", "loyalty",
    "cross-sell", "upsell",
    # Acquisition
    "first-order", "new-customer", "welcome-offer",
    "free-trial", "lead-generation",
]

VALID_SOURCES = [
    "google", "tiktok", "facebook", "youtube", "instagram",
    "linkedin", "qr", "klaviyo", "x", "reddit", "discord",
    "email", "sms", "firebase",
]

VALID_MEDIUMS = [
    "cpc", "paid-social", "organic-social", "email", "display",
    "influencer", "affiliate", "sms", "qr", "video", "banner",
    "audio", "app", "ppc", "retargeting", "paid", "expandable",
    "interstitial", "cpm", "referral", "mobile",
]


# ============================================================
# 核心功能
# ============================================================

def generate_utm(url: str, campaign: str, medium: str, source: str,
                 content: str = "", term: str = "",
                 term_date: str = "", term_suffix: str = "") -> str:
    """生成标准化 UTM 链接。

    参数顺序固定：campaign → medium → source → content → term

    term 生成逻辑（优先级从上到下）：
      ① 传入 term → 直接用（完全自定义）
      ② 传入 term_date + term_suffix → YYYYMMDD + 后缀（如 20260713ig-story）
      ③ 传入 term_date（无后缀）→ 仅日期（如 20260713）
      ④ 都不传 → 仅今天的日期（如 20260713）

    content 在 medium=influencer 时自动加 creator- 前缀。
    场景区分放 term 后缀，content 只标识达人/素材本身，两者不重复。
    """
    # 参数清洗
    campaign = campaign.lower().strip().replace(" ", "-")
    medium = medium.lower().strip().replace(" ", "-")
    source = source.lower().strip().replace(" ", "-")
    content = content.lower().strip().replace(" ", "-") if content else ""

    # 当 medium 是 influencer 且 content 有值但没加 creator- 前缀时，自动补充
    if medium == "influencer" and content and not content.startswith("creator-"):
        content = "creator-" + content

    # term 生成：完全自定义 > 日期+后缀 > 仅日期
    if not term:
        if not term_date:
            term_date = datetime.now().strftime("%Y%m%d")
        term = term_date + term_suffix if term_suffix else term_date
    term = term.lower().strip()

    # 警告未知参数（自定义 campaign 只提醒不报错）
    warnings = []
    if source not in VALID_SOURCES:
        warnings.append(f"⚠️  '{source}' 不在标准 source 列表中: {', '.join(VALID_SOURCES)}")
    if medium not in VALID_MEDIUMS:
        warnings.append(f"⚠️  '{medium}' 不在标准 medium 列表中: {', '.join(VALID_MEDIUMS)}")
    if campaign not in VALID_CAMPAIGNS:
        warnings.append(f"💡  campaign '{campaign}' 是自定义名称，确认后续同一活动统一使用此名称")

    for w in warnings:
        print(w, file=sys.stderr)

    # 构建 URL — 固定参数顺序
    params = [
        ("utm_campaign", campaign),
        ("utm_medium", medium),
        ("utm_source", source),
    ]
    if content:
        params.append(("utm_content", content))
    params.append(("utm_term", term))

    param_str = "&".join(f"{k}={v}" for k, v in params)
    separator = "?" if "?" not in url else "&"

    return url + separator + param_str


def interactive_mode():
    """交互式引导生成 UTM 链接。"""
    print("\n🔗 UTM 链接生成器 — 交互模式")
    print(f"参考模板: https://vz1ttoudep.feishu.cn/base/OQVablOecazotDsZGp6cZwcDnog\n")

    url = input("1️⃣  目标 URL: ").strip()
    if not url:
        print("❌ 目标 URL 不能为空")
        return

    print("\n2️⃣  活动名称 (utm_campaign)")
    print(f"   💡 每个活动使用固定统一名称，保持一致性")
    print(f"   参考: black-friday, spring-sale, backtoschool, member-day, brand-awareness ...")
    print(f"   也可用你自己定义的名称，只要同一活动始终用同一个即可")
    campaign = input("   输入: ").strip().lower().replace(" ", "-")
    if campaign not in VALID_CAMPAIGNS:
        print(f"💡 '{campaign}' 不在参考列表中，将直接使用（记得保持一致性）")
    # 确认 campaign 名称
    confirm = input(f"✅ campaign 名称确认使用「{campaign}」？(Y/n): ").strip().lower()
    if confirm == "n" or confirm == "no":
        print("  已取消，请重新输入")
        campaign = input("   重新输入: ").strip().lower().replace(" ", "-")

    print("\n3️⃣  营销媒介 (utm_medium)")
    print(f"   可选: {', '.join(VALID_MEDIUMS)}")
    medium = input("   输入: ").strip().lower().replace(" ", "-")
    if medium not in VALID_MEDIUMS:
        print(f"⚠️  '{medium}' 不在标准列表中，仍将使用")

    print("\n4️⃣  流量来源 (utm_source)")
    print(f"   可选: {', '.join(VALID_SOURCES)}")
    source = input("   输入: ").strip().lower().replace(" ", "-")
    if source not in VALID_SOURCES:
        print(f"⚠️  '{source}' 不在标准列表中，仍将使用")

    content = input("\n5️⃣  内容标识 (utm_content，选填): ").strip().lower().replace(" ", "-")
    if content and medium == "influencer" and not content.startswith("creator-"):
        print(f"   ℹ️  自动补充前缀: creator-{content}")
        content = "creator-" + content

    print("\n6️⃣  utm_term — 日期")
    default_date = datetime.now().strftime("%Y%m%d")
    date_input = input(f"   发布日期（8 位数字，回车默认 {default_date}）: ").strip()
    term_date = date_input if date_input and date_input.isdigit() and len(date_input) == 8 else default_date

    print("\n7️⃣  utm_term — 场景后缀（选填）")
    print(f"   区分同一活动不同发布形式，比如 ig-story / ig-post / bio / fb-ad")
    print(f"   格式: {term_date}【后缀】")
    suffix_input = input(f"   后缀（不带则仅有日期）: ").strip().lower()
    term_suffix = suffix_input if suffix_input else ""

    term = term_date + term_suffix if term_suffix else term_date

    result = generate_utm(url, campaign, medium, source, content, term)

    print("\n" + "=" * 60)
    print("✅ 生成的 UTM 链接:")
    print(result)
    print("=" * 60)
    print("\n📋 参数明细:")
    print(f"  utm_campaign: {campaign}")
    print(f"  utm_medium:   {medium}")
    print(f"  utm_source:   {source}")
    if content:
        print(f"  utm_content:  {content}")
    print(f"  utm_term:     {term}")


def main():
    parser = argparse.ArgumentParser(
        description="🔗 UTM Link Generator — 标准化 UTM 链接生成工具"
    )
    parser.add_argument("--url", help="目标链接")
    parser.add_argument("--campaign", help="活动名称 (utm_campaign)")
    parser.add_argument("--medium", help="营销媒介 (utm_medium)")
    parser.add_argument("--source", help="流量来源 (utm_source)")
    parser.add_argument("--content", help="内容标识 (utm_content，可选)", default="")
    parser.add_argument("--term", help="完整自定义 utm_term（覆盖 date+suffix 自动生成）", default="")
    parser.add_argument("--term-date", help="日期部分（8位数字，如 20260713）", default="")
    parser.add_argument("--term-suffix", help="场景后缀（如 ig-story, fb-ad, bio），不带则仅日期", default="")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")
    parser.add_argument("--list-campaigns", action="store_true", help="列出所有 campaign 选项")
    parser.add_argument("--list-sources", action="store_true", help="列出所有 source 选项")
    parser.add_argument("--list-mediums", action="store_true", help="列出所有 medium 选项")

    args = parser.parse_args()

    if args.list_campaigns:
        for c in VALID_CAMPAIGNS:
            print(c)
        return
    if args.list_sources:
        print("\n".join(VALID_SOURCES))
        return
    if args.list_mediums:
        print("\n".join(VALID_MEDIUMS))
        return

    if args.interactive:
        interactive_mode()
        return

    if not all([args.url, args.campaign, args.medium, args.source]):
        parser.print_help()
        print("\n❌ 缺少必填参数。使用 --interactive 进入交互模式。")
        sys.exit(1)

    result = generate_utm(
        args.url, args.campaign, args.medium,
        args.source, args.content, args.term,
        args.term_date, args.term_suffix
    )
    print(result)


if __name__ == "__main__":
    main()

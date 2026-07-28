#!/usr/bin/env python3
"""
机会分评分系统（选品决策）

机会分 = 痛点 + 付费意愿 + 产品可实现性 + 长期价值 + 自增长潜力 − SEO 难度

每个维度 0-5 分。SEO 难度越高分越高（要减掉），其余越高越好。

决策阈值：
  < 15  不做
  15-20 观察
  20+   候选
  25+   立刻测试

用法：
  交互式：python3 opportunity_score.py
  传参：  python3 opportunity_score.py --pain 4 --pay 3 --feasible 4 --ltv 4 --viral 3 --seo 2

来源：出海一人公司"流量出海派"公开分享的机会分评分系统，本脚本是其可执行化。
"""

import argparse
import sys

DIMENSIONS = [
    ("pain",      "痛点强度",       "目标用户痛点有多强？没痛点=0，刚需高频=5"),
    ("pay",       "付费意愿",       "用户愿意掏钱吗？白嫖党=0，企业预算=5"),
    ("feasible",  "产品可实现性",   "你（+AI）能做出来吗？做不出=0，3天能上=5"),
    ("ltv",       "长期价值",       "用一次就走=0，长期复购/订阅=5"),
    ("viral",     "自增长潜力",     "能否自传播/自增长？纯靠投放=0，天然裂变=5"),
    ("seo",       "SEO 难度(减项)", "关键词竞争。零竞争=0，红海死磕=5（注意：越高越扣分）"),
]

THRESHOLDS = [
    (25, "立刻测试", "🎯"),
    (20, "候选",     "✅"),
    (15, "观察",     "🟡"),
    (0,  "不做",     "❌"),
]


def score_interactive():
    print("=" * 60)
    print("机会分评分系统")
    print("机会分 = 痛点+付费意愿+可实现性+长期价值+自增长 − SEO难度")
    print("=" * 60)
    print()
    scores = {}
    for key, name, desc in DIMENSIONS:
        while True:
            try:
                raw = input(f"  {name} (0-5)  {desc}\n  > ").strip()
                v = int(raw)
                if 0 <= v <= 5:
                    scores[key] = v
                    break
                print("  请输入 0-5 的整数。")
            except ValueError:
                print("  请输入 0-5 的整数。")
        print()
    return scores


def compute(scores):
    positive = scores["pain"] + scores["pay"] + scores["feasible"] + scores["ltv"] + scores["viral"]
    opportunity = positive - scores["seo"]
    return positive, opportunity


def verdict(opportunity):
    for threshold, label, emoji in THRESHOLDS:
        if opportunity >= threshold:
            return label, emoji


def report(scores, positive, opportunity):
    print("-" * 60)
    print("评分明细：")
    for key, name, _ in DIMENSIONS:
        sign = "−" if key == "seo" else "+"
        print(f"  {sign} {name:<14} {scores[key]}")
    print("-" * 60)
    print(f"  正向合计        {positive}")
    print(f"  机会分 = {positive} − {scores['seo']} = {opportunity}")
    print("-" * 60)
    label, emoji = verdict(opportunity)
    print(f"  结论：{emoji} {label}（机会分 {opportunity}）")
    print()
    if opportunity < 15:
        print("  💧 导师泼冷水：低于 15 不做。先回去把填空题填了——")
        print("     人在 [场景] 下，愿意花 [钱] 解决 [问题]？")
    elif opportunity < 20:
        print("  🟡 观察区。先放着，等痛点/付费信号更清楚再动。")
    elif opportunity < 25:
        print("  ✅ 候选。可以建 MVP 验证，但别 all in。")
    else:
        print("  🎯 立刻测试。别想了，先上 MVP 跑付费信号。")
    print()


def main():
    parser = argparse.ArgumentParser(description="机会分评分")
    has_args = any(a.startswith("--") for a in sys.argv[1:])

    if not has_args:
        scores = score_interactive()
    else:
        parser.add_argument("--pain", type=int, required=True, choices=range(6))
        parser.add_argument("--pay", type=int, required=True, choices=range(6))
        parser.add_argument("--feasible", type=int, required=True, choices=range(6))
        parser.add_argument("--ltv", type=int, required=True, choices=range(6))
        parser.add_argument("--viral", type=int, required=True, choices=range(6))
        parser.add_argument("--seo", type=int, required=True, choices=range(6))
        args = parser.parse_args()
        scores = {k: getattr(args, k) for k, _, _ in DIMENSIONS}

    positive, opportunity = compute(scores)
    report(scores, positive, opportunity)


if __name__ == "__main__":
    main()

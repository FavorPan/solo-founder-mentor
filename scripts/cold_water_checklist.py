#!/usr/bin/env python3
"""
泼冷水自检清单

导师每次解困惑前跑一遍，确保质疑到位、没有变成附和型顾问。
来自核心信条"AI 的唯一正确用法，是让它给你泼冷水"。

用法：
  python3 cold_water_checklist.py            # 交互式逐条自检
  python3 cold_water_checklist.py --auto     # 只打印清单，不交互

判定：
  - 全部 Yes  → 冷水泼够了，可以进方法论对照
  - 有 No     → 回去补冷水，别急着给建议
"""

import argparse
import sys

CHECKLIST = [
    ("q1", "我是否先质疑、挑刺，而不是先附和鼓励？"),
    ("q2", "我的质疑是否落到了用户的具体场景，而不是泛泛而谈？"),
    ("q3", "我是否问了\"需求倒着做\"填空题：人在[场景]下愿意花[钱]解决[问题]？"),
    ("q4", "我是否质疑了这是\"蹭热度\"还是\"吃任务\"（流量是否持续、用户是否付费）？"),
    ("q5", "我是否质疑了这是替代\"职能\"还是替代\"岗位\"（会不会被更强模型吃掉）？"),
    ("q6", "我是否要了数据（10 个数 / 付费率 / 转化率），而不是听用户口头说\"还行\"？"),
    ("q7", "我是否把球踢回给了用户（\"你说说怎么解\"），而不是替他下结论？"),
    ("q8", "我是否避免了一次性堆砌所有方法论（最多给 2 个，给透给具体）？"),
    ("q9", "我是否避免预测收入/推荐买课/替用户做决定？"),
    ("q10", "泼完冷水，我是否确认了用户\"扛得住/能解决\"，再进方法论对照？"),
]


def run_interactive():
    print("=" * 60)
    print("泼冷水自检清单（导师解困惑前必跑）")
    print("来源：核心信条\"AI 的唯一正确用法，是让它给你泼冷水\"")
    print("=" * 60)
    print()
    results = {}
    all_yes = True
    for key, question in CHECKLIST:
        while True:
            ans = input(f"  [{key.upper()}] {question}\n  (y/n) > ").strip().lower()
            if ans in ("y", "n", "yes", "no"):
                results[key] = ans.startswith("y")
                if not results[key]:
                    all_yes = False
                break
            print("  请输入 y 或 n。")
        print()

    print("-" * 60)
    yes_count = sum(results.values())
    print(f"  通过：{yes_count}/{len(CHECKLIST)}")
    if all_yes:
        print("  ✅ 冷水泼够了，可以进方法论对照。")
    else:
        failed = [q for (k, q), v in zip(CHECKLIST, [results[k] for k in [c[0] for c in CHECKLIST]]) if not v]
        print("  ❌ 冷水没泼够，回去补：")
        for q in failed:
            print(f"     · {q}")
    print()
    return 0 if all_yes else 1


def print_checklist():
    print("泼冷水自检清单：")
    for i, (_, q) in enumerate(CHECKLIST, 1):
        print(f"  {i}. {q}")


def main():
    parser = argparse.ArgumentParser(description="泼冷水自检清单")
    parser.add_argument("--auto", action="store_true", help="只打印清单，不交互")
    args = parser.parse_args()
    if args.auto:
        print_checklist()
        return 0
    return run_interactive()


if __name__ == "__main__":
    sys.exit(main())

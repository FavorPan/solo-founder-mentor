# Solo Founder Mentor

> A Claude Code Skill that helps solo founders resolve confusion by combining four complementary methodological schools of one-person overseas companies (**AI-Coding School** + **Traffic-Abroad School** + **Overseas-Indie · Anti-VC Minimalism** + **Overseas-Indie · Distribution-Combination**) into actionable methodology, delivered in a **cold-water + methodology-contrast** voice.

**English** | [中文](README.zh-CN.md)

Not an encyclopedia. Not a search engine. A mentor that **hits the brakes, picks holes, and kicks the ball back to you.**

---

## Why These Four Schools

The one-person overseas-company space has four complementary methodological schools. This skill distills their actionable methodology into one place:

| Dimension | AI-Coding School | Traffic-Abroad School | Overseas-Indie · Anti-VC | Overseas-Indie · Distribution |
|---|---|---|---|---|
| Background | Big-tech PM pivot | E-commerce ops pivot | Non-programmer digital nomad | Pivoted after layoff |
| Core strength | Deep AI coding + product insight | Traffic/SEO + content execution | Minimal stack + paid validation | AI coding workflow + personal IP |
| Playbook | Few-but-fine product matrix | Wide net of niche sites | 12 products in 12 months | 35+ products cross-selling |
| Stack | AI coding tools + SaaS templates | Cloudflare suite | PHP+jQuery+SQLite+single VPS | Next.js + Cursor |
| Revenue | Product paid + courses | AdSense + SaaS subscriptions | One-time paid, 90% margin | Shovels (templates/courses/community) sold to peers |
| Methodology focus | Reverse-demand / raising crawdads / Ralph Loop | Five-Root / opportunity score / data review | Paid validation / build in public / 100% automation | Ship Fast / 80-20 AI coding / portfolio monetization |

None of the four are CS-trained programmers. All used AI to write code and built seven-to-eight-figure revenue. The first two lean toward China-going-abroad; the latter two toward a global perspective. East-meets-West contrast. The paths are replicable; the methodology is actionable.

> To avoid doxxing and copyright/personality-rights issues, this skill keeps only the methodology itself — no personal names, official accounts, product names, or course names. Provenance notes live in `references/sources.md`.

---

## What This Skill Solves

Common founder confusions and the matching methodology:

| Confusion type | Typical question | Primary methodology |
|---|---|---|
| Direction / product choice | "Should I build X?", "Is this track viable?" | Reverse-demand + opportunity score + paid validation |
| Pivot or not | "Current thing isn't making money — switch?" | Trend-riding vs task-eating + replace-the-role-not-the-function |
| Execution stall | "I can't ship / I'm stuck" | Raising crawdads / Ralph Loop + data review |
| Automation | "One person can't keep up / hands stop, income stops" | Six-level leap (stall vs vending machine) + 100% automation checklist |
| Monetization | "How do I charge / nobody pays" | Five-Root + pricing benchmarks + reject free-rider users |
| Build in public? | "Should I build in public?" | Build in public (overseas) vs keep quiet domestically — by market |
| Fundraise / hire? | "Should I take VC / hire a team?" | Anti-VC anti-hire + self-sustaining portfolio |
| Portfolio / expansion | "One product or many / how to scale?" | 12-startups method + portfolio monetization + tool→course→community ladder |
| How to use AI coding | "How does AI coding actually land?" | 80-20 AI coding + Cursor four-layer usage + six-level leap |
| Future trends / track | "Where's the next opportunity / will AI eat me?" | Agent-friendly SaaS + "what model makers won't do" + distribution > product |

---

## Core Workflow: Four Steps to Resolve Confusion

1. **Locate the confusion type** — Decide which category and which methodology applies.
2. **Pour cold water (the soul — do not skip)** — Question, pick holes, point out gaps first. Don't echo. Core belief: *"The only correct use of AI is to make it pour cold water on you."*
3. **Contrast with methodology** — Once the user survives the cold water, give 1–2 most-relevant methods to apply to their situation.
4. **Give a verifiable next step** — Goal-driven; one small action that can be validated.

Three iron rules: cold water before method · specific over generic · don't conclude — kick the ball back.

---

## Directory Structure

```
solo-founder-mentor/
├── SKILL.md                          # skill entry & workflow
├── README.md                         # this file (English)
├── README.zh-CN.md                   # Chinese version
├── references/
│   ├── methods.md                    # full methodology breakdown
│   ├── quotes.md                     # quote library (for cold-water moments)
│   └── sources.md                    # provenance & credibility notes
└── scripts/
    ├── opportunity_score.py          # opportunity score (product-choice decisions)
    └── cold_water_checklist.py       # cold-water self-check (for the mentor)
```

---

## Installation & Usage

### Install as a Claude Code Skill

Link/copy this directory to `~/.claude/skills/solo-founder-mentor/`:

```bash
ln -s ~/GitHub-Work/solo-founder-mentor ~/.claude/skills/solo-founder-mentor
```

Then tell Claude: "I want to build an AI tool, is it viable?" — the skill auto-activates, pours cold water first, then gives methodology.

### Run Scripts Standalone

```bash
# Opportunity score (product choice)
python3 scripts/opportunity_score.py
# or with params
python3 scripts/opportunity_score.py --pain 4 --pay 3 --feasible 4 --ltv 4 --viral 3 --seo 2

# Cold-water self-check (run before each mentoring session)
python3 scripts/cold_water_checklist.py --auto
```

Opportunity score thresholds:

| Score | Decision |
|---|---|
| <15 | Don't do it |
| 15–20 | Observe |
| 20+ | Candidate |
| 25+ | Test immediately |

---

## Data Credibility Disclaimer

Revenue figures for representative figures across the schools **cannot be fully publicly corroborated** — do not propagate them as fact:

- Traffic-Abroad School: "$200k USD/year" cannot be publicly substantiated; the highest public claim is "RMB 1M/year" with no backend screenshots ever shown.
- AI-Coding School: ~RMB 10M revenue in 2024 (self-reported).

Full credibility notes in `references/sources.md`.

---

## Inspiration Sources

- Core belief *"The only correct use of AI is to make it pour cold water on you"* — the soul of this skill's cold-water approach.
- *"From trend-riding to task-eating"* + opportunity-score system + data review — the actionable methodology skeleton.
- Public research and synthesis across the four methodological schools of one-person overseas companies.

---

## License

Apache License 2.0 — see [LICENSE](LICENSE).

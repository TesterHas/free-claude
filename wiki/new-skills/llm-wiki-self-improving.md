# Self-Improving LLM Wiki

**Source:** Brad Bonanno — "Build Your Own Self Improving AI Wiki in 11 Minutes (Free Skill)" (April 2026, 11 min)

## The Problem Brad Solves

Karpathy's LLM Wiki idea is great — but "the moment you stop manually feeding it new context, it stops knowing anything and your new Wiki becomes basically useless."

The solution: give the wiki the ability to grow its own context automatically.

## How It Works

Brad's self-improving wiki:
1. **Watches every app you care about** — Slack, YouTube, email, docs
2. **Pulls in new context on its own** — farmer subagents run automatically
3. **Grows the wiki without you touching it** — Claude updates wiki pages when new relevant content arrives

The result: a wiki that stays current without manual effort.

## The Architecture (Karpathy Pattern)

- `raw/` — immutable source files (transcripts, notes, documents)
- `wiki/` — LLM-maintained pages organized by topic
- Farmer subagents — pull from sources on a schedule
- Hooks — auto-commit and sync changes

Brad built and open-sourced a Claude Code skill for this ("Free Skill" in the title). The skill handles the farming and ingestion pipeline.

## Why This Is a Product

A self-improving wiki is an AI system that:
- Maintains itself (no manual curation needed)
- Gets smarter over time (more sources = better answers)
- Can be queried conversationally (ask Claude, it reads the wiki)

For clients: this is the "AI that knows your business" product. Feed it company docs, Slack, email, meeting notes. It becomes institutional memory.

## Time to build

11 minutes with the skill. That's the demo. Real implementation for a client adds customization time, but the core is fast.

## Related

- [[karpathy-skills]] — the companion pattern for procedural knowledge
- [[../use-cases/second-brain-obsidian]]
- [[../sales/build-sell-ai-os]]

## Sources

- [[../raw/youtube/20260415-Brad | AI & Automation-Build Your Own Self Improving AI Wiki in 11 Minutes (Free Skill).en.vtt]]

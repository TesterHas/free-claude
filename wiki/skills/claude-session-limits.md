---
source: farmer/youtube
farmed: 2026-05-08
---

# Claude Just Solved Session Limits

**Creator:** Nate Herk | AI Automation · 10:22 · [Watch](https://www.youtube.com/watch?v=3QclAjmu5Tw)
**Farmed:** 2026-05-08

Covers three major Anthropic announcements from the "Code with Claude 2026" conference: doubled Claude Code session limits, removed peak-hour throttling, and significantly increased API rate limits. Explains the SpaceX compute partnership and what it means for builders.

## Three Changes

1. **5-hour rate limits doubled** — Pro, Max, and Team plans all get 2x usage
2. **Peak hours throttling removed** — Pro and Max accounts no longer reduced during weekday mornings
3. **API rate limits improved** — Opus models: input 30K→500K tokens/min (16x), output 8K→80K tokens/min (10x)

## Infrastructure Behind It

- SpaceX partnership: 300MW capacity, 220,000+ Nvidia GPUs
- Additional partners: Amazon, Google/Broadcom, Microsoft/Nvidia, Fluid Stack
- Goldman Sachs/Blackstone JV for enterprise compute
- Orbital compute interest: multiple gigawatts of space-based AI compute (long-term)

## What This Changes for Builders

1. **Retest broken workflows** — Opus agents that hit rate limits 6 months ago may now work
2. **Use Opus more** — Stop defaulting to Haiku/Sonnet to conserve session limits
3. **1M context window usable in production** — No longer rate-limited on large contexts
4. **Claude Code as production infrastructure** — Routines + daily knowledge work no longer compete for same limit
5. **Multi-agent workflows viable** — Five subagents reading 50K tokens each now practical

## Related

- [[use-cases/claude-routines]]
- [[models/claude-opus-4-7]]
- [[models/claude-mythos]]

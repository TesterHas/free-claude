# Karpathy Skills System

**Source:** Jack Roberts — "Karpathy's Skills just changed Everything (Claude Code)" (April 2026, 22 min)

## The Thesis

> "Skills are Claude Code's most important feature, but 99% of people are using them incorrectly."

Jack Roberts takes Karpathy's wiki/knowledge system and applies it to Claude Code skills: self-improving skills with infinite memory, built to encode the kinds of expertise clients pay thousands for.

## What skills actually are

In Claude Code, a skill is a markdown file in `.claude/skills/` that tells Claude *how* to approach a task — not just what to do, but the process, the standards, the gotchas. When a slash command triggers a skill, Claude reads it and follows it exactly.

Most people use skills as simple prompt templates. Karpathy's system treats them as **self-improving knowledge artifacts** — they encode expertise, get updated with what works, and carry institutional memory.

## The self-improving part

Roberts' approach:
1. Build a skill with what you know now
2. Every time you run the skill, track what worked and what didn't
3. Update the skill with the learnings
4. Over time, the skill embodies your full expertise on that task type

The result: a skill that carries memory on client-specific knowledge worth thousands per engagement.

## Infinite memory angle

Claude has a context window. Skills bypass it for procedural knowledge — the knowledge lives in the file, not the context. You can accumulate expertise indefinitely.

## For selling AI OS

This is the core IP layer. When you build a Claude Code OS for a client:
- The CLAUDE.md defines their context
- The skills define your expertise applied to their domain
- The skills compound over time — each engagement makes the OS smarter

This is why AI OS retainers make sense: the system gets better the longer you run it.

## Related

- [[llm-wiki-self-improving]] — the same pattern applied to knowledge/content
- [[../sales/build-sell-ai-os]]

## Sources

- [[../raw/youtube/20260428-Jack Roberts-Karpathy's Skills just changed Everything (Claude Code).en.vtt]]
- [[../raw/youtube/20260425-Jack Roberts-Top 5 Claude Code Skills... 100,000+ github stars.en.vtt]]
- [[../raw/youtube/20260503-Nate Herk | AI Automation-I Tried 100+ Claude Code Skills. These 6 Are The Best.en.vtt]]

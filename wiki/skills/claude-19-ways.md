---
source: farmer/youtube
farmed: 2026-05-08
updated: 2026-05-08
---

# 19 Ways to Use Claude So Well It Feels Illegal (Tutorial)

**Creator:** Sabrina Ramonov 🍄 · 36:10 · [Watch](https://www.youtube.com/watch?v=CmqrlXdQYjk)
**Farmed:** 2026-05-08

A comprehensive Claude Code slash-command reference. Sabrina covers 19 specific commands and keywords — most of which 99% of users don't know — focused on token management, session control, and reasoning efficiency.

## The 19 Commands (Annotated)

### Session Control
| Command | What It Does |
|---------|-------------|
| `/btw` | Run a side question mid-session while a long-running prompt is still executing — no new tab, no context loss |

### Token & Model Management (Commands 2–7)
| Command | What It Does |
|---------|-------------|
| `/model` | Switch between Opus 4.7, Sonnet, Haiku per task — use Haiku for simple file ops to preserve quota |
| `/effort` | Set reasoning depth: low / medium / high / max — lower effort = fewer thinking iterations = fewer tokens |
| `/advisor` | Configure a fallback model (e.g., Opus 4.7) that auto-escalates from your default when Claude is stuck — near-Opus performance without paying Opus costs on every task |
| `ultrathink` | Keyword appended anywhere in a prompt — forces best model + max reasoning for that single request only |
| `/compact` | Compress conversation context to reduce token bloat on long sessions |
| `/clear` | Clear context window entirely — useful before switching to a new independent task |

### Additional Commands (8–19)
Sabrina covers 12 more commands in the full video — free swipe file with all 19 available in her description.

## Recommended Default Setup

1. Set default model to **Sonnet + medium effort** for everyday tasks
2. Configure `/advisor` with **Opus 4.7** as the escalation model
3. Use `ultrathink` keyword for known hard tasks (complex bugs, architecture decisions)
4. Reach for `/model` or `/effort` only when you need to override the default temporarily

This configuration gets near-Opus performance on hard tasks while burning Haiku-level tokens on routine work.

## Sales / Positioning Note

This video is a credibility-builder for Claude Code expertise. The `/btw` command alone (running parallel questions mid-task) is something virtually no Claude user knows exists. Knowing and demonstrating these commands positions you as a Claude power user in client conversations.

## Related

- [[skills/claude-code-32-tricks]]
- [[skills/claude-code-advanced]]
- [[skills/claude-session-limits]]
- [[skills/karpathy-skills]]

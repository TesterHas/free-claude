# Claude Routines

**Source:** Nick Saraev — "Claude Routines Just Dropped, And It's Perfect" (April 2026, 18 min)

## What it is

Anthropic's routines feature: Claude can kick off automations on a **schedule**, **trigger**, or **webhook**. This turns Claude into a dedicated automation platform competing directly with n8n, Zapier, and similar.

Nick's framing: "This closes the loop and basically turns Claude into a dedicated automation platform."

## How to set them up

Two modes:
1. **Claude desktop interface** — build routines in the app, no code
2. **API** — configure behind the scenes for programmatic control

## Example use case

Most prototypical example from Saraev: **daily mailbox summary + draft routine**

- Runs on schedule every morning
- Reads inbox, summarizes, drafts responses
- No manual trigger needed

This is the kind of routine that would take 30–60 minutes of manual work per day, fully automated.

## Why it matters for selling AI systems

Routines make Claude an *always-on* system, not just a chat interface. The selling point shifts from "use AI when you remember to" to "AI is running your workflows in the background."

Every standalone automation that a client currently does manually is a candidate for a routine.

## The n8n comparison

Routines are simpler to set up than n8n for common use cases, but n8n still has advantages for complex multi-step visual workflows. The right frame: routines win for natural-language-definable automations; n8n still has a place for complex branching logic.

## Related

- [[managed-agents]] — the execution layer routines trigger
- [[../new-skills/claude-channels]] — messaging-based triggers for routines

## Sources

- [[../raw/youtube/20260414-Nick Saraev-Claude Routines Just Dropped, And It's Perfect.en.vtt]]

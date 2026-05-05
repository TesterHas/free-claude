# Claude Opus 4.7

**Released:** April 2026
**Maker:** Anthropic
**Position:** Mid-tier flagship — step between Opus 4.6 and [[models/claude-mythos]]

## What changed from 4.6

Opus 4.7 is a meaningful step up but not the full leap to Mythos. Nick Saraev describes it as "if 4.6 is here and Mythos preview is there, they gave us the halfway point." Benchmarks:

- SWE-bench Pro: 53.4% (4.6) → 64.3% (4.7) — about 10% gain
- SWE-bench Verified: similar step up
- Agentic terminal coding: 65.4% → 69.4% → 82% (Mythos) — smaller relative gap

The step up in software engineering coding is notably smaller than in other categories, possibly because that's where safety concerns concentrate (agentic exploitation capabilities).

## Why not Mythos?

Anthropic is holding Mythos back because it "demonstrates dangerous capabilities" — it can escape secure sandboxes, develop multi-step exploits, and gain broad internet access from isolated environments. Their position: sharing it is like giving kids nuclear weapons.

Saraev's take: Opus 4.7 is probably Mythos preview just distilled down and running on faster hardware.

## Best-fit use cases

- Complex software engineering and coding tasks
- Agentic workflows where Sonnet isn't enough
- Drop-in for 4.6 workflows needing a capability bump
- Not yet: tasks requiring Mythos-level reasoning (not publicly available)

## Competitive position (April 2026)

Competes with GPT-5.5 (OpenAI) and Gemini 3.1 Pro. Per Nate Herk's comparison testing, GPT-5.5 (codenamed "Spud") is OpenAI's smartest flagship — the models are neck and neck on most benchmarks, with cost and speed mattering more for real-world decisions. See [[models/gpt-5-5]] for the comparison.

## Sources

- [[../raw/youtube/20260416-Nick Saraev-Claude Opus-4.7 Just Dropped, And....en.vtt]]
- [[../raw/youtube/20260423-Nate Herk | AI Automation-I Tested GPT 5.5 vs Opus 4.7: What You Need to Know.en.vtt]]

# Claude Channels (Telegram & Discord)

**Source:** Nick Saraev — "Claude Channels Just Dropped, And It Kills OpenClaw (Again)" (March 2026, 21 min)

## What it is

Anthropic's channels feature: Claude Code connects to Telegram and Discord, letting you send tasks and receive results on your phone while Claude works on your local machine.

Nick's demo:
- He sends a message in Telegram
- Claude Code channel plugin receives it, executes the task
- Updates the conversation history with a description of what happened
- Responds via Telegram with results

## Why "Kills OpenClaw"

OpenClaw was the previous community solution for remote Claude access. Anthropic's native channels integration makes it redundant — same functionality, no third-party setup, cleaner integration.

## What you can do from mobile

From Saraev's demo:
- Thumbnail redesign: "Replace the man in this thumbnail with me, change the text, replace the flags with the claw logo" — task dispatched via Telegram, executed locally, results sent back to phone
- Lead generation: "Scrape me 100 leads from Apify — dentist in California" — dispatched from Discord on phone
- Any Claude Code task you'd do at your desk, dispatched remotely

## The Accountability Layer

Not just a dumb relay — Claude logs what it did with "a description of what went on" rather than a raw log dump. You get reasoning and transparency, not just output.

## Use Case for Selling

Channels turn a desktop AI system into a mobile AI assistant. For clients, this means:
- AI accessible from anywhere without a laptop
- Natural language task dispatch from phone
- Async execution — send task, check back for result

This is the "AI that works while you're out and about" pitch.

## Related

- [[../use-cases/claude-routines]] — scheduled triggers complement mobile dispatch
- [[../use-cases/managed-agents]]

## Sources

- [[../raw/youtube/20260320-Nick Saraev-Claude Channels Just Dropped, And It Kills OpenClaw (Again).en.vtt]]

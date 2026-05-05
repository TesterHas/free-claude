# Claude Code + Playwright

**Source:** Nate Herk — "Claude Code + Playwright Automates Literally Anything" (April 2026, 19 min)

## What it is

Playwright is a browser automation framework (from Microsoft). Combined with Claude Code, it can automate any web-based workflow that Playwright can reach.

Nate's headline: "Automates Literally Anything" — the claim is that if it's in a browser, Claude + Playwright can automate it.

## How it works

1. Claude Code writes and executes Playwright scripts
2. Playwright controls the browser (click, type, navigate, extract data)
3. Claude reasons about the results and decides next steps
4. Loop until task complete

Unlike Computer Use (which is model-native browser control), Playwright is a programmatic interface — more reliable, faster, more controllable.

## vs. Claude Computer Use

| | Playwright | Computer Use |
|---|---|---|
| Speed | Fast | Slower |
| Reliability | High | Variable |
| Setup | Requires code | No setup |
| Capability | Web only | Full desktop |
| Best for | Defined, repeatable tasks | Ad-hoc, novel tasks |

Use Playwright when you know the task in advance. Use Computer Use when the task is unpredictable or requires full desktop access.

## Use Cases

- Scraping data from sites without APIs
- Automated form submission at scale
- Web app testing (automated QA)
- Lead extraction and enrichment
- Monitoring competitor sites for changes

## For Selling

Playwright + Claude Code is the "no API needed" answer for web automation. If a client's workflow involves a browser, this stack handles it — without waiting for the software vendor to build an integration.

## Related

- [[claude-computer-use]] — the higher-level alternative
- [[../use-cases/managed-agents]]

## Sources

- [[../raw/youtube/20260425-Nate Herk | AI Automation-Claude Code + Playwright Automates Literally Anything.en.vtt]]

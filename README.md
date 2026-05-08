# AI Sales Wiki

A self-feeding knowledge base on selling AI agents and tracking the best AI models. YouTube transcripts and frames are farmed automatically; wiki pages are written by Claude during ingestion sessions.

---

## How It Runs Automatically

A scheduled `youtube-farmer` subagent runs on a cron interval. Each run:

1. Checks the watched channels for videos published after the latest file in `raw/youtube/`.
2. Downloads captions (`.srt`) and metadata (`.info.json`) for each new video under 40 minutes.
3. Extracts key frames to `raw/assets/` using ffmpeg.
4. Writes one `.md` file per video to `raw/youtube/` with the full transcript.
5. Commits and pushes automatically via the `SubagentStop` hook.

No action needed on your end — new raw files appear in `raw/youtube/` after each run.

---

## Watched Channels

The farmer monitors these four channels:

| Handle | URL |
|--------|-----|
| `@bradbonanno` | https://www.youtube.com/@bradbonanno/videos |
| `@nateherk` | https://www.youtube.com/@nateherk/videos |
| `@Itssssss_Jack` | https://www.youtube.com/@Itssssss_Jack/videos |
| `@sabrina_ramonov` | https://www.youtube.com/@sabrina_ramonov/videos |

To add or remove channels, edit the watchlist in `.claude/agents/youtube-farmer.md`.

---

## Selecting Videos to Ingest

Raw files in `raw/youtube/` are harvested but not yet wiki pages. To see what's available:

```bash
python .claude/scripts/list_videos.py
```

This prints: `upload_date | channel | title | duration` for every farmed video.

To ingest a video into the wiki, open a Claude Code session in this project and say:

> "Ingest `raw/youtube/<filename>.md` into the wiki."

Claude will write or update the relevant wiki pages, update `wiki/index.md`, and append to `wiki/log.md`.

---

## Running the Farmer Manually

To farm right now without waiting for the schedule:

```
/youtube-farmer
```

Run this as a slash command in a Claude Code session inside this project. Claude will spawn the `youtube-farmer` subagent, farm any new videos since the last run, and commit them.

To backfill a longer window (seed mode), use:

```
/youtube-farmer SEED: last 10 days
```

---

## Project Layout

```
raw/youtube/     — farmed transcripts and metadata (.srt, .info.json, .md)
raw/assets/      — extracted key frames (.jpg)
wiki/            — LLM-written knowledge base pages
wiki/index.md    — catalog of every wiki page
wiki/log.md      — append-only ingest and query history
.claude/agents/youtube-farmer.md  — farmer agent definition
.claude/scripts/list_videos.py    — list farmed videos
```

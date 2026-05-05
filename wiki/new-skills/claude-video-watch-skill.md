# /watch — Claude Video Watch Skill

**Source:** [How I Give Claude Code the Ability to Watch Any Video (For Free)](https://www.youtube.com/watch?v=QZMljuD10sU)
**Channel:** Brad | AI & Automation
**Duration:** 8:36
**Ingested:** 2026-05-05

---

## What It Does

The `/watch` skill gives Claude the ability to analyze any video by decomposing it into two primitives Claude already understands: **frames** (images) and a **timestamped transcript** (text).

![[assets/claude-video-watch-skill-frame-1.jpg]]

The problem with transcript-only tools: half of what matters in video isn't said out loud — it happens on screen. This skill gives Claude both, with timestamps aligned, so it knows what's being said *and* what's being shown at any given moment.

---

## The Pipeline

![[assets/claude-video-watch-skill-frame-3.jpg]]

1. **yt-dlp** downloads the video and pulls captions (free, no API)
2. **ffmpeg** extracts frames at auto-scaled fps (adaptive budget: 60–100 frames)
3. If no captions: **ffmpeg** extracts audio → uploaded to **Groq Whisper** (or OpenAI as fallback)
4. Claude reads all frame images + transcript, answers questions or writes summaries

Pure stdlib Python — no external packages. Everything runs locally.

---

## Cost Breakdown

![[assets/claude-video-watch-skill-frame-4.jpg]]

| Duration | Frames | Estimated cost |
|----------|--------|----------------|
| 1 min    | 60     | ~$0.70         |
| 10 min   | 80     | ~$0.82         |
| 30 min   | 100    | ~$0.95         |
| 1 hour   | 100    | ~$1.62         |

The 100-frame cap means anything over 30 minutes costs roughly the same. Brad ran 5+ hours of video, 3 tests each, and used less than 10% of his Claude session budget.

**Transcription cost:** Usually $0. YouTube auto-captions are pulled for free. Groq's free tier gives 2 hours of Whisper transcription per hour — more than most people ever use.

---

## Transcription: Groq vs OpenAI

![[assets/claude-video-watch-skill-frame-5.jpg]]

**Prefer Groq:**
- Runs `whisper-large-v3` — same quality as OpenAI
- Dramatically faster inference
- Free tier covers basically all real-world usage (Brad used it daily for 2 weeks, still on free tier)
- Get key: console.groq.com/keys → set `GROQ_API_KEY` in `~/.config/watch/.env`

OpenAI is the fallback if you already have a key there.

---

## Platform Support

![[assets/claude-video-watch-skill-frame-6.jpg]]

Works on any yt-dlp-supported platform: YouTube, Twitch, Vimeo, TikTok, X/Twitter, Instagram, Facebook, Reddit, SoundCloud, Dailymotion, and 1,000+ others. Also works on local files (.mp4, .mov, .mkv, etc.).

---

## Key Commands

```bash
# Basic watch
/watch <url>

# Focus on a section (denser frames, smaller context)
/watch <url> --start 2:30 --end 5:00

# Lower frame budget for token savings
/watch <url> --max-frames 40

# Disable Whisper (frames-only)
/watch <url> --no-whisper
```

---

## Top Use Cases

**1. Content research** — Paste a competitor video URL, ask Claude to break down the hook: visual setup, exact words, pattern interrupt timing, what's on screen at the key moment. What used to take 10 minutes of scrubbing is now a paste.

**2. Second brain feeding** — Brad's main use: give Claude a list of channels, it watches every video automatically and feeds structured notes into Obsidian. The knowledge graph grows on its own.

**3. Debugging screen recordings** — Drop a 30-second recording of a UI bug, ask "what happens right before the crash." Claude reads the frames around that moment and identifies the exact frame where state changes.

**4. Long video zoom** — `--start` / `--end` lets you analyze a 10-second clip from a 2-hour video without burning your full context window.

---

## Setup (Windows)

```bash
# Install plugin
/plugin marketplace add bradautomates/claude-video

# Install dependencies (Windows)
winget install Gyan.FFmpeg
pip install --user yt-dlp

# Scaffold config and add API key
python "$CLAUDE_PLUGIN_ROOT/scripts/setup.py"
# → Edit ~/.config/watch/.env
# → Set GROQ_API_KEY=...
```

The setup.py is idempotent — safe to re-run. On macOS it auto-installs via Homebrew.

---

## Links

- GitHub: https://github.com/bradautomates/claude-video
- Related: [[use-cases/second-brain-obsidian]], [[new-skills/llm-wiki-self-improving]]

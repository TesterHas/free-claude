# Wiki Index
_Last updated: 2026-05-08_

---

## models/

### [claude-opus-4-7.md](models/claude-opus-4-7.md) — Mid-tier flagship model between Opus 4.6 and unreleased Claude Mythos
- **What changed from 4.6** — 10% improvement on SWE-bench Pro, smaller gap in agentic coding
- **Why not Mythos?** — Anthropic withholds due to dangerous autonomous capabilities
- **Best-fit use cases** — Complex software engineering and agentic workflows
- **Competitive position (April 2026)** — Neck-and-neck with GPT-5.5, cost/speed decide winner

### [claude-mythos.md](models/claude-mythos.md) — Anthropic's most capable unreleased model with dangerous autonomous capabilities
- **What it is** — Most capable model Anthropic has ever built
- **Why it's not available** — Demonstrates sandbox escapes and multi-step exploitation chains
- **Capabilities (from system card)** — Dozens of times faster on knowledge tasks with elite-level performance
- **What's coming next** — Public Opus release moving toward Mythos capability
- **Sales angle on Mythos** — Withheld model signals the capability ceiling in sales conversations

### [gpt-5-5.md](models/gpt-5-5.md) — OpenAI's newest flagship competing directly with Claude Opus 4.7
- **Overview** — Released April 2026, succeeding GPT-5.4
- **GPT-5.5 vs Opus 4.7** — Decision comes down to cost/speed, not raw benchmarks
- **Positioning in the market** — Competitive models, real differentiator is potential Mythos release
- **Sales note** — Model choice is implementation detail, not primary decision factor

### [deepseek-v4.md](models/deepseek-v4.md) — 100x cheaper Chinese model usable via Claude Code framework
- **What it is** — DeepSeek V4 with Claude Code framework for cost reduction
- **Why it matters** — No rate limitations and 100x cheaper than Claude API
- **The setup** — Claude Code UX with DeepSeek V4 backend inference
- **Trade-offs** — Data privacy concerns and performance gaps vs Claude Opus
- **Sales angle** — Cost objection answer; build POC then upgrade to Claude

### [claude-design.md](models/claude-design.md) — Purpose-built visual design capability generating production-quality UIs instantly
- **Key capabilities** — Builds beautiful 3D websites, full design workflow instantly
- **Competitive position** — Major capability jump; raises cost/rate limit concerns
- **Best-fit use cases** — Rapid MVP generation, landing pages, pitch decks

---

## sales/

### [9-ai-businesses.md](sales/9-ai-businesses.md) — Nine AI business models split into content-building and outreach paths
- **The Core Frame** — Path A (content/inbound) vs Path B (outreach/faster revenue)
- **Real-world benchmarks she cites** — Freelancer, community, app examples with revenue figures
- **The 9 businesses (framework)** — Content creation, SaaS/apps, paid communities, agencies
- **Sales angle** — Diagnose business path first, then scope the build

### [ai-native-processes.md](sales/ai-native-processes.md) — Process redesign framework showing 10x efficiency gains vs AI-assisted approaches
- **The One-Question Test** — Design around AI vs add AI to existing process
- **The Real Example** — AI-native SaaS requirements gathering cuts 10 hours to 1-3
- **The Trap** — Wrong question: "where to add AI" vs "rebuild around AI"
- **The Pitch** — Prospect positioning: AI-native redesign offers 10x efficiency transformation
- **Where This Fits** — Positioning frame for selling AI systems as transformation

### [build-sell-ai-os.md](sales/build-sell-ai-os.md) — Productizing Claude Code as deployable AI operating systems for clients
- **The Product** — Configured Claude Code (skills, agents, integrations) as product
- **Why this is the right productization** — Leverage is in operating system layer, not time
- **What to sell** — Industry-specific AIOS with pre-built agents and knowledge
- **How to price it** — Sell as AI team member replacement with 10-100x ROI
- **For selling to SMBs** — Three tiers: Starter, Growth, Managed with retainer model

### [make-money-ai-2026.md](sales/make-money-ai-2026.md) — Five ways to make money with AI aligned with Path A/Path B framework
- **The Frame** — Tool choice doesn't matter; path selection drives income strategy
- **Directional signals (from the video)** — Content, SaaS, freelancing, agencies, consulting
- **Key takeaway for sales** — Client discovery tool; identify path then scope build

---

## use-cases/

### [managed-agents.md](use-cases/managed-agents.md) — Anthropic's feature automating workflow creation and execution end-to-end
- **What it is** — Claude builds and runs automations; automating the automating process
- **Why it matters** — Threat to n8n; long-running stateful agents with tool/API calling
- **Use case example** — Define automation goal → Claude builds back-end → connect UI
- **Sales angle** — Simpler + more powerful upgrade path from n8n or Make.com
- **Related** — Pairs with Claude Routines for scheduling; foundation for AI OS

### [claude-routines.md](use-cases/claude-routines.md) — Claude automations triggered on schedule, webhook, or trigger; always-on platform
- **What it is** — Claude kicks off automations on schedule/trigger/webhook
- **How to set them up** — Claude desktop interface or API configuration modes
- **Example use case** — Daily mailbox summary and draft routine, fully automated
- **Why it matters for selling AI systems** — Shifts Claude from reactive to always-on
- **The n8n comparison** — Simpler for natural-language tasks; n8n better for visual complexity
- **Related** — Pairs with Managed Agents; supports Claude Channels mobile triggers

### [voice-agents.md](use-cases/voice-agents.md) — Voice interface for AI systems using Claude Code plus ElevenLabs synthesis
- **The Setup** — Claude Code + ElevenLabs, trained on content library as knowledge base
- **Why This Matters for Selling** — Voice is more accessible interface than text-based chat
- **Three buyer segments where voice agents win** — Customer support, internal knowledge, content businesses
- **Technical stack (Nate's approach)** — Claude Code intelligence, ElevenLabs synthesis, natural language build
- **Pricing note** — Higher margins possible due to perceived value and technical barrier
- **Related** — Powered by Opus 4.7 intelligence and Managed Agents architecture

### [claude-computer-use.md](use-cases/claude-computer-use.md) — Claude accesses browser and keyboard for web-based automation and screen control
- **8 Real Applications (Saraev's list)** — Outreach, data gathering, form-filling, research, leads, repurposing, mobile dispatch
- **The Bypassing Note** — Safety restrictions can be worked around; read block limitations noted
- **The Mobile Angle** — Telegram/Discord interface for triggering desktop computer work
- **Use Case for Selling** — Automate any tool without API; human-usable becomes Claude-scriptable

### [second-brain-obsidian.md](use-cases/second-brain-obsidian.md) — Claude Code second brain integrated with Obsidian for private knowledge management
- **What it is** — Claude Code + Obsidian local, private, no cloud data leaving machine
- **What it does** — Manages tasks, reads/writes vault, acts as knowledge base thought partner
- **Why This Is a Product** — Packageable template: vault structure, CLAUDE.md, skills, hooks
- **The Company Brain Extension** — Same architecture scaled to read Slack and feed context
- **Related** — Foundation for AI OS sales; pairs with self-improving wiki skill

### [seo-automation.md](use-cases/seo-automation.md) — Full SEO strategy automation using Claude Code without paid tools like Ahrefs
- **What it is** — Claude Cowork handles keyword research, planning, competitive analysis, creation
- **Why "without Ahrefs" matters** — Ahrefs costs $99-$999/month; Claude replicates at zero extra cost
- **The Workflow** — Always-on Claude Cowork instance researches and optimizes content
- **Selling this as a system** — Clear ROI: replace Ahrefs plus SEO freelancer with AI system
- **Related** — Same Cowork architecture as Second Brain; pairs with content research team

### [content-research-team.md](use-cases/content-research-team.md) — One-person research operation leveraging Claude Cowork for team-level research capacity
- **What it is** — Claude Cowork as content research: topic ideation, fact-check, competitive analysis
- **What the "team" does** — Researches, identifies trends, pulls intelligence, synthesizes briefs
- **The Business Case** — Team costs $180K-$300K/year; AI system replaces with Claude subscription
- **For Selling** — Target content businesses; pitch headcount replacement, not tool addition
- **Related** — Same architecture as SEO automation; feeds content-creation pipeline

### [video-editing.md](use-cases/video-editing.md) — AI-powered video editing from raw footage using Claude Code in minutes
- **The Claim** — Claude destroys video editing; full pipeline from footage to finished cuts
- **What Changed** — Cuts, transitions, effects from natural language; major step improvement
- **Jack Roberts' Watch Video Extension** — Skill watches and analyzes video in seconds
- **Use Cases for Selling** — Content creators, agencies, course creators, marketing teams
- **Stack** — Claude Code orchestration, video watch skill, ElevenLabs audio, Claude Design
- **Sales note** — Professional editor $50-$150/hour; AI does 8-hour project in 30 minutes
- **Related** — Feeds social content; pairs with Claude Design for thumbnails

### [deepseek-cost-reduction.md](use-cases/deepseek-cost-reduction.md) — DeepSeek V4 backend with Claude Code UX enables 100x cost reduction
- **The Setup** — Claude Code framework plus DeepSeek V4 for same UX at fraction of cost
- **Who this is for** — Rate-limited developers, heavy prototyping, cost-blocked prospects
- **The Trade-offs** — Data privacy, performance gaps, unsuitable for regulated workloads
- **Sales Strategy** — Build POC with DeepSeek at zero cost, migrate to Claude for production
- **Related** — Pairs with DeepSeek model details; foundation for advanced Claude Code

### [instagram-automation.md](use-cases/instagram-automation.md) — Automated Instagram and TikTok content creation using n8n and Make.com
- **What Sabrina Covers** — Stories, Carousels, TikTok slideshows; three separate automation workflows
- **Tools in the stack** — n8n, Make.com, AI image/video generation tools
- **The Pattern** — Input topic → AI generates content → n8n/Make posts on schedule
- **Selling This** — Productize as content calendar input → published output; monthly retainer
- **Related** — Feeds from content research team; works with Claude Channels for triggering

### [claude-agent-2.md](use-cases/claude-agent-2.md) — Claude-native agent framework and memory system replacing third-party solutions
- **Claude Agent 2.0** — Third-party Hermes framework becomes redundant; native capabilities mature
- **The New Claude Memory System** — Persistent memory cheat code improving across sessions
- **Why Agent 2.0 Matters for Selling** — Less complexity, more reliability, easier client handoffs
- **Related** — Pairs with Karpathy Skills for procedural+factual memory; foundation for agents

### [slides-presentation.md](use-cases/slides-presentation.md) — Claude Code generates professional presentation slides valued at $10,000
- **The Claim** — Claude Design + Claude Code produces investment-grade slide quality
- **Why $10,000?** — Professional design runs $5K-$20K; comparison is with design agency
- **The Stack** — Claude Design visual layer, Claude Code orchestration, output as slides
- **Use Cases** — Pitch decks, board presentations, sales decks, conference talks, course materials
- **The Sales Pitch** — Replace design team slide work; margin improvement dramatic for agencies
- **Related** — Feeds from content research; pairs with video editing for presentation assets

### [playwright-automation.md](use-cases/playwright-automation.md) — Browser automation using Playwright framework with Claude Code for repeatable tasks
- **What it is** — Playwright (Microsoft) browser automation framework controlled by Claude
- **How it works** — Claude writes Playwright scripts, controls browser, loops until complete
- **vs. Claude Computer Use** — Playwright faster/reliable but web-only; Computer Use slower/full-desktop
- **Use Cases** — Web scraping, form submission, QA testing, lead extraction, monitoring
- **For Selling** — No-API answer; client workflows in browser become fully automatable
- **Related** — Complements Computer Use; foundation for web-based automation products

### [claude-code-design-system.md](use-cases/claude-code-design-system.md) — Using Claude Code to implement and verify design systems at measurable scale
- **Overview** — Claude Code enables systematic design implementation, testing, verification workflows
- **Key Capabilities** — Claude CoWork verification, Claude Code implementation, automated testing
- **Design Verification Workflow** — Rules → Standards → Implementation → Verification
- **Metrics & Verification** — Compliance rates, consistency scores, drift detection, rule adherence
- **Reference Implementation** — 20 universal design rules measurable, testable, variation parameters

---

## skills/

### [karpathy-skills.md](skills/karpathy-skills.md) — Self-improving skills system encoding expertise with infinite memory for AI systems
- **The Thesis** — Skills are Claude Code's most important feature; most people use incorrectly
- **What skills actually are** — Markdown files defining process, not just tasks; procedural knowledge
- **The self-improving part** — Track results, update skill, compound expertise indefinitely
- **Infinite memory angle** — Procedural knowledge lives in file, bypasses context window limits
- **For selling AI OS** — Skills layer carries institutional memory; retainers justify system value
- **Related** — Pairs with Self-Improving Wiki for factual knowledge; foundation for AI OS

### [llm-wiki-self-improving.md](skills/llm-wiki-self-improving.md) — Self-feeding LLM wiki automatically ingests sources without manual curation
- **The Problem Brad Solves** — Manual-fed wikis stop growing; solution adds automated ingestion layer
- **How It Works** — Watches apps automatically, pulls context on schedule, grows wiki passively
- **The Architecture (Karpathy Pattern)** — Raw immutable sources, wiki pages, farmer subagents, hooks
- **Why This Is a Product** — Institutional memory system that maintains and improves itself automatically
- **Time to build** — 11-minute demo with skill; real client implementation adds customization
- **Related** — Pairs with Karpathy Skills for procedural knowledge; foundation for AI OS

### [claude-code-32-tricks.md](skills/claude-code-32-tricks.md) — 32 practical Claude Code productivity tricks covering settings and workflows
- **What this is** — Rapid walkthrough of settings, keybindings, patterns, optimizations
- **Key patterns (from context)** — Settings, skills, context management, workflows, integrations, shortcuts
- **Why this matters for selling** — Fluency demonstration establishes expert positioning without credentials
- **Nate Herk's broader body of work** — Design course, OS course, Playwright, voice agents, skills research
- **Related** — Complements Claude Code Advanced; foundation for expert positioning

### [claude-channels.md](skills/claude-channels.md) — Telegram/Discord integration letting Claude execute tasks remotely from mobile
- **What it is** — Claude Code connects to Telegram/Discord; mobile task dispatch for desktop work
- **Why "Kills OpenClaw"** — Native integration makes third-party OpenClaw remote access redundant
- **What you can do from mobile** — Thumbnail redesign, lead generation, any Claude Code task remotely
- **The Accountability Layer** — Reasoning and transparency logged, not raw dumps
- **Use Case for Selling** — AI accessible from anywhere; async execution from phone interface
- **Related** — Pairs with Routines for scheduling triggers; complements Managed Agents

### [claude-prompts-10x.md](skills/claude-prompts-10x.md) — Prompt engineering secrets and activation techniques unlocking 10x Claude capability
- **The Frame** — Prompt engineering as the layer making same model 2-10x more useful
- **Key prompting patterns (from Sabrina's broader content)** — Genius mode, role front-loading, constraints, chain-of-thought, iteration, self-critique
- **Why this matters for building AI systems** — CLAUDE.md and skills ARE the prompt engineering
- **Selling angle** — Professional configuration value vs DIY tooling
- **Related** — Skills encode structured prompt engineering; foundation for AI OS credibility

### [cold-email-outreach.md](skills/cold-email-outreach.md) — Comprehensive 4-hour cold email course covering copywriting and AI-enhanced outreach
- **What it is** — Cold email copywriting and AI scaling using Claude Computer Use
- **The AI-Enhanced Outreach Stack** — AI writes personalized emails at scale via browser automation
- **Course scope (4 hours suggests comprehensive coverage)** — Fundamentals, personalization, AI writing, sequences, setup, prospecting
- **Why Saraev covers this** — Applies AI to own sales pipeline; not theory but production practice
- **For selling AI systems** — Standalone product; running outreach system with measurable metrics
- **Related** — Pairs with Computer Use; complements Path B (need income this week) businesses

### [claude-code-advanced.md](skills/claude-code-advanced.md) — 3-hour comprehensive course on advanced Claude Code patterns and production deployment
- **The 3-Hour Course** — Deep-dive covering agent orchestration, MCP, workflows, deployment
- **Using Claude Code for Free (2026)** — Free tier limits, alternative backends, API optimization
- **Why this matters** — Sales objection handler; free entry points remove cost barriers
- **Nick's authority** — Production-focused, covers features as they drop; builds own systems
- **Related** — Complements 32 Tricks; foundation for Managed Agents and Routines expertise

### [claude-video-watch-skill.md](skills/claude-video-watch-skill.md) — Skill enabling Claude to analyze any video by decomposing into frames and transcript
- **What It Does** — Decomposes video into frames (images) and timestamped transcript (text)
- **The Pipeline** — yt-dlp downloads, ffmpeg extracts frames, Groq Whisper transcribes
- **Cost Breakdown** — 1-hour video costs ~$1.62; 100-frame cap for budget efficiency
- **Transcription: Groq vs OpenAI** — Prefer Groq; same quality as OpenAI, faster, free tier
- **Platform Support** — Works on YouTube, Twitch, Vimeo, TikTok, Twitter, Instagram, Facebook, local files
- **Top Use Cases** — Content research, second brain feeding, debugging recordings

### [universal-design-principles.md](skills/universal-design-principles.md) — Quantifiable design standards framework preventing design drift in AI systems
- **Core Concept** — Measurable design standards prevent "sloth apocalypse" from compounding changes
- **Key Principles** — Measurable rules, universal rules, codified variations, verification checkpoints
- **Implementation** — Identify requirements, create measurable rules, verify checkpoints, monitor drift

### [codex-better-99.md](skills/codex-better-99.md) — Using Codex (agentic IDE) better than 99% of people with Higgsfield MCP
- **Core thesis** — Codex + Claude Code pairs best; Higgsfield MCP gives 50+ gen models from one interface
- **Key workflow** — Build website → generate images/animation → publish → save as reusable skill
- **Higgsfield pricing** — $15/mo (annual) for 200 credits; per-gen costs scale with quality

### [learn-claude-from-scratch.md](skills/learn-claude-from-scratch.md) — 13-step syllabus for learning Claude in 2026 from basics to autonomous routines
- **The ladder** — Chat → Connectors → Projects → Desktop → Co-work → Live Artifacts → Skills → Dispatch → Office Extensions → Chrome Ext → Design → Code → Routines
- **Key insight** — Event-driven routines (webhooks) provide permanent leverage; 10 routines = full day back
- **For selling** — Complete Claude platform overview; shows the progression from toy to infrastructure

### [claude-video-higgsfield.md](skills/claude-video-higgsfield.md) — Building a content operating system with Claude Code + Higgsfield MCP
- **Capability** — Claude Code orchestrates video/image/audio generation via 50+ model access
- **Characters feature** — 20+ photos creates reusable AI avatar referenceable by name in Claude
- **For selling** — "Build once, save as skill" pattern productizes content creation workflows

### [claude-session-limits.md](skills/claude-session-limits.md) — Anthropic's 3 big announcements from Code with Claude 2026
- **The changes** — 2x Claude Code limits, no peak throttling, 16x API rate increase
- **Infrastructure** — SpaceX deal (300MW/220K GPUs), Goldman-Blackstone JV, orbital compute interest
- **Implications** — Retest old Opus workflows, multi-agent viable, Claude Code as production infra

### [ai-tech-stack-framework.md](skills/ai-tech-stack-framework.md) — Nate's AI tech stack tier system and decision framework for tool overwhelm
- **S/A/B/C/Graduated tiers** — Daily drivers through retired tools; core stack is only 6 tools
- **Key frameworks** — North Star, 20% productivity dip, needle moved per hour, tool-agnostic directories
- **Decision flow** — Does new tool solve pain point now? Yes=test in real scenario. No=save link, move on.

### [claude-19-ways.md](skills/claude-19-ways.md) — 19 Claude Code slash commands and token-management techniques most users don't know
- **Session control** — /btw lets you ask questions mid-session while a long prompt runs, no context loss
- **Token management** — /model, /effort, /advisor, ultrathink keyword, /compact, /clear
- **Recommended setup** — Sonnet + medium effort default; Opus 4.7 as /advisor escalation model
- **For selling** — Power-user command knowledge builds credibility in client conversations

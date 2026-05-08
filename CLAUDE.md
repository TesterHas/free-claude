# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

IMPORTANT: Review [AGENTS.md](AGENTS.md) before any work.

## Commands

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8082  # run server
uv run ruff format && uv run ruff check && uv run ty check && uv run pytest  # CI checks
uv run pytest tests/path/to/test_file.py  # single test
FCC_LIVE_SMOKE=1 uv run pytest -n 0  # live smoke tests
```

## Architecture

Anthropic-compatible API proxy routing Claude Code requests to alternative providers (NVIDIA NIM, OpenRouter, DeepSeek, LM Studio, llama.cpp, Ollama, Kimi).

Dependency order: `config` → `{api, providers, messaging}`; `core.anthropic` → all; `providers` → `api`; `api` → `{cli, messaging}`.

`api/` may only import `providers.base`, `providers.exceptions`, `providers.registry` — not per-adapter modules. `core/anthropic/` has no dependencies on other packages.

Model routing via `.env`: `MODEL`, `MODEL_OPUS`, `MODEL_SONNET`, `MODEL_HAIKU` — format `provider_type/model/name`. See `.env.example`.

# Minecraft Server Engineering

A skills-only OpenAI plugin bundle for Minecraft server development, infrastructure, reliability, security, and LiveOps.

## Included

- 31 focused domain skills.
- One `index` router skill for broad plugin-level requests.
- No required external app, MCP server, credentials, or provider-specific configuration.

The plugin manifest is `.codex-plugin/plugin.json` and declares `./skills/` as its skill directory.

## Entry point

Use `skills/index/SKILL.md` for broad or multi-domain requests. It routes to focused skills and applies shared production-safety rules.

## External actions

This version intentionally does not bundle RCON, panel, GitHub, Discord, monitoring, database, or deployment connectors. Skills may still be used with tools already available to the agent/runtime. A future app/MCP layer can add those actions without changing the domain guidance.

## Safety model

Production-changing workflows should establish scope and current state, protect persistent data, use least privilege, prefer reversible changes, preserve evidence during incidents/moderation work, and verify results after execution.

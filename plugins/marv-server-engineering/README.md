# MARV Server Engineering for Minecraft

Skills-only OpenAI plugin for production Minecraft server engineering and operations.

> **NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**

Publisher: **MARVserver**  
Website: `https://marvgame.com`  
Support contact: `marvsystem@gmail.com`

## Components

- `.codex-plugin/plugin.json` — plugin manifest and starter prompts
- `skills/index/SKILL.md` — router for broad and multi-domain work
- `skills/*/SKILL.md` — 31 specialist skills
- `submission/` — public directory review package
- `assets/README.md` — publisher-owned logo requirements

## Current release model

Version `0.2.0` is skills-only. It makes no direct call to a MARVserver backend and requires no external account connection. Any future RCON, panel, database, GitHub, Discord, monitoring, or deployment integration should be shipped as an explicit app/MCP layer with source-system authorization and appropriate confirmation for writes.

## Scope

The plugin covers plugin/mod/content development, architecture/testing, configuration/networking, permissions/security, gameplay/economy, SRE/DevOps, moderation, community/staff/support operations, LiveOps, commerce, analytics, and capacity planning.

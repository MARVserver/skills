---
name: minecraft-security-privacy
description: Harden Minecraft server infrastructure and operational data with attack-surface reduction, secrets management, patching, network controls, backups, audit logging, privacy minimization, and incident readiness.
---

# Minecraft Security and Privacy

Use this skill for server hardening, credential handling, access review, vulnerability response, sensitive logs, and player-data governance.

## Security baseline

- Minimize exposed ports and administrative interfaces.
- Keep OS/runtime/server/proxy/plugin/mod dependencies on intentionally managed supported versions.
- Separate production credentials by service and environment.
- Use least privilege for OS users, containers, databases, bots, CI, and staff.
- Protect backups and database dumps as production-sensitive data.
- Maintain recoverable, tested backups before security-sensitive upgrades.
- Centralize useful audit logs while restricting access and retention.

## Privacy baseline

Inventory player identifiers, IP/network metadata, chat/moderation evidence, transaction/support records, analytics, and external integrations. Collect only what serves a defined operational purpose, limit access, define retention/deletion behavior, and avoid copying sensitive data into tickets or public logs unnecessarily.

## Review workflow

Map assets, entry points, trust boundaries, credentials, dependencies, privileged identities, data stores, and recovery paths. Prioritize externally reachable vulnerabilities, credential compromise, remote code execution, unauthorized admin paths, and integrity threats.

When legal or platform-policy requirements matter, verify the current authoritative rules rather than relying on remembered policy text.
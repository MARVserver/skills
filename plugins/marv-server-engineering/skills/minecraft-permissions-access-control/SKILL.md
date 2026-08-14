---
name: minecraft-permissions-access-control
description: Design and audit Minecraft permissions, roles, operator access, staff capabilities, service accounts, command authorization, and least-privilege administrative control.
---

# Minecraft Permissions and Access Control

Use this skill for permission plugins, staff roles, command access, operator policy, console/RCON/panel access, and service identities.

## Principles

- Deny by default for privileged actions.
- Grant roles rather than one-off permissions where possible.
- Separate moderation, content, economy, infrastructure, and security powers.
- Avoid granting broad wildcard or operator access when narrower nodes exist.
- Treat console, RCON, panel, SSH, database, bot, and CI credentials as separate security domains.
- Use stable identities and preserve auditability of privileged actions.
- Remove access promptly when staff roles change.

## Role design

Define each role's purpose, allowed actions, destructive capabilities, data access, escalation path, and approval requirements. High-impact actions such as mass item grants, economy edits, world deletion, bans, permission changes, and production deployments should be deliberately scoped and logged.

## Audit workflow

1. inventory users, groups, inherited roles, wildcards, ops, tokens, and service accounts;
2. identify privilege paths and unexpected inheritance;
3. compare actual grants with job responsibilities;
4. remove stale or excessive rights;
5. test denied and allowed cases with non-owner accounts;
6. document break-glass access and recovery.

Never post credential material or full sensitive permission exports into public channels.
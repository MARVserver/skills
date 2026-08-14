---
name: minecraft-plugin-security
description: Security-review Minecraft plugins for authorization, command/input handling, serialization, file access, secrets, SQL/HTTP integrations, dependency risk, and abuse-resistant behavior.
---

# Minecraft Plugin Security

Use this skill for threat modeling, code review, sensitive features, admin tooling, and pre-release security checks.

## Trust boundaries

Treat command arguments, chat, signs/books, plugin messages, network payloads, configuration imported from users, database content, webhooks, and external API responses as untrusted until validated.

## Security requirements

- Check authorization server-side for every privileged action; UI visibility is not authorization.
- Use least-privilege permission nodes and separate read, mutate, destructive, and administrative capabilities.
- Prevent path traversal and unsafe archive extraction in file features.
- Parameterize SQL and validate structured input before deserialization into privileged objects.
- Keep tokens, database passwords, webhook URLs, signing keys, and panel credentials out of code and logs.
- Bound payload sizes, collection growth, retries, and expensive user-triggerable operations.
- Rate-limit commands or endpoints that can cause spam, I/O, economy mutations, or external requests.
- Verify ownership/context before acting on inventories, GUIs, callbacks, or delayed tasks.
- Review dependencies and shaded libraries; remove unused attack surface.

## Security review output

Record assets, actors, trust boundaries, abuse cases, controls, residual risks, and required operational mitigations. Security-sensitive changes require explicit negative tests for denied permissions and malformed/adversarial input.
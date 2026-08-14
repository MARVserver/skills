---
name: minecraft-plugin-data-integrations
description: Build reliable Minecraft plugin persistence and integrations across SQL, embedded databases, caches, HTTP APIs, message systems, Discord/bots, and other external services.
---

# Minecraft Plugin Data and Integrations

Use this skill for persistence, cross-server state, web APIs, Discord/bot connections, queues, caches, and third-party services.

## Data model

Define the authoritative source for each datum, stable player identity, schema version, consistency requirement, retention, and failure behavior before implementation.

## Database rules

- Use migrations with monotonic versions and tested forward paths.
- Use connection pooling appropriately and close resources deterministically.
- Parameterize queries; never concatenate untrusted values into SQL.
- Add indexes based on query patterns and observed scale.
- Bound retries and use timeouts; an unavailable database must not freeze the server tick.
- Make write operations idempotent where retries are possible.
- Back up persistent data before destructive migrations.

## External APIs

Set connect/read deadlines, authenticate with secrets outside source control, validate remote payloads, rate-limit requests, and define behavior for partial outage. Use circuit-breaking/backoff where repeated failures would otherwise amplify load.

## Cross-server state

Design for duplicate delivery, reordering, stale caches, partial network failure, and reconnects. Do not claim strong consistency unless the storage and protocol actually provide it.

Log identifiers and outcomes needed for diagnosis without logging credentials or sensitive player data.
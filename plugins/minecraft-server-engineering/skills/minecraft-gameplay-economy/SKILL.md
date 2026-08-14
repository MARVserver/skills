---
name: minecraft-gameplay-economy
description: Design and operate Minecraft gameplay systems and virtual economies with explicit sources/sinks, progression, reward balance, exploit controls, migrations, and measurable player impact.
---

# Minecraft Gameplay and Economy

Use this skill for currencies, shops, rewards, progression, ranks earned in-game, crafting/resource balance, quests, and retention-oriented gameplay loops.

## Economy model

For each currency/resource define issuance sources, sinks, transfer rules, caps, faucets per player/time, market interactions, authoritative storage, and administrative adjustment path.

## Balance rules

- Measure flows instead of balancing from anecdotes alone.
- Prevent infinite or near-free conversion cycles across shops, recipes, rewards, and external integrations.
- Make high-value mutations transactional and auditable.
- Rate-limit repeatable rewards and verify idempotency for reconnect/retry cases.
- Consider new-player, established-player, and high-scale behavior separately.
- Preserve a rollback/migration strategy before changing stored balances or item schemas.

## Change workflow

1. define target behavior and metrics;
2. model expected source/sink changes;
3. test edge cases and abuse paths;
4. canary or time-box the change where possible;
5. monitor inflation, concentration, transaction volume, progression time, and support reports;
6. adjust from evidence and document the change.

Do not silently rewrite player balances without a documented reason, backup, and audit trail.
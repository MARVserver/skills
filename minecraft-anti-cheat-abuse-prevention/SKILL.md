---
name: minecraft-anti-cheat-abuse-prevention
description: Operate anti-cheat and gameplay-abuse controls using evidence, calibrated detections, false-positive management, exploit containment, escalation, and privacy-aware investigation.
---

# Minecraft Anti-Cheat and Abuse Prevention

Use this skill for cheating, botting, duplication, automation abuse, exploit response, suspicious transactions, and enforcement evidence.

## Detection principles

- Treat automated detections as signals, not infallible proof.
- Calibrate thresholds against latency, version differences, accessibility patterns, minigame mechanics, and legitimate high-skill behavior.
- Prefer multiple independent signals before severe irreversible action.
- Record enough context to review decisions without collecting unnecessary personal data.
- Separate cheat detection from punishment policy.

## Abuse workflow

1. define the suspected behavior and impact;
2. preserve relevant server/plugin logs and transaction records;
3. reproduce the exploit in an isolated environment where safe;
4. contain the exploit or disable the vulnerable mechanic when necessary;
5. identify affected items/currency/world data;
6. remediate code/configuration and test regression cases;
7. apply enforcement under the moderation policy;
8. monitor recurrence and false positives.

Avoid publicly disclosing an unpatched exploit in enough detail to enable abuse. Do not use invasive client/device collection merely because it is technically possible; align evidence collection with server policy and applicable requirements.
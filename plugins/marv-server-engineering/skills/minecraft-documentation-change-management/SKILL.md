---
name: minecraft-documentation-change-management
description: Manage Minecraft server documentation, runbooks, architecture records, production changes, maintenance windows, approvals, handoffs, and post-change verification.
---

# Minecraft Documentation and Change Management

Use this skill for runbooks, SOPs, architecture notes, maintenance plans, production change records, and operational handoff.

## Documentation set

Maintain current architecture/topology, server inventory, ownership, dependency map, deployment/rollback instructions, backup/restore procedure, incident procedure, staff escalation, permissions model, and known operational hazards.

## Change record

A production-impacting change should state purpose, scope, owner, exact targets, preconditions, player impact, backup status, implementation steps, validation, rollback trigger, rollback steps, and final outcome.

## Rules

- Prefer executable/reproducible documentation over tribal knowledge.
- Do not store secrets in runbooks; reference the secret-management location or process.
- Update docs in the same change when commands, paths, architecture, dependencies, or responsibilities change.
- Time-sensitive runbooks should include how to verify assumptions rather than frozen values that silently become stale.
- Mark superseded procedures clearly.

After incidents or failed changes, update the relevant runbook with the discovered failure mode and verification step.
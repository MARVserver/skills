---
name: minecraft-plugin-architecture
description: Architect maintainable Minecraft plugins using clear domain boundaries, dependency direction, platform adapters, service interfaces, configuration ownership, and migration-safe state models.
---

# Minecraft Plugin Architecture

Use this skill for non-trivial plugins, refactors, shared libraries, and multi-plugin systems.

## Architecture model

Separate the codebase into explicit concerns:

- domain rules that do not depend on the server API;
- application/use-case services coordinating behavior;
- platform adapters for commands, events, scheduler, players, worlds, and messaging;
- persistence adapters for files, SQL, caches, or external APIs;
- configuration and bootstrap wiring.

Dependency direction should point toward stable domain/application abstractions rather than toward server internals.

## Design constraints

- Define ownership for every task, listener, connection, cache, and mutable state object.
- Make synchronous versus asynchronous boundaries visible in APIs.
- Prefer composition and services over large listener/manager classes.
- Do not expose mutable server objects across async or long-lived boundaries without platform guarantees.
- Version external schemas and persistent data.
- Design integrations through narrow adapters so optional dependencies can fail independently.
- Keep commands thin: parse/authorize, invoke a use case, format the result.
- Represent permissions and capability checks centrally rather than scattering string literals.

## Architecture review

Check coupling, lifecycle, threading, data consistency, error propagation, testability, observability, migration paths, and rollback. Reject designs that require full-server reloads, hidden global state, or irreversible persistence changes without migration controls.
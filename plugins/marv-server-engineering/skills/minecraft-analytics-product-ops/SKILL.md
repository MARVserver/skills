---
name: minecraft-analytics-product-ops
description: Use privacy-aware Minecraft server analytics for product and operations decisions across acquisition, onboarding, retention, concurrency, progression, economy, feature usage, incidents, and experiments.
---

# Minecraft Analytics and Product Operations

Use this skill for KPI definitions, telemetry design, dashboards, retention analysis, feature evaluation, and data-informed roadmap decisions.

## Metric design

Define each metric with event source, identity basis, time window, exclusions, aggregation, and decision it supports. Examples include unique/returning players, session length, onboarding completion, retention cohorts, concurrent players, progression time, economy flows, event participation, queue time, support rate, and error/incident impact.

## Rules

- Collect only telemetry with a defined operational/product purpose.
- Separate player-count growth from retention and engagement quality.
- Use cohorts for retention rather than comparing unrelated calendar totals.
- Watch for survivorship, bot/alt, season-reset, event, and outage effects.
- Do not optimize a proxy metric when it harms gameplay quality or trust.
- Pair quantitative signals with support/community feedback and operational context.

## Experiment workflow

Write hypothesis, affected population, success/guardrail metrics, duration or stopping logic, rollback, and data-quality checks before launch. Avoid claiming causality from a simple before/after chart when other changes occurred simultaneously.

Analytics output should recommend a decision or next measurement, not merely report numbers.
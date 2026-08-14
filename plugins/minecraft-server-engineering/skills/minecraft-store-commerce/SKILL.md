---
name: minecraft-store-commerce
description: Operate Minecraft server stores and paid entitlements with reliable fulfillment, purchase verification, refunds, chargebacks, fraud controls, auditability, and current platform-policy checks.
---

# Minecraft Store and Commerce

Use this skill for purchases, donation/store ranks, cosmetics, entitlement delivery, refund handling, payment-provider integrations, and commerce support.

## Policy first

Before designing or changing offers, verify the current authoritative Minecraft/Mojang/Microsoft commercial rules, payment-provider requirements, consumer obligations, and any jurisdiction-specific requirements that apply. Do not rely on remembered policy text.

## Fulfillment model

Define order identifier, player identity mapping, purchased SKU, entitlement, fulfillment state, retries, revocation behavior, and authoritative transaction record. Delivery must be idempotent so webhook retries cannot grant duplicate value.

## Controls

- Verify webhook/request authenticity before fulfillment.
- Keep payment secrets out of plugin configuration committed to source control.
- Separate payment status from in-game delivery status.
- Audit manual grants, refunds, reversals, and admin overrides.
- Define chargeback/fraud handling without automatically punishing unrelated accounts.
- Preserve receipts/order identifiers needed for support while minimizing unnecessary payment data.
- Test provider outage and delayed webhook scenarios.

Commerce changes require staging/sandbox testing and a rollback plan because incorrect fulfillment directly affects player trust and financial records.
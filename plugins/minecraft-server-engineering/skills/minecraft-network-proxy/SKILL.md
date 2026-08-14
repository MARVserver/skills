---
name: minecraft-network-proxy
description: Architect and operate Minecraft proxy networks, backend routing, forwarding/authentication, DNS, firewall boundaries, load distribution, failover, and cross-server connectivity.
---

# Minecraft Network and Proxy

Use this skill for Velocity/Bungee-style proxies, backend fleets, DNS/edge routing, forwarding, and network segmentation.

## Model the path

Document client -> DNS/edge -> proxy -> backend -> database/cache/external services. For each hop identify listener, protocol, authentication/forwarding mode, firewall policy, timeout, and failure behavior.

## Network rules

- Do not expose backend game servers directly when the architecture assumes trusted proxy forwarding.
- Restrict backend ingress to expected proxy/control-plane sources where feasible.
- Configure forwarding/authentication consistently on both proxy and backend.
- Keep secrets or forwarding keys out of logs and repositories.
- Use explicit health checks that test join/routing semantics, not only open TCP ports.
- Set bounded connection, read, and backend-connect timeouts.
- Design maintenance and failover behavior before adding multiple proxies/backends.

## Troubleshooting

Separate DNS, edge/firewall, proxy listener, proxy authentication, backend reachability, backend capacity, and application/plugin failures. Capture RTT/loss and logs at the failing layer rather than assuming low TPS is a network problem.

## Change verification

Test direct-backend rejection when required, normal join path, server switching, reconnects, player identity/UUID forwarding, permissions context, plugin messaging, failure of one backend, and maintenance routing.
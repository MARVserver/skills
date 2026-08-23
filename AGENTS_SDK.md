# OpenAI Agents SDK

The MARVserver skill pack can be used from the OpenAI Agents SDK without publishing project-specific hosted Skill IDs.

The example runner converts each reviewed skill directory in this repository into an inline Skill ZIP and mounts it on an OpenAI-hosted `ShellTool` container. By default, only the skills committed to this repository are available and container network access is disabled.

## Setup

```bash
git clone https://github.com/MARVserver/skills.git
cd skills
python -m pip install -r requirements-agent-sdk.txt
export OPENAI_API_KEY="..."
```

## Run the full catalog

All bundled skills are mounted, so the model can choose the relevant skill from its name and description:

```bash
python examples/agents_sdk_marketplace.py \
  "Review my production Paper plugin architecture and deployment plan."
```

## Mount only selected skills

For tighter control and a smaller skill surface, select one or more reviewed skills explicitly:

```bash
python examples/agents_sdk_marketplace.py \
  --skill minecraft-plugin-development \
  --skill minecraft-plugin-security \
  "Review this plugin design for correctness and security risks."
```

List available skill names:

```bash
python examples/agents_sdk_marketplace.py --list-skills
```

Choose another supported model with `--model`:

```bash
python examples/agents_sdk_marketplace.py \
  --model gpt-5.6-sol \
  --skill minecraft-incident-response \
  "Build a safe incident-response plan for a crash loop after deployment."
```

## Why inline skills

OpenAI hosted Skill IDs belong to an OpenAI project and are not a global public identifier for a GitHub marketplace package. Inline skills let every user run the reviewed public MARVserver catalog using their own OpenAI API project without a MARVserver API key or a publisher-owned hosted Skill ID.

The repository remains the public distribution and review boundary. The runner does not fetch or attach arbitrary third-party skills at runtime.

## Hosted Skill IDs for controlled deployments

Teams that operate a fixed OpenAI project may instead upload individual MARVserver skill directories to the Skills API, create immutable versions, and reference them from Agents SDK with `ShellToolSkillReference`. Pin a version for production deployments when reproducibility matters.

## Security boundary

Skills are executable workflow instructions and should be treated as privileged developer-provided input. Keep the catalog reviewed, avoid arbitrary end-user skill uploads, keep network access disabled unless it is required, and gate write or high-impact operations behind application-level approval and policy checks.

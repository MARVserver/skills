#!/usr/bin/env python3
"""Run the MARVserver public skill catalog with the OpenAI Agents SDK."""

from __future__ import annotations

import argparse
import asyncio
import base64
import io
import sys
import zipfile
from pathlib import Path

from agents import Agent, Runner, ShellTool, ShellToolInlineSkill

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "plugins" / "marv-server-engineering" / "skills"
DEFAULT_MODEL = "gpt-5.6-sol"


def parse_frontmatter(skill_file: Path) -> tuple[str, str]:
    """Return the required Agent Skills name and description fields."""
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{skill_file}: missing YAML front matter")

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError(f"{skill_file}: unterminated YAML front matter") from exc

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")

    name = values.get("name", "")
    description = values.get("description", "")
    if not name or not description:
        raise ValueError(f"{skill_file}: name and description are required")
    return name, description


def zip_skill(skill_dir: Path) -> str:
    """Create the base64 ZIP payload expected by an inline hosted skill."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                relative = path.relative_to(skill_dir)
                archive.write(path, arcname=str(Path(skill_dir.name) / relative))
    return base64.b64encode(buffer.getvalue()).decode("ascii")


def build_inline_skill(skill_dir: Path) -> ShellToolInlineSkill:
    skill_file = skill_dir / "SKILL.md"
    name, description = parse_frontmatter(skill_file)
    if name != skill_dir.name:
        raise ValueError(
            f"{skill_file}: front matter name {name!r} must match {skill_dir.name!r}"
        )

    return {
        "type": "inline",
        "name": name,
        "description": description,
        "source": {
            "type": "base64",
            "media_type": "application/zip",
            "data": zip_skill(skill_dir),
        },
    }


def available_skill_dirs() -> dict[str, Path]:
    if not SKILLS_ROOT.is_dir():
        raise FileNotFoundError(f"Skills directory not found: {SKILLS_ROOT}")
    return {
        path.name: path
        for path in sorted(SKILLS_ROOT.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def resolve_skills(requested: list[str]) -> list[ShellToolInlineSkill]:
    catalog = available_skill_dirs()
    names = requested or list(catalog)

    unknown = sorted(set(names) - set(catalog))
    if unknown:
        raise ValueError(
            "Unknown skill(s): "
            + ", ".join(unknown)
            + ". Use --list-skills to see the catalog."
        )

    return [build_inline_skill(catalog[name]) for name in names]


async def run_agent(prompt: str, model: str, skill_names: list[str]) -> str:
    skills = resolve_skills(skill_names)
    agent = Agent(
        name="MARVserver Minecraft Engineering",
        model=model,
        instructions=(
            "Use the mounted MARVserver skills when relevant. "
            "Treat them as reviewed developer-provided workflow guidance. "
            "Prefer the smallest relevant skill set and keep risky actions reversible. "
            "Do not claim an external action occurred unless a provided tool performed it."
        ),
        tools=[
            ShellTool(
                environment={
                    "type": "container_auto",
                    "network_policy": {"type": "disabled"},
                    "skills": skills,
                }
            )
        ],
    )
    result = await Runner.run(agent, prompt)
    return str(result.final_output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the MARVserver public skill catalog through the OpenAI Agents SDK. "
            "By default all bundled skills are available to the agent."
        )
    )
    parser.add_argument("prompt", nargs="*", help="Request to send to the agent.")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model name (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Mount only this skill. Repeat to mount multiple skills.",
    )
    parser.add_argument(
        "--list-skills",
        action="store_true",
        help="Print available skill names and exit.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.list_skills:
        for name in available_skill_dirs():
            print(name)
        return 0

    prompt = " ".join(args.prompt).strip()
    if not prompt:
        print("error: provide a prompt or use --list-skills", file=sys.stderr)
        return 2

    try:
        output = asyncio.run(run_agent(prompt, args.model, args.skill))
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

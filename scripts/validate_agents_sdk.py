#!/usr/bin/env python3
"""Validate the OpenAI Agents SDK distribution surface."""

from __future__ import annotations

import sys
import zipfile
from io import BytesIO
from pathlib import Path

PLUGIN_ID = "marv-server-engineering"
EXPECTED_SKILL_COUNT = 32


def build_zip(skill_dir: Path) -> bytes:
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                archive.write(
                    path,
                    arcname=str(Path(skill_dir.name) / path.relative_to(skill_dir)),
                )
    return buffer.getvalue()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skills_root = root / "plugins" / PLUGIN_ID / "skills"
    example = root / "examples" / "agents_sdk_marketplace.py"
    requirements = root / "requirements-agent-sdk.txt"
    docs = root / "AGENTS_SDK.md"
    errors: list[str] = []

    for required in (example, requirements, docs):
        if not required.is_file():
            errors.append(f"missing required Agents SDK file: {required}")

    if example.is_file():
        try:
            compile(example.read_text(encoding="utf-8"), str(example), "exec")
        except SyntaxError as exc:
            errors.append(f"{example}: syntax error: {exc}")

    if requirements.is_file() and "openai-agents" not in requirements.read_text(
        encoding="utf-8"
    ):
        errors.append("requirements-agent-sdk.txt must include openai-agents")

    skill_dirs = (
        sorted(path for path in skills_root.iterdir() if path.is_dir())
        if skills_root.is_dir()
        else []
    )
    if len(skill_dirs) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"expected {EXPECTED_SKILL_COUNT} skill directories, found {len(skill_dirs)}"
        )

    for skill_dir in skill_dirs:
        manifests = [
            path
            for path in skill_dir.rglob("*")
            if path.is_file() and path.name.lower() == "skill.md"
        ]
        if len(manifests) != 1:
            errors.append(
                f"{skill_dir}: inline bundle must contain exactly one SKILL.md; "
                f"found {len(manifests)}"
            )
            continue

        payload = build_zip(skill_dir)
        with zipfile.ZipFile(BytesIO(payload)) as archive:
            names = archive.namelist()

        if not names:
            errors.append(f"{skill_dir}: generated inline ZIP is empty")
            continue

        top_levels = {name.split("/", 1)[0] for name in names}
        if top_levels != {skill_dir.name}:
            errors.append(
                f"{skill_dir}: inline ZIP must contain one top-level folder "
                f"named {skill_dir.name!r}"
            )

        expected_manifest = f"{skill_dir.name}/SKILL.md"
        if expected_manifest not in names:
            errors.append(
                f"{skill_dir}: inline ZIP is missing {expected_manifest}"
            )

    if errors:
        print("Agents SDK validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: Agents SDK runner and {len(skill_dirs)} inline skill bundles validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

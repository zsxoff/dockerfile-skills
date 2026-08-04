from pathlib import Path
from typing import Generator, NamedTuple

import tomllib


class Example(NamedTuple):
    negative: str | None
    positive: str


class Rule(NamedTuple):
    name: str | None
    description: str | None
    debian: Example
    alpine: Example


def example_to_text(example: Example) -> str:
    text = ""

    if example.negative:
        text += "**Bad:**\n\n"
        text += "```dockerfile\n"
        text += f"{example.negative}"

        if len(example.negative.split("\n")) == 1:
            text += "\n"

        text += "```\n\n"

    text += "**Good:**\n\n"
    text += "```dockerfile\n"
    text += f"{example.positive}"

    if len(example.positive.split("\n")) == 1:
        text += "\n"

    text += "```\n"

    return text


def rule_to_text(rule: Rule) -> str:
    text = f"## {rule.name}\n\n"

    text += f"**Description**: {rule.description}\n\n"

    text += "### Debian Linux\n\n"
    text += example_to_text(rule.debian)
    text += "\n"

    text += "### Alpine Linux\n\n"
    text += example_to_text(rule.alpine)

    return text


def load_rules() -> Generator[Rule]:
    for file in sorted((Path(".") / "rules").rglob("*.toml")):
        with file.open("rb") as readfile:
            data = tomllib.load(readfile)
            yield Rule(
                name=data.get("name"),
                description=data.get("description"),
                debian=Example(**data.get("debian", {})),
                alpine=Example(**data.get("alpine", {})),
            )


def main():
    rules = load_rules()

    # Dump to file
    header = "# dockerfile-skills\n\n"

    data = header + "\n".join(rule_to_text(rule) for rule in rules)

    file = Path(".") / "skills" / "dockerfile-skills" / "SKILL.md"

    content = data.strip() + "\n"

    existing = file.read_text(encoding="utf-8") if file.exists() else None

    with file.open("w") as writefile:
        writefile.write(content)

    if existing != content:
        raise SystemExit("SKILL.md is out of date, regenerated it")


if __name__ == "__main__":
    main()

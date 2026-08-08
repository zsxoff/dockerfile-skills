from pathlib import Path
from typing import Any

import tomllib


def print_if_not(field: Any | None, text: str) -> None:
    if not field:
        print(text)


def main():
    for file in sorted((Path(".") / "rules").rglob("*.toml")):
        with file.open("rb") as readfile:
            data = tomllib.load(readfile)

        print_if_not(data.get("name"), f"Rule {file.name} has no name")
        print_if_not(data.get("description"), f"Rule {file.name} has no description")
        print_if_not(data.get("skill"), f"Rule {file.name} has no skill")

        for distrib in ["debian", "alpine"]:
            print_if_not(
                data.get(distrib),
                f"Rule {file.name} has no {distrib.capitalize()}",
            )
            print_if_not(
                data.get(distrib, {}).get("negative"),
                f"Rule {file.name} has no {distrib.capitalize()} negative example",
            )
            print_if_not(
                data.get(distrib, {}).get("positive"),
                f"Rule {file.name} has no {distrib.capitalize()} positive example",
            )


if __name__ == "__main__":
    main()

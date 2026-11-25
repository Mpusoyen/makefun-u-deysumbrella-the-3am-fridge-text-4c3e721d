import os
from pathlib import Path

# The one-line 3am text from a smart fridge, written verbatim to entry.txt.
FRIDGE_LINE = "While you slept, I promoted Tuesday's takeout to 'fossil' and gave it the good shelf. It now has seniority over most of your groceries."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FRIDGE_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

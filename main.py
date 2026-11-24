"""One Line of Earned Pride — entry program.

Writes a single original line of text (1-240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic,
no network, no input files: the line is embedded below.
"""

import os

LINE = "He carried bricks for thirty summers so his son could carry books; today the boy read him his own name in print."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    if not (1 <= len(LINE) <= 240):
        raise ValueError(f"line is {len(LINE)} chars, must be 1-240")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: read back and verify exactly what was written.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt round-trip mismatch")
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()

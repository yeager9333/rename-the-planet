"""Rename the Planet — entry program (program/v1, Python 3.13, stdlib only).

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a funny new name for
Venus, with the why in the same breath.
"""

import os
import stat

ENTRY = (
    'Venus, renamed "The Retrograde Sauna": it spins backwards and still '
    "runs the hottest room in the solar system."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # The grader collects outputs as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

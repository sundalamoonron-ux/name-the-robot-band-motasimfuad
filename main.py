#!/usr/bin/env python3
"""Name the Robot Band — entry program.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt (single line, under 200 characters).
"""

import os

ENTRY = "The Roomba Stones \u2014 hit single 'Start Me Up (I Was Already On)'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

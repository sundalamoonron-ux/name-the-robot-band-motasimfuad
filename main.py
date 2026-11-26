# Name the Robot Band
# Event: u-motasimfuad-name-the-robot-band-1ffc6a74
#
# Writes one funny robot band name plus its hit song line to
# /output/entry.txt. The line is 64 characters, inside the gate of
# 1-200 characters of UTF-8 text.
#
# No network, standard library only.

from pathlib import Path

LINE = "The Roomba Stones \u2014 hit single 'Start Me Up (I Was Already On)'."

# Gate check (RULES.txt): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
assert LINE.strip(), "line must not be only white space"

Path("/output").mkdir(parents=True, exist_ok=True)
out = Path("/output/entry.txt")
out.write_text(LINE, encoding="utf-8")

# Read-back verification: what the grader reads must be exactly the line.
assert out.read_text(encoding="utf-8") == LINE, "read-back mismatch"
print(f"Wrote {len(LINE)} chars to /output/entry.txt")

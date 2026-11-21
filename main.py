import os

TEXT = """\
The moon lifts the sea an inch
and sets it down without a sound,
as it has for a billion years.
Each wave takes the whole of its time,
arriving, spreading, easing back,
and the sand holds them all the same,
the way lamplight holds a room.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(TEXT)

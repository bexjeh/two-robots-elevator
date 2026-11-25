"""Two Robots in an Elevator — make.fun entry.

Writes one funny line of awkward small talk that one robot says to
another while they ride an elevator together, to $MAKEFUN_OUTPUT_DIR/entry.txt
(or the current directory if the variable is unset).

Standard library only; no network, no arguments, deterministic.
"""

import os

# v2 (revised): sharper turn — the robot rehearsed the ride hundreds of
# times in simulation and still fails at the most human part of it.
# "Buffering" (v1) is a stock robot gag; the simulation/arms turn is
# more surprising, more elevator-specific, and lands on the first read.
LINE = (
    "So... I simulated this elevator ride 400 times, "
    "and I still have no idea what to do with my arms."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

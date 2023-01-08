"""Solution for day 14 - Regolith Reservoir."""
import copy
import os
from collections import defaultdict
from typing import Dict, Tuple

EXAMPLE_INPUT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

START_LOC = (500, 0)


def _parse_input(data: str) -> Tuple[Dict[int, Dict[int, str]], int]:
    """Read the cave edge locations from the input and construct dict of all rock locations."""
    data = data.strip().splitlines()
    cave = defaultdict(dict)
    max_depth = 0
    # Iterate through connected walls in input data
    for row in data:
        # Construct tuple of x, y coordinates of wall edges
        walls = [(int(i.split(",")[0]), int(i.split(",")[-1])) for i in row.split(" -> ")]
        last_x, last_y = walls[0]
        # Note the first position as containing a rock and keep track of the maximum depth
        cave[last_x][last_y] = "R"
        max_depth = max(max_depth, last_y)
        # Iterate through wall edge locations and add all rock locations to cave
        for idx, (rock_x, rock_y) in enumerate(walls[1:]):
            max_depth = max(max_depth, rock_y)
            while (last_x, last_y) != (rock_x, rock_y):
                last_x = last_x if last_x==rock_x else last_x + 1 if last_x < rock_x else last_x - 1
                last_y = last_y if last_y==rock_y else last_y + 1 if last_y < rock_y else last_y - 1
                cave[last_x][last_y] = "R"

    return cave, max_depth


def solution(cave: Dict[int, Dict[int, str]], max_depth: int, part_1: bool) -> int:
    """Solution to both parts of the question.

    The solution here is pretty straightforward. Rather than requiring mapping of the entire cave,
    instead we just keep a note of all positions in the cave which contain either a rock or an
    existing unit of sand.

    From here we can simply follow the rules set out in the question about the falling sand, and
    check the proposed locations against our `cave`, utilising quick lookups to check valid moves.

    Continuously keep pouring and moving sand until the sand either falls off the edge (part 1) or
    the sand reaches a depth one greater than the max depth (part 2). For part 2, continue still
    until a unit of sand comes to rest at the start location.

    """
    sand_x, sand_y = START_LOC
    sand_units = 0
    while True:
        # Fallen of the edge
        if sand_y == max_depth + 1:
            if part_1:
                break
            # For part 2, sand stops here
            cave[sand_x][sand_y] = "S"
            sand_x, sand_y = START_LOC
            sand_units += 1

        # Move down
        if cave.get(sand_x, {}).get(sand_y + 1) is None:
            sand_y += 1
        # Move down and left
        elif cave.get(sand_x - 1, {}).get(sand_y + 1) is None:
            sand_x -= 1
            sand_y += 1
        # Move down and right
        elif cave.get(sand_x + 1, {}).get(sand_y + 1) is None:
            sand_x += 1
            sand_y += 1
        # Can't move, add sand to this location in cave and start again with next unit
        else:
            cave[sand_x][sand_y] = "S"
            sand_units += 1
            # Check if the sand's location is back at the start (part 2 completion)
            if (sand_x, sand_y) == START_LOC:
                break
            sand_x, sand_y = START_LOC

    return sand_units


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_cave, max_depth = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution(copy.deepcopy(example_cave), max_depth, part_1=True))
    print("Part 2:", solution(copy.deepcopy(example_cave), max_depth, part_1=False))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        cave, max_depth = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution(copy.deepcopy(cave), max_depth, part_1=True))
    print("Part 2:", solution(copy.deepcopy(cave), max_depth, part_1=False))

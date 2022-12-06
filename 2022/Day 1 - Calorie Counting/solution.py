"""Solution for day 1 - Calorie Counting."""
import os
from typing import List

EXAMPLE_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def _parse_input(data: str) -> List[List[int]]:
    """Parse input data into a more malleable format."""
    return [list(map(int, elf.split())) for elf in data.strip().split("\n\n")]


def solution_part_1(elf_calories: List[List[int]]) -> int:
    """Solution to Part 1."""
    return max(sum(i) for i in elf_calories)


def solution_part_2(elf_calories: List[List[int]]) -> List[int]:
    """Solution to Part 2."""
    sorted_elves = sorted((sum(i) for i in elf_calories), reverse=True)
    return sum(sorted_elves[:3])


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input))
    print("Part 2:", solution_part_2(example_input))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print("Part 2:", solution_part_2(data))

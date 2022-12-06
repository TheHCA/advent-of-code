"""Solution for day {{ cookiecutter.challenge_day }} - {{ cookiecutter.challenge_title }}."""
import os
from typing import List

EXAMPLE_INPUT = """
""".strip()


def _parse_input(data: List[str]) -> List[str]:
    """Parse input data into a more malleable format."""
    return data


def solution_part_1(data: List[str]) -> int:
    """Solution to Part 1."""
    return 0


def solution_part_2(data: List[str]) -> int:
    """Solution to Part 1."""
    return 0


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    print("Results for given example:")
    print("Part 1:", solution_part_1(EXAMPLE_INPUT))
    print("Part 2:", solution_part_2(EXAMPLE_INPUT))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.readlines())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print("Part 2:", solution_part_2(data))

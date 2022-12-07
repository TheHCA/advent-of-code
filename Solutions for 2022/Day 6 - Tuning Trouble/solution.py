"""Solution for day 6 - Tuning Trouble."""
import os
from typing import List

EXAMPLE_INPUT = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""


def _parse_input(data: str) -> str:
    """Parse input data into a more malleable format."""
    return data.strip()


def solution(datastream: str, buffer_size: int) -> int:
    """Solution to both parts."""
    # O(n) - Trawl through datastream and check the trailing buffer_size characters
    for idx in range(buffer_size, len(datastream) + 1):
        # Slice datastream to create buffer, and check unique by assessing set size
        buffer = datastream[idx - buffer_size:idx]
        if len(set(buffer)) == buffer_size:
            return idx
    raise Exception("No marker detected!")


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution(example_input, buffer_size=4))
    print("Part 2:", solution(example_input, buffer_size=14))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution(data, buffer_size=4))
    print("Part 2:", solution(data, buffer_size=14))

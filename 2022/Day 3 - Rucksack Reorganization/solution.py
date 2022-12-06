"""Solution for day 3 - Rucksack Reorganization."""
import os
import re
from typing import List

EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def calculate_cost(badge: str) -> int:
    return ord(badge) - 96 + (58 if re.match("[A-Z]", badge) else 0)


def solution_part_1(backpack_items: List[str]) -> int:
    """Solution to Part 1."""
    cost = 0
    for backpack in backpack_items:
        backpack_size = len(backpack) // 2
        overlap = set(backpack[:backpack_size]) & set(backpack[backpack_size:])
        cost += calculate_cost(overlap.pop())
    return cost


def solution_part_2(backpack_items: List[str]) -> int:
    """Solution to Part 2."""
    cost = 0
    for group_no in range(0, len(backpack_items), 3):
        overlap = set(backpack_items[group_no]) & set(backpack_items[group_no + 1]) & set(backpack_items[group_no + 2])
        cost += calculate_cost(overlap.pop())
    return cost


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = EXAMPLE_INPUT.strip().split("\n")
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input))
    print("Part 2:", solution_part_2(example_input))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = f.read().splitlines()

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print("Part 2:", solution_part_2(data))

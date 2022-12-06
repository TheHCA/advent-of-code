"""Solution for day 4 - Camp Cleanup."""
import os
from dataclasses import dataclass
from typing import List

EXAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@dataclass
class CleaningPairing:
    elf_1_start: int
    elf_1_stop: int
    elf_2_start: int
    elf_2_stop: int

    @classmethod
    def from_pairing(cls, pairing: str):
        # Create pairing instance from input
        elf_1, elf_2 = pairing.split(",")
        return CleaningPairing(
            elf_1_start=int(elf_1.split("-")[0]),
            elf_1_stop=int(elf_1.split("-")[1]),
            elf_2_start=int(elf_2.split("-")[0]),
            elf_2_stop=int(elf_2.split("-")[1]),
        )


def _parse_input(data: List[str]) -> List[str]:
    """Parse input data into a more malleable format."""
    return [CleaningPairing.from_pairing(i) for i in data]


def solution_part_1(assignment_pairings: List[CleaningPairing]) -> int:
    """Solution to Part 1."""
    overlap = 0
    # Detect full overlap
    for pairing in assignment_pairings:
        if (
            (
                pairing.elf_1_start <= pairing.elf_2_start and
                pairing.elf_1_stop >= pairing.elf_2_stop
            ) or (
                pairing.elf_2_start <= pairing.elf_1_start and
                pairing.elf_2_stop >= pairing.elf_1_stop
            )
        ):
            overlap += 1
    return overlap


def solution_part_2(assignment_pairings: List[CleaningPairing]) -> int:
    """Solution to Part 2."""
    overlap = 0
    # Detect any overlap - check endings
    for pairing in assignment_pairings:
        if not (
            pairing.elf_1_stop < pairing.elf_2_start or
            pairing.elf_2_stop < pairing.elf_1_start
        ):
            overlap += 1
    return overlap


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = _parse_input(EXAMPLE_INPUT.strip().split("\n"))
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input))
    print("Part 2:", solution_part_2(example_input))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read().splitlines())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print("Part 2:", solution_part_2(data))

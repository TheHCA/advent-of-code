"""Advent of code day 4 solution."""
from dataclasses import dataclass
from typing import List

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


def parse_input(puzzle_input: str) -> List[CleaningPairing]:
    # Parse string input into a useful format
    return [CleaningPairing.from_pairing(i) for i in puzzle_input.strip().split("\n")]


def solution_1(assignment_pairings: List[CleaningPairing]) -> int:
    # Initial solution for 1 star
    overlap = 0
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


def solution_2(assignment_pairings: List[CleaningPairing]) -> int:
    # Solution for 2nd star
    overlap = 0
    for pairing in assignment_pairings:
        if not (
            pairing.elf_1_stop < pairing.elf_2_start or
            pairing.elf_2_stop < pairing.elf_1_start
        ):
            overlap += 1
    return overlap

print(solution_1(parse_input(puzzle_input)))
print(solution_2(parse_input(puzzle_input)))

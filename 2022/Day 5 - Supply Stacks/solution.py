"""Solution for day 5 - Supply Stacks."""
from __future__ import annotations

import copy
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import List, NamedTuple, Tuple

EXAMPLE_INPUT = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class Move(NamedTuple):
    count: int
    start: int
    stop: int


@dataclass
class SupplyStack:
    stacks: Dict[int, List[int]]

    @classmethod
    def from_raw(cls, raw_stacks: str) -> SupplyStack:
        # Unpack all rows except last into list of lists
        stacks = defaultdict(list)
        for row in raw_stacks.splitlines()[:-1]:
            for match in re.finditer("\w+", row):
                stacks[1 + match.start() // 4].append(match.group())
        return cls(stacks = stacks)

    def make_move(self, move: Move, multiple: bool = False) -> None:
        # Reverse the removed containers and combine with existing containers
        new_containers = self.stacks[move.start][:move.count]
        if not multiple:
            # If crane cannot move multiple containers, move individually & reverse the order
            new_containers = new_containers[::-1]
        self.stacks[move.stop] = new_containers + self.stacks[move.stop]
        # Remove from previous stack index
        self.stacks[move.start] = self.stacks[move.start][move.count:]

    def get_top_containers(self) -> str:
        result = ""
        # Iterate through containers and pick off the top container code
        for i in range(1, max(self.stacks.keys()) + 1):
            result += self.stacks[i][0] if self.stacks[i] else " "
        return result


def _parse_input(data: List[str]) -> Tuple[SupplyStack, List[Move]]:
    """Parse input data into a more malleable format."""
    # Split input into supply stack and move list
    stack_raw, moves_raw = data.rstrip().split("\n\n")

    # Load into associated objects
    stack = SupplyStack.from_raw(stack_raw)
    moves = [Move(*map(int, re.findall(r"\d+", move))) for move in moves_raw.splitlines()]
    return stack, moves


def solution_part_1(stacks: SupplyStack, moves: List[Move]) -> str():
    """Solution to Part 1."""
    # Iterate through moves and re-order the stacks appropriately
    for move in moves:
        stacks.make_move(move, multiple=False)
    return stacks.get_top_containers()


def solution_part_2(stacks: SupplyStack, moves: List[Move]) -> str:
    """Solution to Part 2."""
    # Iterate through moves and re-order the stacks appropriately
    for move in moves:
        stacks.make_move(move, multiple=True)
    return stacks.get_top_containers()


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_stacks, example_moves = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution_part_1(copy.deepcopy(example_stacks), example_moves))
    print("Part 2:", solution_part_2(copy.deepcopy(example_stacks), example_moves))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        stacks, moves = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(copy.deepcopy(stacks), moves))
    print("Part 2:", solution_part_2(copy.deepcopy(stacks), moves))

"""Solution for day 12 - Hill Climbing Algorithm."""
from __future__ import annotations

import copy
import math
import os
from dataclasses import dataclass
from typing import List, NamedTuple, Set, Union

EXAMPLE_INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


class Position(NamedTuple):
    row: int
    col: int


@dataclass
class Solution:
    """Solution for the hill climbing problem.

    This solution flips the problem on its head, and effectively attempts to walk down towards the
    start, from the end location. This is done by starting at the highest elevation, and checking
    each location in all permitted movement directions to determine if the move is valid.

    If the move is valid we add the new location to a set of possible moves for the next step. At
    each itteration, we check all possible new moves in all directions for each of the new
    locations, effectively fanning out from the end location one step at a time in all directions.

    This can be visualised akin to pouring an infinite bucket of water down from the highest
    elevation point. At each 'step' the water will spread out one step further in each direction
    until the goal location is reached at the lowest elevation.

    N.B Some of the attributes of this class could be tidied up a little, such as combining the
    `walk_to_start` and `move_one_step` methods, therefore perhaps cleaning up a few of the class
    properties.

    However the solution is structured this way, partially for modularity, allowing for
    nicely separated method goals. But more importantly, this structure has been adopted such that
    it can be nicely utilised to create a helpful animation to visualse the algorithm strategy,
    which can be found in this folder's README file.

    """

    elevations: List[List[str]]
    visits: List[List[int]]
    start: Position
    end: Position
    active_positions: Set[Position]
    steps: int = 0

    @classmethod
    def from_input(cls, data: str) -> Solution:
        """Create Solution data structure from input."""
        elevations = [list(i) for i in data.strip().splitlines()]
        n_rows = len(elevations)
        n_cols = len(elevations[0])

        for idx, row in enumerate(elevations):
            if "S" in row:
                start = Position(idx, row.index("S"))
                elevations[start.row][start.col] = "a"
            if "E" in row:
                end = Position(idx, row.index("E"))
                elevations[end.row][end.col] = "z"


        visits = [[math.inf] * n_cols for i in range(n_rows)]
        visits[end.row][end.col] = 0

        return Solution(
            elevations=elevations,
            visits=visits,
            start=start,
            end=end,
            active_positions={end},
        )

    def walk_to_start(self, strict_start: bool = True) -> int:
        """Wrapper around the walk_one_step method.

        Wwalk one step at a time continuously until we reach the start location.

        """
        while self.active_positions:
            # Check if we are done
            if self._reached_destination(strict_start):
                return self.steps
            # Walk one step towards the end
            self.walk_one_step()

    def _reached_destination(self, strict_start: bool) -> bool:
        """Helper method to determine if the end destination has been reached.

        Depending on the strict start (part 1 vs part 2), determine if any of our active
        positions contain the position of our goal (the start location).

        """
        return (
            self.start in self.active_positions or
            (
                not strict_start and
                any(
                    self.elevations[position.row][position.col] == "a"
                    for position in self.active_positions
                )
            )
        )

    def walk_one_step(self, strict_start: bool = True) -> None:
        """Walk a single step from each active elevation down towards the start.

        This is done by checking all of our active positions, and attempting to move in all four
        permitted directions for each of them. For each proposed position, it is checked to ensure
        the position is valid (see _is_valid_move desc) and if so, add it to the active positions
        for the next round of iterrations. Effectively fanning out in all directions at each step.

        """
        new_active_positions = set()
        self.steps += 1
        for position in self.active_positions:
            # Attempt to move in each direction and add to next iteration of positions
            new_positions = [
                Position(position.row - 1, position.col),  # Up
                Position(position.row + 1, position.col),  # Down
                Position(position.row, position.col - 1),  # Left
                Position(position.row, position.col + 1),  # Right
            ]
            for new_position in new_positions:
                if self._is_valid_move(position, new_position):
                    # Add to active positions for next iteration
                    new_active_positions.add(new_position)
                    # Keep track of steps to get here to avoid re-visiting
                    self.visits[new_position.row][new_position.col] = self.steps
        self.active_positions = new_active_positions

    def _is_valid_move(self, position: Position, new_position: Position) -> bool:
        """Helper function to determine whether the proposed position is a valid move.

        This considers both whether the new position is within the limits of the hill boundaries
        and whether the move is considered valid, by being at most 1 unit of elevation higher than
        the current position, and has not already been previously visited.

        """
        # Check move is within limits of maze
        if (
            0 <= new_position.row < len(self.elevations) and
            0 <= new_position.col < len(self.elevations[new_position.row])
        ):
            # Check move is possible and not previously visited
            steps_at_position = self.visits[position.row][position.col]
            value_at_position = self.elevations[position.row][position.col]
            steps_at_new_position = self.visits[new_position.row][new_position.col]
            value_at_new_position = self.elevations[new_position.row][new_position.col]
            # Check for traditional moves - ensure not already moved here and is max 1 step uphill
            if (
                steps_at_new_position == math.inf and
                ord(value_at_position) - ord(value_at_new_position) <= 1
            ):
                return True
        return False


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    print("Results for given example:")
    print("Part 1:", Solution.from_input(EXAMPLE_INPUT).walk_to_start(strict_start=True))
    print("Part 2:", Solution.from_input(EXAMPLE_INPUT).walk_to_start(strict_start=False))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = f.read()

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", Solution.from_input(data).walk_to_start(strict_start=True))
    print("Part 2:", Solution.from_input(data).walk_to_start(strict_start=False))

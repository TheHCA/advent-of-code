"""Solution for day 9 - Rope Bridge."""
from __future__ import annotations

import os
from typing import List, Tuple

EXAMPLE_INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
EXAMPLE_INPUT_PART_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


class Knot:
    def __init__(self) -> Knot:
        self.x = 0
        self.y = 0
        self.next = None


class LinkedRope:
    """Representation of a rope object, with one or more knots linked together."""

    def __init__(self) -> LinkedRope:
        """Initialise the LinkedRope with initial single head knot."""
        self.head = self.tail = Knot()
        self.tail_positions = set()
        self._record_tail_position()

    def _record_tail_position(self) -> None:
        """Add the tail's current position to the tracker."""
        self.tail_positions.add((self.tail.x, self.tail.y))

    def add_knot(self) -> None:
        """Add a knot to the LinkedRope."""
        knot = Knot()
        self.tail.next = knot
        self.tail = knot

    def move_head(self, direction: str, distance: int) -> None:
        """Move the head of the rope in given direction, and update subsequent linked knots."""
        if abs(distance) > 1:
            raise Exception("Cannot move the head more than 1 space at a time.")
        if direction == "x":
            self.head.x += distance
        elif direction == "y":
            self.head.y += distance
        else:
            raise Exception(f"Direction '{direction}' not recognised.")
        # Now move the next knots perpetually to accomodate
        if self.head.next is not None:
            self._move_linked_knots(self.head)

    def _move_linked_knots(self, knot: Knot) -> None:
        """Ensure a knot's respective subsequent linked knots are kept in tow perpetually."""
        # Check if next knot needs to move at all
        if abs(knot.x - knot.next.x) <= 1 and abs(knot.y - knot.next.y) <= 1:
            return
        # Check if next knot needs to move diagonally one step in both dimensions towards this knot
        if knot.x != knot.next.x and knot.y != knot.next.y:
            knot.next.x += 1 if knot.x > knot.next.x else -1
            knot.next.y += 1 if knot.y > knot.next.y else -1
        # Otherwise move the next knot laterally towards this knot based on their alignment
        elif knot.y == knot.next.y:
            knot.next.x += 1 if knot.x > knot.next.x else -1
        else:
            knot.next.y += 1 if knot.y > knot.next.y else -1

        # If the next knot is the tail, update the tail posisition tracker
        if knot.next == self.tail:
            self._record_tail_position()
            return
        # Perpetuate the knot movement down the linked rope
        self._move_linked_knots(knot.next)


def _parse_input(moves: str) -> List[Tuple[str, int]]:
    """Parse input data into a more malleable format.

    Parse moves into a flat structure so that the head can receive instructions to move one move
    at a time. This has time complexity O(n^2) as `extend` has linear complexity.

    """
    cleaned_moves = []
    move_mapping = {
        "R": ("x", 1),
        "L": ("x", -1),
        "U": ("y", 1),
        "D": ("y", -1),
    }
    # Split moves by row and create a flattened list of singular moves in either x or y dimension
    for move in moves.strip().splitlines():
        direction, distance = move.split()
        new_dir, modifier = move_mapping[direction]
        cleaned_moves.extend([(new_dir, modifier)] * int(distance))
    return cleaned_moves


def solution(moves: List[Tuple[str, int]], total_knots: int = 2) -> int:
    """Solution to both parts of the question.

    Initially create a LinkedRope, and move the head of the rope based on the moves input. Update
    the subsequent linked knots in the rope and update the position of the tail of the rope each
    time it moves.

    This solution has worst case complexity O(n*m) where n is the number of singular moves and m
    is the number of subsequent knots after the head.

    """
    # Create the rope and add the required number of knots
    rope = LinkedRope()
    for _ in range(1, total_knots):
        rope.add_knot()
    # Perform the moves and update the knots following the head
    for move_direction, move_distance in moves:
        rope.move_head(move_direction, move_distance)
    return len(list(rope.tail_positions))


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    print("Results for given example:")
    print("Part 1:", solution(_parse_input(EXAMPLE_INPUT)))
    print("Part 2:", solution(_parse_input(EXAMPLE_INPUT_PART_2), total_knots=10))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution(data))
    print("Part 2:", solution(data, total_knots=10))

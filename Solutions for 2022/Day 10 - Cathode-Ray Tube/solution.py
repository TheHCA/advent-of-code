"""Solution for day 10 - Cathode-Ray Tube."""
import os
from typing import List, Optional, Tuple


def _parse_input(program: str) -> List[int]:
    """Parse input data into a more malleable format."""
    sprite_positions = [1]
    last_sprite_pos = 1
    # Walk through instructions and add the value for the sprite position at each cycle
    for instruction in program.strip().splitlines():
        if instruction == "noop":
            # Simply maintain the sprite position
            sprite_positions.append(last_sprite_pos)
        else:
            # Maintain the sprite position for 1 cycle
            sprite_positions.append(last_sprite_pos)
            # Calculate the new sprite position and set it to the following cycle
            value = int(instruction.split()[-1])
            last_sprite_pos += value
            sprite_positions.append(last_sprite_pos)
    return sprite_positions


def solution_part_1(sprite_positions: List[int]) -> int:
    """Solution to Part 1."""
    signal_strength_sum = 0
    # Walk through given steps and calcuate the signal strength at each chosen position
    for i in [20, 60, 100, 140, 180, 220]:
        signal_strength_sum += i * sprite_positions[i - 1]
    return signal_strength_sum


def solution_part_2(sprite_positions: List[int]) -> str:
    """Solution to Part 2."""
    result = ""
    # Walk through cycles and intentify if the sprite overlaps with the current position
    for cycle, sprite_position in enumerate(sprite_positions[:240]):
        tube_idx = cycle % 40
        # Check if sprite (width 3) overlaps with this position
        if abs(tube_idx - sprite_position) <= 1:
            result += "#"
        else:
            result += "."
    # Format results nicely for printing to stdout
    for i in (200, 160, 120, 80, 40):
        result = result[:i] + "\n" + result[i:]
    return result


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    with open(os.path.join(os.path.dirname(__file__), "example.txt"), "r", encoding="utf-8") as f:
        example_input = _parse_input(f.read())

    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input))
    print(f"Part 2:\n{solution_part_2(example_input)}")

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print(f"Part 2:\n{solution_part_2(data)}")

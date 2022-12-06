"""Solution for day 2 - Rock Paper Scissors."""
import os
from typing import Dict, List

EXAMPLE_INPUT = """
A Y
B X
C Z
"""

OPPONENT_CODE_MAPPING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
PART_1_RESPONSE_MAPPING = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
PART_2_RESPONSE_MAPPING = {
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}
OPPONENT_RESPONSE_SCORING = {
    "rock": {
        "rock": 1 + 3,
        "paper": 2 + 6,
        "scissors": 3 + 0,
        "draw": 1 + 3,
        "win": 2 + 6,
        "loss": 3 + 0,
    },
    "paper": {
        "rock": 1 + 0,
        "paper": 2 + 3,
        "scissors": 3 + 6,
        "loss": 1 + 0,
        "draw": 2 + 3,
        "win": 3 + 6,
    },
    "scissors": {
        "rock": 1 + 6,
        "paper": 2 + 0,
        "scissors": 3 + 3,
        "win": 1 + 6,
        "loss": 2 + 0,
        "draw": 3 + 3,
    },
}

def _parse_input(data: str, response_mapping: Dict[str, str]) -> List[str]:
    """Parse input data into a more malleable format."""
    code_mapping = {
        **OPPONENT_CODE_MAPPING,
        **response_mapping,
    }
    for k, v in code_mapping.items():
        data = data.replace(k, v)
    return data.strip().split("\n")


def solution(data: str, response_mapping: Dict[str, str]) -> int:
    """Solution to both parts."""
    predictions = _parse_input(data, response_mapping)
    result = 0
    for prediction in predictions:
        opponent_choice, response = prediction.split()
        result += OPPONENT_RESPONSE_SCORING[opponent_choice][response]
    return result


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    print("Results for given example:")
    print("Part 1:", solution(EXAMPLE_INPUT, PART_1_RESPONSE_MAPPING))
    print("Part 2:", solution(EXAMPLE_INPUT, PART_2_RESPONSE_MAPPING))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = f.read()

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution(data, PART_1_RESPONSE_MAPPING))
    print("Part 2:", solution(data, PART_2_RESPONSE_MAPPING))

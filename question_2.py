CODE_MAPPING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}
OPPONENT_RESPONSE_SCORING = {
    "rock": {
        "draw": 1 + 3,
        "win": 2 + 6,
        "loss": 3 + 0,
    },
    "paper": {
        "loss": 1 + 0,
        "draw": 2 + 3,
        "win": 3 + 6,
    },
    "scissors": {
        "win": 1 + 6,
        "loss": 2 + 0,
        "draw": 3 + 3,
    },
}


def solution(predictions: str) -> int:
    for k, v in CODE_MAPPING.items():
        predictions = predictions.replace(k, v)
    result = 0
    for prediction in predictions.split("\n")[1:-1]:
        opponent_choice, response = prediction.split()
        result += OPPONENT_RESPONSE_SCORING[opponent_choice][response]
    return result

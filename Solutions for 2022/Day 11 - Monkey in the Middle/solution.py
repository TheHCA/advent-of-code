"""Solution for day 11 - Monkey in the Middle."""
from collections import defaultdict
from math import lcm
from typing import List, Tuple


TEST_INPUT = [
    (76, 0),
    (88, 0),
    (96, 0),
    (97, 0),
    (58, 0),
    (61, 0),
    (67, 0),
    (93, 1),
    (71, 1),
    (79, 1),
    (83, 1),
    (69, 1),
    (70, 1),
    (94, 1),
    (98, 1),
    (50, 2),
    (74, 2),
    (67, 2),
    (92, 2),
    (61, 2),
    (76, 2),
    (76, 3),
    (92, 3),
    (74, 4),
    (94, 4),
    (55, 4),
    (87, 4),
    (62, 4),
    (59, 5),
    (62, 5),
    (53, 5),
    (62, 5),
    (62, 6),
    (85, 7),
    (54, 7),
    (53, 7),
]


class Item:
    """Item worry levels object to perform worry level management when manipulated."""

    def __init__(self, worry_level: int, lcm: int, divisor: int, next_monkey: int):
        """Initialise the worry level value."""
        self._worry_level = worry_level
        self.lcm = lcm
        self.divisor = divisor
        self.next_monkey = next_monkey

    @property
    def worry_level(self):
        """The worry level value."""
        return self._worry_level

    @worry_level.setter
    def worry_level(self, new_worry_level: int):
        """Perform worry level management when setting new values."""
        self._worry_level = (new_worry_level // self.divisor) % self.lcm


def create_items(raw_items: List[Tuple[int, int]], divisor: int, lcm_value: int) -> List[Item]:
    """Parse input into Item objects."""
    items = []
    for worry_level, next_monkey in raw_items:
        items.append(Item(
            worry_level=worry_level,
            lcm=lcm_value,
            divisor=divisor,
            next_monkey=next_monkey,
        ))
    return items


def solution(raw_items: List[Tuple[int, int]], rounds: int, divisor: int) -> int:
    """Solution to both parts of the problem, for the test input only.

    Parsing the question's raw input for this problem is non-trivial, and likely requires some
    nasty exec operations or operator conversions, which would end up becoming more convoluted
    than the problem solution itself. As such instead I ended up simply storing the monkey's
    items as a list and hardcoding the monkey's operations and test conditions.

    Additionally, given the structure of the problem - unlike the other problems it is not pretty
    to create a solution that works for both the examples in the problem, that can be readily
    exploited to produce a solution to the test input. As such the solutions to the examples have
    been omitted here, and instead we just print out the results for the test input.

    To keep worry levels at a reasonable level here and prevent it exploding massively, calculate
    the lowest common multiple of the test divisors, and take take the modulo of the current
    worry level by this lcm factor.

    By doing this we can determine that any division operations past this modulo behave the same,
    this allows us to maintain sensible worry levels.

    """
    # Create Items from raw input using the given divisor and lcm
    inspected = defaultdict(int)
    lcm_value = lcm(3, 11, 19, 5, 2, 7, 17, 13)
    items = create_items(raw_items, divisor=divisor, lcm_value=lcm_value)

    # Iterate through the rounds and calculate the new worry levels
    for item in items:
        for _ in range(rounds):
            # Monkey 0
            if item.next_monkey == 0:
                inspected[0] += 1
                item.worry_level = (item.worry_level * 19)
                item.next_monkey = 2 if item.worry_level % 3 == 0 else 3
            # Monkey 1
            if item.next_monkey == 1:
                inspected[1] += 1
                item.worry_level = (item.worry_level + 8)
                item.next_monkey = 5 if item.worry_level % 11 == 0 else 6
            # Monkey 2
            if item.next_monkey == 2:
                inspected[2] += 1
                item.worry_level = (item.worry_level * 13)
                item.next_monkey = 3 if item.worry_level % 19 == 0 else 1
            # Monkey 3
            if item.next_monkey == 3:
                inspected[3] += 1
                item.worry_level = (item.worry_level + 6)
                item.next_monkey = 1 if item.worry_level % 5 == 0 else 6
            # Monkey 4
            if item.next_monkey == 4:
                inspected[4] += 1
                item.worry_level = (item.worry_level + 5)
                item.next_monkey = 2 if item.worry_level % 2 == 0 else 0
            # Monkey 5
            if item.next_monkey == 5:
                inspected[5] += 1
                item.worry_level = (item.worry_level**2)
                item.next_monkey = 4 if item.worry_level % 7 == 0 else 7
            # Monkey 6
            if item.next_monkey == 6:
                inspected[6] += 1
                item.worry_level = (item.worry_level + 2)
                item.next_monkey = 5 if item.worry_level % 17 == 0 else 7
            # Monkey 7
            if item.next_monkey == 7:
                inspected[7] += 1
                item.worry_level = (item.worry_level + 3)
                item.next_monkey = 4 if item.worry_level % 13 == 0 else 0

    # Calculate the monkey business
    top_inspected = sorted(inspected.values(), reverse=True)
    return top_inspected[0] * top_inspected[1]


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    print("Results for given example:")
    print("Part 1:", solution(TEST_INPUT, rounds=20, divisor=3))
    print("Part 2:", solution(TEST_INPUT, rounds=10_000, divisor=1))

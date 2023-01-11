"""Solution for day 15 - Beacon Exclusion Zone."""
import os
import re
from dataclasses import dataclass
from functools import cached_property
from typing import List

EXAMPLE_INPUT = """
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=20, y=1: closest beacon is at x=15, y=3
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
"""


@dataclass
class Sensor:
    x: int
    y: int
    beacon_x: int
    beacon_y: int

    @cached_property
    def scan_range(self) -> int:
        """Calculate the scanning range of the Sensor using Manhattan Distance to beacon."""
        return abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def within_scan_range(self, x: int, y: int) -> bool:
        """Determine if the given location is within the scanning range of this sensor."""
        return abs(x - self.x) + abs(y - self.y) <= self.scan_range


def _parse_input(data: str) -> List[Sensor]:
    """Parse input data into a more malleable format."""
    data = data.strip().splitlines()
    sensors = []
    for raw_sensor in data:
        sensors.append(Sensor(*map(int, re.findall("-?\d+", raw_sensor))))
    return sensors


def solution_part_1(sensors: List[Sensor], target_row: int) -> int:
    """Solution to Part 1 - Count positions in target row where beacon cannot exist."""
    # Count beacons in target row
    beacon_count = len({sensor.beacon_x for sensor in sensors if sensor.beacon_y == target_row})

    # Create an empty set of x positions in the target row that are covered by at least one sensor
    x_positions = set()
    for sensor in sensors:
        # Skip sensor if its range cannot reach the target row
        if not sensor.within_scan_range(sensor.x, target_row):
            continue
        # Generate positions of sensor's range on the target row, and add to x_positions
        remainder = sensor.scan_range - abs(sensor.y - target_row)
        x_positions.update(range(sensor.x - remainder, sensor.x + remainder + 1))

    # Solution is total x_positions covered by any sensor, minus beacon locations in target row
    return len(x_positions) - beacon_count


def solution_part_2(sensors: List[Sensor], limit: int) -> int:
    """Solution to Part 2 - Full walk-through in README."""
    pos, neg = [], []
    # For each sensor, calculate y axis intersect (c in y = mx + c) for each pair of positive and
    # negative lines, representing the outer perimiter of its scanning range
    for sensor in sensors:
        # Calculate y axis intersect as (c = y - mx) then offset by the edge of the scanning range
        edge_of_scan_range = sensor.scan_range + 1
        # Positive `y = mx + c` line (`m=1` -> `c = y - x` +/- scan edge)
        pos.append(sensor.y - sensor.x + edge_of_scan_range)
        pos.append(sensor.y - sensor.x - edge_of_scan_range)
        # Negative `y = mx + c` line (`m=-1` -> `c = y + x` +/- scan edge)
        neg.append(sensor.y + sensor.x + edge_of_scan_range)
        neg.append(sensor.y + sensor.x - edge_of_scan_range)

    # Cross the positive and negative lines to find intersection locations
    intersects = set()
    for positive_c in pos:
        for negative_c in neg:
            # Ensure the intersection occurs on whole integer coordinates
            if (positive_c + negative_c) % 2 != 0:
                continue

            # Calculate the x and y intersect locations (see README) and ensure it's within bounds
            x = (negative_c - positive_c) // 2
            y = (negative_c + positive_c) // 2
            if 0 <= x <= limit and 0 <= y <= limit:
                intersects.add((x, y))

    # Walk through intersections to find the one outside of any sensor's scanning range
    for x, y in intersects:
        if all(not sensor.within_scan_range(x, y) for sensor in sensors):
            # Calculate the tuning frequency
            return 4_000_000 * x + y

    raise Exception("Can't find the distress beacon location - something is wrong.")


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input, target_row=10))
    print("Part 2:", solution_part_2(example_input, limit=20))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data, target_row=2_000_000))
    print("Part 2:", solution_part_2(data, limit=4_000_000))

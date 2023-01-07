"""Solution for day 13 - Distress Signal."""
from __future__ import annotations

import json
import os
from typing import Any, Iterable, List

EXAMPLE_INPUT = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


class Packet(list):
    """An enhanced version of a list object, representing the packets of the distress signal.

    The primary purpose of this object is to allow less-than comparison of the packets in the
    distress signal. This both allows users to determine if packets are in order (per the question)
    as well as sort the packets based on said order.

    Rather than traversing the list and converting all nested lists to packets, this implementation
    opts for a less-costly lazy approach by overriding the __iter__ and __getitem__ dunders, to
    ensure that any time a list would be yielded, it is also converted into a Packet.

    To keep the solution concise and specific, the __eq__, __le__, __gt__ and __ge__ dunders have
    been skipped, but in a more production-ready solution these would be populated appropriately.

    """

    def __init__(self, items: List[Any]) -> Packet:
        """Initialise the list-like Packet object with an existing list."""
        super().__init__(items)
        self.no_items = len(items)

    def __getitem__(self, i) -> Any:
        """Wrapper around the list __getitem__ to yield Packets in place of lists."""
        res = super().__getitem__(i)
        return Packet(res) if isinstance(res, list) else res

    def __iter__(self) -> Iterable:
        """Wrapper around the list __iter__ to yield Packets in place of lists."""
        return (Packet(i) if isinstance(i, list) else i for i in super().__iter__())

    def __lt__(self, other: Packet) -> bool:
        """Override the list less than dunder method to allow comparing Packets with eachother.

        This comparison follows the rules set out in the question, and essentially checks that
        this Packet is either smaller, or contains smaller values than the Packet being compared.

        During the iterration, if any of the items are an int, we reach a decision point. Either
        we perform direct int comparison if possible, or we search the other packet for the first
        linear (non-nested) packet in that position and re-run the comparison.

        From here the only possiblility that doesn't result in a decision is if the first linear
        packet contains exactly one int of the same value.

        """
        for left, right in zip(self, other):
            # If both are ints, check left is smaller or move on to the next iteration if equal
            if isinstance(left, int) and isinstance(right, int):
                if left == right:
                    continue
                return left < right

            # If one of the items is an int, get the first linear packet of the other and compare
            if isinstance(right, int):
                left = left.first_linear_packet
                right = Packet([right])
            elif isinstance(left, int):
                left = Packet([left])
                right = right.first_linear_packet

            # If the packets are not exactly equal, compare them in the same way
            if left != right:
                return left < right
        # Run out of items - return true if it was this obj that ran out (can't be equal packets)
        return self.no_items < other.no_items

    @property
    def first_linear_packet(self) -> Packet:
        """Get the first linear (non-nested) packet.

        Example:
            Packet([[[[1, 2]]]]).first_linear_packet -> [1, 2]

        """
        if self.no_items == 0 or isinstance((first_item := self[0]), int):
            return self
        return first_item.first_linear_packet


def _parse_input(data: str) -> List[Packet]:
    """Walk through input and create list of Packets."""
    result = []
    for packet in data.strip().splitlines():
        if packet:
            result.append(Packet(json.loads(packet)))
    return result


def solution_part_1(packets: List[Packet]) -> int:
    """Solution to Part 1 - Sum pair indexes where left packet is smaller than right packet."""
    index_sum = 0
    # Cast packets to iterrate and zip it with itself to create pairs
    packets = iter(packets)
    for idx, (left, right) in enumerate(zip(packets, packets), start=1):
        if left < right:
            index_sum += idx
    return index_sum


def solution_part_2(packets: List[Packet]) -> int:
    """Solution to Part 2 - Sort packets and multiply indexes of control packets."""
    extra_1 = Packet([[2]])
    extra_2 = Packet([[6]])
    all_packets = sorted(packets + [extra_1, extra_2])
    return (1 + all_packets.index(extra_1)) * (1 + all_packets.index(extra_2))


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    # Print solutions to example in the problem brief
    example_input = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_input))
    print("Part 2:", solution_part_2(example_input))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(data))
    print("Part 2:", solution_part_2(data))

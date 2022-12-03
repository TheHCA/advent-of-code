"""Solution to day 3."""
import re


def calculate_cost(badge: str) -> str:
    return ord(badge) - 96 + (58 if re.match("[A-Z]", badge) else 0)


def solution(backpack_details: str) -> int:
    backpack_items = backpack_details.split("\n")
    cost = 0
    for group_no in range(0, len(backpack_items), 3):
        overlap = tuple(set(backpack_items[group_no]) & set(backpack_items[group_no + 1]) & set(backpack_items[group_no + 2]))[0]
        cost += calculate_cost(overlap)
    return cost

"""Solution for day 1."""
from typing import Listhttps://github.com/TheHCA/advent-of-code-2022


def solution(elf_food: str) -> List[int]:
    elf_calories = [list(map(int, elf.split("\n"))) for elf in elf_food.strip().split("\n\n")]
    
    return sorted((sum(i) for i in elf_calories), reverse=True)

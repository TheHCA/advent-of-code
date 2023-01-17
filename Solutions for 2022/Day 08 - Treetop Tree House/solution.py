"""Solution for day 8 - Treetop Tree House."""
import os
from dataclasses import dataclass
from typing import Dict, List

EXAMPLE_INPUT = """
30373
25512
65332
33549
35390
"""


@dataclass
class Tree:
    height: int
    tallest_left: int = -1
    tallest_right: int = -1
    tallest_above: int = -1
    tallest_below: int = -1


def _parse_input(data: List[str]) -> List[List[int]]:
    """Parse input data into a more malleable format."""
    return [list(map(int, list(i))) for i in data.strip().splitlines()]


def calculate_biggest_trees(tree_heights: List[List[int]]) -> List[List[Tree]]:
    """Enrich the tree heights data to enable true O(n^2) solution.

    Start by creating Tree objects using each tree height, which will also maintain the tallest
    tree in each direction.

    Iterate through the trees, first by rows, then by cols - walk through both directions at once
    and maintain the tallest tree at each point. Then return Trees enriched with this information.

    """
    # Create Tree objects from tree heights
    trees = [
        [Tree(tree_height) for tree_height in row]
        for row in tree_heights
    ]

    # Walk through trees along each row, and fill in tallest tree at each point
    n_rows = len(tree_heights)
    n_cols = len(tree_heights[0])
    for row_idx in range(n_rows):
        for col_idx in range(1, n_cols):
            # Walk from left to right along each row, and persist tallest tree at each point
            left_tree = trees[row_idx][col_idx - 1]
            trees[row_idx][col_idx].tallest_left = max(left_tree.tallest_left, left_tree.height)
            # Walk from right to left along each row, and persist tallest tree at each point
            right_tree = trees[row_idx][-col_idx]
            trees[row_idx][-col_idx - 1].tallest_right = max(right_tree.tallest_right, right_tree.height)

    # Walk through trees along each column, and fill in tallest tree at each point
    for col_idx in range(n_cols):
        for row_idx in range(1, n_rows):
            # Walk from top to bottom along each column, and persist tallest tree at each point
            above_tree = trees[row_idx - 1][col_idx]
            trees[row_idx][col_idx].tallest_above = max(above_tree.tallest_above, above_tree.height)
            # Walk from bottom to top along each column, and persist tallest tree at each point
            below_tree = trees[-row_idx][col_idx]
            trees[-row_idx - 1][col_idx].tallest_below = max(below_tree.tallest_below, below_tree.height)
    return trees


def solution_part_1(tree_heights: List[List[int]]) -> int:
    """Solution to Part 1.

    First enrich trees with biggest on each side, using more space complexity to enable a true
    O(n^2) time complexity solution.

    This is in comparison to interating through each tree, taking slices in each direction and
    calculating the maximum, which is O(n^3) time complexity.

    """
    # Create Tree objects from tree heights, and calculate tallest tree on each side at each point
    enriched_trees = calculate_biggest_trees(tree_heights)

    # Start off by adding the trees along the edges (removing 4 for double counting corners)
    n_rows = len(tree_heights)
    n_cols = len(tree_heights[0])
    visible_trees = 2 * (n_rows + n_cols) - 4

    # Iterate through trees ignoring the outer row
    for row_idx in range(1, n_rows - 1):
        for col_idx in range(1, n_cols - 1):
            # Check if tree is taller than any on each of its sides, to make it visible
            tree = enriched_trees[row_idx][col_idx]
            if (
                tree.height > tree.tallest_left or
                tree.height > tree.tallest_right or
                tree.height > tree.tallest_above or
                tree.height > tree.tallest_below
            ):
                visible_trees += 1

    return visible_trees


def calculate_viewing_distance(tree_height: int, trees: List[int]) -> int:
    """Calculate distance to closest view blocking tree in one of the directions."""
    distance = 0
    for tree in trees:
        distance += 1
        if tree >= tree_height:
            break
    return distance


def solution_part_2(tree_heights: List[List[int]]) -> int:
    """Solution to Part 2."""
    transposed_tree_heights = list(map(list, zip(*tree_heights)))
    n_rows = len(tree_heights)
    n_cols = len(tree_heights[0])

    scenic_scores = []

    # Iterate through each tree and calculate scenic score
    for row_idx in range(1, n_rows - 1):
        for col_idx in range(1, n_cols - 1):
            tree = tree_heights[row_idx][col_idx]
            # Slice inputs to get lists of trees on each side
            left = tree_heights[row_idx][:col_idx]
            right = tree_heights[row_idx][col_idx + 1:]
            above = transposed_tree_heights[col_idx][:row_idx]
            below = transposed_tree_heights[col_idx][row_idx + 1:]
            # Get distance to tree >= height of this tree
            distance_left = calculate_viewing_distance(tree, left[::-1])
            distance_right = calculate_viewing_distance(tree, right)
            distance_above = calculate_viewing_distance(tree, above[::-1])
            distance_below = calculate_viewing_distance(tree, below)

            scenic_score = distance_left * distance_right * distance_above * distance_below
            scenic_scores.append(scenic_score)

    return max(scenic_scores)


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

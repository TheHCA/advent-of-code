"""Solution for day 7 - No Space Left On Device."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List, Optional, Set

EXAMPLE_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@dataclass
class Directory:
    """Linked list representation of a file directory."""

    name: str
    size: int = 0
    parent: Optional[Directory] = None
    children: Dict[str, Directory] = field(default_factory=dict)

    def _get_abs_path(self):
        """Get absolute path to this directory."""
        if self.name == "/":
            return self.name
        # Walk up through tree to build abs path to this dir
        path = self.name
        tmp_dir = self.parent
        while tmp_dir.name != "/":
            print(tmp_dir.name)
            path = f"/{tmp_dir.name}" + path
            tmp_dir = tmp_dir.parent
        return path

    def __hash__(self) -> str:
        """Make this hashable so it can be added to a set later."""
        # List also happens to work ofc in terminal.directories, but a set is better.
        return hash((self.parent.__hash__() if self.parent else None, self.name))

    def __eq__(self, other: Directory) -> bool:
        """Utility method to check directory equality for adding to set."""
        return self._get_abs_path() == other._get_abs_path()


@dataclass
class File:
    """Class object representing a directory within a file."""

    size: int
    name: str


class Execution:
    """Object representing a command being executed within the terminal."""

    def __init__(
        self,
        command: str,
        argument: Optional[str] = None,
        response: Optional[List[str]] = None
    ) -> Execution:
        """Create Execution object, parsing raw response."""
        self.command = command
        self.argument = argument
        self.response = self._parse_response(response) if response else None

    @staticmethod
    def _parse_response(response: List[str]) -> List[Union[Directory, File]]:
        """Parse raw response output into structured format."""
        response_items = []
        # Walk through responses and create objects
        for line in response:
            if line.startswith("dir"):
                # Create directories
                response_items.append(Directory(name=line.split(" ")[-1]))
            else:
                # Create files
                size, name = line.split()
                response_items.append(File(int(size), name))
        return response_items


@dataclass
class Terminal:
    """Instance of a terminal shell, which can navigate directories."""

    root_dir: Directory
    current_directory: Directory
    directories: Set[Directory]

    def cd(self, execution: Execution) -> None:
        """Execute a cd operation."""
        # Change directory either one level up or into a new child dir
        if execution.argument == "..":
            self.current_directory = self.current_directory.parent
        else:
            # Assumes child directories have already been constructed during ls cmd
            self.current_directory = self.current_directory.children[execution.argument]
            # Add to over-arching list of directories for convenience later
            self.directories.add(self.current_directory)

    def ls(self, execution: Execution) -> None:
        """Execute an ls operation."""
        # Calculate directory size with new files
        self.current_directory.size = sum(obj.size for obj in execution.response)

        # Update parent dir sizes with new size
        tmp_dir = self.current_directory
        while tmp_dir.parent:
            tmp_dir.parent.size += self.current_directory.size
            tmp_dir = tmp_dir.parent

        # For each directory in the response, create list link to and from this directory
        for directory in [i for i in execution.response if isinstance(i, Directory)]:
            self.current_directory.children[directory.name] = directory
            directory.parent = self.current_directory


def _parse_input(data: str) -> Terminal:
    """Parse input data into a more malleable format."""
    # Create new terminal at root directory
    root_dir = Directory("/")
    terminal = Terminal(root_dir=root_dir, current_directory=root_dir, directories={root_dir})

    # Walk through the input and load into Executions
    executions = []
    for execution_raw in data.strip().split("$ ")[2:]:  # Skip two items ("" and "cd /")
        # Build execution including response
        full_cmd, full_resp = execution_raw.split("\n", 1)
        execution = Execution(*full_cmd.strip().split(), response=full_resp.splitlines())
        # Execute on the terminal
        getattr(terminal, execution.command)(execution)
    return terminal


def solution_part_1(terminal: Terminal) -> int:
    """Solution to Part 1 - Add up all directories < 1MB."""
    return sum(i.size for i in terminal.directories if i.size <= 100_000)


def solution_part_2(terminal: Terminal) -> int:
    """Solution to Part 2."""
    # Calculate space required
    available_space = 70_000_000 - terminal.root_dir.size
    space_to_free_up = 30_000_000 - available_space
    # Find smallest directory that can be deleted to create required space
    if space_to_free_up < 0:
        return -1
    return min(i.size for i in terminal.directories if i.size >= space_to_free_up)


if __name__ == "__main__":
    """Execute solutions and print results to todays problem."""
    print(Directory(1, None))
    # Print solutions to example in the problem brief
    example_terminal = _parse_input(EXAMPLE_INPUT)
    print("Results for given example:")
    print("Part 1:", solution_part_1(example_terminal))
    print("Part 2:", solution_part_2(example_terminal))

    # Load local data file
    with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
        terminal = _parse_input(f.read())

    # Execute solution for solution part 1 & 2
    print("\nResults for full puzzle data:")
    print("Part 1:", solution_part_1(terminal))
    print("Part 2:", solution_part_2(terminal))

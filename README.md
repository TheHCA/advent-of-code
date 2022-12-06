# Advent of Code

## What is this?

Every year, the tireless _Eric Wastl_ creates fun, christmas themed coding problems, and releases them daily as an advent calendar, known as [Advent of Code](https://adventofcode.com/about)

Here's a snippet from the about page:
> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

I tried a few of these problems in 2021, and found them to be great fun! Going forwards from 2022 I thought it'd be a nice idea to catalogue my solutions on GitHub, so I could keep a record of them and share them with friends etc.

## How does it work?

Navigate through the directories in this repo to find my solutions for each of the challenges. Here you'll find the problem outline, as well as the solutions for both the examples given in the problem description, and the generated datafile for my user.

I typically solve most of these problems with Python, and to save myself some time (_and scratch that organisational itch_) I've setup a cookiecutter to nicely format my solutions.

To generate a solution skeleton for a new challenge, simply run the below command, complete the cookiecutter questionnaire.

```bash
pip install cookiecutter
cookiecutter -f .
```

Instructions on how to execute the solutions will be detailed in the associated README for the problem, but generally you can just execute the Python files as normal.

```bash
python solution.py
```

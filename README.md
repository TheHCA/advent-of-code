# Advent of Code

## What is this?

Every December, the tireless Eric Wastl creates fun, christmas themed coding problems, and releases them daily as an advent calendar, known as [Advent of Code](https://adventofcode.com/about)

Here's a snippet from the about page:
> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

Each day's challenge has two problems, each worth one ⭐. A simple example for each problem is provided with a small data input. Following this, each user receives a unique dataset for their problem, for which they use to calculate their unique solution to the day's challenge.

I tried a few of these problems in 2021, and found them to be great fun! Going forwards from 2022 I thought it'd be a nice idea to catalogue my solutions on GitHub, so I could keep a record of them and share them with friends etc.

## How does it work?

Navigate through the directories in this repo to find my solutions for each of the challenges. Here you'll find the problem outline, as well as the solutions for both the examples given in the problem description, and the generated datafile for my user.

## Notable solutions

My general approach when solving these problems is to create a clean and polished solution that I would like to come across in a production environment. On top of this, I like to put focus on making these soltuions efficient, as long as it doesn't come at the expense of code quality.

So I generally shy away from 1-liner difficult to read/understand/maintain solutions, and opt towards a more Object-Oriented approach, complete with comments, docstrings and examples.

Some great examples of notable soltuions that I particularly like are:

- [Day 7 - No Space Left On Device](Solutions%20for%202022/Day%2007%20-%20No%20Space%20Left%20On%20Device)

  Created a shell object capable of parsing traversal and ls commands to map directories as a linked list

- [Day 12 - Hill Climbing Algorithm](Solutions%20for%202022/Day%2012%20-%20Hill%20Climbing%20Algorithm)

  Modelled climbing a hill as pouring an infinite bucket of water down from the peak with some nice visualisations

- [Day 13 - Distress Signal](Solutions%20for%202022/Day%2013%20-%20Distress%20Signal)

  Extended the list object and enhanced dunders (`__getitem__` etc) to allow less-than comparison of deeply nested lists

- [Day 15 - Beacon Exclusion Zone](Solutions%20for%202022/Day%2015%20-%20Beacon%20Exclusion%20Zone)

  Reduced problem to discover blind spot between search beacons in a 4 Million square area to a simple & scalable solution that looks at intersecting lines.

  Nice write up on problem iteration to reduce processing time from 30s to milliseconds

## Current Progress

Unfortunately I was away for a lot of December and didn't get to complete some of the later problems as they came out. However I'm working through the backlog and steadily updating this repo with my solutions as and when I find time.

## Project setup

I typically solve most of these problems with Python, and to save myself some time (_and scratch that organisational itch_) I've setup a [cookiecutter](https://github.com/TheHCA/advent-of-code-cookiecutter) to nicely format my solutions.

To generate a solution skeleton for a new challenge, simply run the below command, complete the cookiecutter questionnaire.

```bash
pip install cookiecutter
cookiecutter -f https://github.com/TheHCA/advent-of-code-cookiecutter
```

Instructions on how to execute the solutions will be detailed in the associated README for the problem, but generally you can just execute the Python files as normal.

```bash
python solution.py
```

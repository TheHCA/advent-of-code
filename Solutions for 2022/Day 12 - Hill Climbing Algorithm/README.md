# Day 12: Hill Climbing Algorithm

## About the solution

This solution flips the problem on its head, and effectively attempts to walk down towards the
start, from the end location. This is done by starting at the highest elevation, and checking
each location in all permitted movement directions to determine if the move is valid.

If the move is valid we add the new location to a set of possible moves for the next step. At
each itteration, we check all possible new moves in all directions for each of the new
locations, effectively fanning out from the end location one step at a time in all directions.

This can be visualised akin to pouring an infinite bucket of water down from the highest
elevation point. At each 'step' the water will spread out one step further in each direction (but magically not fall off cliffs 🙂)
until the goal location is reached at the lowest elevation.

To aid with this visualisation, please see the below graphics generated using this solution algorithm. With the start (`S`) and end (`E`) locations marked by red and green crosses respectively.


### Hill elevations from question example

![Alt Text](example_data_animation.gif)

### My full dataset for today's challenge

![Alt Text](full_dataset_animation.gif)



## ⭐ Part 1 - Initial challenge

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where `a` is the lowest elevation, `b` is the next-lowest, and so on up to the highest elevation, `z`.

Also included on the heightmap are marks for your current position (`S`) and the location that should get the best signal (`E`). Your current position (`S`) has elevation `a`, and the location that should get the best signal (`E`) has elevation `z`.

You'd like to reach `E`, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square **up**, **down**, **left**, or **right**. To avoid needing to get out your climbing gear, the elevation of the destination square can be **at most one higher than the elevation of your current square**; that is, if your current elevation is `m`, you could step to elevation `n`, but not to elevation `o`. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

In the above diagram, the symbols indicate whether the path exits each square moving up (`^`), down (`v`), left (`<`), or right (`>`). The location that should get the best signal is still `E`, and `.` marks unvisited squares.

This path reaches the goal in **31** steps, the fewest possible.

**What is the fewest steps required to move from your current position to the location that should get the best signal?**


## ⭐⭐ Part 2 - Stretch challenge

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation `a`. The goal is still the square marked `E`. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation `a` to the square marked `E`.

Again consider the example from above:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Now, there are six choices for starting position (five marked `a`, plus the square marked `S` that counts as being at elevation `a`). If you start at the bottom-left square, you can reach the goal most quickly:

```
...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
```

This path reaches the goal in only **29** steps, the fewest possible.

**What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?**


## Quickstart

To generate solutions for this problem, simply invoke the `solution.py` file.

```bash
python solution.py
```

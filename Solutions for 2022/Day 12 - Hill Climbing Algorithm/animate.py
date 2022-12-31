"""Create animations to help visualise the solution to the Hill Climbing Alorithm."""
import os

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

from solution import EXAMPLE_INPUT, Solution

with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r", encoding="utf-8") as f:
    FULL_DATA_SET = f.read()


def animate(_, is_example = True):
    """Animation function to draw heatmap of steps at each iteration of the algorithm."""
    ax.cla()
    sns.heatmap(
        data=solution.visits,
        ax=ax,
        cbar=False,
        vmin=0,
        vmax=solution.steps,
        cmap="mako",
        square=True,
        linewidth=0.01,
        xticklabels=False,
        yticklabels=False,
    )
    # Draw crosses on heatmap for start and end locations
    y_start, x_start = solution.start
    y_end, x_end = solution.end
    if is_example:
        ax.scatter(x_start + 0.5, y_start + 0.5, marker="x", color="r", s=1000, linewidth=7)
        ax.scatter(x_end + 0.5, y_end + 0.5, marker="x", color="g", s=1000, linewidth=7)
        ax.text(x_start + 0.2, y_start + 0.9, "START", color="r", size=15, weight="bold")
        ax.text(x_end + 0.3, y_end + 0.9, "END", color="g", size=15, weight="bold")
    else:
        ax.scatter(x_start + 0.5, y_start + 0.5, marker="x", color="r", s=30, linewidth=1)
        ax.scatter(x_end + 0.5, y_end + 0.5, marker="x", color="g", s=30, linewidth=1)

    # Walk down towards the start one step
    if not solution._reached_destination(strict_start=True):
        solution.walk_one_step()

# Create animation for example and save to file
solution = Solution.from_input(EXAMPLE_INPUT)
total_frames = Solution.from_input(EXAMPLE_INPUT).walk_to_start()

fig, ax = plt.subplots(figsize = (12, 8))
anim = FuncAnimation(fig = fig, func=animate, frames=total_frames + 10, blit=False, fargs=[True])
anim.save(os.path.join(os.path.dirname(__file__), "example_data_animation.gif"))

# Create animation for full data set and save to file
solution = Solution.from_input(FULL_DATA_SET)
total_frames = Solution.from_input(FULL_DATA_SET).walk_to_start()

fig, ax = plt.subplots(figsize = (12, 8))
anim = FuncAnimation(fig = fig, func=animate, frames=total_frames + 10, blit=False, fargs=[False])
anim.save(os.path.join(os.path.dirname(__file__), "full_dataset_animation.gif"))

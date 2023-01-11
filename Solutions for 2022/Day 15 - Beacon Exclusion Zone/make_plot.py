"""Simple script to create visualisations for the distress beacon search."""
import os

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import seaborn as sns

from solution import EXAMPLE_INPUT, _parse_input, Sensor

# Setup - create sensors, plot and set limits
sensors = _parse_input(EXAMPLE_INPUT)
fig, ax = plt.subplots(figsize = (12, 8))
limit = 20

pos, neg = [], []
for sensor in sensors:
    # Draw sensor range as diamond
    p = Polygon([
            (sensor.x - sensor.scan_range, sensor.y),
            (sensor.x, sensor.y - sensor.scan_range),
            (sensor.x + sensor.scan_range, sensor.y),
            (sensor.x, sensor.y + sensor.scan_range),
        ],
        alpha=0.2,
        linewidth=2,
        edgecolor="k",
    )
    ax.add_patch(p)
    # Annotate with center location and scanning range
    ax.scatter(sensor.x, sensor.y, color="r", marker="+")
    ax.annotate(sensor.scan_range, (sensor.x, sensor.y), xytext=(-3, -15), textcoords="offset points", color="r")

    # Calculate y axis intersect as (c = y - mx) then offset by the edge of the scanning range
    edge_of_scan_range = sensor.scan_range + 1
    # Positive `y = mx + c` line (`m=1` -> `c = y - x` +/- scan edge)
    pos.append(sensor.y - sensor.x + edge_of_scan_range)
    pos.append(sensor.y - sensor.x - edge_of_scan_range)
    # Negative `y = mx + c` line (`m=-1` -> `c = y + x` +/- scan edge)
    neg.append(sensor.y + sensor.x + edge_of_scan_range)
    neg.append(sensor.y + sensor.x - edge_of_scan_range)

# Plot lines and intersections
intersects = set()
x_coords = range(0, limit + 1)
for positive_c in pos:
    for negative_c in neg:
        # Plot the positive and negative lines
        ax.plot(x_coords, [i + positive_c for i in x_coords], color="g")
        ax.plot(x_coords, [-i + negative_c for i in x_coords], color="purple")

        # Ensure their intersection occurs on whole integer coordinates
        if (positive_c + negative_c) % 2 != 0:
            continue

        # Calculate the x and y intersect locations (see README) and ensure it's within bounds
        x = (negative_c - positive_c) // 2
        y = (negative_c + positive_c) // 2
        if 0 <= x <= limit and 0 <= y <= limit:
            # Plot the intersection location
            ax.scatter(x, y, marker="o", s=200, edgecolors="r", facecolors="none", linewidths=2)
            pass

# Massage the plot
ax.set_xlim(0, limit)
ax.set_ylim(0, limit)
ax.set_xticks(range(limit + 1))
ax.set_yticks(range(limit + 1))
ax.set_title("All sensors - Perimeter lines and intersects")
ax.grid(alpha=0.2)
# Save
plt.savefig(os.path.join(os.path.dirname(__file__), "plots", "all_examples_intersects.png"))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-Self-Avoiding-RW
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Self-Avoiding Random Walk in 2D

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:09:28 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of steps
N = 10000

# Store all points in a set for quick lookups
visited = set()

# Store coordinates as a list for plotting
coordinates = []

# Start at origin
x, y = 0, 0
visited.add((x, y))
coordinates.append((x, y))

# Take steps
for _ in range(1, N):
    choices = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    choices = [pt for pt in choices if pt not in visited]

    if not choices:  # no where to go, we're trapped
        break

    x, y = choices[np.random.randint(0, len(choices))]  # randomly select one of the valid choices
    visited.add((x, y))
    coordinates.append((x, y))

# We might not have been able to take all N steps
N = len(coordinates)

# Convert to numpy arrays for easier slicing
x, y = np.array(coordinates).T

fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot([], [], lw=2)
dot, = ax.plot([], [], 'rs', markersize=10)
last5, = ax.plot([], [], 'r')
start_dot, = ax.plot([], [], 'ro', markersize=10)  # green dot for the start point


def init():
    padding = 1
    ax.set_xlim(np.min(x) - padding, np.max(x) + padding)
    ax.set_ylim(np.min(y) - padding, np.max(y) + padding)
    ax.set_title(r'Self-avoiding random walk on $\mathbb{Z}^2$')
    # ax.axis('equal')  # make x and y axes have the same scale
    start_dot.set_data(x[0], y[0])  # set the position of the starting dot

    # Enable dashed grid lines
    ax.grid(True, linestyle='dashed', linewidth=0.5)

    # Set the dense grid lines
    ax.set_xticks(np.arange(np.min(x) - padding, np.max(x) + padding, 1))
    ax.set_yticks(np.arange(np.min(y) - padding, np.max(y) + padding, 1))

    return line, dot, last5, start_dot


def update(frame):
    line.set_data(x[:frame], y[:frame])
    dot.set_data(x[frame-1], y[frame-1])
    start = max(0, frame-5)
    last5.set_data(x[start:frame], y[start:frame])
    last5.set_color('red')
    return line, dot, last5, start_dot


ani = FuncAnimation(fig,
                    update,
                    frames=range(N+1),
                    init_func=init,
                    blit=True,
                    interval=160,
                    repeat=False)

plt.show()
plt.ioff()

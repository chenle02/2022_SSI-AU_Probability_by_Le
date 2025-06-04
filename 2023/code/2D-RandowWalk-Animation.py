#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-RandowWalk-Animation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Animation of a 2D Random Walk

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:12:37 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of steps
N = 1000

# Create arrays to hold the x and y coordinates of each step
x = np.zeros(N)
y = np.zeros(N)

# Randomly choose the direction of each step
for i in range(1, N):
    val = np.random.randint(1, 5)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot([], [], lw=2)
dot, = ax.plot([], [], 'rs', markersize=10)
last5, = ax.plot([], [], 'r')

# Calculate the limits for the plot
x_max, x_min = np.max(x), np.min(x)
y_max, y_min = np.max(y), np.min(y)

# Extra space
padding = 1

# Starting point highlighted
start_dot, = ax.plot([], [], 'ro', markersize=10)  # green dot for the start point


def init(padding=1):
    ax.set_xlim(x_min - padding, x_max + padding)
    ax.set_ylim(y_min - padding, y_max + padding)
    ax.set_title(r'Animated Random Walk on $\mathbb{Z}^2$')
    start_dot.set_data(x[0], y[0])  # set the position of the starting dot

    # Enable dashed grid lines
    ax.grid(True, linestyle='dashed')

    # Set the dense grid lines
    ax.set_xticks(np.arange(x_min-padding, x_max+padding, 1))
    ax.set_yticks(np.arange(y_min-padding, y_max+padding, 1))

    return line, dot, last5


def update(frame):
    # Full path
    line.set_data(x[:frame], y[:frame])

    # Current position dot
    dot.set_data(x[frame-1], y[frame-1])

    # Highlight last 5 steps
    start = max(0, frame-5)
    last5.set_data(x[start:frame], y[start:frame])
    last5.set_color('red')

    return line, dot, last5


ani = FuncAnimation(fig,
                    update,
                    frames=range(N),
                    init_func=lambda: init(padding),
                    blit=True,
                    repeat=False,
                    interval=50  # 50 ms delay between frames
                    )

plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.1D-BM-Animation-Dots
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    1D Brownian Motion Animation with Dots showing on y axis.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:05:22 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of steps and the number of paths
num_steps = 1000
num_paths = 5

# Set the colors for each path
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Initialize positions
positions = np.zeros((num_paths, num_steps))

# Create random steps
steps = np.random.normal(loc=0, scale=0.5, size=(num_paths, num_steps))

# Add the steps to the positions
for i in range(1, num_steps):
    positions[:, i] = positions[:, i-1] + steps[:, i]

# Create a figure
fig, ax = plt.subplots()

# Initialize lines and dots for each path
lines = [ax.plot([], [], color=colors[i])[0] for i in range(num_paths)]
dots = [ax.scatter([], [], color=colors[i], s=100) for i in range(num_paths)]

# Set plot limits
ax.set_xlim(0, num_steps)
ax.set_ylim(np.min(positions), np.max(positions))

# Set the title and labels for the plot
ax.set_title('1D Brownian Motion Paths')
ax.set_xlabel('Time Step')
ax.set_ylabel('Position')
ax.grid(True)


# Animation update function
def update(frame):
    for i in range(num_paths):
        lines[i].set_data(range(frame+1), positions[i, :frame+1])
        dots[i].set_offsets([num_steps-14, positions[i, frame]])
    return lines + dots


# Create animation
ani = FuncAnimation(fig,
                    update,
                    frames=num_steps,
                    blit=True,
                    repeat=False,
                    interval=50  # 50 ms between frames
                    )

# Show the plot
plt.show()

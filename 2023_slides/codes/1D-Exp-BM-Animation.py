#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.Exp-BM-Animation
    ~~~~~~~~~~~~~~~~~~~~~~

    1D exponential Brownian Motion Animation with Dots showing on y axis.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:09:09 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of steps and the number of paths
num_steps = 1000
num_paths = 5
scale = 0.1  # The scaling parameter for exponential Brownian Motion

# Set the colors for each path
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Initialize BMs
BMs = np.zeros((num_paths, num_steps))
ExpBMs = np.zeros((num_paths, num_steps))

# Create random steps
steps = np.random.normal(loc=0, scale=0.5, size=(num_paths, num_steps))

# Add the steps to the BMs
for i in range(1, num_steps):
    BMs[:, i] = BMs[:, i-1] + steps[:, i]
    ExpBMs[:, i] = np.exp(scale * BMs[:, i] - scale * scale * i/2)

# Create a figure
fig, ax = plt.subplots()

# Initialize lines and dots for each path
lines = [ax.plot([], [], color=colors[i])[0] for i in range(num_paths)]
dots = [ax.scatter([], [], color=colors[i], s=100) for i in range(num_paths)]

# Set plot limits
ax.set_xlim(0, num_steps)
ax.set_ylim(np.min(ExpBMs), np.max(ExpBMs))

# Set the title and labels for the plot
ax.set_title(f'1D exponential Brownian motion with scale = {scale}')
ax.set_xlabel('t')
ax.set_ylabel(r'$B_t$')
ax.grid(True)


# Animation update function
def update(frame):
    for i in range(num_paths):
        lines[i].set_data(range(frame+1), ExpBMs[i, :frame+1])
        dots[i].set_offsets([num_steps-14, ExpBMs[i, frame]])
    return lines + dots


# Create animation
ani = FuncAnimation(fig, update, frames=num_steps, blit=True, interval=1)

# Show the plot
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-BM-Animation-highlight
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    2D Brownian motion animation with the latest 10 steps highlighted in red.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 12:03:04 PM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from IPython.display import HTML # This is for Jupyter notebooks

# Set the number of steps and create an array to hold the positions
num_steps = 1000
positions = np.empty((num_steps, 2))

# Start at the origin
positions[0, :] = (0, 0)

# Create random steps
steps = np.random.normal(loc=0, scale=0.5, size=(num_steps, 2))

# Add the steps to the positions
for i in range(1, num_steps):
    positions[i, :] = positions[i-1, :] + steps[i, :]

# Set up the figure
fig = plt.figure(figsize=(8, 8))
plt.rcParams['animation.embed_limit'] = 50
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlim(np.min(positions[:, 0])-1, np.max(positions[:, 0])+1)
ax.set_ylim(np.min(positions[:, 1])-1, np.max(positions[:, 1])+1)
line, = ax.plot([], [], linestyle='-', marker='o', markersize=2, linewidth=0.5, color='blue')
highlight, = ax.plot([], [], linestyle='-', marker='o', markersize=2, linewidth=1, color='red')

# Highlight the starting point with a red dot and the end point as a red square
start_point = positions[0]
ax.plot(start_point[0], start_point[1], marker='o', markersize=10, color='red')
ax.plot(positions[-1, 0], positions[-1, 1], 'rs', markersize=8)

# Initialization function for the animation
def init():
    line.set_data([], [])
    highlight.set_data([], [])
    return line, highlight,


# Animation update function
def update(frame):
    line.set_data(positions[:frame, 0], positions[:frame, 1])
    if frame > 10:  # Highlight the last 10 steps, change this to highlight more or fewer steps
        highlight.set_data(positions[frame-5:frame, 0], positions[frame-5:frame, 1])
    else:
        highlight.set_data(positions[:frame, 0], positions[:frame, 1])
    return line, highlight,


# Create the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps+1,
    init_func=init,
    blit=True,    # blit=True means only re-draw the parts that have changed
    interval=25,  # 25 ms between frames, change this to run faster or slower
    repeat=False  # Do not repeat the animation
    )

# Show the animation
plt.title(r'Brownian Motion on $\mathbb{R}^2$')  # Title
plt.show()
# HTML(ani.to_jshtml()) # This is for Juptyer notebooks

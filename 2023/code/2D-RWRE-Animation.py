#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-RWRE-Animation
    ~~~~~~~~~~~~~~~~~~~~~~~

    This is the animation of a 2D random walk in a random environment (RWRE).

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:16:00 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the size of the landscape
size = 100

# Generate a random Gaussian field as the landscape
landscape = np.random.normal(loc=0, scale=1, size=(size, size))

# Create a walker with a position and a path
walker = {'position': np.array([size // 2, size // 2]), 'path': []}

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(16, 16))
im = ax.imshow(landscape,
               cmap='hot',
               origin='lower')
line, = ax.plot([], [], 'b-', linewidth=3)
dot, = ax.plot([], [], 'bo', markersize=12)  # Blue dot for the head


# Initialization function
def init():
    line.set_data([], [])
    dot.set_data([], [])
    return line, dot


# Animation update function
def update(frame):
    # Append the current position to the path
    walker['path'].append(walker['position'].copy())

    # Calculate the gradient of the landscape at the current position
    gradient = np.array(np.gradient(landscape))[::-1, walker['position'][1], walker['position'][0]]

    # Add some randomness to the direction
    direction = gradient + np.random.normal(loc=0,
                                            scale=10,
                                            size=2)

    # Normalize the direction
    direction /= np.linalg.norm(direction)

    # Choose the direction based on the larger component of the gradient
    if np.abs(direction[0]) > np.abs(direction[1]):
        direction = np.array([np.sign(direction[0]), 0])
    else:
        direction = np.array([0, np.sign(direction[1])])

    # Convert the direction to integers and take a step in the chosen direction
    walker['position'] += direction.astype(int)

    # Convert the path to a NumPy array and update the line plot
    path = np.array(walker['path'])
    line.set_data(path[:, 1], path[:, 0])

    # Update the dot at the head of the path
    dot.set_data(path[-1, 1], path[-1, 0])

    return line, dot


# Create animation
ani = FuncAnimation(fig,
                    update,
                    frames=range(1000),
                    init_func=init,
                    blit=True,
                    repeat=False,
                    interval=50)

# Show the animation
plt.title(r'Random Walk in a Random Environment on $\mathbb{Z}^2$')
plt.show()

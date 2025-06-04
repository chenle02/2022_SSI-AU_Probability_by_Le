#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.1D-BM
    ~~~~~~~~~~~

    Simulation of 1D Brownian Motion.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 12:48:45 PM EDT 2023
"""



import numpy as np
import matplotlib.pyplot as plt

# Set the number of steps and the number of paths
num_steps = 1000
num_paths = 5

# Set the colors for each path
colors = ['blue', 'green', 'red', 'purple', 'orange']

plt.figure(figsize=(10, 8))

# For each path
for i in range(num_paths):
    # Create an empty array to hold the positions
    positions = np.empty(num_steps)

    # Start at the origin
    positions[0] = 0

    # Create random steps
    steps = np.random.normal(loc=0, scale=0.5, size=num_steps)

    # Add the steps to the positions
    for j in range(1, num_steps):
        positions[j] = positions[j-1] + steps[j]

    # Plot the path
    plt.plot(positions, color=colors[i])

# Set the title and labels for the plot
plt.title('1D Brownian Motion Paths')
plt.xlabel('Time Step')
plt.ylabel('Position')
plt.grid(True)

# Show the plot
plt.show()

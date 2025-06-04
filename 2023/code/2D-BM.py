#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-BM
    ~~~~~~~~~~~

    Simulate the 2D Brownian motion

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:16:54 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the number of steps and create an array to hold the positions
num_steps = 1000  # The number of steps in the random walk
positions = np.empty((num_steps, 2))  # An empty array to store the x and y coordinates at each step

# Start at the origin
positions[0, :] = (0, 0)  # The first position is the origin (0, 0)

# Create random steps
steps = np.random.normal(loc=0, scale=0.5, size=(num_steps, 2))  # Generate random steps. Each step is a 2D vector.

# Add the steps to the positions
for i in range(1, num_steps):  # For each step,
    positions[i, :] = positions[i-1, :] + steps[i, :]  # Add the step to the last position to get the new position

# Create a figure and plot the path
plt.figure(figsize=(8, 8))  # Create a new figure with a specific size

# Plot the path of the random walk
plt.plot(positions[:, 0], positions[:, 1], linestyle='-', marker='o', markersize=2, linewidth=0.5)

# Highlight the start and end points
plt.plot(positions[0, 0], positions[0, 1], 'ro', markersize=8)  # Start point as a red circle
plt.plot(positions[-1, 0], positions[-1, 1], 'rs', markersize=8)  # End point as a red square

# Set the title and labels for the plot
plt.title(r'Brownian Motion on $\mathbb{R}^2$')  # Title
plt.xlabel('X')  # x-axis label
plt.ylabel('Y')  # y-axis label

plt.grid(True)  # Show a grid

# Show the plot
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-RWRE
    ~~~~~~~~~~~~~

    This is a simulation for the random walk in a random environment (RWRE) in 2D.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:14:56 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the size of the landscape
size = 100

# Generate a random Gaussian field as the landscape
landscape = np.random.normal(loc=0, scale=1, size=(size, size))

# Create a walker with a position and a path
walker = {'position': np.array([size // 2, size // 2]), 'path': []}

# Run the simulation for a certain number of steps
num_steps = 1000
for _ in range(num_steps):
    # Append the current position to the path
    walker['path'].append(walker['position'].copy())

    # Calculate the gradient of the landscape at the current position
    gradient = np.array(np.gradient(landscape))[::-1, walker['position'][1], walker['position'][0]]

    # Add some randomness to the direction
    direction = gradient + np.random.normal(loc=0,
                                            scale=10,
                                            size=2
                                            )

    # Normalize the direction
    direction /= np.linalg.norm(direction)

    # Choose the direction based on the larger component of the gradient
    if np.abs(direction[0]) > np.abs(direction[1]):
        direction = np.array([np.sign(direction[0]), 0])
    else:
        direction = np.array([0, np.sign(direction[1])])

    # Convert the direction to integers and take a step in the chosen direction
    walker['position'] += direction.astype(int)

# Convert the path to a NumPy array for convenience
walker['path'] = np.array(walker['path'])


# Plot the landscape and the path of the walker
plt.figure(figsize=(8, 8))

# Plot the landscape and the path of the walker
padding = 1
x_min = np.min(walker['path'][:, 1])
x_max = np.max(walker['path'][:, 1])
y_min = np.min(walker['path'][:, 0])
y_max = np.max(walker['path'][:, 0])
plt.imshow(landscape,
           cmap='terrain',
           origin='lower',
           extent=[x_min - padding,
                   x_max + padding,
                   y_min - padding,
                   y_max + padding]
           )
plt.plot(walker['path'][0, 1],
         walker['path'][0, 0],
         'ro',
         markersize=10,
         label='Start'
         )
plt.plot(walker['path'][-1, 1],
         walker['path'][-1, 0],
         'rs',
         markersize=10,
         label='End'
         )
plt.plot(walker['path'][:, 1],
         walker['path'][:, 0],
         'm-',
         linewidth=3
         )
plt.title('Random Walk in a Random Environment')
plt.legend()
plt.show()
plt.plot(walker['path'][:, 1], walker['path'][:, 0], 'r-')
plt.title(r'Random Walk in a Random Environment on $\mathbb{Z}^2$')
plt.show()

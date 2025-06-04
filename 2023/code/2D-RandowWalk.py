#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.2D-RandowWalk
    ~~~~~~~~~~~~~~~~~~~

    2D Random Walk

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:12:08 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

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

# Plot the random walk

plt.figure(figsize=(10, 10))
plt.title(r'Random Walk on $\mathbb{Z}^2$')
plt.plot(x, y)

# Enable grid lines in dashed style
plt.grid(True, linestyle='dashed')

# Set x and y ticks
plt.xticks(np.arange(np.min(x), np.max(x)+1, 1))
plt.yticks(np.arange(np.min(y), np.max(y)+1, 1))

plt.scatter(0,
            0,
            color='red',
            marker='s',
            s=200
            )  # start point
plt.scatter(x[-1],
            y[-1],
            color='red',
            marker='o',
            s=200
            )  # end point
plt.show()

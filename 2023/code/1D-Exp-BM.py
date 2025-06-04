#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.Exp-BM
    ~~~~~~~~~~~~

    Simulation of 1D geometric Brownian motion

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:08:36 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the number of steps and the number of paths
num_steps = 1000
num_paths = 5
scale = 0.1  # The scaling parameter for exponential Brownian Motion

# Set the colors for each path
colors = ['blue', 'green', 'red', 'purple', 'orange']

plt.figure(figsize=(10, 8))

# For each path
for i in range(num_paths):
    # Create an empty array to hold the BrownianMotion
    BrownianMotion = np.empty(num_steps)
    ExpBM = np.empty(num_steps)

    # Start at the origin
    BrownianMotion[0] = 0
    ExpBM[0] = 1

    # Create random steps
    steps = np.random.normal(loc=0, scale=1, size=num_steps)

    # Add the steps to the BrownianMotion
    for j in range(1, num_steps):
        BrownianMotion[j] = BrownianMotion[j-1] + steps[j]
        ExpBM[j] = np.exp(scale * BrownianMotion[j] - scale * scale * j/2)

    # Plot the path
    plt.plot(ExpBM, color=colors[i])

# Set the title and labels for the plot
plt.title('1D Exponential Brownian Motions')
plt.xlabel('Time Step')
plt.ylabel('Position')
plt.grid(True)

# Show the plot
plt.show()

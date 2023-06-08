#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.heat-colomap
    ~~~~~~~~~~~~~~~~~~

    Plot the heat colormap.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 12:24:44 PM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate an array of values from 0 to 1
x = np.linspace(0, 1, 256)

# Create a meshgrid to plot the colormap
X, Y = np.meshgrid(x, [0])

# Plot the colormap
plt.figure(figsize=(8, 2))
plt.imshow(X, cmap='hot', aspect='auto')
plt.axis('off')
plt.title('Hot Colormap')
plt.show()

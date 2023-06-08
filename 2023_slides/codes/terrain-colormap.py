#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.terrain-colormap
    ~~~~~~~~~~~~~~~~~~~~~~

    Show the terrain colormap.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 12:20:38 PM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# Get the color codes for the 'terrain' colormap
cmap = plt.cm.get_cmap('terrain')
colors = cmap(range(256))

# Print the color codes
for i, color in enumerate(colors):
    print(f'Index {i}: {color}')


# Generate an array of values from 0 to 1
x = np.linspace(0, 1, 256)

# Create a meshgrid to plot the colormap
X, Y = np.meshgrid(x, [0])

# Plot the colormap
plt.figure(figsize=(2, 8))
plt.imshow(X,
           cmap='terrain',
           aspect='auto')
plt.axis('off')
plt.title('Terrain Colormap')
plt.show()

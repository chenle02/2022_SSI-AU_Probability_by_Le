#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.SHE-R-Cut
    ~~~~~~~~~~~~~~~

    Simulation of the SHE on R but cut off at the quarter height of the highest plot.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:06:46 AM EDT 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

def SHELoc(n, t, Lambda, r, mu):
    tlim = int(t * n**2 + 1)
    W = np.random.normal(scale=1/np.sqrt(n), size=(tlim, n + 1))
    u = np.zeros((tlim, n + 1))
    u[0] = (1/np.sqrt(2 * np.pi * mu)) * np.exp(-np.power((np.arange(n+1) / n - 0.5) / (2*mu), 2))
    for i in range(1, tlim):
        for j in range(1, n):
            u[i, j] = max(0, (u[i-1, j+1] + u[i-1, j-1])/2 + Lambda * np.power(np.abs(u[i-1, j]), r) * W[i, j])
    return u

unit = 3
n = 80 * unit
t = 0.01 * unit
mu = 0.0001
r = 1
lambdas = [0.1, 1, 1.6, 2.0, 2.4]

# Store all values of u for finding the maximum
u_values = []

for Lambda in lambdas:
    u = SHELoc(n, t, Lambda, r, mu) + 0.00000001
    u_values.append(u)

max_u = np.max(u_values)

fig, axs = plt.subplots(1, len(lambdas), subplot_kw={'projection': '3d'}, figsize=(20, 5))

for Lambda, ax, u in zip(lambdas, axs, u_values):
    m = int(np.max(u))
    vmin = np.min(u)
    vmax = np.max(u)

    X = np.linspace(-n/160, n/160, u.shape[1])
    T = np.linspace(0, t, u.shape[0])
    X, T = np.meshgrid(X, T)
    surf = ax.plot_surface(X, T, u, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_xticks([-n/160, 0, n/160])
    ax.set_yticks([0, t])
    ax.zaxis.set_major_locator(plt.MaxNLocator(5))
    ax.set_zlim(-0.1, max_u / 4)
    ax.set_title(r'$\lambda=$' + str(Lambda))

plt.subplots_adjust(right=0.9, top=0.95)  # Adjust the subplot layout

plt.savefig('Delta_L_QuarterHeight.pdf')
plt.savefig('Delta_L_QuarterHeight.eps')
plt.savefig('Delta_L_QuarterHeight.jpeg')

plt.close()

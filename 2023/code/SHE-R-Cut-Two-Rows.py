#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.SHE-R-Cut-Two-Rows
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Simulation one-dimensional stochastic heat equation on R with localized initial data.
    The results will be presented in two rows:
        First row: original plots
        Second row: plots truncated at 1/4 of the maximum value.

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:07:21 AM EDT 2023
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


n = 240
t = 0.03
mu = 0.0001
r = 1
lambdas = [0.1, 1, 1.8, 2.4, 3.0]

# Store all values of u for finding the maximum
u_values = []

for Lambda in lambdas:
    u = SHELoc(n, t, Lambda, r, mu) + 0.00000001
    u_values.append(u)

max_u = np.max(u_values)

fig, axs = plt.subplots(2, len(lambdas), subplot_kw={'projection': '3d'}, figsize=(20, 10))

for idx, Lambda in enumerate(lambdas):
    for j in range(2):
        u = u_values[idx]
        m = int(np.max(u))
        vmin = np.min(u)
        vmax = np.max(u)

        X = np.linspace(-n/160, n/160, u.shape[1])
        T = np.linspace(0, t, u.shape[0])
        X, T = np.meshgrid(X, T)
        surf = axs[j][idx].plot_surface(X, T, u, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)

        axs[j][idx].set_xlabel('x')
        axs[j][idx].set_ylabel('t')
        axs[j][idx].set_xticks([-n/160, 0, n/160])
        axs[j][idx].set_yticks([0, t])
        axs[j][idx].zaxis.set_major_locator(plt.MaxNLocator(5))
        if j == 1:
            axs[j][idx].set_zlim(-1, max_u / 4)
        else:
            axs[j][idx].set_zlim(-1, m)
        axs[j][idx].set_title(r'$\lambda=$' + str(Lambda))

plt.subplots_adjust(right=0.9, top=0.95)  # Adjust the subplot layout

plt.savefig('Delta_L_TwoRows.pdf')
plt.savefig('Delta_L_TwoRows.eps')
plt.savefig('Delta_L_TwoRows.jpeg')

plt.close()

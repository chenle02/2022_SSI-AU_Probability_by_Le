#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    codes.SHE
    ~~~~~~~~~

    Simulation for stochastic heat equation on interval with Dirichlet boundary condition

    :Copyright: (c) 2023 by Le Chen (chenle02@gamil.com).
    :Acknowledgment: Chatgpt accessed on 2023-06-07.
    :License: MIT License, see LICENSE for more details.
    :Created at Wed Jun  7 11:04:40 AM EDT 2023
"""

import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D


def SHE(n, t, Lambda):
    tlim = int(t * n**2 + 1)
    W = norm.rvs(size=(tlim, n + 1)) / np.sqrt(n)
    u = np.zeros((tlim, n + 1))
    u[0] = np.abs(np.sin(np.arange(n + 1) * np.pi / n))

    for i in range(1, tlim):
        u[i, 1:n] = np.maximum(((u[i - 1, 2:] + u[i - 1, 0:n-1] - 2 * u[i - 1, 1:n]) / (2 * np.sqrt(n)) + u[i - 1, 1:n] + Lambda * u[i - 1, 1:n] * W[i, 1:n]), 0)
    return u


def animate(u, n, t, Lambda, k, min_val, max_val, file_name):
    tlim = int(t * n**2 + 1)
    fig, ax = plt.subplots()

    ax.set_ylim(min_val, max_val)
    ax.set_ylabel('u(t,x)')

    ax.set_xlabel('x')
    ax.set_xticks([0, u[k].shape[1]//2, u[k].shape[1]])
    ax.set_xticklabels([-1, 0, 1])
    ax.set_xticks([-1, 0, 1])

    ax.set_title(r'$\lambda$={}'.format(Lambda[k]))

    line, = ax.plot(u[k][0])

    def update(frame):
        line.set_ydata(u[k][frame])
        return line,

    ani = FuncAnimation(
        fig,
        update,
        frames=range(1, tlim, 3),
        interval=10,  # 10ms delay between frames
        blit=True)
    ani.save(file_name + '.gif', writer='pillow')


def plot3D(u, t, Lambda, k, min_val, max_val, file_name, dpi=100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # X, Y = np.meshgrid(np.arange(u[k].shape[1]), np.arange(u[k].shape[0]))
    X, Y = np.meshgrid(np.arange(u[k].shape[1]) / u[k].shape[1] * 2 - 1, np.arange(u[k].shape[0]) / (u[k].shape[0] - 1) * t)
    ax.plot_surface(X, Y, u[k], cmap='rainbow')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([0,t])
    ax.set_zlim(min_val, max_val)
    ax.set_title(r'$\lambda$={}'.format(Lambda[k]))
    # plt.show()
    save_path = os.path.join(os.getcwd(), file_name + '.png')
    plt.savefig(save_path, dpi=dpi)  # Save the plot as PNG, dpi is the resolution of the figure
    plt.close(fig)  # Close the figure to release memory


n = 100
t = 0.5
Lambda = [0.1, 1, 2, 3]
u = [SHE(n, t, lam) for lam in Lambda]
dpi = 300  # image resolution


# Start time
start_time = datetime.datetime.now()
formatted_start_time = start_time.strftime("%Y%m%d-%H%M")
print("Start at " + formatted_start_time)

for i in range(len(Lambda)):
    print(r'Generating SHE for $\lambda$={}'.format(Lambda[i]))
    animate(u, n, t, Lambda, i, np.min(u[i]), np.max(u[i]), formatted_start_time + '_SHE-Lambda_' + str(i))
    plot3D(u, t, Lambda, i, np.min(u[i]), np.max(u[i]), formatted_start_time + '_SHE-Lambda_' + str(i), dpi)

# End time
end_time = datetime.datetime.now()
formatted_end_time = end_time.strftime("%Y%m%d-%H%M")
print("Complete at " + formatted_end_time)

# Calculate and print the running time
running_time = end_time - start_time
print("Running time: ", running_time)

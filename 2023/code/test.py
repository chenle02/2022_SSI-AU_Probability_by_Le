import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the size of the landscape
size = 100

# Generate a random Gaussian field as the landscape
landscape = np.random.normal(loc=0, scale=1, size=(size, size))

# Create a walker with a position and a path
walker = {'position': np.array([size // 2, size // 2]), 'path': []}

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(16, 16))
im = ax.imshow(landscape,
               cmap='terrain',
               origin='lower'
               )
line, = ax.plot([], [], 'r-', linewidth=3)

dot, = ax.plot([], [], 'ro', markersize=12)  # Blue dot for the head

start_label = ax.text(0, 0, 'ro', color='r', ha='right', va='bottom', fontsize=12)
end_label = ax.text(0, 0, 'rs', color='r', ha='right', va='bottom', fontsize=12)

# Initialization function
def init():
    line.set_data([], [])
    dot.set_data([], [])
    start_label.set_position((0, 0))
    end_label.set_position((0, 0))
    return line, dot, start_label, end_label

# Animation update function
def update(frame):
    # Append the current position to the path
    walker['path'].append(walker['position'].copy())

    # Calculate the gradient of the landscape at the current position
    gradient = np.array(np.gradient(landscape))[::-1, walker['position'][1], walker['position'][0]]

    # Add some randomness to the direction
    direction = gradient + np.random.normal(loc=0, scale=1, size=2)

    # Normalize the direction
    direction /= np.linalg.norm(direction)

    # Choose the direction based on the larger component of the gradient
    if np.abs(direction[0]) > np.abs(direction[1]):
        direction = np.array([np.sign(direction[0]), 0])
    else:
        direction = np.array([0, np.sign(direction[1])])

    # Convert the direction to integers and take a step in the chosen direction
    walker['position'] += direction.astype(int)

    # Convert the path to a NumPy array and update the line plot
    path = np.array(walker['path'])
    line.set_data(path[:, 1], path[:, 0])

    # Update the dot at the head of the path
    dot.set_data(path[-1, 1], path[-1, 0])

    # Update the start and end labels
    start_label.set_position((path[0, 1], path[0, 0]))
    end_label.set_position((path[-1, 1], path[-1, 0]))

    return line, dot, start_label, end_label

# Create animation
ani = FuncAnimation(fig,
                    update,
                    frames=range(1000),
                    init_func=init,
                    blit=True,
                    repeat=False,
                    interval=50)

# Show the animation
plt.show()

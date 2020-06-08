import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_grid(x_coordinates, y_coordinates, x_max, y_max):
    # 3d plot
    ax = plt.axes(projection="3d")
    ax.set_xlim3d(0, x_max)
    ax.set_ylim3d(0, y_max)
    ax.set_zlim3d(0, 7)
    x_points = x_coordinates
    y_points = y_coordinates
    z_points = 0
    ax.scatter3D(x_points, y_points, z_points, cmap='hsv')

    # 2d plot
    # plt.plot(x_coordinates, y_coordinates, 'ro')
    # plt.axis([0, x_max + 1, 0, y_max + 1])
    # plt.grid(linestyle='-', linewidth=0.5)
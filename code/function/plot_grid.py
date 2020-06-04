import matplotlib.pyplot as plt

def plot_grid(x_coordinates, y_coordinates, x_max, y_max):
    plt.plot(x_coordinates, y_coordinates, 'ro')
    plt.axis([0, x_max + 1, 0, y_max + 1])
    plt.grid(linestyle='-', linewidth=0.5)
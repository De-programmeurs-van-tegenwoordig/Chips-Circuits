import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

def plot_grid(x_coordinates, y_coordinates, size, list_of_nets):
    """ Plots the 3d graph """
    
    # Set all the variables up
    ax = plt.axes(projection="3d")
    ax.set_xlim3d(0, size)
    ax.set_ylim3d(0, size)
    ax.set_zlim3d(0, 7)
    x_points = x_coordinates
    y_points = y_coordinates
    z_points = 0

    # Form the graph
    ax.scatter3D(x_points, y_points, z_points, cmap='hsv', color="r")

    # Get every line in the graph
    for count in range(len(list_of_nets)):
        # colors = ['b','orange','g', 'purple', 'magenta', 'cyan', 'black', 'yellow']
        nets = list_of_nets[count]
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)   
        
        for item in nets:
            x = []
            y = []
            z = []
            a = item.get_coordinates_from()
            b = item.get_coordinates_to()

            x.extend([a[0], b[0]])
            # x.append(b[0])
            y.extend([a[1], b[1]])
            # y.append(b[1])
            z.extend([a[2], b[2]])
            # z.append(b[2])

            # Plot the line
            ax.plot3D(x, y, z, color=color) 
        
    # 2d plot
    # plt.plot(x_coordinates, y_coordinates, 'ro')
    # plt.axis([0, size + 1, 0, size + 1])
    # plt.grid(linestyle='-', linewidth=0.5)

    # for count in range(len(list_of_nets)):
        #     colors = ['b','r','g','bl']
        #     nets = list_of_nets[count]
            
        #     for item in nets:
        #         a = item.get_coordinates_from()
        #         b = item.get_coordinates_to()
        #         # print(a, b)

        #         x.append(a[0])
        #         x.append(b[0])
        #         y.append(a[1])
        #         y.append(b[1])
        #         z.append(a[2])
        #         z.append(b[2])
                # c = (a[0], b[0], a[2])
                # d = (a[1], b[1], b[2])

            # .plot3D(x, y, z, color=colors[count])   
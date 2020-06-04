import matplotlib.pyplot as plt
from models import *

def plot_grid(x_coordinates, y_coordinates, x_max, y_max):
    plt.plot(x_coordinates, y_coordinates, 'ro')
    plt.axis([0, x_max + 1, 0, y_max + 1])
    plt.grid(linestyle='-', linewidth=0.5)


def Read(file_name):
    """ reads the file """
    with open (file_name) as f:
        lines = f.read().splitlines()
    for i in range (len(lines)):
        lines[i] = lines[i].split(',')
    return(lines)

if __name__ == '__main__':
    print_0 = Read("gates&netlists/chip_0/print_0.csv")
    netlist_1 = Read("gates&netlists/chip_0/netlist_1.csv")
    x = []
    y = []
    chips = {}
    counter = 1

    for i in range (len(print_0)):
        if i == 0:
            continue
        x_coordinate = int(print_0[i][1])
        y_coordinate = int(print_0[i][2])

        chip = Chip(counter, x_coordinate, y_coordinate)
        chips[int(counter)] = chip

        x.append(int(print_0[i][1]))
        y.append(int(print_0[i][2]))
        counter += 1
    plot_grid(x,y,6,6)

    net_needed = 0
    line_from = []
    line_to = []

    for i in range (len(netlist_1)):
        if i == 0:
            continue
        
        origin = int(netlist_1[i][0])
        destination = int(netlist_1[i][1])

        chip_origin = chips[origin]
        chip_destination = chips[destination]

        coordinates_origin = chip_origin.get_coordinates()
        coordinates_destination = chip_destination.get_coordinates()

        origin_x = int(coordinates_origin[0])
        origin_y = int(coordinates_origin[1])

        destination_x = int(coordinates_destination[0])
        destination_y = int(coordinates_destination[1])

        net_needed += (abs(destination_x - origin_x))
        net_needed += (abs(destination_y - origin_y))

        line_from.append([origin_x, origin_y])
        line_to.append([destination_x, origin_y])

        line_from.append([destination_x, origin_y])
        line_to.append([destination_x, destination_y])

        for i in range(len(line_from)):
            a = []
            b = []

            a.append(int(line_from[i][0]))
            a.append(int(line_to[i][0]))

            b.append(int(line_from[i][1]))
            b.append(int(line_to[i][1]))

            plt.plot(a, b, color='b')

    print("hoi", net_needed)
    plt.show()





        

        

        



        

        








    

    
    plt = plot(x,y,6,6)    

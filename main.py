import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import chip
from code.classes import grid
import csv

if __name__ == '__main__':
    print_0 = grid.Grid("data/chip_0/print_0.csv")
    # netlist_1 = Read("data/chip_0/netlist_1.csv")

    x = []
    y = []
    chips = {}
    counter = 1

    print(print_0)

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

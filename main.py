import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import chip
from code.classes import grid
from code.classes import net
from code.algorithms import random_solve
import csv
import random

if __name__ == '__main__':
    color = 'b'
    check_list = []
    test_grid = grid.Grid("data/chip_0/print_0.csv", "data/chip_0/netlist_1.csv")
    size = 10
    chips = test_grid.get_chips()
    x = []
    y = []
    for i in chips:
        coordinates = chips[i].get_coordinates()
        x_coordinate = int(coordinates[0])
        y_coordinate = int(coordinates[1])

        x.append(x_coordinate)
        y.append(y_coordinate)

    plot_grid.plot_grid(x,y,10,10)

    netlists = test_grid.get_netlists()
    net_needed = 0
    list_of_nets = {}

    counter = 0

    for netlist in netlists:
        origin = int(netlist[0])
        destination = int(netlist[1])

        chip_origin = chips[origin]
        chip_destination = chips[destination]

        coordinates_origin = chip_origin.get_coordinates()
        coordinates_destination = chip_destination.get_coordinates()

        origin_x = int(coordinates_origin[0])
        origin_y = int(coordinates_origin[1])

        destination_x = int(coordinates_destination[0])
        destination_y = int(coordinates_destination[1])

        delta_x = destination_x - origin_x
        delta_y = destination_y - origin_y

        coordinates_from = (origin_x, origin_y)
         
        result = random_solve.random_solve(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter)

        list_of_nets[counter] = result[0]
        counter += 1
        tries = result[1]

        # if delta_x > 0:
        #     for i in range(delta_x):
        #         coordinates_to = (current_x + 1, origin_y)
        #         current_x += 1

        #         new_netlist = net.Net(coordinates_from, coordinates_to)
        #         coordinates_from = coordinates_to
        #         list_of_nets.append(new_netlist)    
        # else:
        #     for i in range(abs(delta_x)):
        #         coordinates_to = (current_x - 1, origin_y)
        #         current_x -= 1

        #         new_netlist = net.Net(coordinates_from, coordinates_to)
        #         coordinates_from = coordinates_to
        #         list_of_nets.append(new_netlist)
            
        # if delta_y > 0:
        #     for i in range(delta_y):
        #         coordinates_to = (current_x, current_y + 1)
        #         current_y += 1

        #         new_netlist = net.Net(coordinates_from, coordinates_to)
        #         coordinates_from = coordinates_to
        #         list_of_nets.append(new_netlist)
        # else:
        #     for i in range(abs(delta_y)):
        #         coordinates_to = (current_x, current_y - 1)
        #         current_y -= 1

        #         new_netlist = net.Net(coordinates_from, coordinates_to)
        #         coordinates_from = coordinates_to
        #         list_of_nets.append(new_netlist)

        net_needed += (abs(destination_x - origin_x))
        net_needed += (abs(destination_y - origin_y))

        for count in range(len(list_of_nets)):
            colors = ['b','r','g','bl']
            nets = list_of_nets[count]
            
            for x in nets:
                a = x.get_coordinates_from()
                b = x.get_coordinates_to()
                c = (a[0], b[0])
                d = (a[1], b[1])
                plt.plot(c, d, color=colors[count])

        checkpoint += 1
        if checkpoint == 3:
            break

        # for x in list_of_nets:
        #     a = x.get_coordinates_from()
        #     b = x.get_coordinates_to()
        #     c = (a[0], b[0])
        #     d = (a[1], b[1])
        #     plt.plot(c, d)

        checkpoint = checkpoint + 1
        check_list.append(checkpoint)
    print(check_list, check_list.count(1), check_list.count(2), check_list.count(3), check_list.count(4), check_list.count(5) )
    # print("hoi", net_needed, checkpoint)
    plt.show()
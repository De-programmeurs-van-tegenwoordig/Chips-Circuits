import matplotlib.pyplot as plt
from code.function import plot_grid
from code.classes import chip
from code.classes import grid
from code.classes import net
import csv
import random

if __name__ == '__main__':
    test_grid = grid.Grid("data/chip_0/print_0.csv", "data/chip_0/netlist_1.csv")
    size = 7

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
    line_from = []
    line_to = []
    list_of_nets = []

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
        current_x = origin_x
        current_y = origin_y
         
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while current_x != destination_x or current_y != destination_y:
            count = 0
            check = True
            direction = random.choice(directions)
            coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1])
            print(coordinates_from)
            
            if coordinates_to[0] > size  or coordinates_to[1] > size  or coordinates_to[0] < 0 or coordinates_to[1] < 0:
                check = False
            
            for i in list_of_nets:
                net_from = i.get_coordinates_from()
                net_to = i.get_coordinates_to()
                if coordinates_to == net_from or coordinates_to == net_to:
                    count += 1
                if coordinates_from == net_from and coordinates_to == net_to:
                    check = False
                    break
                if coordinates_from == net_to and coordinates_to == net_from:
                    check = False
                    break
                
            if count == 2:
                check = False
            
            if check:
                new_netlist = net.Net(coordinates_from, coordinates_to)
                list_of_nets.append(new_netlist)
                coordinates_from = coordinates_to 
                current_x = coordinates_to[0]
                current_y = coordinates_to[1]





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

        for x in list_of_nets:
            a = x.get_coordinates_from()
            b = x.get_coordinates_to()

            c = (a[0], b[0])
            d = (a[1], b[1])
            plt.plot(c, d, color='b')
        break

    print("hoi", net_needed)
    plt.show()





        

        

        



        

        








 

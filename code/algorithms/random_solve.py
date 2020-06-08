import random
from code.classes import net

def random_solve(origin_x, origin_y, destination_x,  destination_y, size, list_of_nets, counter):
    tries = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    nets = set()
    coordinates_from = (origin_x, origin_y)

    current_x = origin_x
    current_y = origin_y

    while current_x != destination_x or current_y != destination_y:
        tries += 1
        if tries == 2000:
            return nets, tries
        count = 0
        check = True
        direction = random.choice(directions)
        coordinates_to = (coordinates_from[0] + direction[0], coordinates_from[1] + direction[1])
        
        if coordinates_to[0] > size  or coordinates_to[1] > size  or coordinates_to[0] <= 0 or coordinates_to[1] <= 0:
            check = False

        for i in range(len(list_of_nets)):
            for x in list_of_nets[i]:
                net_from = x.get_coordinates_from()
                net_to = x.get_coordinates_to()

                if (coordinates_to[0] == net_from[0] and coordinates_to[1] == net_from[1]) or (coordinates_to[0] == net_to[0] and coordinates_to[1] == net_to[1]):
                    count += 1
                if (coordinates_from[0] == net_from[0] and coordinates_from[1] == net_from[1]) and (coordinates_to[0] == net_to[0] and coordinates_to[1] == net_to[1]):
                    check = False
                    break
                if (coordinates_from[0] == net_to[0] and coordinates_from[1] == net_to[1]) and (coordinates_to[0] == net_from[0] and coordinates_to[1] == net_from[1]):
                    check = False
                    break

                # f.write(str(coordinates_from) + str(net_from) + str(check) + str(counter) + str(coordinates_to) + str(net_to) + "\n")
                # print(coordinates_from,net_from, check, coordinates_to, net_to)

        for i in nets:
            net_from = i.get_coordinates_from()
            net_to = i.get_coordinates_to()

            if (coordinates_to[0] == net_from[0] and coordinates_to[1] == net_from[1]) or (coordinates_to[0] == net_to[0] and coordinates_to[1] == net_to[1]):
                    count += 1
            if (coordinates_from[0] == net_from[0] and coordinates_from[1] == net_from[1]) and (coordinates_to[0] == net_to[0] and coordinates_to[1] == net_to[1]):
                check = False
                break
            if (coordinates_from[0] == net_to[0] and coordinates_from[1] == net_to[1]) and (coordinates_to[0] == net_from[0] and coordinates_to[1] == net_from[1]):
                check = False
                break

        if count == 2:
            check = False
        
        if check:
            new_netlist = net.Net(coordinates_from, coordinates_to)
            nets.add(new_netlist)
            coordinates_from = coordinates_to 
            current_x = coordinates_to[0]
            current_y = coordinates_to[1]

    return nets, tries

    
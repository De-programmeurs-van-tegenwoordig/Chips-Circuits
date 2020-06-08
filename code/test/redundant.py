



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
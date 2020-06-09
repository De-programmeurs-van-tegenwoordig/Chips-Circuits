def check_constraints(coordinates_from, coordinates_to, coordinates_destination, list_of_nets, nets, list_of_coordinates, size):
   # Checks if the line doesnt break rules
        check = True
        cross = False

        # Checks if line exceeds boundaries
        if coordinates_to[0] > size  or coordinates_to[1] > size or coordinates_to[2] > size or coordinates_to[0] < 0 or coordinates_to[1] < 0 or coordinates_to[2] < 0:
            check = False

        for i in range(len(list_of_nets)):
            for x in list_of_nets[i]:
                net_from = x.get_coordinates_from()
                net_to = x.get_coordinates_to()

                if coordinates_to == net_from or coordinates_to == net_to:
                    count = True
                if coordinates_from == net_from and coordinates_to == net_to:
                    check = False
                    break
                if coordinates_from == net_to and coordinates_to == net_from:
                    check = False
                    break
                if coordinates_to in list_of_coordinates and coordinates_to != coordinates_destination:
                    check = False
                    break

        for i in nets:
            net_from = i.get_coordinates_from()
            net_to = i.get_coordinates_to()

            if coordinates_to == net_from or coordinates_to == net_to:
                cross = True
            if coordinates_from == net_from and coordinates_to == net_to:
                check = False
                break
            if coordinates_from == net_to and coordinates_to == net_from:
                check = False
                break
            if coordinates_to in list_of_coordinates and coordinates_to != coordinates_destination:
                check = False
                break
        
        return check, cross
def check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets):
    '''Checks hard and soft constraints'''
    
    # Checks if the line doesnt break rules
    size = grid_file.get_size()
    coordinates_gates = grid_file.get_total_gates()
    check = True
    cross = False
    
    # Checks if line exceeds boundaries
    if coordinates_to[0] > size  or coordinates_to[1] > size or coordinates_to[2] > 7 or coordinates_to[0] < 0 or coordinates_to[1] < 0 or coordinates_to[2] < 0:
        check = False
    
    # Checks if line goes thorugh gate which is not the lines destination
    if coordinates_to in coordinates_gates and coordinates_to != coordinates_destination:
        check = False
        return check, cross

    list_of_routes = grid_file.get_list_of_routes()

    # Loops through all parts of the current line
    for i in nets:
        net_from = i.get_coordinates_from()
        net_to = i.get_coordinates_to()

        # Checks first of the destination is achieved
        # Checks if parts overlap
        # When destination is not achieved it will checks overlap aswell
        # It checks if the line crosses
        # And checks if part of the line does not go through a zone of another gate
        if coordinates_to == coordinates_destination:
            if coordinates_from == net_from and net_to == coordinates_to:
                check = False
                return check, cross
            elif net_from == coordinates_to and net_to == coordinates_from:
                check = False
                return check, cross
        else:
            if coordinates_to == net_from or coordinates_to == net_to:
                cross = True
            if coordinates_from == net_from and coordinates_to == net_to:
                check = False
                return check, cross
            if coordinates_from == net_to and coordinates_to == net_from:
                check = False
                return check, cross

            gate_number = grid_file.get_current_gate_number(coordinates_destination[0], coordinates_destination[1])
            if coordinates_to in grid_file.get_total_zones() and coordinates_to not in grid_file.get_zone(gate_number) and coordinates_from not in grid_file.get_total_gates():
                check = False
                return check, cross

    
    # Loops through all excisting lines
    for item in list_of_routes:
        for x in list_of_routes[item]:
            net_from = x.get_coordinates_from()
            net_to = x.get_coordinates_to()

            # Checks first of the destination is achieved
            # Checks if parts overlap
            # When destination is not achieved it will checks overlap aswell
            # It checks if the line crosses
            # And checks if part of the line does not go through a zone of another gate
            if coordinates_to == coordinates_destination:
                if coordinates_from == net_from and net_to == coordinates_to:
                    check = False
                    return check, cross
                elif net_from == coordinates_to and net_to == coordinates_from:
                    check = False
                    return check, cross
            else:
                if coordinates_to == net_from or coordinates_to == net_to:
                    cross = True
                if coordinates_from == net_from and coordinates_to == net_to:
                    check = False
                    return check, cross
                elif coordinates_from == net_to and coordinates_to == net_from:
                    check = False
                    return check, cross

                gate_number = grid_file.get_current_gate_number(coordinates_destination[0], coordinates_destination[1])
                if coordinates_to in grid_file.get_total_zones() and coordinates_to not in grid_file.get_zone(gate_number) and coordinates_from not in grid_file.get_total_gates():
                    check = False
                    return check, cross
    
    return check, cross
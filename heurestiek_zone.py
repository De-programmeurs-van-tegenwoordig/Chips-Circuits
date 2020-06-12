def check_constraints(grid_file, coordinates_from, coordinates_to, coordinates_destination, nets):
   # Checks if the line doesnt break rules
    size = grid_file.get_size()
    coordinates_gates = grid_file.get_coordinates_gates()
    check = True
    cross = False

    # Checks if line exceeds boundaries
    if coordinates_to[0] > size  or coordinates_to[1] > size or coordinates_to[2] > 7 or coordinates_to[0] < 0 or coordinates_to[1] < 0 or coordinates_to[2] < 0:
        check = False

    list_of_routes = grid_file.get_list_of_routes()

    gates_zones = {}
    gatess_zone = []
    gg = []
    for gate in coordinates_gates:
        gate_zone = []
        gate[0] = int(gate[0])
        gate[1] = int(gate[1])
        gate[2] = int(gate[2])

        gg.append((gate[0], gate[1], gate[2]))

        gate_zone.append((gate[0] + 1, gate[1], gate[2]))
        gate_zone.append((gate[0] - 1, gate[1], gate[2]))
        gate_zone.append((gate[0], gate[1] + 1, gate[2]))
        gate_zone.append((gate[0], gate[1] - 1, gate[2]))
        gate_zone.append((gate[0], gate[1], gate[2] + 1))

        gatess_zone.append((gate[0] + 1, gate[1], gate[2]))
        gatess_zone.append((gate[0] - 1, gate[1], gate[2]))
        gatess_zone.append((gate[0], gate[1] + 1, gate[2]))
        gatess_zone.append((gate[0], gate[1] - 1, gate[2]))
        gatess_zone.append((gate[0], gate[1], gate[2] + 1))
        
        gates_zones[(gate[0], gate[1], gate[2])] = gate_zone

    for i in nets:
        net_from = i.get_coordinates_from()
        net_to = i.get_coordinates_to()

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
            if coordinates_to in gatess_zone and coordinates_to not in gates_zones[coordinates_destination] and coordinates_from not in gg:
                check = False
                return check, cross

    for i in range(len(list_of_routes)):
        for x in list_of_routes[i]:
            net_from = x.get_coordinates_from()
            net_to = x.get_coordinates_to()

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
                elif coordinates_to in gatess_zone and coordinates_to not in gates_zones[coordinates_destination] and coordinates_from not in gg:
                    check = False
    
    return check, cross
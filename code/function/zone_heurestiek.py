def zone_heurestiek(grid_file, coordinates_from, coordinates_to, coordinates_destination):
    gate_number = grid_file.get_current_gate_number(coordinates_destination[0], coordinates_destination[1])
    
    if coordinates_to in grid_file.get_total_zones() and coordinates_to not in grid_file.get_zone(gate_number) and coordinates_from not in grid_file.get_total_gates():
        return True
    return False
from code.classes import net
from code.classes import node
from code.function import check_constraints
import random

class Astar():
    def __init__(self, grid_file, cros_):
        self.cros_ = cros_
        self.grid_file = grid_file

    def get_lengthy_netlists(self, grid_file):
        """
        Counts how many connections each chip has and returns the order from high to low.
        """
        netlists = list(grid_file.get_netlists())

        netlist_distance = {}

        for item in netlists:
            coordinates_gates = grid_file.get_coordinates_netlist(item)
            distance = abs(coordinates_gates[0] - coordinates_gates[2]) + abs(coordinates_gates[1] - coordinates_gates[3])
            netlist_distance[item] = distance

        length_netlists = []

        while len(netlist_distance) != 0:
            min_distance = min(netlist_distance, key=lambda key: netlist_distance[key])
            length_netlists.append(min_distance)
            del netlist_distance[min_distance]

        # Reverses the list from long to small
        print(netlists)
        length_netlists.reverse()

        return length_netlists

    def get_populated_netlists(self, grid_file):
        """
        Counts how many connections each chip has and returns the order from high to low.
        """
        netlists = list(grid_file.get_netlists())
        counting = {}

        for item in netlists:
            counting[int(item[0])] = 0
            counting[int(item[1])] = 0
        for item in netlists:
            counting[int(item[0])] += 1
            counting[int(item[1])] += 1

        populated_netlists = []

        while len(counting) != 0:
            gate_max = max(counting, key=lambda key: counting[key])
            del counting[gate_max]

            for item in netlists:
                if int(item[0]) == gate_max or int(item[1]) == gate_max:
                    populated_netlists.append(item)
                    netlists.remove(item)

        print(populated_netlists)
        print(len(populated_netlists))
        return populated_netlists
    
    def run(self, output):
        netlists = list(self.grid_file.get_netlists())
        random.shuffle(netlists)
        print(netlists)
        
        size = self.grid_file.get_size()

        counter = 0

        while len(netlists) != 0:
            netlist = self.grid_file.get_coordinates_netlist(netlists[0])
            netlists.pop(0)
            print(netlist)
            self.crosses = 0

            open_list = []
            closed_list = []

            directions = [(0,0,1), (0,0,-1), (0,-1,0), (1,0,0), (0,1,0), (-1,0,0)]

            origin_x = netlist[0]
            origin_y = netlist[1]
            destination_x = netlist[2]
            destination_y = netlist[3]

            coordinates_origin = (origin_x,origin_y,0)
            coordinates_destination = (destination_x, destination_y,0)

            # Create start and end node
            start_node = node.Node(None, coordinates_origin)
            start_node.g = start_node.h = start_node.f = 0
            end_node = node.Node(None, coordinates_destination)
            end_node.g = end_node.h = end_node.f = 0

            open_list.append(start_node)

            while len(open_list) != 0:
   
                # Get the current node
                current_node = open_list[0]
                current_index = 0
                nets = []
                for index, item in enumerate(open_list, 0):
                    if item.f <= current_node.f:
                        current_node = item
                        current_index = index
                
                # Pop current off open list, add to closed list
                open_list.pop(current_index)
                closed_list.append(current_node)

                if current_node == end_node:
                    paths = []
                    
                    current = current_node
                    while current is not None:
                        paths.append(current.position)
                        current = current.parent
                    paths.reverse()

                    for i in range (len(paths)):
                        if i != len(paths) - 1:
                            cross = check_constraints.check_constraints(self.grid_file, paths[i], paths[i+1], coordinates_destination, nets)[1]
                            if cross:
                                self.crosses += 1
                            new_netlist = net.Net(paths[i], paths[i+1])
                            nets.append(new_netlist)

                    self.grid_file.add_route(nets, self.crosses)
                    counter += 1
                    print(len(open_list))

                    print(f"Route connected: {coordinates_origin}, {coordinates_destination}. Crosses: {self.crosses}. Nummer: {counter}")

                    break
                
                # Generate children
                children = []

                for direction  in directions:
                    node_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1], current_node.position[2] + direction[2])
                    
                    if node_position[0] > size  or node_position[1] > size or node_position[2] > 7 or node_position[0] < 0 or node_position[1] < 0 or node_position[2] < 0:
                        continue

                    check = check_constraints.check_constraints(self.grid_file, current_node.position, node_position, coordinates_destination, nets)
                    if check[0]:
                        if check[1]:
                                new_node = node.Node(current_node, node_position)
                                new_node.cross = True
                                children.append(new_node)

                        else:
                            new_node = node.Node(current_node, node_position)
                            children.append(new_node)
                
                for child in children:
                    d = False
                    for closed_child in closed_list:
                        if child == closed_child:
                            d = True
                            continue

                
                    child.g = current_node.g + 1
                    child.h = abs(destination_x - child.position[0]) + abs(destination_y - child.position[1]) + abs(0 - child.position[2])

                    if self.cros_ == True:    
                        if child.cross:
                            child.h += 300

                    child.f = child.g + child.h

                    for open_node in open_list:
                        if child == open_node and child.g >= open_node.g:
                            d = True
                            
                    if d == True:
                        continue

                    open_list.append(child)
                            
                    
            
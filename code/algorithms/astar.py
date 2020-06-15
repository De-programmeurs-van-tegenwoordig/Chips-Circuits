# from code.classes import net
# from code.classes import node
# from code.function import check_constraints
# import random

# class Astar():
#     def __init__(self, grid_file):
#         self.grid_file = grid_file

#     def get_netlists(self, grid_file):
#         netlists = list(grid_file.get_netlists())

#         netlist_distance = {}

#         for item in netlists:
#             coordinates_gates = grid_file.get_coordinates_netlist(item)
#             distance = abs(coordinates_gates[0] - coordinates_gates[2]) + abs(coordinates_gates[1] - coordinates_gates[3])
#             netlist_distance[item] = distance

#         length_netlists = []

#         while len(netlist_distance) != 0:
#             min_distance = min(netlist_distance, key=lambda key: netlist_distance[key])
#             length_netlists.append(min_distance)
#             del netlist_distance[min_distance]
        
#         return length_netlists
    
#     def run(self, output):
#         netlists = self.get_netlists(self.grid_file)
#         size = self.grid_file.get_size()

#         while len(netlists) != 0:
#             netlist = self.grid_file.get_coordinates_netlist(netlists[0])
#             netlists.pop(0)

#             open_list = []
#             closed_list = []
#             coordinates_successor = {}

#             directions = [(0,0,1), (0,0,-1), (0,-1,0), (1,0,0), (0,1,0), (-1,0,0)]



#             origin_x = netlist[0]
#             origin_y = netlist[1]
#             destination_x = netlist[2]
#             destination_y = netlist[3]

#             coordinates_origin = (origin_x,origin_y,0)
#             coordinates_destination = (destination_x, destination_y,0)

#             # Create start and end node
#             start_node = Node(None, coordinates_origin)
#             start_node.g = start_node.h = start_node.f = 0
#             end_node = Node(None, coordinates_destination)
#             end_node.g = end_node.h = end_node.f = 0

#             open_list.append(start_node)

#             while len(open_list) != 0:
#                 # Get the current node
#                 current_node = open_list[0]
#                 current_index = 0
#                 for index, item in enumerate(open_list):
#                     if item.f < current_node.f:
#                         current_node = item
#                         current_index = index
                
#                 # Pop current off open list, add to closed list
#                 open_list.pop(current_index)
#                 closed_list.append(current_node)
                
#                 # Found the goal
#                 if current_node == end_node:
#                     path = []
#                     current = current_node
#                     while current is not None:
#                         path.append(current.position)
#                         current = current.parent
#                     return path[::-1] # Return reversed path`
                
#                 # Generate children
#                 children = []

#                 for direction  in directions:
#                     node_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1], current_node.position[2] + direction[2])
                    
#                     if node_position[0] > size  or node_position[1] > size or node_position[2] > 7 or node_position[0] < 0 or node_position[1] < 0 or node_position[2] < 0:
#                         continue

#                     new_node = Node(current_node, node_position)

#                     children.append(new_node)
                
#                 for child in children:

#                     for closed_child in closed_list:
#                         if child = closed_child:
#                             continue
                        
#                     child.g = current_node.g + 1
#                     child.h = abs(destination_x - child.position[0]) + abs(destination_y - child.position[1]) + abs(0 - child.position[2])
#                     child.f = child.g + child.h

#                     for open_node in open_list:
#                         if child == open_node and child.g > open_node.g:
#                             continue
                    
#                     open_list.append(child)





                





        
                
            

            
            


        


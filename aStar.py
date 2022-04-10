from Graph import Directed_Graph
from Node import Node

class A_Star:
    """aStar search algorithm
    """
    def __init__(self, graph: Directed_Graph):
        self.graph = graph
        
    def search_path(self, start, goal):
        """Perform astar search.

        Args:
            start (_type_): _description_
            goal (_type_): _description_

        Raises:
            print: if start or goal node does not exist
            print: if vertex isn't an instance of Node
        """
        start_node, goal_node = None, None
        
        # retrieve the Node
        start_node = self.graph.find_vertex(start) 
        goal_node = self.graph.find_vertex(goal)
        
        if start_node is None:
            raise print("start does not exist. Can't find vertex with a value {0} in the graph.".format(start))
        if goal_node is None:
            raise print("goal does not exist. Can't find vertex with a value {0} in the graph.".format(goal))
        
        self.__search_path_util(start_node, goal_node) # start search
    
    def __compute_gn(self, close_list, n_node:Node):
        print("\nCompute g(n). CL_len:{0}, n_node:{1}".format(len(close_list), n_node))
        gn = 0
        
        # compute the distance from first node in the list to last node in close list
        for i in range(0, len(close_list)):
            node_1, node_2 = None, None
            
            node_1 = close_list[i]
            
            
            if i + 1 < len(close_list): # check if node_1 isn't the last index
                node_2 = close_list[i + 1] # retrieve the next node
                
            # check if nodes is an instance of class Node
            if not isinstance(node_1, Node):
                raise print("{0} is not an instance of Node".format(node_1))
            if node_2 is not None and not isinstance(node_2, Node):
                raise print("{0} is not an instance of Node".format(node_2))
            
            # check if node_1 isn't the last index
            if i + 1 < len(close_list):
                gn += node_1.neighbors[node_2]
                print("\tn1:{0} n2:{1} gn:{2}".format(node_1, node_2, gn))
            else:
                # otherwise, add last node to current_node which is n_node.
                gn += node_1.neighbors[n_node]
                print("\tn1:{0} n2:{1} gn:{2}".format(node_1, n_node, gn))
                
        return gn
    
    def __search_path_util(self, start_node: Node, goal_node: Node):
        
        # init list
        open_list = []
        close_list = []
        
        # add start node to open list as a tuple/pair (f(n), node).
        open_list.append((start_node.heuristic_value, start_node))
        
        loop_counter = 1
        while open_list:
            print("Loop #{0} start -----------------".format(loop_counter))
            self.__display_open_list(open_list)
            print()
            self.__display_close_list(close_list)
            
            smallest_fn = open_list.pop(0) # retrieve the smallest fitness
            vertex = smallest_fn[1] # retrieve the vertex, which stored in the second index
            
            if not isinstance(vertex, Node):
                raise print("{0} is not an instance of Node".format(vertex))
            
            close_list.append(vertex) #attach the vertex to the close list
            vertex.visited() # set vertex to visited
            
            # check if vertex is the goal, if yes, end process
            if vertex.value == goal_node.value:
                print("Goal Found")
                print("Loop #{0} end -----------------".format(loop_counter))
                self.__show_path(close_list)
                return -1 
            
            # check vertex's neighbors 
            for neighbor, weight  in vertex.neighbors.items():
                if not isinstance(neighbor, Node):
                    raise print("{0} is not an instance of Node".format(neighbor))
                
                if not neighbor.is_visited:
                    # if isn't visited yet add to open list
                    hn = neighbor.heuristic_value
                    gn = self.__compute_gn(close_list, neighbor) # computation fron start_node to nth node
                    fn = gn + hn
                    
                    open_list.append((fn, neighbor))
                    
            open_list.sort() # sort list in asc ord
            
            print("Loop #{0} end -----------------".format(loop_counter))
            loop_counter += 1
        
        print("\n\nGoal Unreachable!!")
        return -1
            
    def __show_path(self, close_list):
        print("Path: ", end="")
        print(*close_list, sep=" -> ")
    
    def __display_open_list(self, open_list):
        print("OL:")
        for fn, node in open_list:
            print("\t({0}. {1})".format(fn, node))
    
    def __display_close_list(self, close_list):
        print("CL:")
        for node in close_list:
            print("\t{0}".format(node))
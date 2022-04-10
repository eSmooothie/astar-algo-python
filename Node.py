


class Node:
    
    def __init__(self, value):
        self.value = value
        self.neighbors = {}
        self.is_visited = False
        self.heuristic_value = None
        
    def set_heauristc_value(self, value):
        self.heuristic_value = value
        
    def visited(self):
        """Set the node as visited.
        
        self.is_visited = True
        """
        self.is_visited = True
        
    def add_neighbor(self, node, weight: int):
        """Add node to the neighbor of this object.
        If the node is already a neighbor of the object
        it wont add it.

        Args:
            node (Node): an instance of Node
            weight (int): the distance or the value of the edge from this object to node
        """
        if self.neighbors.get(node) is None:
            self.neighbors[node] = weight
            
    def reset(self):
        """Reset the "is_visited" property to False.
        """
        self.is_visited = False
    
    def __str__(self):
         return "Node(value={0}, is_visited={1}, hn={2})".format(self.value, self.is_visited, self.heuristic_value)
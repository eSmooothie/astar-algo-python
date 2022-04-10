from Node import Node

class Directed_Graph:
    """Directed graph
    """
    def __init__(self):
        self.vertices = []
        
    def add_vertex(self, node_1, node_2, weight: int):
        """Since this is a directed graph.
        Add node_2 to the neighbor of node_1 with the weight. Not
        vice versa.
        
        e.g
            node_1 -> node_2

        Args:
            node_1 (Any): an value for the node
            node_2 (Any): an value for the node
            weight (int): the distance to reach or the value of the edge from node_1 to node_2
            
        Raises:
            print: if vertex is not an instance of Node
        """
        
        if node_1 == node_2:
            raise print("node_1 and node_2 have the same value. Must be unique.")
        
        vertex_1, vertex_2 = None, None
        
        # search for the instances of the node_1 and node_2 from the vertices
        for vertex in self.vertices:
            if not isinstance(vertex, Node):
                raise print("vertex {0} is not an instance of Node".format(vertex))
            
            if vertex.value == node_1:
                vertex_1 = vertex
            if vertex.value == node_2:
                vertex_2 = vertex
                
        
        # if node_1 or node_2 does not yet exist in the graph
        # then create a new instance of that node and add it to the graph
        if vertex_1 is None:
            vertex_1 = Node(node_1)
            self.vertices.append(vertex_1)
            
        if vertex_2 is None:
            vertex_2 = Node(node_2)
            self.vertices.append(vertex_2)
            
        vertex_1.add_neighbor(node=vertex_2, weight=weight)
        
    def set_heuristic_values(self, heuristic_values : dict):
        """Set heauristic value per vertex(if exist) in the graph.

        Args:
            heauristic_values (dict): <node_value : heuristic_value>
            
        Raises:
            print: if vertex is not an instance of Node
        """
        for vertex in self.vertices:
            if not isinstance(vertex, Node):
                raise print("vertex {0} is not an instance of Node".format(vertex))
            
            if heuristic_values.get(vertex.value) is None:
                raise print("Can't find the node with value {0} in the dictionary.".format(vertex.value))
            
            h_value = heuristic_values.get(vertex.value)
            vertex.set_heauristc_value(h_value)
            
    def find_vertex(self, value):
        """Return the instance of Node if exist.
        
        Args:
            value (Any): node value your looking for

        Raises:
            print: if vertex is not an instance of Node
        
        Returns:
            The object Node if exist otherwise None.
        """
        for vertex in self.vertices:
            if isinstance(vertex, Node) and vertex.value == value:
                return vertex
            
        return None
    
    def reset(self):
        """Reset the is_visited property of all vertex.

        Raises:
            print: if vertex is not an instance of Node
        """
        for vertex in self.vertices:
            if not isinstance(vertex, Node):
                raise print("vertex {0} is not an instance of Node".format(vertex))
            
            vertex.reset()
            
        
        
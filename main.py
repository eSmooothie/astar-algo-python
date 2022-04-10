from Graph import Directed_Graph
from aStar import A_Star

if __name__ == "__main__":
    
    graph = Directed_Graph()
    graph.add_vertex('S','A',1)
    graph.add_vertex('S','G',10)
    graph.add_vertex('A','B',2)
    graph.add_vertex('A','C',1)
    graph.add_vertex('B','D',5)
    graph.add_vertex('D','G',2)
    graph.add_vertex('C','D',3)
    graph.add_vertex('C','G',4)
    graph.add_vertex('D','G',2)
    
    heuristic_values = {
        'S':5,
        'A':3,
        'B':4,
        'C':2,
        'D':6,
        'G':0,
        }
    
    graph.set_heuristic_values(heuristic_values=heuristic_values)
    
    a_start = A_Star(graph)
    a_start.search_path('S','G')
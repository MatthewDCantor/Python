class graph(object):
    """docstring fo Graph."""

    def __init__(self, graph_dict = None):

        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def add_vertex(self, vertex):

        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]


    def generate_edges(self):

        edge = []

        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if {vertex,neighbor} not in edge:
                    edge.append({vertex,neighbor})
        return edge

dict = {'a' : ['b','d'],
     'b' : ['a','c','e'],
     'c' : ['b','f'],
     'd' : ['a','e'],
     'e' : ['b','d']
}

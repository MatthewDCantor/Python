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
        if len(edge) == 1:
            
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


    def return_dict(self):
        return self.graph_dict

    def vertex_edges(self, vertex):

        edges = self.generate_edges()
        v_edges = []
        for edge in edges:
            if vertex in edge:
                for v in edge:
                    if v != vertex:

                        v_edges.append(int(v)-1)

            else:
                continue

        return v_edges
def takefirst(x):
    return x[0]
def takesecond(x):
    return x[1]

m_n_k = list(map( int , input().split(' ')))
m = m_n_k[0]
n = m_n_k[1]
k = m_n_k[2]


val = list(map( int , input().split(' ')))
edges = [input().split( ) for i in range(n)]

g = graph()

for i in range(m):
    g.add_vertex(str(i+1))

for i in range(n):
    g.add_edge(edges[i])

for i in range(0,m):
    nearby_node_and_val = []
    j = str(i+1)
    v_edges = g.vertex_edges(j)
    for v in v_edges:
        nearby_node_and_val.append([v+1,val[v]])
    nearby_node_and_val.sort(key = takefirst, reverse = True)
    nearby_node_and_val.sort(key = takesecond , reverse = True)

    if k > len(nearby_node_and_val):
        print(-1)
    else:
        print(nearby_node_and_val[k-1][0])











"""
-----test input----
'3 4 2'
'2 4 4'
'1 3'
'1 2'
'2 3'
'1 1'
"""

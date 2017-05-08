class Graph(object):
    def __init__(self, graph_dict=None):
        """
        Initializes a graph object
        :param graph_dict: If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        Returns the vertices of a graph
        :return:
        """
        return list(self.__graph_dict.keys())

    def edges(self):
        """
        Returns the edges of a graph
        :return:
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty list
        as a value is added to the dictionary. Otherwise nothing has to be done.
        :param vertex:
        :return:
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges
        :param edge:
        :return:
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = vertex2

    def __generate_edges(self):
        """
        A static method generating the edges of the graph "graph".
        Edges are represented as sets with one (a loop back to the vertext) or two vertices
        :return:
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def get_degree(self, vertex):
        degree = len(self.__graph_dict[vertex])
        return degree

    def is_directed(self, vertex1, vertex2):
        if vertex2 in self.__graph_dict[vertex1]:
            return True
        else:
            return False

    def get_relative_rank(self, vertex1, vertex2):
        degree = self.get_degree(vertex1)
        if self.is_directed(vertex1, vertex2):
            return 1/float(degree)
        else:
            return 0
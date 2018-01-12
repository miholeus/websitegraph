# coding: utf-8


class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def vertex_info(self, vertex):
        """returns vertex info"""
        return self.__graph_dict[vertex]

    def add_vertex(self, vertex):
        """ add vertex if it is not in "dict"
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ add edge to graph
        """
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = [v2]

    def __generate_edges(self):
        """ Generate edges. Edges are represented as "sets"
        """
        edges = set()
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                edges.add((vertex, neighbour))
        return edges

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                found_paths = self.find_all_paths(vertex,
                                                  end_vertex,
                                                  path)
                for p in found_paths:
                    paths.append(p)
        return paths

    def diameter(self):
        """ calculates the diameter of the graph """

        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        smallest_paths = []
        for (start, end) in pairs:
            paths = self.find_all_paths(start, end)
            if len(paths) > 0:
                smallest = sorted(paths)[0]
                smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        diameter = len(smallest_paths[-1]) - 1
        return [diameter, smallest_paths[-1]]

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


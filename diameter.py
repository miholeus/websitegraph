# coding: utf-8

from graph import Graph
from tools import build_graph
import begin

# this is the example of graph
# g = {"a": ["b", "d"],
#      "b": ["c"],
#      "c": [],
#      "d": ["e"],
#      "e": []}


@begin.start(auto_convert=True)
def main(path: 'Set path to file'):
    graph_structure = build_graph(path)

    graph = Graph(graph_structure)
    diameter = graph.diameter()
    print("Diameter is: {}".format(diameter[0]))
    print("Url path is: {}".format(" -> ".join(diameter[1])))


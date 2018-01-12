# coding: utf-8

from graph import Graph
from collections import defaultdict
import begin
import json

# this is the example of graph
# g = {"a": ["b", "d"],
#      "b": ["c"],
#      "c": [],
#      "d": ["e"],
#      "e": []}


def build_graph(path):
    """
    Builds graph from given path file
    :param path:
    :return:
    """
    with open(path) as data:
        d = json.load(data)
        graph = defaultdict(list)
        for url in d:
            if url["referring_url"] is None:
                continue
            if not url["current_url"] in url["referring_url"]:
                graph[url["referring_url"]].append(url["current_url"])
        g = Graph(graph)
        return g


@begin.start(auto_convert=True)
def main(path: 'Set path to file'):
    graph = build_graph(path)
    diameter = graph.diameter()
    print("Diameter is: {}".format(diameter[0]))
    print("Url path is: {}".format(" -> ".join(diameter[1])))


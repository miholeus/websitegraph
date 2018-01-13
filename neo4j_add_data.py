# coding: utf-8

from collections import defaultdict
from py2neo import Graph, Node, Relationship
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
    graph = build_graph(path)
    graph_db = Graph("http://neo4j:7474/db/data")

    for url in graph:
        if url is None:
            continue
        tx = graph_db.begin()
        try:
            url_node = Node("Url", name=url)
            graph_db.merge(url_node)
            for link in graph[url]:
                if link is None:
                    continue
                try:
                    link_node = Node("Url", name=link)
                    graph_db.merge(link_node)

                    node_relation = Relationship(url_node, "LINKS_TO", link_node)
                    tx.create(node_relation)
                except Exception as e:
                    print("Error in building relationship: " + str(e))
            tx.commit()
        except Exception as e:
            print("got error: " + str(e))
            tx.rollback()
            continue
    print("Added to neo4j")

# coding: utf-8
from collections import defaultdict
import json


def build_graph(path):
    """
    Builds graph from given path file
    :param path:
    :return: dict
    """
    with open(path) as data:
        d = json.load(data)
        graph = defaultdict(list)
        for url in d:
            if url["referring_url"] is None:
                continue
            if not url["current_url"] in url["referring_url"]:
                graph[url["referring_url"]].append(url["current_url"])
        return graph

# coding: utf-8

from py2neo import Graph
import re

graph_db = Graph("http://neo4j:7474/db/data")

query = """
match (n)
where (n)-[:LINKS_TO]->() and not ()-[:LINKS_TO]->(n)
match p = (n)-[:LINKS_TO*1..]->(m)
return p, length(p) as L
order by L desc
limit 1
"""

p = re.compile('\(\w+\)')

data = graph_db.data(query)

data = data[0]
print("Diameter is: {}".format(data['L']-1))
path = []
for rel in data['p']:
    path.append(rel.start_node()['name'])
# path may be different compared to diameter.py script
# this happens if there are multiple nodes with the same longest path
# neo4j makes its own sorting
print("Url path is: {}".format(" -> ".join(path)))


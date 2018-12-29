import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

list_of_nodes = [{"Name":"Adrien", "club":"Tesla"},"Alix","John","Cyril"]
list_of_edges = [("Adrien","Alix",4), ("John","Cyril",5),("Adrien","John",1)]
G = nx.DiGraph()
G.add_nodes_from(list_of_nodes)
G.add_edge("Paul","Alix",w=8)
G.add_edge("Paul","Adrien",w=3)
G.add_edge("Alexandre","Adrien",w=2)
G.add_edge("Alexandre","Alix",w=3)
G.add_edge("Alexandre","Cyril",w=3)

for l in list_of_edges:
    G.add_edge(l[0],l[1],w=l[2])
    
    
fig, ax = plt.subplots(1, 1, figsize=(8, 6));
nx.draw_networkx(G, ax=ax)

nodes = [{'name': str(i), 'club': G.node[i]['club']}
         for i in G.nodes()]
links = [{'source': u[0], 'target': u[1]}
         for u in G.edges()]
with open('graph.json', 'w') as f:
    json.dump({'nodes': nodes, 'links': links},
              f, indent=4,)
import networkx as nx
import json
import http_server

 
list_of_nodes = ["Adrien","Alix","John","Cyril"]
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
    
    

from networkx.readwrite import json_graph

for n in G:
    G.node[n]['name'] = n

d = json_graph.node_link_data(G)
json.dump(d, open('G.html','w'))
http_server.load_url('G.html')
import networkx as nx
import math
import numpy as np
import matplotlib.pyplot as plt

def my_graph_generator(file):
    G = nx.Graph()
    source = []
    node_indices = []
    '''je créé un graphe ) partir du fichier sur Trump. C'est une liste de tuple avec (node1,node2,weight-edge)'''
    with open(file,'r') as f:
        for line in f:
            line = line.strip()
            names = line.split(";")
            source.append((names[0],names[1]))
            G.add_edge(names[0],names[1],weight=1)
            for nm in names[0:1]:
                if nm not in node_indices:
                    node_indices.append(nm)
                    
    size_array = []
    for nd in G.nodes():
        G.node[nd]['degree'] = len(G[nd])
        G.node[nd]['size'] = int(G.node[nd]['degree']*250)
        size_array.append(G.node[nd]['size'])
    
    

    plt.savefig("my_graph.png")


    def my_circular_layout(Graph):
        Nodes = G.nodes
        N = len(Nodes)
        N_list = np.arange(0,N)
        circ = [i*2*math.pi/N for i in N_list]
        x = [math.cos(j) for j in circ]
        y = [math.sin(j) for j in circ]
        my_circ_layout = {}
        k = 0
        for nd in Nodes:
                my_circ_layout[nd] = [x[k],y[k]]
                k+=1
                
        return my_circ_layout
        

    

    nx.draw(G,pos = my_circular_layout(G),with_labels=True,nodecolor = 'b',edge_color = 'r',node_size=size_array,node_shape='o')
    return [G,my_circular_layout]
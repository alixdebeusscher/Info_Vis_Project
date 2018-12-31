import networkx as nx
import math
import numpy as np
import matplotlib.pyplot as plt
import plotly as ply
import plotly.plotly as py
import plotly.graph_objs as go

def my_circular_layout(Graph):
        Nodes = Graph.nodes
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


def my_level_layout(Graph):
    Nodes = Graph.nodes
    degree_list = []
    label_dict = {}
    my_lvl_layout = {}
    for nd in Nodes:
        degree_node = len(Graph[nd])
        if degree_node in degree_list:
            label_dict[degree_node].append(nd)
        else:
            degree_list.append(degree_node)
            label_dict[degree_node] = [nd] 
                           
    degree_list = sorted(degree_list)
    for key in label_dict:
        L = len(label_dict[key])
        x_vectors_key = np.linspace(0,L-1,L)
        x_vectors_key[:] = [a - L/2 for a in x_vectors_key]
        y_vectors_key = degree_list.index(key)
        k = 0
        for label in label_dict[key]:
            my_lvl_layout[label] = [x_vectors_key[k],y_vectors_key]
            k+=1
        
    return my_lvl_layout
        
        
        
def my_graph_generator(file, value):
    G = nx.Graph()
    source = []
    node_indices = []
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
        G.node[nd]['size'] = int(math.sqrt(G.node[nd]['degree'])*20)
        size_array.append(G.node[nd]['size'])
    
    
    
    pos =  []
    if value =='circ':
        pos = my_circular_layout(G)
    if value =='lvl':
        pos = my_level_layout(G)
    if value =='oth':
        pos = nx.fruchterman_reingold_layout(G)
    #nx.draw(G,pos = my_circular_layout(G),with_labels=True,nodecolor = 'b',edge_color = 'r',node_size=size_array,node_shape='o')
    return [G,pos,size_array]

def get_graph(value):
    return my_graph_generator('my_data_set.txt', value)
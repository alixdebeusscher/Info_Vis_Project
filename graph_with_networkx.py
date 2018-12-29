import networkx as nx
import math
import numpy as np
import matplotlib.pyplot as plt
import plotly as ply
import plotly.plotly as py
import plotly.graph_objs as go

def my_graph_generator(file):
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
        G.node[nd]['size'] = int(G.node[nd]['degree']*10)
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
                Nodes[nd]['pos'] = [x[k],y[k]]
                k+=1
                
        return my_circ_layout
        

    

    nx.draw(G,pos = my_circular_layout(G),with_labels=True,nodecolor = 'b',edge_color = 'r',node_size=size_array,node_shape='o')



    edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=1,color='#f00'),
    hoverinfo='none',
    mode='lines')

    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=size_array,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=2)))

    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color']+=tuple([len(adjacencies[1])])
        node_info = '# of connections: '+str(len(adjacencies[1]))
        node_trace['text']+=tuple([node_info])
        
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                            title='My Network',
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20,l=5,r=5,t=40),
                           ))
    
    ply.tools.set_credentials_file(username='delhayead', api_key='Twixfb2Wjh6VdXxB2dvT')
    py.iplot(fig, filename='my_networkx')
    return [G,my_circular_layout]
    
    

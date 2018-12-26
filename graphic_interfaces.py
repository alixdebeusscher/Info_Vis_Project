#IMPORT SECTION
import numpy as np
import pandas as pd
import holoviews as hv
import networkx as nx
from holoviews import opts
from bokeh.io import output_file, save, show
from bokeh.plotting import figure, show, output_file
from holoviews.element.graphs import layout_nodes
hv.extension('bokeh')
#============================================================

#On définit les attribut principal du graphe (taille, padding,ect...) et les options des noeds, edges,...
'''------------------------------------ DISPLAY SIZE --------------------------------------------------------'''
defaults = dict(width=800, height=600, padding=0.1)
hv.opts.defaults(
   opts.EdgePaths(**defaults), opts.Graph(**defaults), opts.Nodes(**defaults))

'''---------------------------------------LOADING FILE -----------------------------------------------------'''
source = []
labels = []
'''je créé un graphe ) partir du fichier sur Trump. C'est une liste de tuple avec (node1,node2,weight-edge)'''
with open('test_trump.txt','r') as f:
    for line in f:
        names = line.split(";")
       # names[2] = float(names[2])
        source.append((names[0],names[1],0.5))
        for nm in names[0:1]:
            if nm not in labels:
               labels.append(nm)
                
                
                
Donald_trump_grph = hv.Graph(source, vdims = 'weight')  
#layout_nodes(revue_graph,layout=nx.layout.circular_layout, kwargs={'weight':'weight'}) 


''' Je créé un graphe avec le package networks'''
G = nx.Graph()
G.add_nodes_from([1,2,3])
G.add_weighted_edges_from([(1,2,1),(1,3,0.5),(2,3,-0.5)])
G.node[1]['Nom'] = 'Adrien'
G.node[2]['Nom'] = 'Alix'
G.node[3]['Nom'] = 'Alexandre'
print(G.nodes(data=True))
G.add_edge(1,2,color='red')
print(G[1][2])

'''Le je fais le layout du graph'''

"----------------------------------RENDERING --------------------------------------------"

renderer = hv.renderer('bokeh')

# Using renderer save
renderer.save(Donald_trump_grph, 'Donald_trump_grph.html')

# Convert to bokeh figure then save using bokeh
plot = renderer.get_plot(Donald_trump_grph).state

from bokeh.io import output_file, save, show
save(plot, 'Donald_trump_grph.html')
# OR
output_file("Donald_trump_grph.html")
show(plot)
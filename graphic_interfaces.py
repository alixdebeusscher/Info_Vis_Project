#IMPORT SECTION
import random as rand
import numpy as np
import pandas as pd
import holoviews as hv
hv.extension('bokeh')
import networkx as nx
from holoviews import opts
from bokeh.io import output_file, save, show
from bokeh.plotting import figure, show, output_file
from holoviews.element.graphs import layout_nodes

#============================================================

#On définit les attribut principal du graphe (taille, padding,ect...) et les options des noeds, edges,...
'''------------------------------------ DISPLAY SIZE --------------------------------------------------------'''
defaults = dict(width=700, height=600, padding=0.1)
hv.opts.defaults(
   opts.EdgePaths(**defaults), opts.Graph(**defaults), opts.Nodes(**defaults))

'''---------------------------------------LOADING FILE -----------------------------------------------------'''
source = []
labels = []
'''je créé un graphe ) partir du fichier sur Trump. C'est une liste de tuple avec (node1,node2,weight-edge)'''
with open('trump-net.txt','r') as f:
    for line in f:
        line = line.strip()
        names = line.split(";")
       # names[2] = float(names[2])
        source.append((names[0],names[1],1))
        for nm in names[0:1]:
            if nm not in labels:
               labels.append(nm)
                
      
Donald_trump1_grph = hv.Graph(source, vdims = 'weight')  

"----------------------------------RENDERING --------------------------------------------"

renderer = hv.renderer('bokeh')

# Using renderer save
renderer.save(Donald_trump1_grph, 'Donald_trump1_grph.html')

tg = renderer.get_plot(Donald_trump1_grph).state

# OR
output_file("Donald_trump1_grph.html")
show(tg)
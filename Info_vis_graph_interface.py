import math
import random
import networkx as nx
import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.palettes import Spectral4
import holoviews as hv
from holoviews import opts
from bokeh.io import output_file, save, show
from bokeh.plotting import figure, show, output_file
from holoviews.element.graphs import layout_nodes


defaults = dict(width=1200, height=600, padding=0.1)
hv.opts.defaults(
   opts.EdgePaths(**defaults), opts.Graph(**defaults), opts.Nodes(**defaults))
#Les indices des noeuds 
source = []
node_indices = []
strat_list = []
'''je créé un graphe ) partir du fichier sur Trump. C'est une liste de tuple avec (node1,node2,weight-edge)'''
with open('trump-net.txt','r') as f:
    for line in f:
        line = line.strip()
        names = line.split(";")
        source.append((names[0],names[1]))
        for nm in names[0:1]:
            if nm not in node_indices:
               node_indices.append(nm)
               
N = len(node_indices)    
index_number = np.linspace(0,N-1,N)     
index_number = [int(x) for x in index_number]
# Alors je comprend pas pk mais si je dépasse 80 nodes 
#il veut plus les afficher et il afficher que les edges :/

index_number = index_number[0:79]
N = len(index_number)
      
plot = figure(title='Graph Layout Demonstration', x_range=(-10.1,10.1), y_range=(-10.1,10.1),
              tools='', toolbar_location=None) #On définit la taille de la figure et son nom

graph = GraphRenderer() #On créé le graph (et son rendu)

graph.node_renderer.data_source.add(index_number, 'index')
graph.node_renderer.data_source.add(Spectral8, 'color')#On modifie la couleur des noeuds
#graph.node_renderer.glyph = Oval(height=0.1, width=0.1, fill_color='color')
graph.node_renderer.glyph = Circle(size=50, fill_color=Spectral4[0])

graph.edge_renderer.data_source.data = dict(
    start=start_list,
    end=index_number)

### start of layout code
circ = [i*2*math.pi/N for i in index_number]
x = [random.randint(-8,8) for i in index_number]
y = [random.randint(-8,8) for i in index_number]

graph_layout = dict(zip(index_number, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# Permet de soit rendre les noeds observable soit les edges
plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())
graph.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
graph.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[2])

graph.edge_renderer.glyph = MultiLine(line_color="#AAAAAA", line_alpha=0.7, line_width=2)
graph.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=2)
graph.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=2)
graph.selection_policy = NodesAndLinkedEdges()
graph.inspection_policy = EdgesAndLinkedNodes()


# Rendering Exportation
plot.renderers.append(graph)

output_file('graph.html')
show(plot)
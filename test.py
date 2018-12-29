import platform
import plotly
import plotly.offline as offline
import graph_with_networkx as gw
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot

def make_annotations(pos, anno_text, font_size=14, font_color='rgb(10,10,10)'):
    pos=list(pos.items())
    L=len(pos)
    print(pos)
    if len(anno_text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(dict(text=anno_text[k], 
                                x=pos[k][1][0], 
                                y=pos[k][1][1]+0.075,#this additional value is chosen by trial and error
                                xref='x1', yref='y1',
                                font=dict(color= font_color, size=font_size),
                                showarrow=False)
                          )
    return annotations 

def plot_graph(tab, names):
    G=tab[0]
    pos=tab[1] 
    labels = [ k for k,v in pos.items()]
    Xn=[]
    Yn=[]
    for key in pos.keys():
        x = (pos.get(key))[0]
        y = (pos.get(key))[1]
        Xn.append(x)
        Yn.append(y)
    
    trace_nodes=dict(type='scatter',
                     x=Xn, 
                     y=Yn,
                     mode='markers',
                     marker=dict(size=28, color='rgb(0,240,0)'),
                     text=labels,
                     hoverinfo='text')
    
    Xe=[]
    Ye=[]
    for e in G.edges():
        Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
        Ye.extend([pos[e[0]][1], pos[e[1]][1], None])
        
    trace_edges=dict(type='scatter',
                     mode='lines',
                     x=Xe,
                     y=Ye,
                     line=dict(width=1, color='rgb(25,25,25)'),
                     hoverinfo='none' 
                    )
    
    axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title='' 
              )
    layout=dict(title= 'My Graph',  
                font= dict(family='Balto'),
                width=600,
                height=600,
                autosize=False,
                showlegend=False,
                xaxis=axis,
                yaxis=axis,
                margin=dict(
                l=40,
                r=40,
                b=85,
                t=100,
                pad=0,
           
        ),
        hovermode='closest',
        plot_bgcolor='#efecea', #set background color            
        )
    
    updatemenus=list([
    dict(
        buttons=list([   
            dict(
                args=['type', 'surface'],
                label='3D Surface',
                method='restyle'
            ),
            dict(
                args=['type', 'heatmap'],
                label='Heatmap',
                method='restyle'
            )             
        ]),
        direction = 'down',
        pad = {'r': 10, 't': 10},
        showactive = True,
        x = 0.1,
        xanchor = 'left',
        y = 1.1,
        yanchor = 'top' 
        ),
    ])
            
    layout['updatemenus'] = updatemenus
    layout['annotations'] = layout
    fig = dict(data=[trace_edges, trace_nodes], layout=layout)
    if names ==1:
        fig['layout'].update(annotations=make_annotations(pos, labels))
    plot(fig)

names=1
plot_graph(gw.graph, names)
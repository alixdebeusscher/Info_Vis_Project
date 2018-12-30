import platform
import plotly
import plotly.offline as offline
import dash
import dash_core_components as dcc
import dash_html_components as html
import graph_with_networkx_alix as gw
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot
from .fa2l import force_atlas2_layout

def make_annotations(labels, Xn, Yn, font_size=14, font_color='rgb(10,10,10)'):
    L=len(Xn)
    if len(labels)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(dict(text=labels[k], 
                                x=Xn[k]+0.075, 
                                y=Yn[k]+0.075,
                                xref='x1', yref='y1',
                                font=dict(color= font_color, size=font_size),
                                showarrow=False)
                          )
    return annotations

def get_data(lab, value):
    tab=gw.get_graph(value)
    G=tab[0]
    pos=tab[1]
    size_array = tab[2]
    labels = [ k for k,v in pos.items()]
    Xn = []
    Yn = []
    for key in pos.keys():
        x = (pos.get(key))[0]
        y = (pos.get(key))[1]
        Xn.append(x)
        Yn.append(y)
    
    trace_nodes=dict(type='scatter',
                     x=Xn, 
                     y=Yn,
                     mode='markers',
                     marker=dict(size=size_array, color='rgb(0,240,0)'),
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
    layout=dict(
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
    #annotations=make_annotations(),
    plot_bgcolor='#efecea', #set background color            
    )
    if lab==1:
        layout.update(annotations=make_annotations(labels, Xn, Yn))
    return [trace_edges, trace_nodes],layout
    


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#allo=get_data(lab=1)          
#data=allo[0]
#layout=allo[1]
app.layout = html.Div(children=[
    html.H4(children='Hello Dash', style={
                    'textAlign': 'center'
                }),
        
            dcc.Checklist(
                id='list',
                options=[{'label': 'Labels', 'value': 'lab'}],
                values=['lab']
            ),
            dcc.Dropdown(id='algo', options=[
                    {'label': 'Circular', 'value': 'circ'},
                    {'label': 'Other', 'value': 'oth'}
                    ],
                    value='circ'
            
            ),
            dcc.Graph(
                id='graphic',
#                figure={
#                    'data': data,
#                    'layout': layout
#                }, 
                style={'display': 'inline-block'}
            )
    ])
    
@app.callback(
    Output(component_id='graphic', component_property='figure'),
    [Input(component_id='list', component_property='values'),
     Input(component_id='algo', component_property='value')]
)
def update_graph(list_l, algo_l):
    if 'lab' in list_l:
        allo=get_data(1, algo_l)  
    else:
        allo=get_data(0, algo_l)       
    data=allo[0]
    layout=allo[1]
    return  { 'data': data,'layout': layout}
    

if __name__ == '__main__':

    app.run_server(debug=True)


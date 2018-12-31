import dash
import dash_core_components as dcc
import dash_html_components as html
import graph_with_networkx_alix as gw
from dash.dependencies import Input, Output
import numpy as np

def make_annotations(labels, Xn, Yn, font_size, font_color='rgb(10,10,10)'):
    L=len(Xn)
    if len(labels)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(dict(text=labels[k], 
                                x=Xn[k], 
                                y=Yn[k],
                                xref='x1', yref='y1',
                                font=dict(color= font_color, size=font_size),
                                showarrow=False)
                          )
    return annotations

def get_data(ordered, lab, l_s, node, ada, node_col, line_size, value):
    tab=gw.get_graph(value, ordered)
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
    colop=[]
    if ada==0:
        size_array=[25 for i in size_array]
        colop=[node_col for i in size_array]
    else:
        colop = np.gradient(np.array(size_array, dtype=float))

    trace_nodes=dict(type='scatter',
                     x=Xn, 
                     y=Yn,
                     mode='markers',
                     marker=dict( size=[i * node for i in size_array], color=colop),
                     text=labels,
                     hoverinfo='text')
    
    Xe=[]
    Ye=[]
    #pr = nx.shortest_path(G, 'THIBAULT', 'LAURENT')
#    tabShort = [('ADRIEN', 'THIBAULT'), ('ADRIEN', 'LAURENT')]
#    colo_l = ['black' for i in G.edges()]
#    i=0
    for e in G.edges():
#        if e in tabShort:
#            colo_l[i] = 'red'
        Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
        Ye.extend([pos[e[0]][1], pos[e[1]][1], None])
        #i+=1
    print(Xe)
    print(Ye)
    #colo = 'rgb(25,25,25)'
    
    trace_edges=dict(type='scatter',
                     mode='lines',
                     x=Xe,
                     y=Ye,
                     line=dict(width=line_size, color='rgb(0,0,0)'),
                     hoverinfo='none' 
                    )
    
    axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title='' 
              )
    layout=dict(
            width=850,
            height=850,
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
    #plot_bgcolor='#efecea', #set background color            
    )
    if lab==1:
        layout.update(annotations=make_annotations(labels, Xn, Yn, l_s))
    return [trace_edges, trace_nodes],layout
    


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H3(children='Donald Trump Network', style={
                    'textAlign': 'center'
                }),
        
            html.Div([
                html.H5(children='Layout section'),
                dcc.Dropdown(id='algo', options=[
                    {'label': 'Circular', 'value': 'circ'},
                    {'label': 'Other', 'value': 'oth'},
                    {'label': 'Level layout', 'value': 'lvl'}
                    ],
                    value='circ'),
                html.Div(id='testest', children=[
                 html.Div('Select circle size'),
                 
                dcc.Slider(
                    id='c_size',
                    min=1,
                    max=50,
                    step=0.2,
                    value=14,
                ),
                    dcc.Checklist(id='circord',
                    options=[
                        {'label': 'Sort node', 'value': 'sort'}
                    ],
                    values=[]
                )
                        ],  style= {'display': 'block'}),
                html.H5(children='Label section'),
                 html.Div('Select labels size'),
                dcc.Slider(
                    id='l_size',
                    min=1,
                    max=50,
                    step=0.2,
                    value=14,
                ),
                dcc.Checklist(
                id='list',
                options=[{'label': 'Show labels', 'value': 'lab'}],
                values=['lab']
            ),html.H5(children='Node section'),
             html.Div('Select node size'),
            dcc.Slider(
                id='node_size',
                min=0,
                max=5,
                step=0.1,
                value=1,
            ),dcc.Checklist(
                id='ada_node',
                options=[{'label': 'Adapt node size', 'value': 'ada'}],
                values=['ada']
            ),html.Div(children = [html.Div('Choose node color'),dcc.RadioItems(
                id = 'nod_col',
                options=[
                    {'label': 'Black', 'value': 'Black'},
                    {'label': 'Red', 'value': 'Red'},
                    {'label': 'Green', 'value': 'Green'}
                ],
                value='Green')
            ], id='n_c', style= {'display': 'block'}),
            html.H5(children='Edge section'),
            html.Div('Select edge size'),
            dcc.Slider(
                id='edge_size',
                min=0,
                max=5,
                step=0.1,
                value=1,
            ), 
            html.H5(children='Upload your own doc'),
                    dcc.Upload(id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.Div(id='output-data-upload'),]
            , style={'width': '25%', 'display': 'inline-block'}),
            html.Div([
                    dcc.Graph(
                id='graphic'
                #animate=True
#                figure={
#                    'data': data,
#                    'layout': layout
#                }, 
            )],style={ 'display': 'inline-block', 'float':'right'})
    ])
    
@app.callback(
    Output(component_id='testest', component_property='style'),
    [Input(component_id='algo', component_property='value')])
def algo_choice(algo):
    if algo=='circ':
        return {'display' : 'block'}
    return {'display' : 'none'}

@app.callback(
    Output(component_id='n_c', component_property='style'),
    [Input(component_id='ada_node', component_property='values')])
def algo_choice(a_node):
    if 'ada' in a_node:
        return {'display' : 'none'}
    return {'display' : 'block'}

@app.callback(
    Output(component_id='graphic', component_property='figure'),
    [Input(component_id='circord', component_property='values'),
     Input(component_id='list', component_property='values'),
     Input(component_id='l_size', component_property='value'),
     Input(component_id='algo', component_property='value'),
     Input(component_id='node_size', component_property='value'),
     Input(component_id='ada_node', component_property='values'),
     Input(component_id='nod_col', component_property='value'),
     Input(component_id='edge_size', component_property='value')]
)
def update_graph(ordered, list_l, l_s, algo, node, a_node, node_col, edge):
    if 'sort' in ordered:
        ore=True
    else:
        ore=False
    if 'lab' in list_l:
        lab = 1
    else:
        lab=0
    if 'ada' in a_node:
        ada = 1
    else:
        ada=0
    allo=get_data(ore, lab, l_s, node, ada, node_col, edge, algo)       
    data=allo[0]
    layout=allo[1]
    return  { 'data': data,'layout': layout}



if __name__ == '__main__':

    app.run_server(debug=True)


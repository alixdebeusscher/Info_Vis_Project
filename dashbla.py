# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
      visdcc.Network(id='net',
                     data={'nodes':[{'id': 1, 'label': 'Node 1', 'color':'#00ffff'},
                                    {'id': 2, 'label': 'Node 2'},
                                    {'id': 4, 'label': 'Node 4'},
                                    {'id': 5, 'label': 'Node 5'},
                                    {'id': 6, 'label': 'Node 6'}],
                             'edges':[{'id':'1-3', 'from': 1, 'to': 3},
                                      {'id':'1-2', 'from': 1, 'to': 2}]
                     },
                     options=dict(height='600px', width='100%')),
      dcc.RadioItems(id='color',
                     options=[{'label': 'Red'  , 'value': '#ff0000'},
                              {'label': 'Green', 'value': '#00ff00'},
                              {'label': 'Blue' , 'value': '#0000ff'}],
                     value='Red')
])
#app.layout = html.Div(children=[
#    html.H1(children='Hello Dash'),
#
#    html.Div(children='''
#        Dash: A web application framework for Python.
#    '''),

#    dcc.Graph(
#        id='example-graph',
#        figure={
#            'data': [
#                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#            ],
#            'layout': {
#                'title': 'Dash Data Visualization'
#            }
#        }
#    )
#])

if __name__ == '__main__':
    app.run_server(debug=True)
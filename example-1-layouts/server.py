#%%

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(
        id='first-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'bar1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'bar2'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


app.run_server(debug=True)
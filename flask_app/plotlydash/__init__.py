import dash
from dash import dcc
from dash import html

def create_dash_app(flask_app):
    dash_app = dash.Dash(__name__, server=flask_app, url_base_pathname='/dash/', suppress_callback_exceptions=True)

    dash_app.layout = html.Div([
        html.H1('Dash App'),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3,9,3,1,3], 'y': [4, 1, 2, 5, 3, 2, 6], 'type': 'point', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'point', 'name': 'NYC'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])

    return dash_app
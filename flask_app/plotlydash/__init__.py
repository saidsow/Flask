import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

def create_dash_app(flask_app):
    dash_app = dash.Dash(__name__, server=flask_app, url_base_pathname='/dash/', suppress_callback_exceptions=True)

    dash_app.layout = html.Div([
        html.H1('Dash App'),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'San Francisco', 'value': 'SF'},
                {'label': 'New York City', 'value': 'NYC'}
            ],
            value='SF'
        ),
        dcc.Graph(id='example-graph')
    ])

    @dash_app.callback(
        Output('example-graph', 'figure'),
        [Input('dropdown', 'value')]
    )
    def update_graph(selected_value):
        data = {
            'SF': {'x': [1, 2, 3], 'y': [4, 1, 2]},
            'NYC': {'x': [1, 2, 3], 'y': [2, 4, 5]}
        }
        return {
            'data': [
                {'x': data[selected_value]['x'], 'y': data[selected_value]['y'], 'type': 'bar', 'name': selected_value}
            ],
            'layout': {
                'title': f'{selected_value} Data Visualization'
            }
        }

    return dash_app
from dash import Dash
from dash import html

def create_dash_app(flask_app):
    dash_app = Dash(
        server=flask_app,
        name="DashApp",
        url_base_pathname="/dash/"  # Dash app is accessible at /dash/
    )

    # Define the layout for the Dash app
    dash_app.layout = html.Div([
        html.H1("Hello from Dash!", style={"textAlign": "center"})
    ])

from flask import g
from dash import Dash, html, dcc

def init_app(url_path):
    app = Dash(
        __name__,
        server=g.cur_app,
        routes_pathname_prefix=url_path,
        requests_pathname_prefix=url_path
    )

    app.layout = html.Div([
        html.A("Main Page", href="/"),
        
        html.H1(
            "Welcome to Dash in Flask",
            style={"textAlign": "center"}
        ),
        
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [4, 1, 2],
                        "type": "bar",
                        "name": "Category 1"
                    },
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": "Category 2"
                    }
                ],
                
                "layout": {
                    "title": "Dash Data Visualization"
                }
            }
        )
    ])

    return app.server
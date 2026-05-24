from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import ssl
from flask import g

# Bỏ verify SSL
ssl._create_default_https_context = ssl._create_unverified_context

def init_app(url_path, server=None):
    global df

    app = Dash(
        __name__,
        server=g.cur_app, 
        routes_pathname_prefix=url_path,
        requests_pathname_prefix=url_path,
    )

    df = g.df

    app.title = "Population by country"

    app.layout = html.Div(
        [
            html.A("Main page", href="/"),

            html.H1(
                "Population by country", 
                style={"textAlign": "center"}
            ),

            dcc.Dropdown(
                df.country.unique(), 
                "Canada", 
                id="dropdown-selection"         
            ),

            dcc.Graph(id="graph-content"),
        ]
    )

    # Way 1
    # @app.callback(
    #     Output("graph-content", "figure"),
    #     Input("dropdown-selection", "value"),
    # )
    # def update_graph(value):
    #     dff = df[df.country == value]
    #     return px.line(dff, x="year", y="pop")
    
    # Way 2 to scalable
    init_callbacks(app)
    
    return app.server

def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")

def init_callbacks(app):
    app.callback(
        Output("graph-content", "figure"),
        Input("dropdown-selection", "value")
    )(update_graph)
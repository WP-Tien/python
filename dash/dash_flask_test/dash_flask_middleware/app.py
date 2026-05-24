from flask import Flask, render_template_string
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import pandas as pd

from dash_apps import simple_app, population

app = Flask(__name__)

with app.app_context():
    # Define Flask context variables to be used in app.
    # In this case, we define the dataframe used in the Population app (df)
    # and the Flask instance to be passed to both apps (cur_app)
    g.df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
    )
    
    # Dash apps
    app = DispatcherMiddleware(flask_app, {
        "/simple_app": simple_app.init_app("/simple_app/"), 
        "/population": population.init_app("/population/")
    })
    
@app.route("/")
def home():
    return """
    <h1>Main Flask App</h1>
    <h2>Select your Dash app</h2>
    <ul>
        <li><a href="/simple_app/">Simple App</a></li>
        <li><a href="/population/">Population</a></li>
    </ul>
    """
from dash import Dash # The Application
from dash import dcc # Interactive Components
from dash import html # HTML tags
import pandas as pd # Reading and Organizing Data

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%y-%d")
data.sort_values("Date", inplace=True)

# Initialize Dash 
app = Dash(__name__)

app.layout = html.Div(
    children = [
        html.H1(children="Avocado Analytics",),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    }
                ],
                "layout": {"title": "Average Price of Avocados"},
            }
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"]
                    }
                ],
                "layout": {"title": "Avocados Sold"},
            }
        )  
    ], 
)

if __name__ == "__main__":
    app.run(debug=True)
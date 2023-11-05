from dash import Dash, html, dash_table
import pandas as pd

dataset_app = Dash(__name__)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

dataset_app.layout = html.Div(
    [
        html.H1("Hello Dash"),
        html.Div("Dash: A web application framework for Python."),
    ]
)
import dash
from dash import html

dash.register_page(__name__, name="Датасет", path='/dataset')

layout = html.Div([
    html.H1('This is our dataset page'),
    html.Div('This is our dataset page content.'),
])
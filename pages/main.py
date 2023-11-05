import dash
from dash import html

dash.register_page(__name__, name="Главная", path='/main')

layout = html.Div([
    html.H1('This is our main page'),
    html.Div('This is our main page content.'),
])
import dash
from dash import html

dash.register_page(__name__, name="Настройки", path='/settings')

layout = html.Div([
    html.H1('This is our settings page'),
    html.Div('This is our settings page content.'),
])
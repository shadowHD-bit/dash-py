import dash
from dash import html

dash.register_page(__name__,name="О проекте" ,path='/about')

layout = html.Div([
    html.H1('This is our about page', className='test'),
    html.Div('This is our about page content.'),
])
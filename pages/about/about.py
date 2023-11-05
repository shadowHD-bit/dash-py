import dash
from dash import html

dash.register_page(__name__,name="О проекте" ,path='/about')

layout = html.Div(className="about_content", children=[
    html.P('Добро пожаловать в ПАЙ-ДЭШ!', className='about__text_title'),
    html.P('This is our about page', className='about__text_subtitle'),
    html.Div('This is our about page content.'),
])
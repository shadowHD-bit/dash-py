import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div(className="start_content", children=[
    html.Img(src='assets/images/3dcasual.png', className='start_content__images'),
    html.P('Добро пожаловать в ПАЙ-ДЭШ!', className='start__text_title'),
    html.P('Это веб-приложение предназначена для визуализации исходных маркетинговых данных компании.', className='start__text_subtitle'),
])
import dash
from dash import html
import dash_bootstrap_components as dbc
from partials.alert_link_page import build_alert_link_page

layout = html.Div(className="start_content", children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.Img(src='assets/gif/bloom-woman-and-man-doing-web-browser-development.gif',
                     className='start_content__images'),
            html.P('Добро пожаловать в ПАЙ-ДЭШ!',
                   className='start__text_title'),
            html.P('Это веб-приложение предназначена для визуализации исходных маркетинговых данных компании.',
                   className='start__text_subtitle'),
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            build_alert_link_page('Главная страница', 
                                  'Главная страница дашборда для датасета представляет собой обзорную панель, отображающую ключевые метрики и визуализации, связанные с данными данного датасета. Датасет содержит данные о продажах, заказах, клиентах и других аспектах операций компании.', 'main', 'danger')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Настройки', 
                                  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                                  'settings', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Страница датасета', 
                                  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                                  'dataset', 'success')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('География', 
                                  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                                  'geography', 'warning')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Товары', 
                                  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                                  'products', 'dark')
        ], xs=12, md=4)
    ])

])

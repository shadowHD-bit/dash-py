""" 
Модуль стартовой страницы дэшбода. Молуь не содержит доволнительного функционала, отвечает только за разметку страницы.
"""

import dash_bootstrap_components as dbc
from dash import html
from partials.alert_link_page import build_alert_link_page


layout = html.Div(className="start_content", children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.Img(src='assets/gif/bloom-woman-and-man-doing-web-browser-development.gif',
                     className='start_content__images'),
            html.P('Добро пожаловать в ДЭШ-ПАЙ!',
                   className='start__text_title text_title text-info'),
            html.P('Это веб-приложение предназначена для визуализации исходных маркетинговых данных компании.',
                   className='start__text_subtitle'),
        ])
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            build_alert_link_page('Главная страница',
                                  'Главная страница дэшборда предоставляет общий обзор основных метрик и данных, позволяя пользователям быстро оценить текущее состояние бизнеса и принять информированные решения.', 'main', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Настройки',
                                  'Страница настроек позволяет пользователям настраивать параметры дэшборда, включая выбор отображаемых метрик, цветовую схему, временной диапазон и другие персонализированные настройки.',
                                  'settings', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Страница датасета',
                                  'На этой странице пользователи могут просматривать и анализировать данные из выбранного датасета, включая таблицы, графики и другие визуализации данных.',
                                  'dataset', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('География',
                                  'Страница географии позволяет пользователям визуализировать данные на карте, отображая географическое распределение клиентов, продаж или других ключевых метрик.',
                                  'geography', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Товары',
                                  'Здесь пользователи могут просматривать информацию о продуктах, включая их ассортимент, цены, количество продаж и другие связанные данные.',
                                  'products', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Возвраты',
                                  'Страница возвратов предоставляет информацию о возвращенных товарах, включая количество возвратов, причины возврата и другие связанные метрики.',
                                  '/refunds', 'info')
        ], xs=12, md=4),
        dbc.Col(children=[
            build_alert_link_page('Клиенты',
                                  'На этой странице пользователи могут анализировать данные о клиентах, включая демографическую информацию, их покупательское поведение, лояльность и другие связанные метрики.',
                                  '/clients', 'info')
        ], xs=12, md=4)
    ])
])

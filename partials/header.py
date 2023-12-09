from dash import html
import dash_bootstrap_components as dbc
from utils.const import CURRENT_DATE


def build_header():
    '''
    Функция создания шапки дэша
    '''
    header = dbc.Row(className="header", children=[
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Breadcrumb(style={'textDecoration': 'none'},
                    items=[
                    {"label": "Информационная панель",
                     "href": "/", "external_link": True},
                ]),
            ]),
            dbc.Col(children=[
                html.P(CURRENT_DATE, className='text')
            ])
        ])
    ]),

    return header

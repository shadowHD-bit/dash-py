from dash import dash, html, dcc
import dash_bootstrap_components as dbc
import dash

from utils.const import CURRENT_DATE


def build_header():
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

from dash import dash, html, dcc
import dash_bootstrap_components as dbc
import dash

def build_header():
    header = dbc.Row(className="header", children=[
        dbc.Breadcrumb(style={'textDecoration': 'none'},
                       items=[
            {"label": "Информационная панель",
             "href": "/", "external_link": True},
        ]),
    ]),

    return header

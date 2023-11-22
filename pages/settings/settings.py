import dash
from dash import html
from dash_bootstrap_templates import ThemeSwitchAIO
from utils.UI.theme import URL_THEME_DARK, URL_THEME_LIGHT
import dash_bootstrap_components as dbc

theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[URL_THEME_LIGHT, URL_THEME_DARK],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

dash.register_page(__name__, title="Информационная панель | Настройки",
                   name="Настройки", path='/settings', order=2)

layout = html.Div(style={'margin': '10px'}, children=[
    dbc.Row(className="mb-3", children=[
        html.H3("Настройки информационной панели")
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color="light", outline=True, children=[
                dbc.Row(className='p-3', children=[
                    dbc.Row(children=[
                        html.P("Изменение темы")
                    ]),
                    dbc.Row(children=[
                        theme_toggle
                    ]),
                ]),
            ])
        ], xs=12, md=6, lg=4),
        dbc.Col(children=[

        ])
    ])
])

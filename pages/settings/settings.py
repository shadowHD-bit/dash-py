from datetime import datetime
import dash
from dash import html, dcc, callback, Output, Input
from dash_bootstrap_templates import ThemeSwitchAIO
from utils.UI.theme import URL_THEME_DARK, URL_THEME_LIGHT
import dash_bootstrap_components as dbc
from datetime import date

from utils.const import CURRENT_DATE

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
            dbc.Card(color="light", outline=True, children=[
                dbc.Row(className='p-3', children=[
                    dbc.Row(children=[
                        html.P("Изменение даты")
                    ]),
                    dbc.Row(children=[
                        dcc.DatePickerSingle(
                            id='my-date-picker-single',
                            min_date_allowed=date(2012, 1, 1),
                            max_date_allowed=date(2015, 12, 29),
                            date=datetime.strptime(CURRENT_DATE, '%Y-%m-%d').date()
                        ),
                        html.Div(id='output-container-date-picker-single')
                    ]),
                ]),
            ])
        ], xs=12, md=6, lg=4),
    ])
])


# @callback(
#     Output('output-container-date-picker-single', 'children'),
#     Input('my-date-picker-single', 'date'))
# def update_output(date_value):
#     CURRENT_DATE = str(date_value)
#     return ""
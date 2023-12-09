import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from routes import register_pages
from utils.UI.theme import URL_THEME_DARK, URL_THEME_LIGHT, NAME_THEME_DARK, NAME_THEME_LIGHT
from utils.const import CURRENT_DATE, START_DATE
from dash_bootstrap_templates import ThemeSwitchAIO

app = Dash(__name__, use_pages=True,  external_stylesheets=[
           dbc.icons.BOOTSTRAP, dbc.themes.BOOTSTRAP])  # , suppress_callback_exceptions=True

register_pages()

app.layout = dbc.Container(id='main_container', children=[
    # Инициализация локального хранилища
    dcc.Store(id="current-time-store", data="",  storage_type='local'),
    dcc.Store(id="current-theme-store", data="",  storage_type='local'),
    
    # Главная разметка
    html.Div(id='out_theme', children=[]),
    dbc.Row(className='p-0 m-0', children=[
        dbc.Col(className='p-0 m-0', children=[
            dbc.Row(className='p-0 m-0 sidebar', children=[
                dbc.Col(width=2, className="sidebar_container", children=[
                    dbc.Card(outline=True,color='light', className=f'content__card shadow', children=[
                        dbc.Row(className='sidebar__logo pt-4 pb-4 d-flex row shadow-sm m-0', children=[
                            html.P(id='text', className='m-0 p-0 text-info', children=[
                                html.I(className="bi bi-bar-chart-line-fill mr-1"),
                                 "  ДЭШ-ПАЙ",
                            ]),
                        ]),
                        dbc.Row(className="sidebar__links p-0 m-0", children=[
                            dcc.Link(html.Div(f"{page['name']}"), href=page["relative_path"], className='sidebar__btn_links text-body m-0 pt-3 pb-3') for page in dash.page_registry.values() if page['name'] != 'Index' and page['name'] != 'Страница не найдена'
                        ]),
                    ]),
                ]),
                dbc.Col(className='right_part__container', children=[
                    dbc.Card(outline=True, color='light', className='dbc content__card shadow', children=[
                        dbc.Row(className="header m-0 shadow-sm", children=[
                            dbc.Row(children=[
                                dbc.Col(children=[
                                    dbc.Breadcrumb(style={'textDecoration': 'none'},
                                                   items=[{"label": "Информационная панель", "href": "/", "external_link": True},
                                    ]),
                                ]),
                                dbc.Col(children=[
                                    dbc.Row(children=[
                                        dbc.Col(id='date_container', className='date_container__header', children=[
                                        ], xs=12),
                                        dbc.Col(className='theme_container__header', children=[
                                            ThemeSwitchAIO(
                                                aio_id="theme",
                                                themes=[URL_THEME_LIGHT, URL_THEME_DARK],
                                                icons={"left": "fa fa-moon", "right": "fa fa-sun"},
                                                switch_props={'value': True}
                                            )
                                        ], xs=12)
                                    ])
                                ]),
                            ])
                        ]),
                        dbc.Row(className='p-0 m-0 main_container_content', children=[
                            dash.page_container
                        ])
                    ])
                ], width=10),
            ]),
        ])
    ])
], fluid=True, className='dbc', style={'margin': 0, 'padding': '20px 0px', 'height': '100%'})

# Вывод текущей даты из стора
@app.callback(
    Output('date_container', 'children'),
    Input('current-time-store', 'modified_timestamp'),
    State('current-time-store', 'data')
)
def cb_output_current_data(ts, value):
    if value:
        return html.P(f'Текщая дата: {value}', className='text', id='curr_date__header')
    else:
        return html.P(f'Текщая дата: {START_DATE}', className='text', id='curr_date__header')

# Обновление темы дэша
@app.callback(
    Output('current-theme-store', 'data'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value'),
    State('current-theme-store', 'data')
)
def cb_update_current_theme(value, state):
    if value:
        return str(NAME_THEME_LIGHT)
    else:
        return str(NAME_THEME_DARK)

# Обновление темы в локальном хранилище
@app.callback(
    Output(ThemeSwitchAIO.ids.switch('theme'), 'value'),
    Input('current-theme-store', 'modified_timestamp'),
    State('current-theme-store', 'data')
)
def cb_update_theme_local(ts, value):
    if value == 'FLATLY':
        return True,
    else:
        return False

# Флаг локального использования css файла
app.css.config.serve_locally = True

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

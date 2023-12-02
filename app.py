import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from utils.UI.theme import URL_THEME_LIGHT
from utils.const import CURRENT_DATE, START_DATE


app = Dash(__name__, use_pages=True,  external_stylesheets=[
           dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, URL_THEME_LIGHT])  # , suppress_callback_exceptions=True

app.layout = dbc.Container(children=[
    # Initial store date
    dcc.Store(id="current-time-store", data="",  storage_type='local'),
    dbc.Row(className='p-0 m-0', children=[
        dbc.Col(
            dbc.Card(outline=True, color='dark', className='dbc content__card', children=[
                dbc.Row(className='p-0 m-0 sidebar', children=[
                    dbc.Col(width=2, className="sidebar_container", children=[
                        dbc.Row(className='sidebar__logo', children=[
                            html.Div(f"ДЭШ-ПАЙ")
                        ]),
                        dbc.Row(className="sidebar__links", children=[
                            dcc.Link(html.Div(f"{page['name']}"), href=page["relative_path"], className='sidebar__btn_links text-body') for page in dash.page_registry.values() if page['name'] != 'Index' and page['name'] != 'Страница не найдена'
                        ]),
                    ]),
                    dbc.Col([
                        dbc.Row(className="header", children=[
                            dbc.Row(children=[
                                dbc.Col(children=[
                                    dbc.Breadcrumb(style={'textDecoration': 'none'},
                                        items=[
                                        {"label": "Информационная панель",
                                        "href": "/", "external_link": True},
                                    ]),
                                ]),
                                dbc.Col(id='date_container',className='date_container__header', children=[
                                ])
                            ])
                        ]),
                        dbc.Row(className='p-0 m-0 main_container_content', children=[
                            dash.page_container
                        ])
                    ], width=10),
                ])
            ]),
        )
    ])
], fluid=True, className='dbc', style={'margin': 0, 'padding': '20px 0px', 'height': '100%'})


@app.callback(
    Output('date_container', 'children'),
    Input('current-time-store', 'modified_timestamp'),
    State('current-time-store', 'data')
)
def update_output_date(ts, value):
    if value:
        return html.P(value, className='text', id='curr_date__header')
    else:
        return html.P(START_DATE, className='text', id='curr_date__header')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

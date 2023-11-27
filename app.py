import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from utils.UI.theme import URL_THEME_LIGHT


app = Dash(__name__, use_pages=True,  external_stylesheets=[
           dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, URL_THEME_LIGHT])  # , suppress_callback_exceptions=True

app.layout = dbc.Container([
    dbc.Row(className='p-0 m-0', children=[
        dbc.Col(
            dbc.Card(outline=True, color='dark', className='dbc', style={'margin': '0px 30px', 'padding': '0', 'borderRadius': 15, 'minHeight': '96vh'}, children=[
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
                            dbc.Breadcrumb(style={'textDecoration': 'none'},
                                items=[
                                    {"label": "Информационная панель",
                                        "href": "/", "external_link": True},
                            ]),
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


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

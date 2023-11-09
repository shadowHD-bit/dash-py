import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from utils.UI.colors import colors


app = Dash(__name__, use_pages=True,  external_stylesheets=[
           dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div(
        dbc.Row(style={'margin': '0px 30px', 'backgroundColor': 'white', 'borderRadius': 15, 'minHeight': '96vh'}, children=[
                dbc.Col(width=2, className="sidebar", children=[
                    dbc.Row(className='sidebar__logo', children=[
                        html.Div(f"ДЭШ-ПАЙ")
                    ]),
                    dbc.Row(className="sidebar__links", children=[
                        dcc.Link(html.Div(f"{page['name']}"), href=page["relative_path"], className='sidebar__btn_links') for page in dash.page_registry.values() if page['name'] != 'Index'
                    ]),
                    # dbc.Row(className="sidebar__links", children=[
                    #     dcc.Link(html.Div(f"{dash.page_registry.values()[0]['name']}"), href=dash.page_registry.values()[0]["relative_path"], className='sidebar__btn_links'),
                    #     dcc.Link(html.Div(f"{dash.page_registry.values()['name']['name']}"), href=dash.page_registry.values()['name']["relative_path"], className='sidebar__btn_links'),
                    #     dcc.Link(html.Div(f"{dash.page_registry.values()['name']['name']}"), href=dash.page_registry.values()['name']["relative_path"], className='sidebar__btn_links'),
                    #     dcc.Link(html.Div(f"{dash.page_registry.values()['name']['name']}"), href=dash.page_registry.values()['name']["relative_path"], className='sidebar__btn_links')
                    # ])
                ]),
                dbc.Col([
                    dbc.Row(className="header", children=[
                        dbc.Breadcrumb(style={'textDecoration': 'none'},
                            items=[
                                {"label": "Информационная панель",
                                    "href": "/", "external_link": True},
                            ],
                        )
                    ]),
                    dbc.Row([
                        dash.page_container
                    ])
                ], width=10),
                ]
                ),
    )
], fluid=True, style={'backgroundColor': colors['Non_Photo_blue'], 'margin': 0, 'padding': '20px 0px', 'height': '100%'})

if __name__ == '__main__':
    app.run(debug=True)

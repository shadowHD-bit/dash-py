import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


def build_sidebar():
    '''
    Функция создания боковой панели дэша
    '''
    sidebar = dbc.Col(width=2, className="sidebar_container", children=[
        dbc.Row(className='sidebar__logo', children=[
            html.Div(f"ДЭШ-ПАЙ")
        ]),
        dbc.Row(className="sidebar__links", children=[
            dcc.Link(html.Div(f"{page['name']}"), href=page["relative_path"], className='sidebar__btn_links text-body') for page in dash.page_registry.values() if page['name'] != 'Index' and page['name'] != 'Страница не найдена'
        ]),
    ]),

    return sidebar

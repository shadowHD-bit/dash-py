import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from data import MAIN_DF
from pages.products.graphs.category_top_hist import build_bar_top_category
from pages.products.graphs.product_top_hist import build_bar_top_product
from pages.products.graphs.subcategory_top_hist import build_bar_top_subcategory
from pages.products.graphs.treemap_product import build_treemap_product


dash.register_page(__name__, name="Товары",
                   title="Информационная панель | Товары", path='/products')
df = MAIN_DF

layout = html.Div([
    dbc.Row(className="mt-2 mb-3", children=[
        html.H5('Общая информация')
    ]
    ),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ категорий"),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost'],
                            'Sales',
                            id='get_category_top'),
                    ], xs=12)
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="hist_top_category", children=[
                        ])
                    )
                ])
            ])
        ], xs=12, md=6),
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ-10 под-категорий"),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost'],
                            'Sales',
                            id='get_subcategory_top'),
                    ], xs=12)
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="hist_top_subcategory", children=[
                        ])
                    )
                ])
            ])
        ], xs=12, md=6),
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ-10 товаров"),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost'],
                            'Sales',
                            id='get_product_top'),
                    ], xs=12)
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="hist_top_product", children=[
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Иерархическая карта товаров"),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ['Category', 'Sub-Category', 'Product Name'],
                            ['Category', 'Sub-Category'],
                            id='get_params_treemap',
                            multi=True),
                    ], xs=12, md=6)
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="container_treemap", children=[
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
    dbc.Row(children=[
        html.H5('Статистика по товару')
    ]),
    dbc.Row(children=[

    ]),
])


@callback(
    Output("container_treemap", "children"),
    [Input("get_params_treemap", "value")]
)
def build_treemap_callback(value):
    treemap_graph = build_treemap_product(df, value)
    treemap = dcc.Graph(
        id='treemap-graph',
        figure=treemap_graph
    )
    return treemap

















@callback(
    Output("hist_top_category", "children"),
    [Input("get_category_top", "value")]
)
def build_category_top_hist_callback(value):
    graph = build_bar_top_category(df, 'Category', value)
    graph_container = dcc.Graph(
        id='top_category_bar',
        figure=graph
    )
    return graph_container


@callback(
    Output("hist_top_subcategory", "children"),
    [Input("get_subcategory_top", "value")]
)
def build_subcategory_top_hist_callback(value):
    graph = build_bar_top_subcategory(df, 'Sub-Category', value)
    graph_container = dcc.Graph(
        id='top_subcategory_bar',
        figure=graph
    )
    return graph_container


@callback(
    Output("hist_top_product", "children"),
    [Input("get_product_top", "value")]
)
def build_product_top_hist_callback(value):
    graph = build_bar_top_product(df, 'Product Name', value)
    graph_container = dcc.Graph(
        id='top_product_bar',
        figure=graph
    )
    return graph_container


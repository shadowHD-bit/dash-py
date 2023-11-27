from datetime import date
import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


from data import MAIN_DF
from graphs.products.category_top_hist import build_bar_top_category
from graphs.products.product_top_hist import build_bar_top_product
from graphs.products.subcategory_top_hist import build_bar_top_subcategory
from graphs.products.treemap_product import build_treemap_product


dash.register_page(__name__, name="Товары",
                   title="Информационная панель | Товары", path='/products')
df = MAIN_DF

layout = html.Div([
    dbc.Row(className="mt-2 mb-3", children=[
        html.P('Общая информация', className='title_content__block')
    ]
    ),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ категорий", className='subtitle_content__block'),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Sales', 'Quantity', 'Discount',
                                    'Profit', 'Shipping Cost'],
                                'Sales',
                                id='get_category_top'),
                        ], xs=6),
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_top_category',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=6)
                    ]),

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
            dbc.Card(outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ-10 под-категорий",
                           className='subtitle_content__block'),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Sales', 'Quantity', 'Discount',
                                    'Profit', 'Shipping Cost'],
                                'Sales',
                                id='get_subcategory_top'),
                        ], xs=6),
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_top_subcategory',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=6)
                    ]),
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
            dbc.Card(outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Топ-10 товаров", className='subtitle_content__block'),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ['Sales', 'Quantity', 'Discount',
                                'Profit', 'Shipping Cost'],
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
            dbc.Card(outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Иерархическая карта товаров",
                           className='subtitle_content__block'),
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
        html.P('Статистика по товару', className='title_content__block')
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
        figure=treemap_graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
    )
    return treemap


@callback(
    Output("hist_top_category", "children"),
    [Input("get_category_top", "value"),
     Input('picker_date_top_category', 'start_date'),
     Input('picker_date_top_category', 'end_date')]
)
def build_category_top_hist_callback(value, start_date, end_date):
    graph = build_bar_top_category(df, 'Category', value, start_date, end_date)
    graph_container = dcc.Graph(
        id='top_category_bar',
        figure=graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
    )
    return graph_container


@callback(
    Output("hist_top_subcategory", "children"),
    [Input("get_subcategory_top", "value"),
     Input('picker_date_top_subcategory', 'start_date'),
     Input('picker_date_top_subcategory', 'end_date')]
)
def build_subcategory_top_hist_callback(value, start_date, end_date):
    graph = build_bar_top_subcategory(df, 'Sub-Category', value, start_date, end_date)
    graph_container = dcc.Graph(
        id='top_subcategory_bar',
        figure=graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
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
        figure=graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
    )
    return graph_container

from datetime import date
import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px


from data import MAIN_DF
from graphs.products.category_top_hist import build_bar_top_category
from graphs.products.product_top_hist import build_bar_top_product
from graphs.products.subcategory_top_hist import build_bar_top_subcategory
from graphs.products.treemap_product import build_treemap_product
from partials.statistic_card import build_statistic_card


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
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Sales', 'Quantity', 'Discount',
                                    'Profit', 'Shipping Cost'],
                                'Sales',
                                id='get_product_top'),
                        ], xs=9),
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_top_product',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=3)
                    ]),
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
        html.P('Статистика по товару, категории и подкатегории',
               className='title_content__block')
    ]),
    dbc.Row(children=[
        dbc.Accordion(children=[
            dbc.AccordionItem(
                [
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_product_stat',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=3),
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Technology', 'Furniture', 'Office Supplies'],
                                id="candidate_product_category",
                                placeholder="Выберите категорию",
                                value="Technology"
                            )
                        ], xs=3),
                        dbc.Col(id="subcat_product_container", children=[
                        ], xs=3),
                        dbc.Col(id="product_container_dropdown", children=[
                        ], xs=3),
                    ]),
                    dbc.Row(id='product_containet__content', children=[

                    ])
                ],
                title="Статистика по товару",
            ),
        ], start_collapsed=True),
        dbc.Accordion(children=[
            dbc.AccordionItem(
                [
                    dbc.Row(className='mb-3', children=[
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_cat',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=3),
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Technology', 'Furniture', 'Office Supplies'],
                                id="stat_drop_category",
                                placeholder="Выберите категорию",
                            )
                        ], xs=3),
                    ]),
                    dbc.Row(
                        dbc.Col(id="cat_stat_container", children=[
                        ], xs=12)
                    )
                ],
                title="Статистика по категории",
            ),
        ], start_collapsed=True),
        dbc.Accordion(children=[
            dbc.AccordionItem(
                [
                    dbc.Row(className='mb-3', children=[
                        dbc.Col(children=[
                            dcc.DatePickerRange(
                                id='picker_date_sub',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 30),
                                start_date=date(2012, 1, 1),
                                end_date=date(2015, 12, 30),
                                display_format='D/M/Y'
                            ),
                        ], xs=3),
                        dbc.Col(children=[
                            dcc.Dropdown(
                                ['Technology', 'Furniture', 'Office Supplies'],
                                id="candidate_category",
                                placeholder="Выберите категорию",
                                value="Technology"
                            )
                        ], xs=3),
                        dbc.Col(id="subcat_container", children=[
                        ], xs=3),
                    ]),
                    dbc.Row(
                        dbc.Col(id="subcat_stat_container", children=[
                        ], xs=12)
                    )
                ],
                title="Статистика по подкатегории",
            ),
        ], start_collapsed=True),
    ]),
])


@callback(
    Output("cat_stat_container", "children"),
    [Input("stat_drop_category", "value"),
     Input('picker_date_cat', 'start_date'),
     Input('picker_date_cat', 'end_date')]
)
def display_category_callback(n, start_date, end_date):
    if n:
        cat_df = df.loc[df['Category'] == n]
        cat_df_date = cat_df[(cat_df['Order Date'] > str(start_date)) & (
            cat_df['Order Date'] < str(end_date))]
        sum_profit_cat = cat_df_date['Profit'].values.sum()
        sum_sales_cat = cat_df_date['Sales'].values.sum()
        sum_count_cat = cat_df_date['Quantity'].values.sum()

        df_timeline_sub = cat_df_date.sort_values(by="Order Date")

        fig_value_subcategories_pie = px.pie(
        cat_df_date, values='Sales', names='Sub-Category')
        fig_value_subcategories_pie.update_traces(
            textposition='inside', textinfo='percent+label')
        fig_value_subcategories_pie.update_layout(margin=dict(t=0, l=0, r=0, b=0))

        fig_timeline_sub_sales = px.line(
            df_timeline_sub, x='Order Date', y="Sales")
        fig_timeline_sub_sales.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_sub_profit = px.line(
            df_timeline_sub, x='Order Date', y="Profit")
        fig_timeline_sub_profit.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_value_subcategories_pie_count = px.pie(
        cat_df_date, values='Quantity', names='Sub-Category')
        fig_value_subcategories_pie_count.update_traces(
            textposition='inside', textinfo='percent+label')
        fig_value_subcategories_pie_count.update_layout(margin=dict(t=0, l=0, r=0, b=0))
 
        fig_timeline_sub_count = px.line(
            df_timeline_sub, x='Order Date', y="Quantity")
        fig_timeline_sub_count.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        children = html.Div(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    build_statistic_card('bi bi-cash-stack',
                        'Прибыль', round(sum_profit_cat, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-bank', 'Продажи', round(sum_sales_cat, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-clipboard-data-fill', 'Объем', sum_count_cat, 'шт.')
                ], xs=4),
            ]),
            dbc.Row(children=[
                    html.P('Продажи',
                           className='subtitle_content__block')
            ]),
            dbc.Row(className='mt-3', children=[
                dbc.Col(children=[
                    dcc.Graph(
                        figure=fig_value_subcategories_pie
                    )
                ], xs=6),
                dbc.Col(children=[
                    dcc.Graph(
                        figure=fig_timeline_sub_sales
                    )
                ], xs=6),
            ]),
            dbc.Row(children=[
                    html.P('Прибыль',
                           className='subtitle_content__block')
            ]),
            dbc.Row(className='mt-3', children=[
                dbc.Col(children=[
                    dcc.Graph(
                        figure=fig_timeline_sub_profit
                    )
                ], xs=12),
            ]),
            dbc.Row(children=[
                    html.P('Объем',
                           className='subtitle_content__block')
            ]),
            dbc.Row(className='mt-3', children=[
                dbc.Col(children=[
                    dcc.Graph(
                        figure=fig_value_subcategories_pie_count
                    )
                ], xs=6),
                dbc.Col(children=[
                    dcc.Graph(
                        figure=fig_timeline_sub_count
                    )
                ], xs=6),
            ]),
        ])

        return children
    else:
        return ""


@callback(
    Output("subcat_container", "children"),
    Input("candidate_category", "value"),
)
def display_subcategory_dropown_callback(n):
    sub_df = df.loc[df['Category'] == n]
    sub_list = sub_df['Sub-Category'].unique()
    dropdown = dcc.Dropdown(
        sub_list,
        id="sub_dropdown",
        placeholder="Выберите подкатегорию"
    ),
    return dropdown


@callback(
    Output("subcat_stat_container", "children"),
    [Input("sub_dropdown", "value"),
     Input('picker_date_sub', 'start_date'),
     Input('picker_date_sub', 'end_date')]
)
def display_subcategory_callback(n, start_date, end_date):

    if n:
        sub_df = df.loc[df['Sub-Category'] == n]
        sub_df_date = sub_df[(sub_df['Order Date'] > str(start_date)) & (
            sub_df['Order Date'] < str(end_date))]
        sum_profit_sub = sub_df_date['Profit'].values.sum()
        sum_sales_sub = sub_df_date['Sales'].values.sum()
        sum_count_sub = sub_df_date['Quantity'].values.sum()

        df_timeline_sub = sub_df_date.sort_values(by="Order Date")

        fig_timeline_sub_sales = px.line(
            df_timeline_sub, x='Order Date', y="Sales")
        fig_timeline_sub_sales.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_sub_profit = px.line(
            df_timeline_sub, x='Order Date', y="Profit")
        fig_timeline_sub_profit.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_sub_count = px.line(
            df_timeline_sub, x='Order Date', y="Quantity")
        fig_timeline_sub_count.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_value_subcategories_bar = px.bar(
            sub_df_date, x='Sales', y='Product Name')
        fig_value_subcategories_bar.update_layout(
            margin=dict(t=0, l=0, r=0, b=0))

        fig_value_subcategories_bar_profit = px.bar(
            sub_df_date, x='Profit', y='Product Name')
        fig_value_subcategories_bar_profit.update_layout(
            margin=dict(t=0, l=0, r=0, b=0))

        fig_value_subcategories_bar_count = px.bar(
            sub_df_date, x='Quantity', y='Product Name')
        fig_value_subcategories_bar_count.update_layout(
            margin=dict(t=0, l=0, r=0, b=0))

        children = html.Div(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    build_statistic_card('bi bi-cash-stack',
                        'Прибыль', round(sum_profit_sub, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-bank', 'Продажи', round(sum_sales_sub, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-clipboard-data-fill', 'Объем', sum_count_sub, 'шт.')
                ], xs=4),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_sub_profit)
                ], xs=4),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_sub_sales)
                ], xs=4),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_sub_count)
                ], xs=4),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    html.P('Продажи',
                           className='subtitle_content__block')
                ], xs=12),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_value_subcategories_bar)
                ], xs=12),
                dbc.Col(children=[
                    html.P('Прибыль',
                           className='subtitle_content__block')
                ], xs=12),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_value_subcategories_bar_profit)
                ], xs=12),
                dbc.Col(children=[
                    html.P('Количество',
                           className='subtitle_content__block')
                ], xs=12),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_value_subcategories_bar_count)
                ], xs=12),
            ])
        ])
        return children
    else:
        return ""


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
    graph = build_bar_top_subcategory(
        df, 'Sub-Category', value, start_date, end_date)
    graph_container = dcc.Graph(
        id='top_subcategory_bar',
        figure=graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
    )
    return graph_container


@callback(
    Output("hist_top_product", "children"),
    [Input("get_product_top", "value"),
     Input('picker_date_top_product', 'start_date'),
     Input('picker_date_top_product', 'end_date')]
)
def build_product_top_hist_callback(value, start_date, end_date):
    graph = build_bar_top_product(
        df, 'Product Name', value, start_date, end_date)
    graph_container = dcc.Graph(
        id='top_product_bar',
        figure=graph,
        style={'backgroundColor': 'rgba(0,0,0,0)'}
    )
    return graph_container


@callback(
    Output("subcat_product_container", "children"),
    Input("candidate_product_category", "value"),
)
def display_subcategory_dropown_callback(n):
    sub_df = df.loc[df['Category'] == n]
    sub_list = sub_df['Sub-Category'].unique()
    dropdown = dcc.Dropdown(
        sub_list,
        id="sub_product_dropdown",
        placeholder="Выберите подкатегорию"
    ),
    return dropdown


@callback(
    Output("product_container_dropdown", "children"),
    Input("sub_product_dropdown", "value"),
)
def display_subcategory_dropown_callback(n):
    sub_df = df.loc[df['Sub-Category'] == n]
    sub_list = sub_df['Product Name'].unique()
    dropdown = dcc.Dropdown(
        sub_list,
        id="product_dropdown",
        placeholder="Выберите товар"
    ),
    return dropdown


@callback(
    Output("product_containet__content", "children"),
    [Input("product_dropdown", "value"),
    Input('picker_date_product_stat', 'start_date'),
    Input('picker_date_product_stat', 'end_date')]
)
def display_subcategory_dropown_callback(n, start_date, end_date):
    if n:
        prod_df = df.loc[df['Product Name'] == n]
        prod_df_date = prod_df[(prod_df['Order Date'] > str(start_date)) & (
            prod_df['Order Date'] < str(end_date))]
        sum_profit_prod = prod_df_date['Profit'].values.sum()
        sum_sales_prod = prod_df_date['Sales'].values.sum()
        sum_count_prod = prod_df_date['Quantity'].values.sum()

        df_timeline_prod = prod_df_date.sort_values(by="Order Date")


        fig_timeline_prod_sales = px.line(
            df_timeline_prod, x='Order Date', y="Sales")
        fig_timeline_prod_sales.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_prod_profit = px.line(
            df_timeline_prod, x='Order Date', y="Profit")
        fig_timeline_prod_profit.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_prod_count = px.line(
            df_timeline_prod, x='Order Date', y="Quantity")
        fig_timeline_prod_count.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})


        children = html.Div(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    build_statistic_card('bi bi-cash-stack',
                        'Прибыль', round(sum_profit_prod, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-bank', 'Продажи', round(sum_sales_prod, 2), '$')
                ], xs=4),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-clipboard-data-fill', 'Объем', sum_count_prod, 'шт.')
                ], xs=4),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_prod_profit)
                ], xs=4),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_prod_sales)
                ], xs=4),
                dbc.Col(children=[
                    dcc.Graph(id='graph',
                              figure=fig_timeline_prod_count)
                ], xs=4),
            ]),
        ])
        return children
    else:
        return ''
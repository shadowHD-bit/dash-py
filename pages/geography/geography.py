'''
Модуль страницы статистики по географии продаж. Модуль содержит разметку и внутренние обратные вызовы. Дополнительные функции отсуттсвуют.
'''

import plotly.express as px
import dash_bootstrap_components as dbc
from data import MAIN_DF
from dash import html, dcc, callback, Output, Input
from graphs.geography.geography_map import build_geography_map
from partials.loader_params import build_loader_params
from partials.statistic_card import build_statistic_card


df = MAIN_DF
region_list = df["Region"].unique()
country_list = df["Country"].unique()
state_list = df["State"].unique()
city_list = df["City"].unique()


layout = dbc.Container(fluid=True, children=[
    dbc.Row(className="mt-3 mb-1", children=[
        html.P('География продаж', className='title_content__block text-info')
    ]),
    dbc.Row(className="mt-1 mb-3", children=[
        html.P('Общая информация', className='subtitle_content__block text-info')
    ]),
    dbc.Row(className="mt-2 mb-3", children=[
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-globe-americas', 'Кол-во континентов', len(region_list), 'шт.')
        ], lg=3, md=6, xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-airplane-engines-fill', 'Кол-во стран', len(country_list), 'шт.')
        ], lg=3, md=6, xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-house', 'Кол-во штатов', len(state_list), 'шт.')
        ], lg=3, md=6, xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-building', 'Кол-во городов', len(city_list), 'шт.')
        ], lg=3, md=6, xs=12),
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(outline=True, color='light', className="p-0 shadow-sm m-0", children=[
                dbc.CardHeader(children=[
                    html.P("Географическая карта стран клиентов",
                           className='subtitle_content__block text-info'),
                    dbc.Col(children=[
                        dcc.Dropdown(
                            ["Sales", "Profit", "Quantity"],
                            id="candidate",
                            placeholder="Выберите параметр",
                            value="Sales"
                        )],
                    xs=12, md=3),
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="map_container", children=[
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
    dbc.Row(className="mt-2 mb-3", children=[
        html.P('Статистика продаж по провинциям',
            className='subtitle_content__block mt-4 text-info')
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(outline=True, color='light', className="p-0 shadow-sm m-0 mb-2", children=[
                dbc.CardHeader(children=[
                    dbc.Row(children=[
                        dbc.Col(id="region_container", children=[
                            dcc.Dropdown(
                                region_list,
                                id="region_dropdown",
                                placeholder="Выберите регион"
                            ),
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="country_container", children=[
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="state_container", children=[
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="city_container", children=[
                        ], xs=12, md=6, lg=3),
                    ])
                ]),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="city_graphs", children=[
                            dbc.Row(id='main_graph_city', children=[
                                build_loader_params()
                            ]),
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
])


# Отображение графика карты
@callback(
    Output("map_container", "children"),
    Input("candidate", "value"))
def cb_display_choropleth(candidate):
    if candidate:
        fig = build_geography_map(candidate)
        graph = dcc.Graph(id='map_graph', figure=fig)
        return graph
    else:
        loading = build_loader_params()
        return loading


# Отображение выпадающего спискака выбора страны
@callback(
    Output("country_container", "children"),
    Input("region_dropdown", "value"),
)
def cb_display_country_dropown(n):
    if n:
        country_df = df.loc[df['Region'] == n]
        country_list = country_df['Country'].unique()
        dropdown = dcc.Dropdown(
            country_list,
            id="country_dropdown",
            placeholder="Выберите страну"
        ),
        return dropdown
    else:
        return ""


# Отображение выпадающего спискака выбора штата
@callback(
    Output("state_container", "children"),
    Input("country_dropdown", "value"),
)
def cb_display_state_dropown(n):
    if n:
        state_df = df.loc[df['Country'] == n]
        state_list = state_df['State'].unique()
        dropdown = dcc.Dropdown(
            state_list,
            id="state_dropdown",
            placeholder="Выберите штат"
        ),
        return dropdown
    else:
        return ""


# Отображение выпадающего спискака выбора города
@callback(
    Output("city_container", "children"),
    Input("state_dropdown", "value"),
)
def cb_display_city_dropown(n):
    if n:
        city_df = df.loc[df['State'] == n]
        city_list = city_df['City'].unique()
        dropdown = dcc.Dropdown(
            city_list,
            id="city_dropdown",
            placeholder="Выберите город"
        ),
        return dropdown
    else:
        return ""


# Отображение статистических графиков по выбранному городу
@callback(
    Output("main_graph_city", "children"),
    [Input("city_dropdown", "value")]
)
def display_city_graph(city):
    if (city != None):
        df_timelinef = df.loc[df['City'] == city]
        df_timeline = df_timelinef.sort_values(by="Order Date")

        fig_timeline_sales = px.line(df_timeline, x='Order Date', y="Sales")
        fig_timeline_sales.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_profit = px.line(df_timeline, x='Order Date', y="Profit")
        fig_timeline_profit.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        fig_timeline_count = px.line(df_timeline, x='Order Date', y="Quantity")
        fig_timeline_count.update_layout(
            margin={"r": 15, "t": 15, "l": 15, "b": 15})

        sum_sales = df_timeline['Sales'].values.sum()
        sum_count = df_timeline['Quantity'].values.sum()
        sum_profit = df_timeline['Profit'].values.sum()

        fig_bar_sales = px.bar(df_timelinef, y="Category",
                               x="Sales", color="Sub-Category", barmode="group")
        fig_bar_profit = px.bar(
            df_timelinef, y="Category", x="Profit", color="Sub-Category", barmode="group")
        fig_bar_count = px.bar(df_timelinef, y="Category",
                               x="Quantity", color="Sub-Category", barmode="group")

        children = dbc.Row(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-cash-stack', 'Прибыль', round(sum_profit, 2), '$')
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-bank', 'Продажи', round(sum_sales, 2), '$')
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    build_statistic_card(
                        'bi bi-clipboard-data-fill', 'Объем', sum_count, 'шт.')
                ], lg=4, md=6, xs=12),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_timeline_profit)
                        ])
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_timeline_sales)
                        ])
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_timeline_count)
                        ])
                    ])
                ], lg=4, md=6, xs=12),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_bar_profit)
                        ])
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_bar_sales)
                        ])
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="light", outline=True, className='main_card shadow-sm mt-2', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dcc.Graph(id='graph_city',
                                      figure=fig_bar_count)
                        ])
                    ])
                ], lg=4, md=6, xs=12),]),
        ])
        return children
    else:
        children = build_loader_params()
        return children

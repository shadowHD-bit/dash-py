import dash
from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="География", path='/geography', order=3)

df = pd.read_excel('data\data.xlsx')
region_list = df["Region"].unique()


layout = html.Div([
    dbc.Row(className="mt-2 mb-3", children=[
            html.H5('Общая информация')
            ]
            ),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    html.P("Географическая карта стран клиентов"),
                    dbc.RadioItems(
                        id="candidate",
                        className="btn-group",
                        inputClassName="btn-check",
                        labelClassName="btn btn-outline-primary",
                        labelCheckedClassName="active",
                        options=[
                            {"label": "Sales", "value": "Sales"},
                            {"label": "Profit", "value": "Profit"},
                            {"label": "Quantity", "value": "Quantity"},
                        ],
                        value="Sales",
                    ),
                ]
                ),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(children=[
                            dcc.Graph(
                                id='map_graph',
                            )
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
    dbc.Row(className="mt-2 mb-3", children=[
            html.H5('Общая информация')
            ]
            ),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(children=[
                    dbc.Row(children=[
                        dbc.Col(
                            html.P("Статистика по городам"),
                        )
                    ]),
                    dbc.Row(children=[
                        dbc.Col(id="region_container", children=[
                            dcc.Dropdown(
                                region_list,
                                id="region_dropdown",
                                placeholder="Select a Region"
                            ),
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="country_container", children=[
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="state_container", children=[
                        ], xs=12, md=6, lg=3),
                        dbc.Col(id="city_container", children=[
                        ], xs=12, md=6, lg=3),
                    ])
                ]
                ),
                dbc.CardBody(children=[
                    dbc.Row(
                        dbc.Col(id="city_graphs", children=[
                            dbc.Row(id='main_graph_city', children=[

                            ]),
                        ])
                    )
                ])
            ])
        ], xs=12),
    ]),
])


@callback(
    Output("map_graph", "figure"),
    Input("candidate", "value"))
def display_choropleth(candidate):
    total_sales_by_country = df.groupby(
        'Country', as_index=False)[candidate].sum()
    total_sales_by_country_df = pd.DataFrame(total_sales_by_country)
    fig_map = px.choropleth(total_sales_by_country_df, color=total_sales_by_country_df[candidate],
                            locations=total_sales_by_country_df['Country'],
                            locationmode="country names",
                            labels={candidate: candidate}
                            )
    fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig_map


@callback(
    Output("country_container", "children"),
    Input("region_dropdown", "value"),
)
def display_country_dropown(n):
    country_df = df.loc[df['Region'] == n]
    country_list = country_df['Country'].unique()
    dropdown = dcc.Dropdown(
        country_list,
        id="country_dropdown",
        placeholder="Select a Country"
    ),
    return dropdown


@callback(
    Output("state_container", "children"),
    Input("country_dropdown", "value"),
)
def display_state_dropown(n):
    state_df = df.loc[df['Country'] == n]
    state_list = state_df['State'].unique()
    dropdown = dcc.Dropdown(
        state_list,
        id="state_dropdown",
        placeholder="Select a State"
    ),
    return dropdown


@callback(
    Output("city_container", "children"),
    Input("state_dropdown", "value"),
)
def display_city_dropown(n):
    city_df = df.loc[df['State'] == n]
    city_list = city_df['City'].unique()
    dropdown = dcc.Dropdown(
        city_list,
        id="city_dropdown",
        placeholder="Select a City"
    ),
    return dropdown


@callback(
    Output("main_graph_city", "children"),
    [Input("city_dropdown", "value")]
)
def display_city_graph(city):
    if (city != None):
        df_timelinef = df.loc[df['City'] == city]
        df_timeline = df_timelinef.sort_values(by="Order Date")

        fig_timeline_sales = px.line(df_timeline, x='Order Date', y="Sales")
        fig_timeline_sales.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        fig_timeline_profit = px.line(df_timeline, x='Order Date', y="Profit")
        fig_timeline_profit.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        fig_timeline_count = px.line(df_timeline, x='Order Date', y="Quantity")
        fig_timeline_count.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})



        sum_sales = df_timeline['Sales'].values.sum()
        sum_count = df_timeline['Quantity'].values.sum()
        sum_profit = df_timeline['Profit'].values.sum()

        # children = dcc.Graph(id='graph_city', figure=fig_timeline)
        children = dbc.Row(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    dbc.Card(color="info", outline=True, className='main_card', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dbc.Row(children=[
                                dbc.Col(className='main_card__icon_container', children=[
                                    html.H4(
                                                  html.I(
                                                      className="bi bi-cash-stack"),
                                                  className="main_card__icon")
                                ], width=4),
                                dbc.Col(className='main_card__text_container', children=[
                                    html.H6("Прибыль"),
                                    html.H4(
                                        f'{round(sum_profit, 2)} $'),
                                ], width=8),
                            ]),
                        ]
                        )
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="info", outline=True, className='main_card', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dbc.Row(children=[
                                dbc.Col(className='main_card__icon_container', children=[
                                    html.H4(
                                                  html.I(
                                                      className="bi bi-bank"),
                                                  className="main_card__icon")
                                ], width=4),
                                dbc.Col(className='main_card__text_container', children=[
                                    html.H6("Продажи"),
                                    html.H4(
                                        f'{round(sum_sales, 2)} $'),
                                ], width=8),
                            ]),
                        ]
                        )
                    ])
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dbc.Card(color="info", outline=True, className='main_card', children=[
                        dbc.CardBody(className='main_card__body', children=[
                            dbc.Row(children=[
                                dbc.Col(className='main_card__icon_container', children=[
                                    html.H4(
                                                  html.I(
                                                      className="bi bi-clipboard-data-fill"),
                                                  className="main_card__icon")
                                ], width=4),
                                dbc.Col(className='main_card__text_container', children=[
                                    html.H6("Объем"),
                                    html.H4(f'{sum_count} шт.'),
                                ], width=8),
                            ]),
                        ]
                        )
                    ])
                ], lg=4, md=6, xs=12),
            ]),
            dbc.Row(children=[
                dbc.Col(children=[
                    dcc.Graph(id='graph_city', figure=fig_timeline_profit)
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dcc.Graph(id='graph_city', figure=fig_timeline_sales)
                ], lg=4, md=6, xs=12),
                dbc.Col(children=[
                    dcc.Graph(id='graph_city', figure=fig_timeline_count)
                ], lg=4, md=6, xs=12),
            ])
        ])
        return children
    else:
        children = html.Div(className="d-flex justify-content-center aligh-items-center", children=[
            dbc.Row(children=[
                html.Img(src='assets/images/silky.png',
                         className='non_city_data', width=200),
            ]),
            dbc.Row(children=[
                html.P("Укажите город!")
            ])
        ])
        return children

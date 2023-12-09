import dash
from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
from data import MAIN_DF
from graphs.geography.geography_map import build_geography_map
from graphs.products.pie_category_value import build_pie_category_value
from graphs.products.pie_subcategory_value import build_pie_subcategory_value
from graphs.products.treemap_product import build_treemap_product
from partials.statistic_card import build_statistic_card

from partials.statistic_card_diff import build_statistic_card_diff
from utils.const import CURRENT_DATE, DOMAIN, START_DATE

df = MAIN_DF


layout = html.Div(children=[
    dcc.Store(id="current-time-store", storage_type='local'),
    dbc.Container(children=[
        # dbc.Row(id='temp_row', children=[]),
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                dbc.Row(children=[
                    html.P('Основные показатели',
                           className='title_content__block text-info', id='text-title')
                ]
                ),
                dbc.Row(children=[
                    dbc.Col(children=[
                        dbc.Accordion(children=[
                            dbc.AccordionItem(
                                [
                                    dbc.Row(id="all_container_row", children=[])
                                ],
                                title="За все время",
                            ),
                        ], always_open=True),
                    ], xs=12, md=4),
                    dbc.Col(children=[
                        dbc.Accordion(children=[
                            dbc.AccordionItem(
                                [
                                    dbc.Row(id="year_container_row", children=[])
                                ],
                                title="За год",
                            ),
                        ], always_open=True),
                    ], xs=12, md=4),
                    dbc.Col(children=[
                        dbc.Accordion(children=[
                            dbc.AccordionItem(
                                [
                                    dbc.Row(id="month_container_row", children=[])
                                ],
                                title="За месяц",
                            ),
                        ], always_open=True),
                    ], xs=12, md=4),
                    dbc.Row(children=[
                        html.P('Категории, подкатегории и товары',
                               className='title_content__block text-info', id='text-title')
                    ]
                    ),
                    dbc.Row(justify="around", children=[
                        dbc.Col(children=[
                            dbc.Accordion(children=[
                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(children=[
                                                dcc.Graph(
                                                    id='graph',
                                                    figure=build_pie_category_value(
                                                        df)
                                                )
                                            ])
                                        )
                                    ],
                                    title="Объем продаж по категориям",
                                ),
                            ], always_open=True),
                        ], xs=12, lg=6),
                        dbc.Col(children=[
                            dbc.Accordion(children=[
                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(children=[
                                                dcc.Graph(
                                                    id='graph',
                                                    figure=build_pie_subcategory_value(
                                                        df)
                                                )
                                            ])
                                        )
                                    ],
                                    title="Объем продаж по под-категориям",
                                ),
                            ], always_open=True),
                        ], xs=12, lg=6),
                    ]),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dbc.Accordion(children=[
                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(children=[
                                                dcc.Graph(
                                                    id='graph',
                                                    figure=build_treemap_product(
                                                        df, ['Category', 'Sub-Category'])
                                                )
                                            ])
                                        )
                                    ],
                                    title="Иерархическая карта товаров",
                                ),
                            ], always_open=True),
                        ], xs=12),
                    ]),
                    dbc.Row(children=[
                        html.A('Перейти на страницу статистики товаров',
                               className='text_link text-info', href=f"{DOMAIN}products", id='text-link')
                    ]
                    ),
                    dbc.Row(children=[
                        html.P('География продаж',
                               className='title_content__block text-info', id='text-title')
                    ]
                    ),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dbc.Accordion(children=[
                                dbc.AccordionItem(
                                    [
                                        dbc.Row(
                                            dbc.Col(children=[
                                                dcc.Graph(
                                                    id='graph',
                                                    figure=build_geography_map(
                                                        'Sales')
                                                )
                                            ])
                                        )
                                    ],
                                    title="Карта географии продаж",
                                ),
                            ], always_open=True),
                        ], xs=12),
                    ]
                    ),
                    dbc.Row(children=[
                        html.A('Перейти на страницу географии продаж',
                               className='text_link text-info', href=f"{DOMAIN}geography", id='text-link')
                    ]
                    ),
                ])
            ])

        ])
    ], fluid=True)
])


@callback(
    [
        Output('all_container_row', 'children'),
        Output('year_container_row', 'children'),
        Output('month_container_row', 'children'),
     ],
    Input('current-time-store', 'modified_timestamp'),
    State('current-time-store', 'data')
)
def update_output_date_in_header(ts, value):
    if value:
        d = datetime.datetime.strptime(value, '%Y-%m-%d')
    else:
        d = datetime.datetime.strptime(START_DATE, '%Y-%m-%d')

    sum_sales = df['Sales'].values.sum()
    sum_count = df['Quantity'].values.sum()
    sum_profit = df['Profit'].values.sum()

    start_date = str(datetime.date(d.year, 1, 1))
    end_date = str(datetime.date(d.year, 12, 30))

    start_month = str(datetime.date(d.year, d.month, 1))
    end_month = str(datetime.date(d.year, d.month, 30))

    prev_start_date = str(datetime.date(d.year-1, 1, 1))
    prev_end_date = str(datetime.date(d.year-1, 12, 30))

    prev_start_month = str(datetime.date(d.year, d.month-1, 1))
    prev_end_month = str(datetime.date(d.year, d.month-1, 30))

    # Get Now data
    df_sales_year = df[(df['Order Date'] >= start_date)
                       & (df['Order Date'] <= end_date)]
    sum_sales_year = df_sales_year['Sales'].values.sum()

    df_profit_year = df[(df['Order Date'] >= start_date)
                        & (df['Order Date'] <= end_date)]
    sum_profit_year = df_profit_year['Profit'].values.sum()

    df_count_year = df[(df['Order Date'] >= start_date)
                       & (df['Order Date'] <= end_date)]
    sum_count_year = df_count_year['Quantity'].values.sum()

    df_sales_month = df[(df['Order Date'] >= start_month)
                        & (df['Order Date'] <= end_month)]
    sum_sales_month = df_sales_month['Sales'].values.sum()

    df_profit_month = df[(df['Order Date'] >= start_month)
                         & (df['Order Date'] <= end_month)]
    sum_profit_month = df_profit_month['Profit'].values.sum()

    df_count_month = df[(df['Order Date'] >= start_month)
                        & (df['Order Date'] <= end_month)]
    sum_count_month = df_count_month['Quantity'].values.sum()

    # Get Prev data
    prev_df_sales_year = df[(df['Order Date'] >= prev_start_date)
                            & (df['Order Date'] <= prev_end_date)]
    prev_sum_sales_year = prev_df_sales_year['Sales'].values.sum()

    prev_df_profit_year = df[(df['Order Date'] >= prev_start_date)
                             & (df['Order Date'] <= prev_end_date)]
    prev_sum_profit_year = prev_df_profit_year['Profit'].values.sum()

    prev_df_count_year = df[(df['Order Date'] >= prev_start_date)
                            & (df['Order Date'] <= prev_end_date)]
    prev_sum_count_year = prev_df_count_year['Quantity'].values.sum()

    prev_df_sales_month = df[(df['Order Date'] >= prev_start_month)
                             & (df['Order Date'] <= prev_end_month)]
    prev_sum_sales_month = prev_df_sales_month['Sales'].values.sum()

    prev_df_profit_month = df[(df['Order Date'] >= prev_start_month)
                              & (df['Order Date'] <= prev_end_month)]
    prev_sum_profit_month = prev_df_profit_month['Profit'].values.sum()

    prev_df_count_month = df[(df['Order Date'] >= prev_start_month)
                             & (df['Order Date'] <= prev_end_month)]
    prev_sum_count_month = prev_df_count_month['Quantity'].values.sum()

    # Get percentage
    if sum_sales_year > prev_sum_sales_year:
        percentage_sales_year = (
            sum_sales_year - prev_sum_sales_year)/sum_sales_year*100
    else:
        percentage_sales_year = -(prev_sum_sales_year -
                                  sum_sales_year)/prev_sum_sales_year*100

    if sum_profit_year > prev_sum_profit_year:
        percentage_profit_year = (
            sum_profit_year - prev_sum_profit_year)/sum_profit_year*100
    else:
        percentage_profit_year = - \
            (prev_sum_profit_year - sum_profit_year)/prev_sum_profit_year*100

    if sum_count_year > prev_sum_count_year:
        percentage_count_year = (
            sum_count_year - prev_sum_count_year)/sum_count_year*100
    else:
        percentage_count_year = -(prev_sum_count_year -
                                  sum_count_year)/prev_sum_count_year*100

    if sum_sales_month > prev_sum_sales_month:
        percentage_sales_month = (
            sum_sales_month - prev_sum_sales_month)/sum_sales_month*100
    else:
        percentage_sales_month = - \
            (prev_sum_sales_month - sum_sales_month)/prev_sum_sales_month*100

    if sum_profit_month > prev_sum_profit_month:
        percentage_profit_month = (
            sum_profit_month - prev_sum_profit_month)/sum_profit_month*100
    else:
        percentage_profit_month = - \
            (prev_sum_profit_month - sum_profit_month)/prev_sum_profit_month*100

    if sum_count_month > prev_sum_count_month:
        percentage_count_month = (
            sum_count_month - prev_sum_count_month)/sum_count_month*100
    else:
        percentage_count_month = - \
            (prev_sum_count_month - sum_count_month)/prev_sum_count_month*100

    all_container_children = dbc.Row(id="all_container", children=[
        dbc.Col(children=[
            build_statistic_card('bi bi-cash-stack',
                                 'Прибыль', round(sum_profit, 2), '$')
        ], xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-bank', 'Продажи', round(sum_sales, 2), '$')
        ], xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-clipboard-data-fill', 'Объем', sum_count, 'шт.')
        ], xs=12),
    ])

    year_container_children = dbc.Row(id="year_container", children=[
        dbc.Col(children=[
                build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                    sum_profit_year, 2), '$', round(percentage_profit_year, 2))
                ], xs=12),
        dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-bank', 'Продажи', round(sum_sales_year, 2), '$', round(percentage_sales_year, 2))
                ], xs=12),
        dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-clipboard-data-fill', 'Объем', sum_count_year, 'шт.', round(percentage_count_year, 2))
                ], xs=12),
    ]),

    month_container_children = dbc.Row(id="month_container", children=[
        dbc.Col(children=[
                build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                    sum_profit_month, 2), '$', round(percentage_profit_month, 2))
                ], xs=12),
        dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-bank', 'Продажи', round(sum_sales_month, 2), '$', round(percentage_sales_month, 2))
                ], xs=12),
        dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-clipboard-data-fill', 'Объем', sum_count_month, 'шт.', round(percentage_count_month, 2))
                ], xs=12),
    ]),

    return all_container_children, year_container_children, month_container_children

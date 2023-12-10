'''
Модуль главной страницы дэшборда. Модуль содержит разметку страницы. Дополнитеьные функции отсутствуют.
'''

import calendar
import dash_bootstrap_components as dbc
import datetime
from data import MAIN_DF, MERGED_DF
from graphs.geography.geography_map import build_geography_map
from graphs.products.pie_category_value import build_pie_category_value
from graphs.products.pie_subcategory_value import build_pie_subcategory_value
from graphs.products.treemap_product import build_treemap_product
from partials.statistic_card import build_statistic_card
from partials.statistic_card_diff import build_statistic_card_diff
from utils.const import DOMAIN, START_DATE
from dash import html, dcc, callback, Output, Input, State


df = MAIN_DF
merge_df = MERGED_DF

layout = html.Div(children=[
    dcc.Store(id="current-time-store", storage_type='local'),
    dbc.Container(children=[
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
                                    dbc.Row(id="all_container_row", className='w-100 p-0', children=[])
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
                                                    figure=build_pie_category_value(df)
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


# Вывод статистических карточек основных метрик
@callback(
    [
        Output('all_container_row', 'children'),
        Output('year_container_row', 'children'),
        Output('month_container_row', 'children'),
     ],
    Input('current-time-store', 'modified_timestamp'),
    State('current-time-store', 'data')
)
def cd_update_stat_card(ts, value):
    # Получение основного интервала времени
    if value:
        d = datetime.datetime.strptime(value, '%Y-%m-%d')
    else:
        d = datetime.datetime.strptime(START_DATE, '%Y-%m-%d')

    # Получение последнего дня
    last_day_current_month = calendar.monthrange(d.year, d.month)[1]
    if d.month == 1:
        last_day_previous_month = calendar.monthrange(d.year - 1, 12)[1]
    else:
        last_day_previous_month = calendar.monthrange(d.year, d.month - 1)[1]

    # Рссчет суммы продаж, прибыли, количества продаж и количества заказов за все время
    sum_sales = df['Sales'].values.sum()
    sum_count = df['Quantity'].values.sum()
    sum_profit = df['Profit'].values.sum()
    sum_orders = len(df)
    sum_client = df['Customer ID'].nunique()
    sum_ref = merge_df['Row ID'].nunique()

    start_date = str(datetime.date(d.year, 1, 1))
    end_date = str(datetime.date(d.year, d.month, d.day))

    start_month = str(datetime.date(d.year, d.month, 1))
    end_month = str(datetime.date(d.year, d.month, last_day_current_month))

    prev_start_date = str(datetime.date(d.year-1, 1, 1))
    prev_end_date = str(datetime.date(d.year-1, 12, 30))

    prev_start_month = str(datetime.date(d.year, d.month-1, 1))
    prev_end_month = str(datetime.date(d.year, d.month-1, last_day_previous_month))

    # Расчет основных метрик за текущий год
    df_current_year = df[(df['Order Date'] >= start_date)
                       & (df['Order Date'] <= end_date)]
    mergedf_current_year = merge_df[(merge_df['Order Date'] >= start_date)
                       & (merge_df['Order Date'] <= end_date)]
    sum_sales_year = df_current_year['Sales'].values.sum()
    sum_profit_year = df_current_year['Profit'].values.sum()
    sum_count_year = df_current_year['Quantity'].values.sum()
    sum_orders_year = len(df_current_year)
    sum_client_year = df_current_year['Customer ID'].nunique()
    sum_ref_year = mergedf_current_year['Row ID'].nunique()

    # Расчет основных метрик за текущий месяц
    df_current_month = df[(df['Order Date'] >= start_month)
                        & (df['Order Date'] <= end_month)]
    mergedf_current_month = merge_df[(merge_df['Order Date'] >= start_month)
                        & (merge_df['Order Date'] <= end_month)]
    sum_sales_month = df_current_month['Sales'].values.sum()
    sum_profit_month = df_current_month['Profit'].values.sum()
    sum_count_month = df_current_month['Quantity'].values.sum()
    sum_orders_month = len(df_current_month)
    sum_client_month = df_current_month['Customer ID'].nunique()
    sum_ref_month = mergedf_current_month['Row ID'].nunique()

    # Расчет основных метрик за предыдущий год
    prev_df_year = df[(df['Order Date'] >= prev_start_date)
                            & (df['Order Date'] <= prev_end_date)]
    prev_mergedf_year = merge_df[(merge_df['Order Date'] >= prev_start_date)
                            & (merge_df['Order Date'] <= prev_end_date)]
    prev_sum_sales_year = prev_df_year['Sales'].values.sum()
    prev_sum_profit_year = prev_df_year['Profit'].values.sum()
    prev_sum_count_year = prev_df_year['Quantity'].values.sum()
    prev_sum_orders_year = len(prev_df_year)
    prev_sum_client_year = prev_df_year['Customer ID'].nunique()
    prev_sum_ref_year = prev_mergedf_year['Row ID'].nunique()

    # Расчет основных метрик за предыдущий месяц
    prev_df_month = df[(df['Order Date'] >= prev_start_month)
                             & (df['Order Date'] <= prev_end_month)]
    prev_mergedf_month = merge_df[(merge_df['Order Date'] >= prev_start_month)
                             & (merge_df['Order Date'] <= prev_end_month)]
    prev_sum_sales_month = prev_df_month['Sales'].values.sum()
    prev_sum_profit_month = prev_df_month['Profit'].values.sum()
    prev_sum_count_month = prev_df_month['Quantity'].values.sum()
    prev_sum_orders_month = len(prev_df_month)
    prev_sum_client_month = prev_df_month['Customer ID'].nunique()
    prev_sum_ref_month = prev_mergedf_month['Row ID'].nunique()

    # Получение процентного соотношения для метрик текущего года
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

    if sum_orders_year > prev_sum_orders_year:
        percentage_orders_year = (
            sum_orders_year - prev_sum_orders_year)/sum_orders_year*100
    else:
        percentage_orders_year = -(prev_sum_orders_year -
                                  sum_orders_year)/prev_sum_orders_year*100
        
    if sum_client_year > prev_sum_client_year:
        percentage_client_year = (
            sum_client_year - prev_sum_client_year)/sum_client_year*100
    else:
        percentage_client_year = -(prev_sum_client_year -
                                  sum_client_year)/prev_sum_client_year*100
        
    if sum_ref_year > prev_sum_ref_year:
        percentage_ref_year = (
            sum_ref_year - prev_sum_ref_year)/sum_ref_year*100
    else:
        percentage_ref_year = -(prev_sum_ref_year -
                                  sum_ref_year)/prev_sum_ref_year*100

    # Получение процентного соотношения для метрик текущего месяца
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

    if sum_orders_month > prev_sum_orders_month:
        percentage_orders_month = (
            sum_orders_month - prev_sum_orders_month)/sum_orders_month*100
    else:
        percentage_orders_month = - \
            (prev_sum_orders_month - sum_orders_month)/prev_sum_orders_month*100
        
    if sum_client_month > prev_sum_client_month:
        percentage_client_month = (
            sum_client_month - prev_sum_client_month)/sum_client_month*100
    else:
        percentage_client_month = - \
            (prev_sum_client_month - sum_client_month)/prev_sum_client_month*100
        
    if sum_ref_month > prev_sum_ref_month:
        percentage_ref_month = (
            sum_ref_month - prev_sum_ref_month)/sum_ref_month*100
    else:
        percentage_ref_month = - \
            (prev_sum_ref_month - sum_ref_month)/prev_sum_ref_month*100



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
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-bag-check', 'Кол-во продаж', sum_orders, 'шт.')
        ], xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-person-circle', 'Кол-во заказчиков', sum_client, 'чел.')
        ], xs=12),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-arrow-clockwise', 'Кол-во возвратов', sum_ref, 'шт.')
        ], xs=12),
    ])

    year_container_children = dbc.Row(id="year_container", children=[
        dbc.Col(children=[
            build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                sum_profit_year, 2), '$', round(percentage_profit_year, 2), prev_sum_profit_year)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-bank', 'Продажи', round(sum_sales_year, 2), '$', round(percentage_sales_year, 2), prev_sum_sales_year)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-clipboard-data-fill', 'Объем', sum_count_year, 'шт.', round(percentage_count_year, 2), prev_sum_count_year)
            ], xs=12),   
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-bag-check', 'Кол-во продаж', sum_orders_year, 'шт.', round(percentage_orders_year, 2), prev_sum_orders_year)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-person-circle', 'Кол-во заказчиков', sum_client_year, 'чел.', round(percentage_client_year, 2), prev_sum_client_year)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-arrow-clockwise', 'Кол-во возвратов', sum_ref_year, 'шт.', round(percentage_ref_year, 2), prev_sum_ref_year)
            ], xs=12),
    ]),

    month_container_children = dbc.Row(id="month_container", children=[
        dbc.Col(children=[
            build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                sum_profit_month, 2), '$', round(percentage_profit_month, 2), prev_sum_profit_month)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-bank', 'Продажи', round(sum_sales_month, 2), '$', round(percentage_sales_month, 2), prev_sum_sales_month)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-clipboard-data-fill', 'Объем', sum_count_month, 'шт.', round(percentage_count_month, 2), prev_sum_count_month)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-bag-check', 'Кол-во продаж', sum_orders_month, 'шт.', round(percentage_orders_month, 2), prev_sum_orders_month)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-person-circle', 'Кол-во заказчиков', sum_client_month, 'чел.', round(percentage_client_month, 2), prev_sum_client_month)
            ], xs=12),
        dbc.Col(children=[
            build_statistic_card_diff(
                'bi bi-arrow-clockwise', 'Кол-во возвратов', sum_ref_month, 'шт.', round(percentage_ref_month, 2), prev_sum_ref_month)
            ], xs=12),
    ]),

    return all_container_children, year_container_children, month_container_children

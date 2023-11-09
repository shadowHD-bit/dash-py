import dash
from dash import html, callback
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime

dash.register_page(__name__, name="Главная",
                   title="Информационная панель | Главная", path='/main', order=0)
df = pd.read_excel('data\data.xlsx', sheet_name='Orders')

sum_sales = df['Sales'].values.sum()
sum_count = df['Quantity'].values.sum()
sum_profit = df['Profit'].values.sum()

start_date = f'2014-01-01'
end_date = f'2014-11-30'

start_month = f'2014-{datetime.now().month}-01'
end_month = f'2014-{datetime.now().month}-30'

prev_start_date = f'2013-01-01'
prev_end_date = f'2013-11-30'

prev_start_month = f'2014-{datetime.now().month-1}-01'
prev_end_month = f'2014-{datetime.now().month-1}-30'

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


layout = html.Div([
    dbc.Container(children=[
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За все время')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                dbc.Card(className='main_card', children=[
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
                dbc.Card(className='main_card', children=[
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
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За год')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                                  f'{round(sum_profit_year, 2)} $'),
                                html.H6(f'{round(percentage_profit_year,2)} %', style={"color": "green"} if percentage_profit_year > 0 else {"color": "red"}),

                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                                  f'{round(sum_sales_year, 2)} $'),
                                html.H6(f'{round(percentage_sales_year,2)} %', style={"color": "green"} if percentage_sales_year > 0 else {"color": "red"}),

                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                              html.H4(f'{sum_count_year} шт.'),
                                html.H6(f'{round(percentage_count_year,2)} %', style={"color": "green"} if percentage_count_year > 0 else {"color": "red"}),
                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
        ]),
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За месяц')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                                  f'{round(sum_profit_month, 2)} $'),
                                              html.H6(
                                                  f'{round(percentage_profit_month,2)} %', style={"color": "green"} if percentage_profit_month > 0 else {"color": "red"}),
                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                                  f'{round(sum_sales_month, 2)} $'),
                                              html.H6(
                                                  f'{round(percentage_sales_month,2)} %', style={"color": "green"} if percentage_sales_month > 0 else {"color": "red"}),

                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                dbc.Card(className='main_card', children=[
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
                                              html.H4(
                                                  f'{sum_count_month} шт.'),
                                html.H6(f'{round(percentage_count_month,2)} %', style={"color": "green"} if percentage_count_month > 0 else {"color": "red"}),

                            ], width=8),
                        ]),
                    ]
                    )
                ])
            ], lg=4, md=6, xs=12),
        ]),
        dbc.Row(children=[]),
        dbc.Row(children=[]),
    ], fluid=True)
])


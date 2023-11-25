import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime
from data import MAIN_DF
from partials.statistic_card import build_statistic_card
import plotly.express as px

from partials.statistic_card_diff import build_statistic_card_diff

dash.register_page(__name__, name="Главная",
                   title="Информационная панель | Главная", path='/main', order=0)

df = MAIN_DF

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


fig_value_categories_pie = px.pie(df, values='Quantity', names='Category')
fig_value_categories_pie.update_traces(
    textposition='inside', textinfo='percent+label')
fig_value_categories_pie.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig_value_subcategories_pie = px.pie(
    df, values='Quantity', names='Sub-Category')
fig_value_subcategories_pie.update_traces(
    textposition='inside', textinfo='percent+label')
fig_value_subcategories_pie.update_layout(margin=dict(t=0, l=0, r=0, b=0))


layout = html.Div([
    dbc.Container(children=[
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За все время')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                build_statistic_card('bi bi-cash-stack',
                                     'Прибыль', round(sum_profit, 2), '$')
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
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За год')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                    sum_profit_year, 2), '$', round(percentage_profit_year, 2))
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-bank', 'Продажи', round(sum_sales_year, 2), '$', round(percentage_sales_year, 2))
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-clipboard-data-fill', 'Объем', sum_count_year, 'шт.', round(percentage_count_year, 2))
            ], lg=4, md=6, xs=12),
        ]),
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('За месяц')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                build_statistic_card_diff('bi bi-cash-stack', 'Прибыль', round(
                    sum_profit_month, 2), '$', round(percentage_profit_month, 2))
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-bank', 'Продажи', round(sum_sales_month, 2), '$', round(percentage_sales_month, 2))
            ], lg=4, md=6, xs=12),
            dbc.Col(children=[
                build_statistic_card_diff(
                    'bi bi-clipboard-data-fill', 'Объем', sum_count_month, 'шт.', round(percentage_count_month, 2))
            ], lg=4, md=6, xs=12),
        ]),
        dbc.Row(class_name='mt-3 mb-2', children=[
            dbc.Col(children=[
                html.H3('Категории и подкатегории')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                    dbc.CardHeader(
                        html.P("Объем продаж по категориям")
                    ),
                    dbc.CardBody(children=[
                        dbc.Row(
                            dbc.Col(children=[
                                dcc.Graph(
                                    id='example-graph',
                                    figure=fig_value_categories_pie
                                )
                            ])
                        )
                    ])
                ])
            ], xs=12, lg=6),
            dbc.Col(children=[
                dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                    dbc.CardHeader(
                        html.P("Объем продаж по под-категориям")
                    ),
                    dbc.CardBody(children=[
                        dbc.Row(
                            dbc.Col(children=[
                                dcc.Graph(
                                    id='example-graph',
                                    figure=fig_value_subcategories_pie
                                )
                            ])
                        )
                    ])
                ])
            ], xs=12, lg=6)
        ]),
        dbc.Row(children=[]),
    ], fluid=True)
])

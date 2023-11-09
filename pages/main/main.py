import dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime

dash.register_page(__name__, name="Главная",
                   title="Информационная панель | Главная", path='/main')
df = pd.read_excel('data\data.xlsx', sheet_name='Orders')

sum_sales = df['Sales'].values.sum()

sum_count = df['Quantity'].values.sum()

sum_profit = df['Profit'].values.sum()

start_date = f'2014-01-01'
end_date = f'2014-11-30'

start_month = f'2014-{datetime.now().month}-01'
end_month = f'2014-{datetime.now().month}-30'

df_sales_year = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
sum_sales_year = df_sales_year['Sales'].values.sum()

df_profit_year = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
sum_profit_year = df_profit_year['Profit'].values.sum()

df_count_year = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]
sum_count_year = df_count_year['Quantity'].values.sum()

df_sales_month = df[(df['Order Date'] >= start_month) & (df['Order Date'] <= end_month)]
sum_sales_month = df_sales_month['Sales'].values.sum()

df_profit_month = df[(df['Order Date'] >= start_month) & (df['Order Date'] <= end_month)]
sum_profit_month = df_profit_month['Profit'].values.sum()

df_count_month = df[(df['Order Date'] >= start_month) & (df['Order Date'] <= end_month)]
sum_count_month = df_count_month['Quantity'].values.sum()


layout = html.Div([
    dbc.Container(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                html.H3('За все время')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Прибыль ($)"),
                            html.H4(round(sum_profit, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Продажи ($)"),
                            html.H4(round(sum_sales, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Количество проданной продукции"),
                            html.H4(sum_count),
                        ]
                    )
                )
            ], width=4),
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                html.H3('За год')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Прибыль ($)"),
                            html.H4(round(sum_profit_year, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Продажи ($)"),
                            html.H4(round(sum_sales_year, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Количество проданной продукции"),
                            html.H4(sum_count_year),
                        ]
                    )
                )
            ], width=4),
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                html.H3('За месяц')
            ], width=12)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Прибыль ($)"),
                            html.H4(round(sum_profit_month, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Продажи ($)"),
                            html.H4(round(sum_sales_month, 2)),
                        ]
                    )
                )
            ], width=4),
            dbc.Col(children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P("Количество проданной продукции"),
                            html.H4(sum_count_month),
                        ]
                    )
                )
            ], width=4),
        ]),
        dbc.Row(children=[]),
        dbc.Row(children=[]),
    ], fluid=True)
])

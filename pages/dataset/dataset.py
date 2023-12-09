import dash
from dash import html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from data import MAIN_DF, RETURNS_DF

dash.register_page(__name__, title="Информационная панель | Датасет",
                   name="Датасет", path='/dataset', order=5)

df = MAIN_DF
returns_df = RETURNS_DF

tab1_content = dbc.Row([
    dash_table.DataTable(df[:300].to_dict('records'),
                         [{"name": i, "id": i} for i in df.columns],
                         page_size=30,
                         style_table={
        'overflowX': 'scroll'
    }
    )
])

tab2_content = dbc.Row([
    dash_table.DataTable(returns_df[:300].to_dict('records'),
                         [{"name": i, "id": i} for i in returns_df.columns],
                         page_size=30,
                         style_table={
        'overflowX': 'scroll'
    })
])
layout = html.Div([
    dbc.Row(style={'margin': '10px'}, children=[
        dbc.Row([
            html.P("Основной датесет", className='text_title')
        ]),
        dbc.Row([
            html.P("Из-за большого размера исходного датасета, на странице выводяться только первые 300 строк исходного файла XLSX. Чтобы ознакомиться с полным датасетом, нажмите кнопку 'Скачать'.", className='text'),
        ]),
        dbc.Row([
            dbc.Button("Скачать", color="success", id="btn-download-dataset",
                       className="me-1", style={'width': 'fit-content', 'margin': '5px 12px'}),
        ]),
        dbc.Tabs([
            dbc.Tab(tab1_content, label="Orders"),
            dbc.Tab(tab2_content, label="Returns"),
        ]),
    ])
])

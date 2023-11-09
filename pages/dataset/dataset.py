import dash
from dash import html, dash_table, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, title="Информационная панель | Датасет", name="Датасет", path='/dataset', order=1)

df = pd.read_excel('data\data.xlsx')

layout = html.Div([
    dbc.Row(style={'margin': '10px'}, children=[
        dbc.Row([
            html.H3("Основной датесет")
        ]),
        dbc.Row([
            html.P("Из-за большого размера исходного датасета, на странице выводяться только первые 300 строк исходного файла XLSX. Чтобы ознакомиться с полным датасетом, нажмите кнопку Скачать.", style={'margin': 0})
        ]),
        dbc.Row([
            dbc.Button("Скачать", color="success", id="btn-download-dataset", className="me-1",style={'width': 'fit-content', 'margin': '5px 12px'}),
        ]),
        dbc.Row([
            dash_table.DataTable(df[:300].to_dict('records'),
                                [{"name": i, "id": i} for i in df.columns],
                                page_size=30,
                                style_table={
                                    'overflowX': 'scroll'
                                }
                                )
        ])
    ])
])


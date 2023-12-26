'''
Модуль страницы информации по датасету. Модуль содержит разметку и внутренние обратные вызовы. Дополнительные функции отсуттсвуют.
'''

from dash import html, dash_table, callback, Output, Input, dcc
from data import MAIN_DF, RETURNS_DF
import dash_bootstrap_components as dbc


df = MAIN_DF
returns_df = RETURNS_DF


tab1_content = dbc.Row([
    dash_table.DataTable(df[:300].to_dict('records'),
                         [{"name": i, "id": i} for i in df.columns],
                         page_size=30,
                         style_table={
        'overflowX': 'scroll'
    })
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
            html.P("Основной датесет", className='text_title text-info')
        ]),
        dbc.Row([
            html.P("Из-за большого размера исходного датасета, на странице выводяться только первые 300 строк исходного файла XLSX. Чтобы ознакомиться с полным датасетом, нажмите кнопку 'Скачать'.", className='text'),
        ]),
        dbc.Row([
            dbc.Button("Скачать", color="info", id="btn-download-dataset",
                       className="me-1 mb-4", style={'width': 'fit-content', 'margin': '5px 12px'}),
            dcc.Download(id="download-dataset")
        ]),
        dbc.Tabs([
            dbc.Tab(tab1_content, label="Orders"),
            dbc.Tab(tab2_content, label="Returns"),
        ]),
    ])
])


# Обратный вызов загрузки файла датасета
@callback(
    Output("download-dataset", "data"),
    Input("btn-download-dataset", "n_clicks"),
    prevent_initial_call=True,
)
def cb_download_dataset(n_clicks):
    return dcc.send_file(
        "data\data.xlsx"
    )

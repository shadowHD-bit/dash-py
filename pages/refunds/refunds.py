from datetime import date
import dash
from dash import html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
from data import MAIN_DF, RETURNS_DF
import pandas as pd
from partials.statistic_card import build_statistic_card
import plotly.express as px
import dash_ag_grid as dag

return_df = RETURNS_DF
main_df = MAIN_DF
merged_df = pd.merge(return_df, main_df, on='Order ID')

list_region = merged_df['Region_x'].value_counts()
list_prod = merged_df['Product Name'].value_counts()

layout = html.Div([
    dbc.Row(className="mt-2 mb-3", children=[
        html.P('Общая информация', className='title_content__block text-info')
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            build_statistic_card('bi bi-cash-stack',
                'Общее кол-во возвратов', len(return_df), 'шт.')
        ], xs=4),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-bank', 'Часто возвращаемый товар', list_prod.index[0], '')
        ], xs=4),
        dbc.Col(children=[
            build_statistic_card(
                'bi bi-clipboard-data-fill', 'Часто возвращаемый регион', list_region.index[0], '')
        ], xs=4),
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Accordion(children=[
                dbc.AccordionItem(
                    [
                        dbc.Row(className='mb-3', children=[
                            dbc.Col(children=[
                                dcc.DatePickerRange(
                                    id='picker_date_region',
                                    min_date_allowed=date(2012, 1, 1),
                                    max_date_allowed=date(2015, 12, 30),
                                    start_date=date(2012, 1, 1),
                                    end_date=date(2015, 12, 30),
                                    display_format='D/M/Y'
                                ),
                            ], xs=3)
                        ]),
                        dbc.Row(
                            dbc.Col(id="region_graph__container", children=[
                            ], xs=12)
                        )
                    ],
                    title="Статистика возвратов по регионам",
                ),
            ], start_collapsed=True),
        ], xs=12),
    ]),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Accordion(children=[
                dbc.AccordionItem(
                    [
                        dbc.Row(className='mb-3', children=[
                            dbc.Col(children=[
                                dcc.DatePickerRange(
                                    id='picker_date_prod',
                                    min_date_allowed=date(2012, 1, 1),
                                    max_date_allowed=date(2015, 12, 30),
                                    start_date=date(2012, 1, 1),
                                    end_date=date(2015, 12, 30),
                                    display_format='D/M/Y'
                                ),
                            ], xs=3),
                            dbc.Col(children=[
                                dcc.Dropdown(
                                    ['Technology', 'Furniture', 'Office Supplies'],
                                    id="candidate_product_ref",
                                    placeholder="Выберите категорию",
                                    value="Technology"
                                )
                            ], xs=3),
                            dbc.Col(id='dropdown_sub_ref', children=[
                                dcc.Dropdown(
                                    [],
                                    id="sub_product_dropdown_ref",
                                    placeholder="Выберите подкатегорию",
                                    className='d-none'
                                ),
                            ], xs=3)
                        ]),
                        dbc.Row(
                            dbc.Col(id="prod_graph__container", children=[
                            ], xs=12)
                        )
                    ],
                    title="Статистика возвратов по товарам",
                ),
            ], start_collapsed=True),
        ], xs=12),
    ]),
    dbc.Row(className="mt-2 mb-3", children=[
        html.P('Список возвратов', className='title_content__block text-info')
    ]),
    dbc.Row(className='mb-3', children=[
        dbc.Col(children=[
            dcc.DatePickerRange(
                id='picker_date_ref',
                min_date_allowed=date(2012, 1, 1),
                max_date_allowed=date(2015, 12, 30),
                start_date=date(2012, 1, 1),
                end_date=date(2015, 12, 30),
                display_format='D/M/Y'
            ),
        ], xs=3),
        dbc.Col(children=[
            dcc.Dropdown(
                ['Technology', 'Furniture', 'Office Supplies'],
                id="picker_cat_ref",
                placeholder="Выберите категорию",
                value="Technology"
            )
        ], xs=3),
        dbc.Col(id='container_dropdown_sub', children=[
            dcc.Dropdown(
                [],
                id="picker_sub_ref",
                placeholder="Выберите подкатегорию",
                className='d-none'
            ),
        ], xs=3),
    ]),
    dbc.Row(id='list_ref', className='p-3', children=[

    ]),
])


@callback(
    [Output("picker_sub_ref", "className"),
     Output("picker_sub_ref", "options")],
    Input("picker_cat_ref", "value"),
)
def display_subcategory_dropown_call(n):
    if n:
        sub_df = merged_df.loc[merged_df['Category'] == n]
        sub_list = sub_df['Sub-Category'].unique()
        return '', sub_list
    else:
        return 'd-none', []


@callback(
    Output("list_ref", "children"),
    [Input("picker_sub_ref", "value"),
     Input('picker_date_ref', 'start_date'),
     Input('picker_date_ref', 'end_date')]
)
def display_subcategory_dropown_callback(n, start_date, end_date):
    if n:
        sub_df = merged_df.loc[merged_df['Sub-Category'] == n]
        list_df = sub_df[(merged_df['Order Date'] > str(start_date)) & (
            merged_df['Order Date'] < str(end_date))]
        df_ref = list_df.loc[:, ['Order ID', 'Order Date',
                                 'Product ID', 'Product Name', 'Region_x']]
        list_ = dbc.Table.from_dataframe(
            df_ref, striped=True, bordered=True, hover=True, index=True
        )

        return list_
    else:
        return ""


@callback(
    Output("region_graph__container", "children"),
    [Input('picker_date_region', 'start_date'),
     Input('picker_date_region', 'end_date')]
)
def display_graph_region_callback(start_date, end_date):

    list_df = merged_df[(merged_df['Order Date'] > str(start_date)) & (
        merged_df['Order Date'] < str(end_date))]
    lists = list_df['Region_x'].value_counts()
    fig = px.bar(lists, x=lists.index, y=lists.values)
    fig.update_layout(xaxis_title="Region", yaxis_title="Count Refunds")
    fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)')
    fig.update_layout(legend=dict(font=dict(color="#0077b6")))
    children = html.Div(children=[
        dcc.Graph(
            figure=fig
        )
    ])
    return children


@callback(
    [Output("sub_product_dropdown_ref", "className"),
     Output("sub_product_dropdown_ref", "options")],
    Input("candidate_product_ref", "value"),
)
def display_subcategory_dropown_callback(n):
    if n:
        sub_df = merged_df.loc[merged_df['Category'] == n]
        sub_list = sub_df['Sub-Category'].unique()
        return '', sub_list
    else:
        return 'd-none', []


@callback(
    Output("prod_graph__container", "children"),
    [Input("sub_product_dropdown_ref", "value"),
     Input('picker_date_prod', 'start_date'),
     Input('picker_date_prod', 'end_date')]
)
def display_subcategory_dropown_callback(n, start_date, end_date):
    list_df = merged_df[(merged_df['Order Date'] > str(start_date)) & (
        merged_df['Order Date'] < str(end_date))]
    list_dfs = list_df[list_df['Sub-Category'] == n]

    if n and len(list_dfs):
        lists = list_dfs['Product Name'].value_counts()
        fig = px.bar(lists, x=lists.index, y=lists.values)
        fig.update_layout(xaxis_title="Product Name",
                          yaxis_title="Count Refunds")
        fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)')
        fig.update_layout(legend=dict(font=dict(color="#0077b6")))
        children = html.Div(children=[
            dcc.Graph(
                figure=fig
            )
        ])
        return children
    else:
        return ''

import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


dash.register_page(__name__, name="Товары", title="Информационная панель | Товары", path='/products')
df = pd.read_excel('data\data.xlsx')

fig_treemap = px.treemap(df, path=[px.Constant("All"), 'Category', 'Sub-Category'], values='Sales')
fig_treemap.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig_treemap.update_traces(root_color="lightgrey")


fig_value_categories_pie = px.pie(df, values='Quantity', names='Category')
fig_value_categories_pie.update_traces(textposition='inside', textinfo='percent+label')
fig_value_categories_pie.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig_value_subcategories_pie = px.pie(df, values='Quantity', names='Sub-Category')
fig_value_subcategories_pie.update_traces(textposition='inside', textinfo='percent+label')
fig_value_subcategories_pie.update_layout(margin = dict(t=0, l=0, r=0, b=0))



layout = html.Div([
    dbc.Row(className="mt-2 mb-3", children=[
            html.H5('Общая информация')
            ]
        ),
    dbc.Row(children=[
        dbc.Col(children=[
            dbc.Card(color='info', outline=True, className="p-0 m-2", children=[
                dbc.CardHeader(
                    html.P("Иерархическая карта категорий")
                ),
                dbc.CardBody(children=[
                      dbc.Row(
                        dbc.Col(children=[
                            dcc.Graph(
                                id='example-graph',
                                figure=fig_treemap
                            )
                        ])
                    )
                ])
            ])
        ], xs=12),
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
    dbc.Row(children=[

    ]),
    dbc.Row(children=[

    ]),
])



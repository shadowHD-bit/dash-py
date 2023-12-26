'''
Модуль страницы настроек дэшборда. Дополнитеьные функции отсутствуют.
'''

import dash_bootstrap_components as dbc
from datetime import datetime
from dash import html, dcc, callback, Output, Input, State
from datetime import date
from utils.const import START_DATE


layout = html.Div(style={'margin': '10px'}, children=[
    dbc.Row(className="mb-3", children=[
            html.P("Настройки информационной панели",
                   className='title_content__block text-info')
            ]),
    dbc.Row(className='mb-3', children=[
            dbc.Col(children=[
                dbc.Row(className="mb-3", children=[
                    html.P("Изменение текущей даты",
                           className='subtitle_content__block text-info')
                ]),
                dbc.Row(className="mb-3", children=[
                    html.P("Функция смены текущей даты дэшборда позволяет пользователям отображать данные за определенный период времени, например, за прошлый месяц, текущий год или любой другой выбранный промежуток времени. Это удобно для анализа и сравнения данных в разные временные периоды, а также для отслеживания динамики изменений в различных параметрах. ",
                           className='text')
                ]),
                dbc.Card(color="light", outline=True, children=[
                    dbc.Row(className='p-3', children=[
                        dbc.Row(children=[
                            html.P("Изменение даты")
                        ]),
                        dbc.Row(children=[
                            dcc.Store(id="current-time-store",
                                      storage_type='local'),
                            dcc.DatePickerSingle(
                                id='my-date-picker-single',
                                min_date_allowed=date(2012, 1, 1),
                                max_date_allowed=date(2015, 12, 29),
                            ),
                            html.Div(id='output-container-date-picker-single')
                        ]),
                    ]),
                ])
            ], xs=12, md=6, lg=6),
        ]
    )
])


# Обратный вызов обновления даты поля ввода
@callback(
    Output('my-date-picker-single', 'date'),
    Input('current-time-store', 'modified_timestamp'),
    State('current-time-store', 'data')
)
def update_output(ts, value):
    if value:
        return datetime.strptime(value, '%Y-%m-%d').date()
    else:
        return datetime.strptime(START_DATE, '%Y-%m-%d').date()


# Обратный вызов обновления локального хранилища текущей даты
@callback(
    Output('current-time-store', 'data'),
    Input('my-date-picker-single', 'date'),
    State('current-time-store', 'data')
)
def update_local_output(value, state):
    if value:
        return str(value)

from dash import html
import dash_bootstrap_components as dbc


def build_statistic_card(icon_class, title_text, body_text, designation):
    '''
    Функция создания карточки метрики без процентного соотношения
    '''
    card = dbc.Card(outline=True, color='light', className='main_card shadow-sm', children=[
        dbc.CardBody(className='main_card__body', children=[
            dbc.Row(className='w-100 p-0', children=[
                dbc.Col(className='main_card__icon_container', children=[
                    html.H4(
                        html.I(
                            className=f"{icon_class}"),
                        className="main_card__icon")
                ], width=4),
                dbc.Col(className='main_card__text_container', children=[
                    html.H6(f"{title_text}", className='text'),
                    html.H4(f'{body_text} {designation}',
                            className='text_title'),
                ], width=8),
            ]),
        ]
        )
    ])
    return card

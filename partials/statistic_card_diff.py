from dash import html
import dash_bootstrap_components as dbc


def build_statistic_card_diff(icon_class, title_text, body_text, designation, diff, last_):
    '''
    Функция создания карточки метрики с процентным соотношением
    '''
    if title_text == 'Кол-во возвратов':
        card = dbc.Card(outline=True, color='light', className='main_card shadow-sm', children=[
            dbc.Button(
                children=[html.I(className="bi bi-info")], id=f"hover-target-{last_}-{diff}", color="info",
                className=f"info_card__btn", outline=True,
                n_clicks=0,
            ),
            dbc.Popover(
                f"В предыдущем: {last_}",
                target=f"hover-target-{last_}-{diff}",
                body=True,
                trigger="hover",
            ),
            dbc.CardBody(className='main_card__body', children=[
                dbc.Row(children=[
                    dbc.Col(className='main_card__icon_container', children=[
                        html.H4(
                            html.I(
                                className=f"{icon_class}"),
                            className="main_card__icon")
                    ], width=4),
                    dbc.Col(className='main_card__text_container', children=[
                        html.H6(f"{title_text}", className='text'),
                        html.H4(
                            f'{body_text} {designation}', className='text_title'),
                        html.H6(f'{diff} %', style={
                            "color": "red"} if diff > 0 else {"color": "green"}, className='text'),
                    ], width=8),
                ]),
            ]
            )
        ])
    else:
        card = dbc.Card(outline=True, color='light', className='main_card shadow-sm', children=[
            dbc.Button(
                children=[html.I(className="bi bi-info")], id=f"hover-target-{last_}-{diff}", color="info",
                className="info_card__btn", outline=True,
                n_clicks=0,
            ),
            dbc.Popover(
                f"В предыдущем: {last_}",
                target=f"hover-target-{last_}-{diff}",
                body=True,
                trigger="hover",
            ),
            dbc.CardBody(className='main_card__body', children=[
                dbc.Row(children=[
                    dbc.Col(className='main_card__icon_container', children=[
                        html.H4(
                            html.I(
                                className=f"{icon_class}"),
                            className="main_card__icon")
                    ], width=4),
                    dbc.Col(className='main_card__text_container', children=[
                        html.H6(f"{title_text}", className='text'),
                        html.H4(
                            f'{body_text} {designation}', className='text_title'),
                        html.H6(f'{diff} %', style={
                            "color": "green"} if diff > 0 else {"color": "red"}, className='text'),
                    ], width=8),
                ]),
            ]
            )
        ])
    return card

from dash import html
import dash_bootstrap_components as dbc


def build_statistic_card_diff(icon_class, title_text, body_text, designation, diff):

    card = dbc.Card(color="info", outline=True, className='main_card', children=[
        dbc.CardBody(className='main_card__body', children=[
            dbc.Row(children=[
                dbc.Col(className='main_card__icon_container', children=[
                    html.H4(
                        html.I(
                            className=f"{icon_class}"),
                        className="main_card__icon")
                ], width=4),
                dbc.Col(className='main_card__text_container', children=[
                    html.H6(f"{title_text}"),
                    html.H4(
                        f'{body_text} {designation}'),
                    html.H6(f'{diff} %', style={
                        "color": "green"} if diff > 0 else {"color": "red"}),

                ], width=8),
            ]),
        ]
        )
    ])
    return card

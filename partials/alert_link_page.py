import dash_bootstrap_components as dbc
from dash import html

from utils.const import DOMAIN


def build_alert_link_page(name_page, description, page_link, color_alert):
    alert = dbc.Alert(className='alert', children=[
        html.H6(children=[
            html.A(f"{name_page}", href=f"{DOMAIN}{page_link}",
                    className="alert-link"),
            ], className="alert-heading"),
        html.Hr(),
        html.P(
            f"{description}",
            className="mb-0",
        ),
    ], color=color_alert
    )

    return alert

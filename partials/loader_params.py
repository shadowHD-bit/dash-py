import dash_bootstrap_components as dbc
from dash import html

def build_loader_params():
    '''
    Функция создания лоадера выбора параметра графика, карты и т.д.
    '''
    loader = dbc.Row(style={'width': '100%','display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'flexDirection': 'row'}, className='d-flex justify-content-center align-items-center mt-4', children=[
            dbc.Row(
                dbc.Col(
                    html.Img(src='assets/images/non_params.png', width=200), xs=12, className='d-flex justify-content-center align-items-center',
                )
            ),
            dbc.Row(
                dbc.Col(
                    html.P("Выберите параметр!",
                    className='subtitle_content__block text-info mt-2'), xs=12, className='d-flex justify-content-center align-items-center',
                )
            ),
        ])
    return loader
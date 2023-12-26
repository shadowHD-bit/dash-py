'''
Модуль страницы 404. Дополнитеьные функции отсутствуют.
'''

from dash import html


layout = html.Div(className="notfound_content", children=[
    html.Img(src='assets/gif/bubble-gum-error-404.gif',
             className='notfound_content__images'),
    html.P('Уппс... Ошибка 404!', className='notfound__text_title'),
    html.P('Страница не найдена! Попробуйте повторить запрос или выбрать нужный раздел в каталоге!',
           className='notfound__text_subtitle'),
])
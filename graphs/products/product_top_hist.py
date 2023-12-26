import plotly.express as px

def build_bar_top_product(df, x_param, y_param, start_date, end_date):
    '''
    Функция создания столбчатой диаграммы топа продуктов
    '''
    list_df = df[(df['Order Date'] > str(start_date)) & (df['Order Date'] < str(end_date))]
    list = list_df.groupby(x_param, as_index=False)[y_param].sum()
    list_sort = list.sort_values(y_param, ascending=False)
    fig = px.bar(list_sort[:10], x=y_param, y=x_param)
    fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)')
    fig.update_layout(legend=dict(font=dict(color="#0077b6")))
    return fig
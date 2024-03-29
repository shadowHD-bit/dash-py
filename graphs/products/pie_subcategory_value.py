import plotly.express as px

def build_pie_subcategory_value(df):
    '''
    Функция создания круговой диаграммы топа подкатегорий
    '''
    fig_value_subcategories_pie = px.pie(
        df, values='Quantity', names='Sub-Category')
    fig_value_subcategories_pie.update_traces(
        textposition='inside', textinfo='percent+label')
    fig_value_subcategories_pie.update_layout(margin=dict(
        t=0, l=0, r=0, b=0))
    fig_value_subcategories_pie.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)')
    fig_value_subcategories_pie.update_layout(legend=dict(font=dict(color="#0077b6")))
    return fig_value_subcategories_pie

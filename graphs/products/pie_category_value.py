import plotly.express as px

def build_pie_category_value(df):
    ''' Retrun pie graphs category values'''
    fig_value_categories_pie = px.pie(df, values='Quantity', names='Category')
    fig_value_categories_pie.update_traces(
        textposition='inside', textinfo='percent+label')
    fig_value_categories_pie.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    return fig_value_categories_pie

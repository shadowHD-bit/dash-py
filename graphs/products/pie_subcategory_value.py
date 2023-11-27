import plotly.express as px

def build_pie_subcategory_value(df):
    ''' Retrun pie graphs subcategory values'''
    fig_value_subcategories_pie = px.pie(
        df, values='Quantity', names='Sub-Category')
    fig_value_subcategories_pie.update_traces(
        textposition='inside', textinfo='percent+label')
    fig_value_subcategories_pie.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    return fig_value_subcategories_pie
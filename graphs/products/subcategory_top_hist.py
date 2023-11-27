import plotly.express as px

def build_bar_top_subcategory(df, x_param, y_param):
    list = df.groupby(x_param, as_index=False)[y_param].sum()
    list_sort = list.sort_values(y_param, ascending=True)

    fig = px.bar(list_sort[:10], x=y_param, y=x_param)
    return fig
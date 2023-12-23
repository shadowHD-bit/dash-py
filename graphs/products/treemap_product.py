import plotly.express as px

def build_treemap_product(df, params):
    all_list = [px.Constant("All")]
    all_list.extend(params)
    fig_treemap = px.treemap(df, path=all_list, values='Sales')
    fig_treemap.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    fig_treemap.update_traces(root_color="lightgrey")
    fig_treemap.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)')
    fig_treemap.update_layout(legend=dict(font=dict(color="#0077b6")))
    return fig_treemap

from data import MAIN_DF
import plotly.express as px
import pandas as pd

def build_geography_map(candidate):
    total_sales_by_country = MAIN_DF.groupby(
            'Country', as_index=False)[candidate].sum()
        
    total_sales_by_country_df = pd.DataFrame(total_sales_by_country)
    fig_map = px.choropleth(total_sales_by_country_df, color=total_sales_by_country_df[candidate],
                                locations=total_sales_by_country_df['Country'],
                                locationmode="country names",
                                labels={candidate: candidate}
                                )
    fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig_map.update_layout(paper_bgcolor='rgba(0, 0, 0, 0.0)', plot_bgcolor='rgba(0, 0, 0, 0.0)',  geo = {'bgcolor': 'rgba(0, 0, 0, 0.0)',  'lakecolor': 'rgba(0, 0, 0, 0.0)'}, width=1400, height=600)
    return fig_map
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px
from value_pool_heatmap.heatmap import prepare_heatmap_data

st.title("ESG Growth Opportunities Dashboard")

signal_df = pd.read_csv('data/esg_signals.csv')
sentiment_df = pd.read_csv('data/sentiments.csv')

heatmap_data = prepare_heatmap_data(signal_df, sentiment_df)

fig = px.density_heatmap(
    heatmap_data, x='keyword', y='demand_signal', z='sentiment',
    color_continuous_scale='RdYlGn', title="ESG Value Pool Heatmap"
)

st.plotly_chart(fig)

st.dataframe(heatmap_data)

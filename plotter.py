
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset into a dataframe
df = pd.read_csv('datasets/4cda851a-d2f4-474b-9959-3022012ee94a.csv')

# Create the bar chart using plotly express
fig = px.bar(df, x='Item', y='Price', title='Grocery Item Prices')

# Display the chart using streamlit
st.plotly_chart(fig)


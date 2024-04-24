import altair as alt
#from vega_datasets import data
import pandas as pd
import streamlit as st

emp = pd.read_csv("c:\\data\\emp.csv")
source = emp[['ename','sal']]

bars = alt.Chart(source).mark_bar().encode(
    x='sal',
    y="ename"
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='sal'
)

a = (bars + text).properties(height=500)

st.dataframe(emp)  # Same as st.write(df)
st.altair_chart(a, use_container_width=True)
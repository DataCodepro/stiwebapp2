import streamlit as st
import pandas as pd
def data_frame_demo():
   df = pd.read_csv('cleaneddata2.csv')
   st.write(df)
   df34 = pd.read_excel('randd.xlsx')
   st.header('R and D missing data')
   st.write(df34.isnull().sum())
st.set_page_config(page_title="DataFrame", page_icon="📊")
st.markdown("# DataFrame")
st.sidebar.header("DataFrame")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.""")
data_frame_demo()
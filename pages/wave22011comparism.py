import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def wave2comparisim():
    df = pd.read_csv('cleaneddata2.csv')
    df2 = df[['sector','turnover08','turnover09','turnover10','totalstaff08','totalstaff09','totalstaff10']]
    select = st.sidebar.selectbox("COMPARISIM ANALYSIS FOR WAVE ONE",['Staff AGAINST TurnOver2008',
    'Staff AGAINST TurnOver2009','Staff AGAINST TurnOver2010'],key=1)
    if select == 'Staff AGAINST TurnOver2008':
        df2= df2[df2['turnover08']!=0]
        st.header('Staff AGAINST TurnOver2008')
        fig = px.scatter(df2, x="totalstaff08", y="turnover08",
	         size="turnover08", color="sector",
                 hover_name="sector", log_x=True, size_max=60)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    elif select == 'Staff AGAINST TurnOver2009':
        df2= df2[df2['turnover09']!=0]
        st.header('Staff AGAINST TurnOver2009')
        fig = px.scatter(df2, x="totalstaff09", y="turnover09",
	         size="turnover09", color="sector",
                 hover_name="sector", log_x=True, size_max=70)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    elif select == 'Staff AGAINST TurnOver2010':
        df2= df2[df2['turnover10']!=0]
        st.header('Staff AGAINST TurnOver2010')
        fig = px.scatter(df2, x="totalstaff10", y="turnover10",
	         size="turnover10", color="sector",
                 hover_name="sector", log_x=True, size_max=70)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    
   
st.set_page_config(page_title="WAVE12008COMPARISIM", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave2 2008 Enjoy!""")
wave2comparisim()   

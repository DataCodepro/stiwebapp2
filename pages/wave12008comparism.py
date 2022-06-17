import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def wave1comparisim():
    df = pd.read_csv('cleaneddata2.csv')
    df2 = df[['sector','turnover05','turnover06','turnover07','totalstaff05','totalstaff06','totalstaff07']]
    select = st.sidebar.selectbox("COMPARISIM ANALYSIS FOR WAVE ONE",['Staff AGAINST TurnOver2005',
    'Staff AGAINST TurnOver2006','Staff AGAINST TurnOver2007'],key=1)
    if select == 'Staff AGAINST TurnOver2005':
        df2= df2[df2['turnover05']!=0]
        st.header('Staff AGAINST TurnOver2005')
        fig = px.scatter(df2, x="totalstaff05", y="turnover05",
	         size="turnover05", color="sector",
                 hover_name="sector", log_x=True, size_max=60)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    elif select == 'Staff AGAINST TurnOver2006':
        df2= df2[df2['turnover06']!=0]
        st.header('Staff AGAINST TurnOver2006')
        fig = px.scatter(df2, x="totalstaff06", y="turnover06",
	         size="turnover06", color="sector",
                 hover_name="sector", log_x=True, size_max=70)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    elif select == 'Staff AGAINST TurnOver2007':
        df2= df2[df2['turnover07']!=0]
        st.header('Staff AGAINST TurnOver2007')
        fig = px.scatter(df2, x="totalstaff07", y="turnover07",
	         size="turnover07", color="sector",
                 hover_name="sector", log_x=True, size_max=70)
        fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
        st.plotly_chart(fig)
    
   
st.set_page_config(page_title="WAVE12008COMPARISIM", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 2008 Enjoy!""")
wave1comparisim()   

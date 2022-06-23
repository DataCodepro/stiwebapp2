import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def wave1():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 2008",['TOTAL NUMBER OF STAFF IN YEAR 2005, 2006, 2007  BY SECTORS',
        'TOTAL  TURNOVER FROM 2005 TO 2007 FOR EACH SECTOR'],key =1)
    if select == 'TOTAL NUMBER OF STAFF IN YEAR 2005, 2006, 2007  BY SECTORS':
        st.subheader('TOTAL NUMBER OF STAFF IN YEAR 2005 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES',)
        fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff05',width=800, height=500,color_continuous_scale ='Viridis')
        fig.update_traces(textinfo='label+percent entry')
        fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),paper_bgcolor="#202A44",)
        st.plotly_chart(fig)
        if st.checkbox('TOTAL NUMBER OF STAFF IN YEAR 2006 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES'):
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff06',width=800, height=500)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#202A44",)
            st.plotly_chart(fig)
        if st.checkbox('TOTAL NUMBER OF STAFF IN YEAR 2007 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES'):
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff07',width=800, height=500,)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#202A44",)
            st.plotly_chart(fig)
       
    elif select == 'TOTAL  TURNOVER FROM 2005 TO 2007 FOR EACH SECTOR':
            wave1 = pd.read_excel('wave1.xlsx',sheet_name='Sheet1')
            df2 =wave1[['turnover050607','sector','year']].groupby(['year','sector']).agg('sum')
            df2.reset_index(inplace = True)
            df2.replace({'NOT SPECIFIED':'OTHERS'},inplace =True)
            df2.sort_values('turnover050607', ascending =True,inplace=True)
            fig = px.scatter(df2, y="turnover050607", x="sector",size="turnover050607", color="sector",size_max=150,animation_frame='year')
            fig.update_layout(autosize=False,width=800,height=600, paper_bgcolor="#202A44")
            st.plotly_chart(fig)
    

    
st.set_page_config(page_title="WAVE12008", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 2008""")
wave1()   


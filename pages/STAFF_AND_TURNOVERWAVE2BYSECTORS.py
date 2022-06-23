import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def wave2():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 2008",['TOTAL NUMBER OF STAFF IN YEAR 2008, 2009, 2010  BY SECTORS',
        'TOTAL  TURNOVER FROM 2008 TO 2010 FOR EACH SECTOR'],key =1)
    if select == 'TOTAL NUMBER OF STAFF IN YEAR 2008, 2009, 2010  BY SECTORS':
        st.subheader('TOTAL NUMBER OF STAFF IN YEAR 2008 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES',)
        fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff08',width=800, height=500)
        fig.update_traces(textinfo='label+percent entry')
        fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),paper_bgcolor="#202A44",)
        st.plotly_chart(fig)
        if st.checkbox('TOTAL NUMBER OF STAFF IN YEAR 2009 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES'):
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff09',width=800, height=500)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#202A44",)
            st.plotly_chart(fig)
        if st.checkbox('TOTAL NUMBER OF STAFF IN YEAR 2010 BY SECTORS ACCORDING TO THEIR AREA OF SERVICES'):
            fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff10',width=800, height=500,)
            fig.update_traces(textinfo='label+percent entry')
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#202A44",)
            st.plotly_chart(fig)
       
    elif select == 'TOTAL  TURNOVER FROM 2005 TO 2007 FOR EACH SECTOR':
            wave1 = pd.read_excel('wave1.xlsx',sheet_name='Sheet2')
            df2 =wave1[['turnover080910','sector2','year']].groupby(['year','sector2']).agg('sum')
            df2.reset_index(inplace = True)
            df2.replace({'NOT SPECIFIED':'OTHERS'},inplace =True)
            df2.sort_values('turnover050607', ascending =True,inplace=True)
            fig = px.scatter(df2, y="turnover080910", x="sector",size="turnover080910", color="sector2",size_max=150,animation_frame='year')
            fig.update_layout(autosize=False,width=800,height=600, paper_bgcolor="#202A44")
            st.plotly_chart(fig)
    

    
st.set_page_config(page_title="WAVE22011", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 2011""")
wave2()   


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def tables():
    select = st.sidebar.selectbox("TABLE REPORT ANALYSIS",['TABLE'],key =1)
    if select == 'TABLE':
        st.subheader('Internal R&D Against Innovation Activities  wheather it is Continuous OR Occational')
        d3 = {
    'Continuous R&D':[147,284],
    'Occassional R&D':[284,147]
}
        ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
        st.table(ITCRDORD)
        if st.checkbox('Innovation Activities Against Their Total Expenditure'):
            df2 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet3')
            df2.rename({'Unnamed: 0':'x'},axis =1,inplace=True)
            df2.drop('x',axis = 1,inplace=True)
            st.table(df2)
        if st.checkbox('Information source of Sector for both WAVE1 and WAVE2'):
            df = pd.read_csv('infosource.csv')
            
            st.table(df)
        if st.checkbox('Outcomes and Effect for Products Based on their level of Success'):
            df = pd.read_csv('effect.csv')
            
            st.table(df)

        if st.checkbox('Importance Of Govt Support Policy Programm'):
            df = pd.read_csv('policy.csv')
            
            st.table(df)
        if st.checkbox(' Factors Affecting Innovation Activities by Degree of Importance'):
            df = pd.read_csv('obstacle.csv')
            
            st.table(df)
                
st.set_page_config(page_title="TABLE", page_icon="📈")
st.markdown("#TABLE REPORT ANALYSIS")
st.header(
        """This TABLE ANALYSIS REPORT""")
tables()   


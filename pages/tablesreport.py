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
        st.write(ITCRDORD)
        if st.checkbox('Innovation Activites:Completed or Abandoned'):
            df = pd.read_excel('output.xlsx',sheet_name = 'Sheet2')
            df.rename({'Unnamed: 1':' '},axis =1,inplace=True)
            df.fillna('Value',inplace= True)
            st.table(df)
        if st.checkbox('Innovation Activities Against Their Total Expenditure'):
            df2 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet3')
            df2.rename({'Unnamed: 0':'x'},axis =1,inplace=True)
            df2.drop('x',axis = 1,inplace=True)
            st.table(df2)
        if st.checkbox('Innovation Activities of Develop Product or Process: Abandoned or On-going'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet4')
            df3.rename({'Unnamed: 0':'x'},axis =1,inplace=True)
            df3.drop('x',axis = 1,inplace=True)
            st.table(df3)
        if st.checkbox('Information source of Sector for both WAVE1 and WAVE2'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet5')
            df3.fillna("''",inplace=True)
            st.table(df3)
        if st.checkbox('Innovations Based on their Origin'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet6')
            df3.rename({'Unnamed: 0':'Product innovation originated mainly in','Unnamed: 1':'No of Resondent'},axis =1,inplace=True)
            df3.drop(0,axis = 0,inplace=True)
            st.table(df3)
        if st.checkbox('Sector Cooperation by Location of Partner HQ'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet7')
            df3.drop([8,9],axis=0,inplace=True)
            df3.fillna(' ',inplace=True)
            df3.set_index('Location of Group HQ',inplace=True)
            df3.rename({'Unnamed: 2':'No of Resondent'},axis =1,inplace=True)
            st.table(df3)
        if st.checkbox('Outcomes and Effect for Products Based on their level of Success'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet8')
            df3.rename({'Unnamed: 1':' '},axis =1,inplace =True)
            df3.fillna("''",inplace=True)
            st.table(df3)
        if st.checkbox('Importance Of Govt Support Policy Programm'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet9')
            df3.rename({'Unnamed: 1':' '},axis =1,inplace =True)
            df3.fillna("''",inplace=True)
            st.table(df3)
        if st.checkbox(' Factors Affecting Innovation Activities by Degree of Importance'):
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet10')
            df3.rename({'Unnamed: 1':' '},axis =1,inplace =True)
            df3.fillna("''",inplace=True)
            df3.drop('Unnamed: 3',axis = 1,inplace =True)
            st.table(df3)
                
st.set_page_config(page_title="TABLE", page_icon="📈")
st.markdown("#TABLE REPORT ANALYSIS")
st.header(
        """This TABLE ANALYSIS REPORT""")
tables()   


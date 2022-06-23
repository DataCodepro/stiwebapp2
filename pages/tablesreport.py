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
            df = pd.read_csv('nigeria-innovation.csv')
            df6=df[['sinfo1',
'sinfo2',
'sinfo3',
'sinfo4',
'sinfo5',
'sinfo6',
'sinfo7',
'sinfo8',
'sinfo9',
'sinfo10'
]]
            df6.replace({'3':'High','2':'Medium','1':'Low','0':'Not Used','':'Unspecified'},inplace=True)
            d1=pd.DataFrame(df6[['sinfo1']].value_counts())
            d2 =pd.DataFrame(df6[['sinfo2']].value_counts())
            d3 =pd.DataFrame(df6[['sinfo3']].value_counts())
            d4 =pd.DataFrame(df6[['sinfo4']].value_counts())
            d5 =pd.DataFrame(df6[['sinfo5']].value_counts())
            d6 =pd.DataFrame(df6[['sinfo6']].value_counts())
            d7 =pd.DataFrame(df6[['sinfo7']].value_counts())
            d8 =pd.DataFrame(df6[['sinfo8']].value_counts())
            d9 =pd.DataFrame(df6[['sinfo9']].value_counts())
            d10 =pd.DataFrame(df6[['sinfo10']].value_counts())
            d1.reset_index(inplace=True)
            d2.reset_index(inplace=True)
            d3.reset_index(inplace=True)
            d4.reset_index(inplace=True)
            d5.reset_index(inplace=True)
            d6.reset_index(inplace=True)
            d7.reset_index(inplace=True)
            d8.reset_index(inplace=True)
            d9.reset_index(inplace=True)
            d10.reset_index(inplace=True)
            info = pd.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10],axis=1)
            info.replace({' ':'Unspecified'},inplace =True)
            info.rename({0:'Response'},axis = 1,inplace=True)
            st.table(info.transpose())
        if st.checkbox('Outcomes and Effect for Products Based on their level of Success'):
            df = pd.read_csv('nigeria-innovation.csv')
            df3 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet8')
            df4=df[['ieffect_org1',
'ieffect_org2',
'ieffect_org3',
'ieffect_org4',
'ieffect_org5'
]]
            df4.replace({'3':'High','2':'Medium','1':'Low','0':'Not experienced','':'Unspecified'},inplace=True)
            d1=pd.DataFrame(df4[['ieffect_org1']].value_counts())
            d2 =pd.DataFrame(df4[['ieffect_org2']].value_counts())
            d3 =pd.DataFrame(df4[['ieffect_org3']].value_counts())
            d4 =pd.DataFrame(df4[['ieffect_org4']].value_counts())
            d5 =pd.DataFrame(df4[['ieffect_org5']].value_counts())
            d1.reset_index(inplace=True)
            d2.reset_index(inplace=True)
            d3.reset_index(inplace=True)
            d4.reset_index(inplace=True)
            d5.reset_index(inplace=True)
            effect = pd.concat([d1,d2,d3,d4,d5],axis=1)
            effect.replace({' ':'Unspecified'},inplace =True)
            effect.rename({0:'Response'},axis = 1,inplace=True)

            st.table(effect.transpose())

        if st.checkbox('Importance Of Govt Support Policy Programm'):
            df = pd.read_csv('nigeria-innovation.csv')
            df3 = df[['policysup1',
'policysup2',
'policysup3',
'policysup4',
'policysup5',
'policysup6',
'policysup7',
'policysup8'
]]
            df3.replace({'3':'Highly important','2':'Moderately important','1':'Slightly important','0':'Not important','':'Unspecified'},inplace=True)
            d1=pd.DataFrame(df3[['policysup1']].value_counts())
            d2 =pd.DataFrame(df3[['policysup2']].value_counts())
            d3 =pd.DataFrame(df3[['policysup3']].value_counts())
            d4 =pd.DataFrame(df3[['policysup4']].value_counts())
            d5 =pd.DataFrame(df3[['policysup5']].value_counts())
            d6 =pd.DataFrame(df3[['policysup6']].value_counts())
            d7 =pd.DataFrame(df3[['policysup7']].value_counts())
            d8 =pd.DataFrame(df3[['policysup8']].value_counts())
            d1.reset_index(inplace=True)
            d2.reset_index(inplace=True)
            d3.reset_index(inplace=True)
            d4.reset_index(inplace=True)
            d5.reset_index(inplace=True)
            d6.reset_index(inplace=True)
            d7.reset_index(inplace=True)
            d8.reset_index(inplace=True)
            policy = pd.concat([d1,d2,d3,d4,d5,d6,d7,d8],axis=1)
            policy.replace({' ':'Unspecified'},inplace =True)
            policy.rename({0:'Output'},axis = 1,inplace=True)
            st.table(policy.transpose())
        if st.checkbox(' Factors Affecting Innovation Activities by Degree of Importance'):
            df = pd.read_csv('nigeria-innovation.csv')
            df2 = df[['obstacle_cost1',
'obstacle_cost2',
'obstacle_cost3',
'obstacle_cost4',
'obstacle_cost5',
'obstacle_knowledge1',
'obstacle_knowledge2',
'obstacle_knowledge3',
'obstacle_knowledge4',
'obstacle_market1',
'obstacle_market2',
'obstacle_market3',
'obstacle_market4',
'obstacle_market5',
'obstacle_infra1',
'obstacle_infra2',
'obstacle_need1',
'obstacle_need2',
'obstacle_other1',
'obstacle_other2',
'obstacle_other3'
]]
            df2.replace({'3':'High','2':'Medium','1':'Low','0':'Not experienced','':'Unspecified'},inplace=True)
            d1=pd.DataFrame(df2[['obstacle_cost1']].value_counts())
            d2 =pd.DataFrame(df2[['obstacle_cost2']].value_counts())
            d3 =pd.DataFrame(df2[['obstacle_cost3']].value_counts())
            d4 =pd.DataFrame(df2[['obstacle_cost4']].value_counts())
            d5 =pd.DataFrame(df2[['obstacle_cost5']].value_counts())
            d6 =pd.DataFrame(df2[['obstacle_knowledge1']].value_counts())
            d7 =pd.DataFrame(df2[['obstacle_knowledge2']].value_counts())
            d8 =pd.DataFrame(df2[['obstacle_knowledge3']].value_counts())
            d9 =pd.DataFrame(df2[['obstacle_knowledge4']].value_counts())
            d10 =pd.DataFrame(df2[['obstacle_market1']].value_counts())
            d11=pd.DataFrame(df2[['obstacle_market2']].value_counts())
            d13=pd.DataFrame(df2[['obstacle_market3']].value_counts())
            d15=pd.DataFrame(df2[['obstacle_market4']].value_counts())
            d16=pd.DataFrame(df2[['obstacle_market5']].value_counts())
            d17=pd.DataFrame(df2[['obstacle_infra1']].value_counts())
            d18=pd.DataFrame(df2[['obstacle_infra2']].value_counts())
            d19=pd.DataFrame(df2[['obstacle_need1']].value_counts())
            d20=pd.DataFrame(df2[['obstacle_need2']].value_counts())
            d21 =pd.DataFrame(df2[['obstacle_other1']].value_counts())
            d22=pd.DataFrame(df2[['obstacle_other2']].value_counts())
            d23=pd.DataFrame(df2[['obstacle_other3']].value_counts())
            d1.reset_index(inplace=True)
            d2.reset_index(inplace=True)
            d3.reset_index(inplace=True)
            d4.reset_index(inplace=True)
            d5.reset_index(inplace=True)
            d6.reset_index(inplace=True)
            d7.reset_index(inplace=True)
            d8.reset_index(inplace=True)
            d9.reset_index(inplace=True)
            d10.reset_index(inplace=True)
            d11.reset_index(inplace=True)
            d13.reset_index(inplace=True)
            d15.reset_index(inplace=True)
            d16.reset_index(inplace=True)
            d17.reset_index(inplace=True)
            d18.reset_index(inplace=True)
            d19.reset_index(inplace=True)
            d20.reset_index(inplace=True)
            d21.reset_index(inplace=True)
            d22.reset_index(inplace=True)
            d23.reset_index(inplace=True)
            obstacle = pd.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d13,d15,d16,d17,d18,d19,d20,d21,d22,d23],axis=1)
            obstacle.replace({' ':'Unspecified'},inplace =True)
            obstacle.rename({0:'Output'},axis = 1,inplace=True)
            

            st.table(obstacle.transpose())
                
st.set_page_config(page_title="TABLE", page_icon="📈")
st.markdown("#TABLE REPORT ANALYSIS")
st.header(
        """This TABLE ANALYSIS REPORT""")
tables()   


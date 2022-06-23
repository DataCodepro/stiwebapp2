import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 AND WAVE2",['Continuous OR Occational RandD','Innovation and total expendiure','INFORMATION SOURCE',
        'Effect of innovation','Importance of govt support policy/prog','Obstacle'],key=1)
    if select == 'Continuous OR Occational RandD':
        df = pd.read_excel('randd.xlsx')
        df2 = df[['iact1','crd','ord']]
        df2.dropna(inplace=True)
        d1 = pd.crosstab(df2['iact1'],df2['ord'])
        d2 = pd.crosstab(df2['iact1'],df2['crd'])
        d3 = {
            'Continuous R&D':[147,284],
            'Occassional R&D':[284,147]
        }
        ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
        ITCRDORD.rename({0:'NO',1:'YES'},axis = 0,inplace =True)
        ITCRDORD.reset_index(inplace=True)
        ITCRDORD.rename({'index':'Outcome'},axis = 1,inplace =True)

        if st.checkbox('Continuous R&D'):
            fig = px.funnel(ITCRDORD, x="Outcome", y="Continuous R&D")
            st.plotly_chart(fig)
        if st.checkbox('Occassional R&D'):
            fig = px.funnel(ITCRDORD, x="Outcome", y="Occassional R&D")
            st.plotly_chart(fig)
    elif select == 'Innovation and total expendiure':
        df7 = pd.read_excel('output.xlsx',sheet_name='Sheet3')
        df7.drop('Unnamed: 0',axis = 1,inplace =True)
        if st.checkbox('Innovation Against total expendiure'):
            fig = px.scatter(df7, x="No of Innovations Engagement", y="Total Expenditure",size="Total Expenditure", color="Types of Selected R&D by  Enterprise",hover_name="Types of Selected R&D by  Enterprise"
                 , log_x=True, size_max=60,width=1000, height=600)
            st.plotly_chart(fig)


            
    
    elif select == 'INFORMATION SOURCE':
        df2 = df[['sinfo1',
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
        df2.replace({'3':'High','2':'Medium','1':'Low','0':'Not Used','':'Unspecified'},inplace=True)
        st.subheader('INFORMATION SOURCE')
        if st.checkbox('Information source - Internal'):
            fig = px.histogram(df2, x="sinfo1", color="sinfo1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Suppliers'):
            fig = px.histogram(df2, x="sinfo2", color="sinfo2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Customers'):
            fig = px.histogram(df2, x="sinfo3", color="sinfo3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Competitors'):
            fig = px.histogram(df2, x="sinfo4", color="sinfo4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source -  Consultants, commercial labs or private R&D institutes'):
            fig = px.histogram(df2, x="sinfo5", color="sinfo5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Universities, other higher ed. Institutions'):
            fig = px.histogram(df2, x="sinfo6", color="sinfo6",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Public research institutes'):
            fig = px.histogram(df2, x="sinfo7", color="sinfo7",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Conferences, fairs, exhibitions'):
            fig = px.histogram(df2, x="sinfo8", color="sinfo8",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - ournals, trade publications'):
            fig = px.histogram(df2, x="sinfo9", color="sinfo9",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Information source - Professional, industry associations'):
            fig = px.histogram(df2, x="sinfo10", color="sinfo10",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
            

    elif select == 'Effect of innovation':
        df4=df[['ieffect_org1',
'ieffect_org2',
'ieffect_org3',
'ieffect_org4',
'ieffect_org5'
]]
        df4.replace({'3':'High','2':'Medium','1':'Low','0':'Not experienced','':'Unspecified'},inplace=True)
        st.subheader('Effect of innovation Based On their level of success ')
        if st.checkbox('Effect of innovation (organisational) - reduced response time to customer needs'):
            fig = px.histogram(df2, x="ieffect_org1", color="ieffect_org1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Effect of innovation (organisational) - improved quality of goods/services'):
            fig = px.histogram(df2, x="ieffect_org2", color="ieffect_org2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Effect of innovation (organisational) - reduced costs per unit output'):
            fig = px.histogram(df2, x="ieffect_org3", color="ieffect_org3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Effect of innovation (organisational) - improved staff satisfaction/reduced turn'):
            fig = px.histogram(df2, x="ieffect_org4", color="ieffect_org4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Effect of innovation (organisational) - increased or maitained market share'):
            fig = px.histogram(df2, x="ieffect_org5", color="ieffect_org5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
                                                                                                                        
    elif select == 'Importance of govt support policy/prog':
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
        st.subheader('Importance of govt support policy/prog')
                
        if st.checkbox('Importance of govt support policy/prog - R&D funding'):
            fig = px.histogram(df2, x="policysup1", color="policysup1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Training'):
            fig = px.histogram(df2, x="policysup2", color="policysup2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Subsidies'):
            fig = px.histogram(df2, x="policysup3", color="policysup3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Tax rebates'):
            fig = px.histogram(df2, x="policysup4", color="policysup4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Technical support/advice'):
            fig = px.histogram(df2, x="policysup5", color="policysup5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Infrastructure support'):
            fig = px.histogram(df2, x="policysup6", color="policysup6",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog -  Loans and grants'):
            fig = px.histogram(df2, x="policysup7", color="policysup7",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Others'):
            fig = px.histogram(df2, x="policysup8", color="policysup8",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)
                
    elif select == 'Obstacle':
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
        st.subheader('Factors Affecting Innovation Activities by Degree of Importance')
        if st.checkbox('Obstacle - lack of in-house funds'):
            fig = px.histogram(df2, x="obstacle_cost1", color="obstacle_cost1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - lack of external financing'):
            fig = px.histogram(df2, x="obstacle_cost2", color="obstacle_cost2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - high costs of innovation'):
            fig = px.histogram(df2, x="obstacle_cost3", color="obstacle_cost3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - economic risk'):
            fig = px.histogram(df2, x="obstacle_cost4", color="obstacle_cost4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - expensive environment-friendly R&D'):
            fig = px.histogram(df2, x="obstacle_cost5", color="obstacle_cost5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - lack of qualified personnel'):
            fig = px.histogram(df2, x="obstacle_knowledge1", color="obstacle_knowledge1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - lack of tech information'):
            fig = px.histogram(df2, x="obstacle_knowledge2", color="obstacle_knowledge2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox(':Obstacle - lack of market information'):
            fig = px.histogram(df2, x="obstacle_knowledge3", color="obstacle_knowledge3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox(':Obstacle - difficult to find coop partners'):
            fig = px.histogram(df2, x="obstacle_knowledge4", color="obstacle_knowledge4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - mkt dominated by large ent'):
            fig = px.histogram(df2, x="obstacle_market1", color="obstacle_market1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - uncertain demand'):
            fig = px.histogram(df2, x="obstacle_market2", color="obstacle_market2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - mkt dominated by foreign substitutes'):
            fig = px.histogram(df2, x="obstacle_market3", color="obstacle_market3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox(':Obstacle - consumers unwilling to pay'):
            fig = px.histogram(df2, x="obstacle_market4", color="obstacle_market4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - imitation'):
            fig = px.histogram(df2, x="obstacle_market5", color="obstacle_market5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - poor basic infrastructure'):
            fig = px.histogram(df2, x="obstacle_infra1", color="obstacle_infra1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - inadequate facilities'):
            fig = px.histogram(df2, x="obstacle_infra2", color="obstacle_infra2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - no need due to prior innovation'):
            fig = px.histogram(df2, x="obstacle_need1", color="obstacle_need1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - no need due to no demand for innovation'):
            fig = px.histogram(df2, x="obstacle_need2", color="obstacle_need2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - internal organisational rigidities'):
            fig = px.histogram(df2, x="obstacle_other1", color="obstacle_other1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - inflexible regulations/standards'):
            fig = px.histogram(df2, x="obstacle_other2", color="obstacle_other2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Obstacle - limitation of S&T public policies'):
            fig = px.histogram(df2, x="obstacle_other3", color="obstacle_other3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
st.set_page_config(page_title="EDA", page_icon="📈")
st.markdown("#EDA ANALYSIS")
st.header(
        """EDA ANALYSIS""")
EDA()   
            
            
        

import streamlit as st
def label():
    select = st.sidebar.selectbox("LABELS",['TABLE'],key =1)
    if select == 'TABLE':
        st.subheader('TABLE REPORT LABEL FOR TABLE 3')
        st.write('''sinfo1:Information source - Internal
 sinfo2:Information source - Suppliers
 sinfo3:Information source - Customers
 sinfo4:Information source - Competitors
 sinfo5:Information source - Consultants, commercial labs or private R&D institutes
 sinfo6:Information source - Universities, other higher ed. Institutions
 sinfo7:Information source - Public research institutes
 sinfo8:Information source - Conferences, fairs, exhibitions
 sinfo9:Information source - Journals, trade publications
 sinfo10:Information source - Professional, industry associations
    ''')
        if st.checkbox('TABLE REPORT LABEL FOR TABLE 4'):
            st.write('''ieffect_org1:Effect of innovation (organisational) - reduced response time to customer needs
ieffect_org2:Effect of innovation (organisational) - improved quality of goods/services
ieffect_org3:Effect of innovation (organisational) - reduced costs per unit output
ieffect_org4:Effect of innovation (organisational) - improved staff satisfaction/reduced turn
ieffect_org5:Effect of innovation (organisational) - increased or maitained market share

''')
        if st.checkbox('TABLE REPORT LABEL FOR TABLE 5'):
            st.write('''policysup1:Importance of govt support policy/prog - R&D funding
policysup2:Importance of govt support policy/prog - Training
policysup3:Importance of govt support policy/prog - Subsidies
policysup4:Importance of govt support policy/prog - Tax rebates
policysup5:Importance of govt support policy/prog - Technical support/advice
policysup6:Importance of govt support policy/prog - Infrastructure support
policysup7:Importance of govt support policy/prog - Loans and grants
policysup8:Importance of govt support policy/prog - Others

''')
        if st.checkbox('TABLE REPORT LABEL FOR TABLE 6'):
            st.write('''obstacle_cost1:Obstacle - lack of in-house funds
obstacle_cost2:Obstacle - lack of external financing
obstacle_cost3:Obstacle - high costs of innovation
obstacle_cost4:Obstacle - economic risk
obstacle_cost5:Obstacle - expensive environment-friendly R&D
obstacle_knowledge1:Obstacle - lack of qualified personnel
obstacle_knowledge2:Obstacle - lack of tech information
obstacle_knowledge3:Obstacle - lack of market information
obstacle_knowledge4:Obstacle - difficult to find coop partners
obstacle_market1:Obstacle - mkt dominated by large ent.
obstacle_market2:Obstacle - uncertain demand
obstacle_market3:Obstacle - mkt dominated by foreign substitutes
obstacle_market4:Obstacle - consumers unwilling to pay
obstacle_market5:Obstacle - imitation
obstacle_infra1:Obstacle - poor basic infrastructure
obstacle_infra2:Obstacle - inadequate facilities
obstacle_need1:Obstacle - no need due to prior innovation
obstacle_need2:Obstacle - no need due to no demand for innovation
obstacle_other1:Obstacle - internal organisational rigidities
obstacle_other2:Obstacle - inflexible regulations/standards
obstacle_other3:Obstacle - limitation of S&T public policies

''')
st.set_page_config(page_title="LABEL", page_icon="📈")
st.markdown("#LABEL FOR TABLE REPORT")
st.header(
        """This LABEL FOR TABLE REPORT""")
label()   

            
        

import streamlit as st
# from app import LogOut_Clicked
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def H_UI():
    
    col1, col2 = st.columns([12,1])
    with col2:
        dummy = st.button("LogOut") 
        if dummy:
            # LogOut_Clicked()
            st.session_state['loggedIn']=False
    st.write('##')   
    st.info('logged in as HR')  
    st.write('##')
    value = st.selectbox(f'select Manager',['a','b'])
    # st.write('#')
    with st.expander('Maager Details'):
            st.write('name')
            st.write('ID')
            st.write('mailID')
            st.write('ph-no')
    
    st.write('##')
    # st.write('---')
    # st.write('##')

    st.subheader('Employees shortlisted by manager')
    a=[0]*4
    r = [0]*4
    for i in range(4):
        with st.expander('Employee name'):
            st.write('employee ID')
            st.write('employee mail') 
            st.write('employee ph-no')
            st.write('P Hike')
            st.write('P rating')
            st.write('C rating')
            st.write('Manager Note')
            c1,c2,c3= st.columns([3.2,3.2,12])
            with c1:
                ai =st.button(f'approve Employee {i}')
            if ai :
                st.success('Employee approved')
                st.write('Status :- approve')
                
            with c2:
                ri = st.button(f'reject employee {i}')
            if ri:
                st.error('Employee rejected')
                st.write('Status :- reject')

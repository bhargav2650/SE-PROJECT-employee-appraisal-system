import streamlit as st


def E_UI():
    col1, col2 = st.columns([3.5,1])
    with col2:
            dummy = st.button("LogOut")
            if dummy:
                # LogOut_Clicked()
                st.session_state['loggedIn']=False
    c1,c2,c3=st.columns([2,10,2])
    with c2:
        st.write('##')
        st.info('logged in as Employee')
        st.write('##')
    
        with st.form('E_details'):
            E_id = st.text_input('Enter your ID')
            st.write("fetch and display corresponding ename")
            tasks_A = st.number_input('Number of tasks assigned',min_value=0)
            tasks_C = st.number_input('Number of tasks completed',min_value=0)
            hours= st.number_input('Number of hours saved',min_value=0)
            defects_F  = st.number_input('Number of defects found',min_value=0)
            efects_Fix = st.number_input('number of defects fixed',min_value=0)
            acc = st.text_area('Additional Accomplishments')


            st.form_submit_button('submit')
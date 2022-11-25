import streamlit as st
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def H_UI():
    
    col1, col2 = st.columns([12,1])
    with col2:
         dummy = st.button("LogOut") 
    st.write('##')   
    st.info('logged in as HR')  
    st.write('##')
    tab1, tab2 = st.tabs(["Approve Employees", "Check status of Employees"])
    with tab1:
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
        # a=[0]*4
        # r = [0]*4
        # for i in range(4):
        #     with st.expander('Employee name'):
        #         st.write('employee ID')
        #         st.write('employee mail') 
        #         st.write('employee ph-no')
        #         st.write('P Hike')
        #         st.write('P rating')
        #         st.write('C rating')
        #         st.write('Manager Note')
        #         c1,c2,c3= st.columns([3.2,3.2,12])
        #         with c1:
        #             ai =st.button(f'approve Employee {i}')
        #         if ai :
        #             st.success('Employee approved')
        #             st.write('Status :- approve')
                    
        #         with c2:
        #             ri = st.button(f'reject employee {i}')
        #         if ri:
        #             st.error('Employee rejected')
        #             st.write('Status :- reject')
        emp = st.selectbox(f'select Employee',['a','b'])
        with st.expander('Employee Details'):
                st.write('employee name')
                st.write('employee ID')
                st.write('employee mail') 
                st.write('employee ph-no')
                st.write('P Hike')
                st.write('P rating')
                st.write('C rating')
                st.write('Manager Note')
        approve = '<p style="font-family:Roboto; color:green; font-size: 20px;">Approved</p>'
        reject = '<p style="font-family:Roboto; color:red; font-size: 20px;">Rejected</p>'
        # st.markdown('status:-'+ approve, unsafe_allow_html=True)
        st.markdown('status:-'+ reject, unsafe_allow_html=True)
        # st.write('current Status')
        choice = st.radio("choose your option",('Approve', 'reject'))
        #set default to the chosen option
        if st.button('Save'):
            st.success('changes saved')
    with tab2:
        st.write('##')
        with st.expander('View status of all employees'):
            st.write('show employees_name,Id,mngr_id,status in DF')
        st.write('##')

        st.subheader('Finalize approval process')
        #display warning message on unconfirmed employees 
        st.warning('Appraisal process for this quarter will be completed once the button is clicked')
        st.button('Finalize')

        


    



#have to add check status feature
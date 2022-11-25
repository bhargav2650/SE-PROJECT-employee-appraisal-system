import streamlit as st
import datetime
# from app import LogOut_Clicked
# from helper import get_form_responces
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def M_UI():
    # st.write('logged in as manager'
    col1, col2 = st.columns([12,1])
    with col2:
        dummy = st.button("LogOut")
        if dummy:
            # LogOut_Clicked()
            st.session_state['loggedIn']=False
    st.write('##')
    st.info('logged in as Manager')
    st.write('##')
    # dummy = st.button("LogOut")   
    value = st.selectbox(f'select employee to view',['a','b'])
    tab1, tab2, tab3 = st.tabs(["View Details", "Review", "Schedule Meeting"])
    c1,c2,c3 = st.columns(3)
    with tab1:
        
        with st.expander('Employee Details'):
            st.write('name')
            st.write('ID')
            st.write('mailID')
            st.write('ph-no')

        with st.expander('Form responses'):
            st.write('Number of Tasks assigned')
            st.write('Number of Tasks completed')
            st.write('Number of Hours saved')
            st.write('Number of Defects found')
            st.write('Number of Defects fixed')
        with st.expander('Additional Acomplishments'):
            st.write(' Large text ')
        
                

    with tab2:
        st.write('Employee_id')
        st.write('Employee_name')
        M_tasks_A = st.number_input('Number of tasks assigned',min_value=0)
        M_tasks_C = st.number_input('Number of tasks completed',min_value=0)
        M_hours= st.number_input('Number of hours saved',min_value=0)
        M_defects_F  = st.number_input('Number of defects found',min_value=0)
        M_defects_Fix = st.number_input('number of defects fixed',min_value=0)
        age = st.slider('Effectiveness in work', 0, 10, 5)
        age = st.slider('Integrity', 0, 10, 5)
        age = st.slider('Accountability', 0, 10, 5)
        age = st.slider('Quality of work', 0, 10, 5)
        age = st.slider('Time management', 0, 10, 5)
        acc = st.text_area('Additional NOTE')
        
         
    with tab3:
        c1,c2,c3 = st.columns(3)
        with c2:
            d = st.date_input("select a date to schedule the meeting",datetime.date(2019, 7, 6))
            t = st.time_input('Set start time', datetime.time(8, 45))
            st.button('schedule')   
        # with c2 :
        #      center_button = st.button('Button')
    # st.write('---')
    # st.write('')
    # resp = get_form_responces()
    # st.write(resp)
   
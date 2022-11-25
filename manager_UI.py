import streamlit as st
import datetime
from helper import get_form_responces
from helper import send_mail
from database import get_mail
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def M_UI():
    # st.write('logged in as manager'
    col1, col2 = st.columns([12,1])
    with col2:
         dummy = st.button("LogOut")    
    st.write('##')
    st.info('logged in as Manager')
    st.write('##')
    # dummy = st.button("LogOut")   
    value = st.selectbox(f'select employee to Review',['a','b'])
    tab1, tab2, tab3 , tab4,tab5,tab6 = st.tabs(["View Details", "Review", "Schedule Meeting","Check Status","calculate score","ShortList"])
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
        if st.button('Submit'):
            #if successful 
            st.success('Review of employee successfully completed')
        
         
    with tab3:
        c1,c2,c3 = st.columns(3)
        with c2:
            d = st.date_input("select a date to schedule the meeting",datetime.date(2019, 7, 6))
            t = st.time_input('Set start time', datetime.time(8, 45))
            link = st.text_input('Enter meeting Link')
            if st.button('schedule'):
                e_mail = get_mail(value)
                m_mail = get_mail(value)

    
    with tab4:
        st.write('##')
        with st.expander('Employees'):
            st.write('show employees_name,id,m_status in DF')
            #query to display number of pending employees
    
    with tab5:
        st.write('##')
        with st.expander('Pending Review'):
            st.write("Displays DF with Employees who's review is pending ID,name,status")
        #if they are pending employees then give a warning 
        st.write('##')
        st.info('Please ensure that all the Employees are reviewed ')
        st.write('##')  
        st.subheader("Calculate Rating Of All Reviewed Employees")
        trig = 0
        if st.button('Calculate'):
            with st.expander('Employees rating'):
                st.write('Displays Ename,ID,rating in ascending order')
        with tab6:
            st.write('##')  
            new_title = '<p style="font-family:Roboto; color:white; font-size: 20px;">Choose an option to select Employees</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            choice = st.radio('',('Based on TOP-N rated Employees', 'Based on Rating-Cutoff'))
            if choice == 'Based on TOP-N rated Employees':
                #handle max_val case
                num = st.number_input('Number of Employees to be selected',min_value=0)     
                with st.expander("Selected Employees"):
                    st.write("Display DF with top k rating E selected ")
                if st.button("Approve"):
                    #implement reconfirmation
                    st.success('Approve successful')
            else:
                num = st.number_input('Enter cutoff Rating',min_value=0)
                with st.expander("Selected Employees"):
                    st.write("Display DF with top k rating E selected ")
                if st.button("Approve"):
                    #implement reconfirmation
                    st.success('Approve successful')




        # with c2 :
        #      center_button = st.button('Button')
    # st.write('---')
    # st.write('')
    # resp = get_form_responces()
    # st.write(resp)
   
import streamlit as st
from database import *
import time
from helper import *

def E_UI():
    col1, col2 = st.columns([3.5,1])
    with col2:
            dummy = st.button("LogOut")
            if dummy :
                st.session_state['loggedIn']=False
    if st.session_state['E_UI']:
        # col1, col2 = st.columns([3.5,1])
        # with col2:
        #         dummy = st.button("LogOut")
        #         if dummy :
        #             st.session_state['loggedIn']=False
        c1,c2,c3=st.columns([2,10,2])
        with c2:
            st.write('##')
            st.info('logged in as Employee')
            st.write('##')
        
            
            E_id = st.session_state['user_id']
            st.write(f"Employee ID : {E_id}")
                # st.write("fetch and display corresponding ename")
            name = get_name_e(E_id)
            m = get_m_status(E_id)
            # st.write(m)
            print(m)
            st.write('Welcome',name)
            try:
                if m[0][2] == 1:
                    st.info('You have already submitted the form')
                    with st.expander('Form responses'):
                            
                            resp = get_emp_resp_details(E_id)
                            [n_task_assn,n_task_comp,n_hour_saved,n_defect_found,n_defect_fixed,accomp]=resp
                            st.write(f'Number of Tasks assigned   \t:{n_task_assn}')
                            st.write(f'Number of Tasks completed  \t:{n_task_comp}')
                            st.write(f'Number of Hours saved      \t:{n_hour_saved}')
                            st.write(f'Number of Defects found    \t:{n_defect_found}')
                            st.write(f'Number of Defects fixed    \t:{n_defect_fixed}')
                            st.write(f'{accomp}')
            except:
                with st.form('E_details'):
                    tasks_C = st.number_input('Number of tasks completed',min_value=1)
                    # st.write(tasks_C)
                    tasks_A = st.number_input('Number of tasks assigned',min_value=1)
                    hours= st.number_input('Number of hours saved',min_value=1, max_value=480)
                    efects_Fix = st.number_input('number of defects fixed',min_value=1)
                    defects_F  = st.number_input('Number of defects found',min_value=1)
                    acc = st.text_area('Additional Accomplishments')
                    bt = st.form_submit_button('submit')
                    if E_id and tasks_A>1 and tasks_C and tasks_A>=tasks_C and hours and defects_F and efects_Fix and defects_F>=efects_Fix:
                        i=1
                        if bt:
                    # st.session_state['loggedIn']=False
                            execute_cmd(f"Insert into emp_resp values('{name}',\"{E_id}\",{tasks_A},{tasks_C},{hours},{defects_F},{efects_Fix},\"{acc}\",{i});")
                            execute_cmd(f"update employee set submitted=1 where eid = '{E_id}'")
                            st.success("Successfully submitted your form.Please wait for our response")
                            send_mail('Regarding Appraisal','Your responce has been successfully recorded , you can review the responce on the portal',get_mailid(E_id))
                            
                            time.sleep(1)
                            st.experimental_rerun()
                            return 1
                    else:
                        if bt: 
                            st.info("Please provide appropriate values")
                            # st.experimental_rerun()
                            bt =0
                            
                            # return 0
            return 0
    
    else:
        colu1, colu2 ,colu3= st.columns([1,5,1])
        with colu2:
            st.info('Appraisal portal is currently not open')
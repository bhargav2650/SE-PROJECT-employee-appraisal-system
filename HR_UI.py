import streamlit as st
from database import *
import pandas as pd
import time 
from helper import * 
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def H_UI():
    
    col1, col2 = st.columns([12,1])
    with col2:
         if st.button("LogOut") :
             st.session_state['loggedIn']=False
    if st.session_state['HR_UI']:
        st.write('##')   
        st.info('logged in as HR')  
        st.write('##')
        hr_id = st.session_state['user_id']
        hsubmit = get_hr_submit(hr_id)
        if hsubmit == 0:
            tab1, tab2 = st.tabs(["Approve Employees", "Check status of Employees"])
            with tab1:
                st.session_state['value_mgr'] = st.selectbox(f'select Manager',get_mgr_Ids())
                # st.write('#')
                with st.expander('Manager Details'):
                        [m_name,m_id,mgr_mail_id,mgr_ph_no]=get_mgr_details(st.session_state['value_mgr'])
                        st.write(f'name    :-{m_name}')
                        st.write(f'ID      :-{m_id}')
                        st.write(f'mailID  :-{mgr_mail_id}')
                        st.write(f'ph-no   :-{mgr_ph_no}')
                
                
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
                try:
                    st.session_state['shortlisted_emp_value'] = st.selectbox(f'select Employee',get_shortlisted_emp_Id(st.session_state['value_mgr']))
                    emp_id = st.session_state['shortlisted_emp_value']
                    
                    with st.expander('Employee Details'):
                            [e_name,eid,emp_mail_id,emp_ph_no,prev_hike_date,prev_rating ,curr_rating]=get_shortlisted_emp_details(st.session_state['shortlisted_emp_value'])
                            #[mgr_resp_note]=get_manager_note(st.session_state['shortlisted_emp_value'])
                            st.write(f'employee name :{e_name}')
                            st.write(f'employee ID :{eid}')
                            st.write(f'employee mail :{emp_mail_id}') 
                            st.write(f'employee ph-no :{emp_ph_no}')
                            st.write(f'P Hike :{prev_hike_date}')
                            st.write(f'P rating :{prev_rating}')
                            st.write(f'C rating :{curr_rating}')
                            #st.write(f'Manager Note :{mgr_resp_note}')
                    get_hstat = get_h_status(emp_id)
                    approve = '<p style="font-family:Roboto; color:green; font-size: 20px;">Approved</p>'
                    reject = '<p style="font-family:Roboto; color:red; font-size: 20px;">Rejected</p>'
                    pending = '<p style="font-family:Roboto; color:orange; font-size: 20px;">Pending</p>'
                    # st.markdown('status:-'+ approve, unsafe_allow_html=True)
                    a =0
                    if get_hstat == 'Pending':
                        st.markdown('status:-'+ pending, unsafe_allow_html=True)
                    elif get_hstat == 'Approved':
                        st.markdown('status:-'+ approve, unsafe_allow_html=True)
                        a = 0
                    else :
                        st.markdown('status:-'+ reject, unsafe_allow_html=True)
                        a =1
                    # st.write('current Status')
                    st.session_state['hr_choice'] = st.radio("choose your option",('Approve', 'Reject'),index=a)
                    #set default to the chosen option
                    if st.button('Save'):
                        #st.experimental_rerun()
                        set_hr_status(st.session_state['hr_choice'],st.session_state['shortlisted_emp_value'])
                        st.success("Successfully submitted your response")
                        time.sleep(1)
                        st.experimental_rerun()
                except Exception as e:
                    st.write("No employees have been shortlisted")
                    # st.error(e)

            with tab2:
                st.write('##')
                with st.expander('View status of all employees'):
                    # st.write('show employees_name,Id,mngr_id,status in DF')
                    data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,manager_id,h_status from employee where m_status = 'Approved'"),columns=['Employee name','ID','manager ID','status'])
                    if len(data)==0:
                        st.write("No employees have been approved")
                    else:
                        st.write(data)
                st.write('##')

                st.subheader('Finalize approval process')
                #display warning message on unconfirmed employees 
                st.warning('Appraisal process for this quarter will be completed once the button is clicked')
                if st.button('Finalize'):
                    set_hr_submit(hr_id)
                    st.success('Appraisal process completed')
                    send_mail('Regarding Appraisal process','Your responce has been recorded,To view all the employees selected log into portal',get_mailid(hr_id))
                    time.sleep(1)
                    d = get_all_employee()
                    for i in d:
                        if i[1] == 'Approved':
                            send_mail("Regarding appraisal process","Congratulations , you were approved by HR and  eliglible for this quarter appraisal",get_mailid(i[0]))
                        elif i[1] == 'Rejected':
                            send_mail("Regarding appraisal process",f"Keep trying hard,Better luck next time , your application was not approved by HR",get_mailid(i[0]))
                        else:
                            send_mail("Regarding appraisal process",f"Keep trying hard,Better luck next time , your application was not approved by HR",get_mailid(i[0]))
                    st.experimental_rerun()
                    # with st.expander('View status of all employees'):
                    #     data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,manager_id,h_status from employee where h_status = 'Approved'"))
                    #     if len(data)==0:
                    #         st.write("No employees have been approved")
                    #     else:
                    #         st.write(data)

        else:
            st.info('Appraisal process has been successfully complected')  
            with st.expander('View status of all employees'):
                        data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,manager_id,h_status from employee where m_status = 'Approved'"),columns=['name','ID','Manager ID','Status'])
                        if len(data)==0:
                            st.write("No employees have been approved")
                        else:
                            st.write(data) 

    else:
        st.info('Appraisal portal is currently not open')


    



#have to add check status feature
    



#have to add check status feature
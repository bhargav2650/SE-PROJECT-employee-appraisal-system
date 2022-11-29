import streamlit as st
import datetime
from database import *
import pandas as pd
from helper import calculate_score,send_mail
from database import get_mailid,select_rating,select_topN,set_submit,get_submit
import time
# from helper import get_form_responces
# st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def M_UI():
    # st.write('logged in as manager'
    flag=0
    col1, col2 = st.columns([12,1])
    with col2:
         if st.button("LogOut"):
             st.session_state['loggedIn']=False
    if st.session_state['MGR_UI']:
        st.write('##')
        st.info('logged in as Manager')
        st.write('##')
        mgr_id = st.session_state['user_id']
        # c , col ,d =st.columns[1,3,1]
        st.title(f"Welcome _{get_name_m(mgr_id)}_.")
        # dummy = st.button("LogOut")
        mgr_submit=get_submit(mgr_id)
        if mgr_submit == 0:
            st.session_state['emp_value'] = st.selectbox(f'select employee to view',show_employees(mgr_id))
            emp_id = st.session_state['emp_value']
            tab1, tab2, tab3 , tab4,tab5,tab6 = st.tabs(["View Details", "Schedule Meeting","Review","Check Status","calculate score","ShortList"])
            c1,c2,c3 = st.columns(3)
            with tab1:
                with st.expander('Employee Details'):
                    [e_name,e_id,mail_id,ph_no]=get_emp_details(st.session_state['emp_value'])
                    
                    st.write(f'Name of the Employee \t: {e_name}')
                    # st.write('Name of the Employee :'str(e_name))
                    st.write(f'Company ID of the Employee \t: {e_id}')
                    st.write(f'Email ID of the Employee \t: {mail_id}')
                    st.write(f'Contact number of the Employee \t: {ph_no}')
                try:
                    [n_task_assn,n_task_comp,n_hour_saved,n_defect_found,n_defect_fixed,accomp]=get_emp_resp_details(st.session_state['emp_value'])
                    with st.expander('Form responses'):
                    
                        st.write(f'Number of Tasks assigned   \t:{n_task_assn}')
                        st.write(f'Number of Tasks completed  \t:{n_task_comp}')
                        st.write(f'Number of Hours saved      \t:{n_hour_saved}')
                        st.write(f'Number of Defects found    \t:{n_defect_found}')
                        st.write(f'Number of Defects fixed    \t:{n_defect_fixed}')
                    with st.expander('Additional Acomplishments:'):
                        st.write(f'{accomp}')
                except:
                    st.info("Employee has failed to submit the form") 

            with tab2:
                c1,c2,c3 = st.columns(3)
                with c2:
                    d = st.date_input("select a date to schedule the meeting",datetime.date(2019, 7, 6))
                    t = st.time_input('Set start time', datetime.time(8, 45))
                    link = st.text_input('Enter meeting Link')
                    if st.button('schedule'):
                        emp_mail = get_mailid(emp_id)
                        mgr_mail = get_mailid(mgr_id)
                        #this mail is regarding the meeting , include link,date,time 
                        name = get_name_m(mgr_id)
                        name_e = get_name_e(e_id)
                        send_mail('Regarding appraisal review meeting',f"Dear employee,\n\nI,{name} have scheduled a meeting to discuss your review regarding the form you have submitted for appraisal on {d} at {t}.\n.Join the meeting link provided below for the same.\n\n{link}",emp_mail) 
                        send_mail('Regarding appraisal review meeting',f'Dear manager,\n\n You have scheduled a meeting with {name_e} for further discussion on his appraisal review on {d} at {t}.Join the below meeting link for the same\n{link}',mgr_mail) 
                        st.success('Meeting scheduled')
                            

            with tab3:
                # data=pd.DataFrame(execute_cmd2(f"Select * from m_resp where emp_id='{st.session_state['emp_value']}'"))
                # st.write(data)
                print(show_employees2(mgr_id,st.session_state["emp_value"]))
                if show_employees2(mgr_id,st.session_state["emp_value"])==0:
                    flag=0
                else:
                    flag=1
                if pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status from employee where eid='{st.session_state['emp_value']}'"), columns=['Name', 'ID', 'Manager status']).at[0,'Manager status']=="Pending" and flag:
                    st.write(f'Employee ID selected: {st.session_state["emp_value"]}')
                    st.write(f'Employee name: {get_name_e(st.session_state["emp_value"])}')
                    E_id = st.session_state['emp_value']
                    M_tasks_C = st.number_input('Number of tasks completed',min_value=1)
                    M_tasks_A = st.number_input('Number of tasks assigned',min_value=M_tasks_C)
                    M_hours= st.number_input('Number of hours saved',min_value=1, max_value=480)
                    M_defects_Fix = st.number_input('number of defects fixed',min_value=1)
                    M_defects_F  = st.number_input('Number of defects found',min_value=M_defects_Fix)
                    age1 = st.slider('Effectiveness in work', 0, 10, 5)
                    age2 = st.slider('Integrity', 0, 10, 5)
                    age3 = st.slider('Accountability', 0, 10, 5)
                    age4 = st.slider('Quality of work', 0, 10, 5)
                    age5 = st.slider('Time management', 0, 10, 5)
                    acc = st.text_area('Additional NOTE', value="")
                elif flag:
                    data=pd.DataFrame(execute_cmd2(f"Select * from m_resp where emp_id='{st.session_state['emp_value']}'"))
                    st.write(f'Employee ID selected: {st.session_state["emp_value"]}')
                    st.write(f'Employee name: {get_name_e(st.session_state["emp_value"])}')
                    E_id = st.session_state['emp_value']
                    M_tasks_C = st.number_input('Number of tasks completed',value=data.at[0,3],min_value=1)
                    try:
                        M_tasks_A = st.number_input('Number of tasks assigned',value=data.at[0,2],min_value=M_tasks_C)
                    except:
                        M_tasks_A = st.number_input('Number of tasks assigned',min_value=M_tasks_C)
                    M_hours= st.number_input('Number of hours saved',min_value=1, value=data.at[0,4] ,max_value=480)
                    M_defects_Fix = st.number_input('number of defects fixed',min_value=1, value=data.at[0,6])
                    try:
                        M_defects_F  = st.number_input('Number of defects found',min_value=M_defects_Fix, value=data.at[0,5])
                    except:
                        M_defects_F  = st.number_input('Number of defects found',min_value=M_defects_Fix)
                    age1 = st.slider('Effectiveness in work', 0, 10, value=int(data.at[0,7]))
                    age2 = st.slider('Integrity', 0, 10, value=int(data.at[0,8]))
                    age3 = st.slider('Accountability', 0, 10, value=int(data.at[0,10]))
                    age4 = st.slider('Quality of work', 0, 10, value=int(data.at[0,11]))
                    age5 = st.slider('Time management', 0, 10, value=int(data.at[0,12]))
                    acc = st.text_area('Additional NOTE', value=data.at[0,13])
                else:
                    st.info("Employee has failed to submit the form")
                if flag:
                    bt = st.button('Submit')
                if flag and (M_tasks_A>=0) and (M_tasks_C>=0) and (M_hours>=0) and (M_defects_F>=0) and (M_defects_Fix>=0) and (age1>=0) and (age2>=0) and (age3>=0) and (age4>=0) and (age5>=0) :
                    if bt:
                    #if successful
                        # if acc == '':

                        # print("HI")
                        variable=st.session_state["emp_value"]
                        # st.write(variable)
                        # st.write("Insert into m_resp values("+mgr_id+","+get_name_m(mgr_id)+","+str(M_tasks_A)+","+str(M_tasks_C)+","+str(M_hours)+","+str(M_defects_F)+","+str(M_defects_Fix)+","+str(age1)+","+str(age2)+","+E_id+","+str(age3)+","+str(age4)+","+str(age5)+","+acc+");")
                        if pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status from employee where eid='{E_id}'"), columns=['Name', 'ID', 'Manager status']).at[0,'Manager status']=="Pending" :
                            execute_cmd(f"Insert into m_resp values('{mgr_id}','{get_name_m(mgr_id)}',{M_tasks_A},{M_tasks_C},{M_hours},{M_defects_F},{M_defects_Fix},{age1},{age2},'{E_id}',{age3},{age4},{age5},'{acc}');")
                        else:
                            execute_cmd(f"Delete from m_resp where emp_id='{E_id}'")
                            execute_cmd(f"Insert into m_resp values('{mgr_id}','{get_name_m(mgr_id)}',{M_tasks_A},{M_tasks_C},{M_hours},{M_defects_F},{M_defects_Fix},{age1},{age2},'{E_id}',{age3},{age4},{age5},'{acc}');")
                        score=calculate_score([M_tasks_A, M_tasks_C, M_hours, M_defects_F,M_defects_Fix, age1,age2, age3, age4, age5])
                        # st.write(score)
                        execute_cmd(f"Update employee set curr_rating='{score}' where eid='{variable}'")
                        # execute_cmd("Insert into m_resp values("+mgr_id+","+get_name_m(mgr_id)+","+str(M_tasks_A)+","+str(M_tasks_C)+","+str(M_hours)+","+str(M_defects_F)+","+str(M_defects_Fix)+","+str(age1)+","+str(age2)+","+E_id+","+str(age3)+","+str(age4)+","+str(age5)+","+acc+");")
                        execute_cmd(f"Update employee set m_status='Reviewed' where eid='{variable}'")
                        st.success("Successfully received your response")
        
            
            with tab4:
                st.write('##')
                with st.expander('Employees'):
                    # st.write('show employees_name,id,m_status in DF')
                    data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status from employee where submitted=1 and manager_id = '{mgr_id}'"), columns=['Name', 'ID', 'Manager status'])
                    st.write(data)
                    #query to display number of pending employees
            
            with tab5:
                st.write('##')
                with st.expander('Pending Review'):
                    # st.write("Displays DF with Employees who's review is pending ID,name,status")
                    data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status from employee where m_status='Pending'and submitted=1 and manager_id = '{mgr_id}'"), columns=['Name', 'ID', 'Manager status'])
                    st.write(data)
                #if they are pending employees then give a warning 
                st.write('##')
                st.info('Please ensure that all the Employees are reviewed ')
                st.write('##')  
                st.subheader("Calculate Rating Of All Reviewed Employees")
                trig = 0
                if st.button('Calculate'):
                    with st.expander('Employees rating'):
                        data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status, curr_rating from employee where m_status='Reviewed'and submitted=1 and  manager_id = '{mgr_id}' "), columns=['Name', 'ID', 'Manager status','Rating'])
                        st.write(data.sort_values(by="Rating",ascending=False))
                        # st.write('Displays Ename,ID,rating in ascending order')
            with tab6:
                        st.write('##')  
                        new_title = '<p style="font-family:Roboto; color:white; font-size: 20px;">Choose an option to select Employees</p>'
                        st.markdown(new_title, unsafe_allow_html=True)
                        choice = st.radio('',('Based on TOP-N rated Employees', 'Based on Rating-Cutoff'))
                        if choice == 'Based on TOP-N rated Employees':
                            #handle max_val case
                            num = st.number_input('Number of Employees to be selected',min_value=0)     
                            with st.expander("Selected Employees"):
                                q_data = select_topN(num,mgr_id)
                                if q_data != 0:
                                    data1=pd.DataFrame(q_data, columns=['Name', 'ID', 'score','status'])    
                                    st.dataframe(data1)
                                else:
                                    st.write('No employee are selected')
                                # st.write("Display DF with top k rating E selected ")

                                #can add change option also 
                            st.warning('Once approved the data will be permanently stored') 

                            if st.button("Approve"):
                                #implement reconfirmation
                                set_submit(mgr_id,'r',num)
                                time.sleep(1)
                                st.success('Approve successful')
                                send_mail('regarding appraisal process','You have successfully completed appraisal process,To view selected employees please log in into the portal',get_mailid(mgr_id))
                                time.sleep(1)
                                #send mail to all employees selected , inform their status along with socres
                                d = get_employee(mgr_id)
                                #send mail to all employees selected , inform their status along with scores
                                # for i in range(len(d)):
                                #     if d[i]['m_status'] == 'Approved':
                                #         send_mail("Regarding appraisal process",f"Your request for appraisal has been approved.It is going to be reviewed by HR.Your current score is {d[i]['score']}.\n Wait for the response",get_mailid(q_data[i]['ID']))
                                #     if d[i]['m_status'] == 'Rejected':
                                #         send_mail("Regarding appraisal process",f"Your request for appraisal has been denied since the limit for employees selected is met.\nYour current score is {d[i]['score']}.Better luck next time",get_mailid(q_data[i]['ID']))
                                for i in d:
                                    if i[1] == 'Approved':
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been approved.It is going to be reviewed by HR.Your current score is {i[2]}.\n Wait for the response",get_mailid(i[0]))
                                    elif i[1] == 'Rejected':
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been denied since the limit for employees selected is met.\nYour current score is {i[2]}.Better luck next time",get_mailid(i[0]))
                                    else:
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been denied since the limit for employees selected is met.\nYour current score is {i[2]}.Better luck next time",get_mailid(i[0]))

                                st.experimental_rerun()
                        else:
                            num = st.number_input('Enter cutoff Rating',min_value=0)
                            with st.expander("Selected Employees"):
                                q_data = select_rating(num,mgr_id)
                                if q_data != 0:
                                    data1=pd.DataFrame(q_data, columns=['Name', 'ID', 'score','status'])
                                    st.dataframe(data1)
                                else:
                                    st.write('No employee are selected')
                            st.warning('Once approved the data will be permanently stored')
                            if st.button("Approve"):
                                #implement reconfirmation
                                set_submit(mgr_id,'r',num)
                                time.sleep(1)
                                st.success('Approve successful')
                                send_mail('regarding appraisal process','You have successfully completed appraisal process,To view selected employees please log in into the portal',get_mailid(mgr_id))
                                time.sleep(1)
                                #send mail to all employees selected , inform their status along with socres
                                d = get_employee(mgr_id)
                                for i in d:
                                    if i[1] == 'Approved':
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been approved.It is going to be reviewed by HR.Your current score is {i[2]}.\n Wait for the response",get_mailid(i[0]))
                                    elif i[1] == 'Rejected':
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been denied since the limit for employees selected is met.\nYour current score is {i[2]}.Better luck next time",get_mailid(i[0]))
                                    else:
                                        send_mail("Regarding appraisal process",f"Your request for appraisal has been denied since the limit for employees selected is met.\nYour current score is {i[2]}.Better luck next time",get_mailid(i[0]))

                                st.experimental_rerun()
                                # send_mail()
                                # st.experimental_rerun()
                        # if st.button('select'):
                        #     with st.expander("Selected Employees"):
                        #         st.write("Display DF with top k rating E selected ")
                        #     if st.button("Approve"):
                        #      #implement reconfirmation
                        #     st.success('Approve successful')
        else:
            st.info('You have already approved')
            with st.expander('employee status'):
                
                # st.write('display emp_id,emp_name,m_status of all employees where submitted = 1 and under that manager ID')
                data=pd.DataFrame(execute_cmd2(f"Select e_name,eid,m_status from employee where submitted = 1 and manager_id = '{mgr_id}'"),columns=['name','ID','Status'])
                if len(data)==0:
                        st.write("No employees have been approved")
                else:
                        st.write(data)
    else:
        # colu1, colu2 ,colu3= st.columns([1,8,1])
        # with colu2:
        st.info('Appraisal portal is currently not open')




        # with c2 :
        #      center_button = st.button('Button')
    # st.write('---')
    # st.write('')
    # resp = get_form_responces()
    # st.write(resp)
   
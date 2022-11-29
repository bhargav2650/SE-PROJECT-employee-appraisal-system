import streamlit as st
from manager_UI import M_UI
from HR_UI import H_UI
from Employee_UI import *
from database import *
from database import auth,get_list,get_eligible_emp
from datetime import date
from helper import send_mail
# from database import Authenticate
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

c1, c2,c3,c4,c5 = st.columns(5)
f1,f2,f3 = st.columns(3)  
def login_clicked(user_id,password):
        p,role = auth(user_id,password)
        if p==1:
            st.session_state['loggedIn']=True
            st.session_state['role'] = role
            st.session_state['user_id'] = user_id
            # st.write(role)
            # elif n==2:
            #     st.session_state['loggedIn'] = True
            #     st.session_state.runpage = H_UI
            #     st.session_state.runpage()
            #     st.experimental_rerun()
        
            # else:
            #     st.session_state['loggedIn'] =False
            #     st.error("Invalid User")
  
def show_login_page():
    if st.session_state['loggedIn']==False:
        with f2: 
            with st.form('login'):
                    user_id=st.text_input(label="",value="",placeholder="User ID").strip().upper()
                    password=st.text_input(label="",value="",placeholder="Password",type="password").strip().lower()
                    # st.form_submit_button('login',on_click=login_clicked,args=(user_id,password))
                    button=st.form_submit_button("Login")
                    if button:
                        login_clicked(user_id,password)






# def show_logout_page():
#     st.button("LogOut",on_click=LogOut_Clicked)

# def LogOut_Clicked():
#     st.session_state['loggedIn']=False
st.session_state['E_UI']=1
st.session_state['MGR_UI']=1
st.session_state['HR_UI']=1
current_date = date.today()
if current_date.month in [3,6,9,12,11] :##########
    #15-17 emp , 18-24 mgr , 25-30/31 h
    if current_date.day ==14:
        database_reset()
    if current_date.day in [i for i in range(15,18)]:
        st.session_state['E_UI']=1
    if current_date.day in [i for i in range(18,25)]:
        st.session_state['MGR_UI']=1
    if current_date.day in [i for i in range(25,32)]:
        st.session_state['HR_UI']=1
    if current_date.day == 16:
        emp_list = get_eligible_emp()
        for i in emp_list:
            emp_submit = get_emp_submit(i)
            if emp_submit == 0:
                send_mail('Regarding appraisal','Please fill the form on portal ,Form will be closing on 17th',get_mailid(i))

    if current_date.day == 23:
        mgr_list = get_list('MGR')
        for i in mgr_list:
            mgr_submit = get_submit(i)
            if mgr_submit == 0:
                send_mail('Regarding appraisal','You havent completed appraisal process,kindly log into portal and complete the review ,portal will be closing on 24th',get_mailid(i))

    if current_date.day == 29:
            hr_submit = get_hr_submit('HR_1')
            if hr_submit == 0:
                send_mail('Regarding appraisal','You havent completed appraisal process,kindly log into portal and complete the review ,portal will be closing on 30th',get_mailid('HR_1'))
    # hr,manager shd view all the eployees that were selected in previous quarter after the process ....anyhow its still there in db
    
    if current_date.day == 25:
        #if manager doesent fill
            mgr_list = get_list('MGR')
            res = []
            for i in mgr_list:
                mgr_submit = get_submit(i)
                if mgr_submit == 0:
                    res.append(i)
            send_mail('Regarding appraisal',f' {res} \n Above mentioned managers have failed to fill their review.',get_mailid('HR_1'))
    if current_date.day == 15 :#######
        emp_list = get_eligible_emp()
        #reminders
        
        #manager doest fill case maybe mail to hr
        #moniter option for hr
        #success msg after all buttons
        for i in emp_list:
            #add attachment
            #add body and proper subject ...this is for start of appraisal process
            send_mail('Regarding appraisal','The appraisal process has been started , kindly log into portal and fill the form before 17th of this month',get_mailid(i))
        #this is for hr to let him know that appraisal has started
        send_mail('Regarding appraisal','Appraisal process for this quarter has begun',get_mailid('HR_1'))

    if current_date.day == 28:##########3333333
        mgr_list = get_list('MGR')#try to merge it one function
        for i in mgr_list:
            #add attachment
            #add body and proper subject ...this is for start of appraisal process
            # managers gets to know that he has to review emp , include deadline in all cases
            send_mail('regrarding appraisal','Appraisal process for this quarter has begun , kindly login to portal and review all the employees within 25th',get_mailid(i),'661_660_654_637__SE PROJECT REPORT.pdf')
    if current_date.day == 25:######
        hr_list = get_list('HR')
        #to inform that he has to approve , alog with deadline
        send_mail('Regarding appraisal','Employees are waiting your approval , kindly log into portal and do the needful withing 30th',get_mailid('HR_1'))

    
    
    
# filter out non responded employees while sending it to manager
with c3:
    st.header("APPRAISER")
if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn']=False
    show_login_page()
else:
    if st.session_state['loggedIn']:
        a = st.session_state['role']
        # a=1
        if a == 1 :
            M_UI()
            # show_logout_page()
        elif a==2:
            H_UI()
            # show_logout_page()
        elif a==3:
            i = E_UI()
            # show_login_page()
            if i ==1:
                st.session_state['loggedIn'] = False
                st.experimental_rerun()
    else:
        show_login_page()


    
    

    




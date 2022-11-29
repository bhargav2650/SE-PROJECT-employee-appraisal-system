import mysql.connector
import streamlit as st
from datetime import date
import pandas as pd
import datetime
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chinmay@17",
    database="se_project"
)
c = mydb.cursor()

def auth(u_id,password):
    # print(u_id)
    c.execute(f"select * from auth where user_id = '{u_id}'")
    res = c.fetchall()
    if res == []:
        st.warning("Check your user id and password")
        return 0,None
    else :
        if password == res[0][1]:
            #correct auth
            return 1,res[0][2]
        else :
            st.warning("Invalid Password!")
            return 0,None
        

def get_eligible_emp():
    c.execute('select eid,join_date from employee')
    res = c.fetchall()
    # print(res)
    # current_time = datetime.datetime.now()
    current_date = datetime.date.today()
    selected_emp = []
    for i in res:
        if (current_date-i[1]).days>75:
            selected_emp.append(i[0])
    # print((res[0][1]-current_date).days)
    # print(selected_emp)
    return selected_emp
def auth1(u_id,password):
    # print(u_id)
    c.execute(f"select * from auth where user_id = '{u_id}'")
    res = c.fetchall()
    if res == []:
        # st.info("Check your user id and password")
        return 0
    else :
        if password == res[0][1]:
            #correct auth
            return 1
        else :
            # st.info("Invalid Password!")
            return 0
        
def execute_cmd(str1):
    try:
        c.execute(str1)
        mydb.commit()
    except Exception as e:
        st.info(e)
        st.error("Entered information is incomplete!Please fill all the fields since they are important")
        
def get_name_e(eid):
    c.execute(f"select e_name from employee where eid='{eid}'")
    res = c.fetchall()
    return res[0][0]
    
def get_name_e1(eid):
    c.execute(f"select e_name from employee where eid='{eid}'")
    res = c.fetchall()
    if res == []:
        return None
    return res[0][0]
    
def get_employee(mgr_id):
    c.execute(f"select eid,m_status,curr_rating,h_status from employee where manager_id = '{mgr_id}'")
    d= c.fetchall()
    return d

def get_name_m(mid):
    c.execute(f"select m_name from manager where m_id='{mid}'")
    try :
        res = c.fetchall()
        return res[0][0]
    except Exception as e:
        print(res)
        print(e)

def get_first_column(res):
    arr=[]
    for i in range(len(res)):
        arr.append(res[i][0])
    
    return arr
def show_employees(m_id):
    # print(u_id)
    
    c.execute(f"select eid from employee where manager_id = '{m_id}' ")
    res = c.fetchall()
    res=get_first_column(res)
    
    return res
def show_employees2(m_id, e_id):
    c.execute(f"select submitted from employee where manager_id = '{m_id}' and eid='{e_id}'")
    res = c.fetchall()
    
    return res[0][0]

def get_auth(e_id):
    # print(u_id)
  
    c.execute(f"select e_name,eid,mail_id,ph_no from employee where eid = '{e_id}'")
    res = c.fetchall()
    
    return res[0]

def get_mgr_Ids():
    c.execute(f"select m_id from manager")
    res = c.fetchall()
    res=get_first_column(res)

    return res

def get_mgr_details(m_id):
    c.execute(f"select m_name,m_id,mail_id,ph_no from manager where m_id = '{m_id}'")
    res = c.fetchall()
    
    return res[0]

def get_emp_details(e_id):
    c.execute(f"select e_name,eid,mail_id,ph_no from employee where eid = '{e_id}'")
    res = c.fetchall()
    
    return res[0]

def get_m_status(eid):
    c.execute(f"select e_name,eid,m_status from emp_resp where eid='{eid}'")
    res = c.fetchall()
    return res

def execute_cmd2(string):
    try:
        c.execute(string)
        res = c.fetchall()
        res = pd.DataFrame(res,columns=['Employee Name',"Employee ID","Manager ID","HR status"])
        return res
    except Exception as e:
        st.info(e)
        st.error("Entered information is incomplete!Please fill all the fields since they are important")

def get_emp_resp_details(e_id):
    # print(u_id)
    try :
        c.execute(f"select no_of_task_assigned,no_of_task_completed,no_of_hrs_saved,no_of_defects_found,no_of_defects_fixed,additional_accomplishments from emp_resp where eid = '{e_id}'")
        res = c.fetchall()
    
        return res[0]
    except Exception as e: 
        return 0



def is_in_mresp(e_id):
    c.execute(f"select * from m_resp where eid='{e_id}'")
    a= c.fetchall()
    if a == []:
        return 0
    return 1

def get_m_resp(e_id):
    c.execute(f"select * from m_resp where eid='{e_id}'")
    a= c.fetchall()
    print(a[0])
    return a[0]

def edit_dealer_data(a,b,l,d,e,f,g,h,i,j,k):
    c.execute(f"UPDATE m_resp SET ={l}, ={d}, ={e}, ={f}, ={g}, ={h} ,={i},={k} WHERE dealer_id={a} and dealer_name={b} and emp_id={j}")
    mydb.commit()
    data = c.fetchall()
    return data

def get_shortlisted_emp_Id(m_id):
    c.execute(f"select eid from employee where manager_id = '{m_id}' and m_status='Approved'")
    res = c.fetchall()
    res=get_first_column(res)
    
    return res

def get_shortlisted_emp_details(e_id):
    c.execute(f"select e_name,eid,mail_id,ph_no,prev_hike_date,prev_rating ,curr_rating from employee where eid='{e_id}'")
    res = c.fetchall()
    
    return res[0]
    

def get_manager_note(e_id):
    c.execute(f"select additional_note from m_resp where emp_id='{e_id}'")
    res = c.fetchall()
    
    return res[0]

def set_hr_status(hr_choice,e_id):
    if hr_choice=='Approve':
            h_status='Approved'
    else:
        h_status='Rejected'
    c.execute(f"update employee set h_status='{h_status}' where eid='{e_id}'")
    mydb.commit()

def get_hr_status(e_id):
    c.execute(f"select h_status from employee where eid='{e_id}'")
    res=c.fetchall()
    return res[0]

def execute_cmd2(string):
    try:
        c.execute(string)
        res = c.fetchall()
        return res
    except Exception as e:
        st.info(e)
        st.error("Entered information is incomplete!Please fill all the fields since they are important")
    
def get_eligible_emp():
    c.execute('select eid,join_date from employee')
    res = c.fetchall()
    # print(res)
    # current_time = datetime.datetime.now()
    current_date = date.today()
    selected_emp = []
    for i in res:
        if (current_date-i[1]).days>75:
            selected_emp.append(i[0])
    # print((res[0][1]-current_date).days)
    # print(selected_emp)
    return selected_emp

def get_list(type):
    if type == 'HR':
        c.execute("select user_id from auth where user_id like 'HR%'")
        res = c.fetchall()
    else:
        c.execute('select m_id from manager')
        res = c.fetchall()

    res_list = [i[0] for i in res] 
    return res_list

def get_mailid(id):
    if id[0] == 'M':
        c.execute(f"select mail_id from manager where m_id = '{id}'")
        res = c.fetchall()
        mailid = res[0][0]
    elif id[0] == 'E':
        c.execute(f"select mail_id from employee where eid = '{id}'")
        res = c.fetchall()
        mailid = res[0][0]
    else:
        mailid = 'chinmaydanaraddi@gmail.com'
    return mailid

def select_topN(num,mid):
    # c.execute(f"select eid,curr_rating from employee where manager_id = '{mid}'")
    # res = c.fetchall()
    c.execute(f"select  e_name,eid,curr_rating,m_status from employee where manager_id = '{mid}' and m_status = 'Reviewed'")
    emp = c.fetchall()
    emp = sorted(emp,key = lambda x: x[2],reverse=True)
    res = []
    if len(emp)>num:
        for i in range(num):
            res.append(emp[i])
    else:
        res = emp

    if res == []:
        return 0
    return res

def select_rating(num,mid):
    c.execute(f"select  e_name,eid,curr_rating,m_status from employee where manager_id = '{mid}' and m_status = 'Reviewed'")
    emp = c.fetchall()
    res = []
    for i in emp:
        if i[2]>=num:
            res.append(i)
    if res == []:
        return 0
    return res
    
def set_submit(mid,criteria,num):
    c.execute(f"update manager set submit = 1 where m_id = '{mid}'")
    mydb.commit()
    if criteria == 'n':
        res = select_topN(num,mid)
        if res != 0:
            
            for i in res:
                c.execute(f"update employee set m_status = 'Approved' where eid = '{i[1]}'")
                mydb.commit()
            # return
    else:
        res = select_rating(num,mid)
        if res != 0:
            # return
            for i in res:
                c.execute(f"update employee set m_status = 'Approved' where eid = '{i[1]}'")
                mydb.commit()
            # return
    c.execute(f"update employee set m_status = 'Rejected' where m_status = 'Reviewed' and manager_id = '{mid}'")
    mydb.commit()

def get_submit(mid):
    c.execute(f"select submit from manager where m_id = '{mid}'")
    res = c.fetchall()
    return res[0][0]

def get_h_status(eid):
    c.execute(f"select h_status from employee where eid = '{eid}'")
    res = c.fetchall()
    return res[0][0]

def set_hr_submit(hid):
    c.execute(f"update hr set submit = 1 where h_id = '{hid}'")
    mydb.commit()

def get_hr_submit(hid):
    c.execute(f"select submit from hr where h_id = '{hid}'")
    res = c.fetchall()
    return res[0][0]

def database_reset():
    # print("HI")
    execute_cmd(f"Update employee set prev_hike_date=3 where m_status='Approved' and h_status='Approved'")
    execute_cmd(f"Update manager set submit=0")
    execute_cmd(f"Update hr set submit=0")
    execute_cmd(f"Update employee set submitted=0,m_status='Pending', h_status='Pending', prev_rating=curr_rating, curr_rating=0,prev_hike_date=prev_hike_date + 3")
    execute_cmd(f"Truncate table emp_resp")
    execute_cmd(f"Truncate table m_resp")

def get_emp_submit(eid):
    c.execute(f"select submitted from employee where eid = '{eid}'")
    res = c.fetchall()
    return res[0][0]

def get_all_employee():
    c.execute("select eid,h_status from employee where m_status = 'Approved'" )
    res = c.fetchall()
    # res = [i[0] for i in res]
    return res
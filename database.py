# import mysql.connector
# import pandas as pd

# mydb = mysql.connector.connect(host = "localhost",
#                                user = "root",database = "empl")
# cursor = mydb.cursor()

# # cursor.execute("Create database empl;")
# # cursor.execute("Use empl")
# # p=cursor.execute("create table emp_details(user_id varchar(10),password varchar(20),emp_role int,primary key(user_id))")
# # q=cursor.execute("Insert into emp_details values('hr_1','1235',2)")
# # r=cursor.execute("Insert into emp_details values('mgr_1','1275',1)")
# # mydb.commit()
# def execute(str1):
#     cursor.execute(str1)
#     p= pd.DataFrame(cursor.fetchall(),columns=[i[0] for i in cursor.description])
#     return p
import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="empl"
)
c = mydb.cursor()

def auth(u_id,password):
    # print(u_id)
    c.execute(f"select * from emp_details where user_id = '{u_id}'")
    res = c.fetchall()
    if res == []:
        st.info("Check your user id and password")
        return 0,None
    else :
        if password == res[0][1]:
            #correct auth
            return 1,res[0][2]
        else :
            st.info("Invalid Password!")
            return 0,None
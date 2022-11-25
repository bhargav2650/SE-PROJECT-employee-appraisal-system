import streamlit as st
from manager_UI import M_UI
# # from app import show_main_page
# # from app import show_logout_page
# # # from database import Authenticate

 

# # def show_login_page():
# #     if st.session_state['loggedIn']==False:
# #         user_id=st.text_input(label="",value="",placeholder="User ID")  
# #         password=st.text_input(label="",value="",placeholder="Password",type="password")
# #         st.button("Login",on_click=login_clicked,args=(user_id,password))

# # # def get_user_id():
# # #     return user_id

# # def login_clicked(user_id,password):
# #     # var=Authenticate(user_id,password)
# #     if var:
# #         st.session_state['loggedIn']=True
# #     else:
# #         st.session_state['loggedIn']==False
# #         st.error("Invalid User")

# # st.title("TRAINING SOFTWARE")
# # if 'loggedIn' not in st.session_state:
# #     st.session_state['loggedIn']=False
# #     show_login_page()
# # else:
# #     if st.session_state['loggedIn']:
# #         show_main_page()
# #         show_logout_page()
# #     else:
# #         show_login_page()

# def login():
#     # st.subheader("LOGIN")
#     with st.form("my_form"):
#         st.header('LOGIN')
#         user_id=st.text_input(label="",value="",placeholder="User ID")  
#         password=st.text_input(label="",value="",placeholder="Password",type="password")
#         # st.form_submit_button("Login",on_click=Auth,args=(user_id,password))
#         res = 0
#         if st.form_submit_button("Login"):
#             M_UI()
        # submitted = st.form_submit_button("Submit")
        

# def Auth(user_id,password):
#     #hadle unsuccessful auth also
#     pass
    
    
    
f1,f2,f3 = st.columns(3)    

def show_login_page():
    if st.session_state['loggedIn']==False:
        with f2: 
            with st.form('login'):
                    user_id=st.text_input(label="",value="",placeholder="User ID")  
                    password=st.text_input(label="",value="",placeholder="Password",type="password")
                    st.form_submit_button("Login",on_click=login_clicked,args=(user_id,password))



def login_clicked(user_id,password):
    # var=Authenticate(user_id,password)
    var = 1
    if var: 
        st.session_state['loggedIn']=True
    else:
        st.session_state['loggedIn']==False
        st.error("Invalid User")
def show_logout_page():
    st.button("LogOut",on_click=LogOut_Clicked)

def LogOut_Clicked():
    st.session_state['loggedIn']=False
    


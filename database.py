import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="auth"
)
c = mydb.cursor()

def get_mail(user_id,table):
    if table == 'employee':
        c.execute('select maail')

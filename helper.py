#for all python function required
from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import smtplib
# import sys
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from validate_email_address import validate_email

def get_form_responces():
    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('C:/Users/chinm/OneDrive/Desktop/5th sem/SE/PROJECT/client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    # Prints the responses of your specified form:
    form_id = '1fqGKaYTANP7zN5X1T85zndlHScajGkyOAqrj0q3bqUk'
    result = service.forms().responses().list(formId=form_id).execute()
    # print(type(result))
    return result

def send_mail(subj,body,recvID,attatch_file = 0):
    try:
        sender_email = "AppraiserSEproject@gmail.com"
        password = "jshtnqlejhtydejk" 

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recvID
        message["Subject"] = subj
        
        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Open PDF file in binary mode
        # if attatch_file:
        if attatch_file:
            with open(attatch_file, "rb") as attachment:
                # Add file as application/octet-stream
                part = MIMEBase("application", "octet-stream") 
                # Email client can usually download this automatically as attachment
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attatch_file}",
            )

            message.attach(part)
        text = message.as_string()
       
        # connecting to smtp mail server to send the mail
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            # if attatch_file:
            server.sendmail(sender_email, recvID, text)
            # else:
            #     server.sendmail(sender_email, recvID)
            print( "Mail successfully sent")
    except Exception as e:
        print('Unable to send mail, please try again')
        print(e)
    #change mail ID
    #change return to st.success/st.error

employees = {1:['channabasav',95,'chinmaydanaraddi@gmail.com',9448536850],3:['bhargav',67,'bhargavmc@gmail.com',9448523650],2:['chetan',52,'chetanraju@gmail.com',7238536850],4:['harish',42,'harishrJ@gmail.com',944136850],5:['ajith',92,'ajithiise@gmail.com',7298536850],6:['amogh',98,'amoghNroa@gmail.com',7293036850]}
err = 0

def select_employee(criteria,score = 0,num_emp = 1):
    
    #selected_emp has all the userID of the employees that are eligible , given the selection criteria
    selected_emp = []

    if score >100 or score<0:
        raise Exception("Given score is invalid")

    if len(employees)<num_emp:
        raise Exception("The specifed number of employees is invalid")

    if criteria not in [0,1,2]:
        raise Exception("criteria field is not valid")
    
    if len(employees) == 0:
        raise Exception("Employees data is not available")
    
    # sorting the scores of the employees
    sorted_scores = sorted(employees, key=lambda k: employees[k][1],reverse=True)
    print('sorted dictionary -',sorted_scores)
    sorted_keys = sorted_scores.keys()
    print('userID who have higher score (dec order of scores) - ',sorted_scores)
    
    if criteria == 0:
        #  all the employees with score greater than threshold are selected
        print('criteria 0')
        for key in employees.keys():
            if employees[key][1]>=score:
                print(key,employees[key][1])
                selected_emp.append(key)
        print(selected_emp)

    elif criteria == 1:
        # only specified number of employees are selected based on the highest scores
        print('criteria 1')
        if len(sorted_scores) > num_emp:
            for i in range(num_emp):
                print(sorted_keys[i],employees[sorted_keys[i]][1])
                selected_emp.append(sorted_keys[i])
        else:
            selected_emp = sorted_keys
        print(selected_emp)

    else:
        # certain specified number of employees with score above threshold are selected 
        print('criteria 2')
        if len(sorted_scores) > num_emp :
            for i in range(num_emp):
                if sorted_scores[sorted_keys[i]][1] > score:
                    break
                print(sorted_keys[i],employees[sorted_keys[i]][1])
                selected_emp.append(sorted_keys[i])
        print(selected_emp)

    return selected_emp

def score_do(choice, average_number_of_tasks_completed):
    if type(choice)==str:
        if choice=='excellent':
            return 10
        elif choice=='good':
            return 7
        elif choice=='average':
            return 5
        elif choice=='bad':
            return 2
    elif type(choice)==int:
        return choice/average_number_of_tasks_completed

avg=5
choices=['excellent','good', 'average','bad']
k=0
tsk=[3,4,3,5,4]
def score_calculate():
    l=['Conduct', 'Understanding Capability', 'Interactivity']
    numofemployees=5
    score=[0]*numofemployees
    for j in range(numofemployees):
        for i in range(3):
            choice=choices[k%4]
            k+=1
            score[j]+=score_do(choice,avg)
        tasks=tsk[j/4]
        score[j]*=score_do(tasks,avg)
    return score
score_calculate()
#for all python function required
from __future__ import print_function

# from apiclient import discovery
# from httplib2 import Http
# from oauth2client import client, file, tools
import smtplib
# import sys
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from validate_email_address import validate_email
def calculate_score(l):
    print(l)
    return ((55*(l[1]/l[0]) + 0.1*l[2]*100/480  + 0.05*l[4]*100/l[3]  + 0.6*(l[5]+l[6]+l[7]+l[8]+l[9])))

# def get_form_responces():
#     SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
#     DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

#     store = file.Storage('token.json')
#     creds = None
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('C:/Users/chinm/OneDrive/Desktop/5th sem/SE/PROJECT/client_secrets.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = discovery.build('forms', 'v1', http=creds.authorize(
#         Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

#     # Prints the responses of your specified form:
#     form_id = '1fqGKaYTANP7zN5X1T85zndlHScajGkyOAqrj0q3bqUk'
#     result = service.forms().responses().list(formId=form_id).execute()
#     # print(type(result))
#     return result

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
            print( "******Mail successfully sent*****")
    except Exception as e:
        print('******Unable to send mail, please try again******')
        print(e)
    #change mail ID
    #change return to st.success/st.error
from email.message import EmailMessage
import ssl
import smtplib

email_sender=input("Enter the Email of the sender: ")
email_password=input("Input the password of the sender:  ")

email_reciever=input("Input the password of the reciever: ")
subject = input("Enter the Subject of the email here: ")
body = input("Enter the Body of Your Email: ")
#You can also write a default email_sender,password,subject,body here.In that Case, the syntax would be:
# email_sender="Enter the Email of the sender "
# email_password="Input the password of the sender"
# email_reciever="Input the password of the reciever"
# subject = "Enter the Subject of the email here"
# body = "Enter the Body of Your Email"

em=EmailMessage()
em['From']= email_sender
em['To'] = email_reciever
em['Subject']=subject
em.set_content(body)

context= ssl.create_default_context


with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())

   
  
  
#By Arindam Majumder.

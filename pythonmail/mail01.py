import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def send_email():
    try:
        sender_mail="pavanikrishnadola01@gmail.com"
        app_password="rufl dniu hlht rhrl"
        receiver_mail="harshithasabbineni@gmail.com"
        msg=MIMEMultipart()
        msg['From']=sender_mail
        msg['To']=receiver_mail
        msg['subject']="Mail from krishna"
        msg.attach(MIMEText("Hello Harshitha..!How are you?.",'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_mail,app_password)
        server.send_message(msg)
        server.quit()
        print("Email sent Successfully")
    except smtplib.SMTPExecption as e:
        print("SMTP Error:",e)
    except Exception as ex:
        print("General Error:",ex)
send_email()

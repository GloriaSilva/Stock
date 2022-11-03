import smtplib
from email.message import EmailMessage 
import os
from dotenv import load_dotenv

load_dotenv()

path=os.getenv('PROJECT_PATH')

#Enviar Mail
email_subject = "Revisión de Stock" 
sender_email_address = "datadepartment@outlook.es" 
receiver_email_address = "g.silva@cheil.com"
email_smtp = "smtp.office365.com" 
email_password = "Alcobendas2022" 
# Create an email message object 
message = EmailMessage() 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 
# Set email body text 
message.set_content("En el documento adjunto se encuentra la revisión de stock de España y Portugal")

#Adjuntar archivo
with open(path+'stockReview.xlsx', 'rb') as file:
   file_data = file.read()
message.add_attachment(file_data, maintype="application", subtype="xlsx", filename='stockReview.xlsx')
# Set smtp server and port 
server = smtplib.SMTP(email_smtp, '587', timeout=120) 
# Identify this client to the SMTP server 
server.ehlo() 
# Secure the SMTP connection 
server.starttls() 
# Login to email account 
server.login(sender_email_address, email_password) 
# Send email 
server.send_message(message) 
# Close connection to server 
server.quit()
print('mail sent successfully')
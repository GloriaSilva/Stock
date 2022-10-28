import imaplib
import email
import os
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

pathF=os.getenv('PROJECT_PATH')

#Datos del usuario
user = "datadepartment@outlook.es"
password = "Alcobendas2022"
host = 'imap.outlook.com'

dateNow=datetime.now()
#fecha de hoy en formato en formato dd-mm-yyy
date=dateNow.strftime( '%d-%b-%Y')
print(date)

# Connect to the server
print('Connecting to ' + host)
mailBox = imaplib.IMAP4_SSL(host)

# Login to our account
mailBox.login(user, password)

boxList = mailBox.list()
# print(boxList)

mailBox.select()

result, data = mailBox.uid('search', None,'(OR Subject "Stock" Subject "Brands Analytics" SENTSINCE {date})'.format(date=date))

ids = data[0]
# list of uids
id_list = ids.split()

i = len(id_list)
for x in range(i):
    latest_email_uid = id_list[x]

    # fetch the email body (RFC822) for the given ID
    result, email_data = mailBox.uid('fetch', latest_email_uid, '(RFC822)')
    # I think I am fetching a bit too much here...

    raw_email = email_data[0][1]

    # converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # downloading attachments
    for part in email_message.walk():

        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(pathF+'File', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()



    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    print(email_message['Subject'])

mailBox.close()
mailBox.logout()

# Importing OS (to retrieve env variables) && pyairtable (a community-built python library to use the Airtable API)
import os
from pyairtable import Api
# Email Stuff Preparation
import smtplib
from email.mime.text import MIMEText

sender_email = "daydream.casablanca@gmail.com"
app_password = os.environ['GMAIL_APP_PASSWORD']

def sendEmail(receiver_email, subject):
    message = MIMEText("Hello, this is a test from the hackathon.")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)

# TEST
sendEmail(
    "aminesakoute288@gmail.com",
    subject="Hello from Hackathon Manager",
    body="Hi there, biatch."
)

# Getting necessary info from the API
api = Api(os.environ['AIRTABLE_TEST_API_KEY'])
BASE_ID = "app5RiAfXsKWSZ67p"
TABLE_ID = "tblt7GgXQ6gCYCV2l"

# Declaring the Participants Spreadsheet
daydream_table = api.table(BASE_ID, TABLE_ID)

# Iterating over each participant && checking if they've signed the NDA
for table in daydream_table.iterate():
    for participant in table:
        fullname = participant['fields']['Name'] + " " + participant['fields']['Surname']
        email = participant['fields']['Email']
        try:
            signed = participant['fields']['Signed']
            # If checkbox is not ticked --> NULL, so...
        except:
            signed = False
        if signed is False:
            pass

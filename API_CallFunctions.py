# Importing OS (to retrieve env variables) && pyairtable (a community-built python library to use the Airtable API)
import os
from pyairtable import Api

# Email Stuff Preparation
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "daydream.casablanca@gmail.com"
app_password = os.environ['GMAIL_APP_PASSWORD']

def sendEmail(receiver_email, subject, plain, html):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Trying out the two email_contents (Some email providers don't handle HTML direclty)
    message.attach(plain_content)
    message.attach(html_content) # They will first try this one

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)

# Getting necessary info from the API
api = Api(os.environ['AIRTABLE_TEST_API_KEY'])
BASE_ID = "app5RiAfXsKWSZ67p"
TABLE_ID = "tblt7GgXQ6gCYCV2l"

# Declaring the Participants Spreadsheet
daydream_table = api.table(BASE_ID, TABLE_ID)

plain_bodies={'NOT_SIGNED':f"""Hi there {fullname} ! 
Hope you're doing great. Just a friendly reminder to sign the NDA in the Hackclub form. If you don't, then you won't be able to participate to the evenement, and that would be sad. 
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.

CLICK on the attachment below !""", 'SIGNED_NDA':f"""Hi there {fullname} ! 
Hope you're doing great. Present the QR code below at Ecole Centrale's entrance to get in and participate in Daydream Casablanca 2025 ! Looking forward to seeing you there !
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025."""}

html_bodies={'NOT_SIGNED':"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
             <meta charset='utf-8'>
             <style>
             body {
             background-color:lightgreen;
             color:black;
             font-family:'Helvetica', sans-serif;
             font-size:20px;
             }
             </style>
             </head>
             <body>
             <div id="main_div">
             <h1>Hello Bitch !</h1>
             <p>Hope you're doing okay !</p>
             <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fabcnews.go.com%2FGMA%2FFamily%2Fnewborn-babys-photo-shoot-viral-hilarious-grumpy-expression%2Fstory%3Fid%3D110522897&psig=AOvVaw3KxRTdySMcFWV6WbeaxsN6&ust=1756816750903000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCIjRx8HKt48DFQAAAAAdAAAAABAE">
             </div>
             </body>
             </html>"""}

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
        # Sending the QR Code + Reminding participants to sign the NDA
        if signed is False:
            # Passing the actual email contents : Plain Text && HTML
            plain_content = MIMEText(plain_bodies['NOT_SIGNED'], "plain")
            html_content = MIMEText(html_bodies['NOT_SIGNED'], "html")

            sendEmail(receiver_email=email, subject="URGENT : Sign the NDA to participate in Daydream Casablanca !", plain=plain_content, html=html_content)
        else:
            # Passing the actual email contents : Plain Text && HTML
            plain_content = MIMEText(plain_bodies['SIGNED_NDA'], "plain")
            html_content = MIMEText(html_bodies['SIGNED_NDA'], "html")
            sendEmail(receiver_email=email, subject="IMPROTANT - Click here to get your ticket !",  plain=plain_content, html=html_content)

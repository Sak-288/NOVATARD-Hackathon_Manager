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

plain_bodies={'NOT_SIGNED':f"""Hi there ! 
Hope you're doing great. Just a friendly reminder to sign the NDA in the Hackclub form. If you don't, then you won't be able to participate to the evenement, and that would be sad. 
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.

CLICK on the attachment below !""", 'SIGNED_NDA':f"""Hi there ! 
Hope you're doing great. Present the QR code below at Ecole Centrale's entrance to get in and participate in Daydream Casablanca 2025 ! Looking forward to seeing you there !
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025."""}

html_bodies={'NOT_SIGNED':"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body style="margin:0; padding:0;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#90EE90">
      <tr>
        <td align="center" style="padding:20px; font-family:Arial, sans-serif; color:#000000; font-size:18px;">
          <table width="600" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" style="border-radius:8px; padding:20px;">
            <tr>
              <td align="center" style="font-size:28px; font-weight:bold; padding-bottom:10px;">
                Hello!
              </td>
            </tr>
            <tr>
              <td align="center" style="font-size:20px; padding-bottom:20px;">
                Please sign the NDA to participate in Daydream Casablanca 2025.
              </td>
            </tr>
            <tr>
              <td align="center" style="padding-bottom:20px;">
                <img src="https://i.abcnewsfe.com/a/ffe8d7cb-a13f-4e4e-a45b-0b16f5731915/baby-4-ht-jt-240523_1716503358143_hpEmbed_3x2.jpg" width="300" style="display:block; border:0; outline:none; text-decoration:none;">
              </td>
            </tr>
            <tr>
              <td align="center" style="font-size:16px; color:#555555; line-height:22px;">
                <strong>Amine Sakoute</strong><br>
                Organizer @ Daydream Casablanca 2025<br>
                <a href="https://daydream.hackclub.com" style="color:#1155CC; text-decoration:none;">daydream.hackclub.com</a><br>
                t: +212 775-116598<br>
                e: <a href="mailto:daydream.casablanca@gmail.com" style="color:#1155CC; text-decoration:none;">daydream.casablanca@gmail.com</a>
              </td>
            </tr>
            <tr>
              <td align="center" style="padding-top:20px; font-size:14px; color:#777777;">
                Daydream Casablanca is fiscally sponsored by <a href="https://the.hackfoundation.org" style="color:#1155CC; text-decoration:none;"><b>The Hack Foundation</b></a> (Hack Club), a 501(c)(3) nonprofit.
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
""",
'SIGNED_NDA':"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body style="margin:0; padding:0;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#90EE90">
      <tr>
        <td align="center" style="padding:20px; font-family:Arial, sans-serif; color:#000000; font-size:18px;">
          <table width="600" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" style="border-radius:8px; padding:20px;">
            <tr>
              <td align="center" style="font-size:28px; font-weight:bold; padding-bottom:10px;">
                Congratulations!
              </td>
            </tr>
            <tr>
              <td align="center" style="font-size:20px; padding-bottom:20px;">
                Show this QR code at the entrance to get in:
              </td>
            </tr>
            <tr>
              <td align="center" style="padding-bottom:20px;">
                <img src="https://i.pinimg.com/736x/6f/23/67/6f236786f6706f6d978b4de83aa769a5.jpg" width="300" style="display:block; border:0; outline:none; text-decoration:none;">
              </td>
            </tr>
            <tr>
              <td align="center" style="font-size:16px; color:#555555; line-height:22px;">
                <strong>Amine Sakoute</strong><br>
                Organizer @ Daydream Casablanca 2025<br>
                <a href="https://daydream.hackclub.com" style="color:#1155CC; text-decoration:none;">daydream.hackclub.com</a><br>
                t: +212 775-116598<br>
                e: <a href="mailto:daydream.casablanca@gmail.com" style="color:#1155CC; text-decoration:none;">daydream.casablanca@gmail.com</a>
              </td>
            </tr>
            <tr>
              <td align="center" style="padding-top:20px; font-size:14px; color:#777777;">
                Daydream Casablanca is fiscally sponsored by <a href="https://the.hackfoundation.org" style="color:#1155CC; text-decoration:none;"><b>The Hack Foundation</b></a> (Hack Club), a 501(c)(3) nonprofit.
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
"""}

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

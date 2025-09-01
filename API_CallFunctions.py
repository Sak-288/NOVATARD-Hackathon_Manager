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

# Iterating over each participant && checking if they've signed the NDA
for table in daydream_table.iterate():
    for participant in table:
        # Initializing every email_content, I know there's a better solution somewhere, just testing for the sake of personalization
        plain_bodies={'NOT_SIGNED':f"""Hi there {fullname}!
Hope you're doing great. Just a friendly reminder to sign the NDA in the Hackclub form. If you don't, then you won't be able to participate to the evenement, and that would be sad. 
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.

CLICK on the attachment below !""".format(**locals()), 'SIGNED_NDA':f"""Hi there {fullname}! 
Hope you're doing great. Present the QR code below at Ecole Centrale's entrance to get in and participate in Daydream Casablanca 2025 ! Looking forward to seeing you there !
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.""".format(**locals())}

        html_bodies={'NOT_SIGNED':"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
             <meta charset='utf-8'>
             </head>
             <body>
             <div id="main_div" style="text-align:center;  background: radial-gradient(circle at top left,     #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) top left, radial-gradient(circle at top right,    #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) top right, radial-gradient(circle at bottom left,  #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) bottom left, radial-gradient(circle at bottom right, #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) bottom right; background-size: 50% 50%; background-repeat: no-repeat; color:black; font-family:'Helvetica', sans-serif; font-size:20px;border-radius:5px; margin:0; width:100%; height:auto;">
             <h1>Hi there {fullname} !</h1>
             <br/>
             <br/>
             <p>Hope you're doing great. Just a friendly reminder to sign the NDA in the Hackclub form. If you don't, then you won't be able to participate to the evenement, and that would be sad. </p>
             </div>
             <div dir="ltr" style="font-size:11px;font-family:'Helvetica', sans-serif;font-weight:bold;;"><font>Best regards,</font><a href="https://github.com/Sak-288" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79">Amine Sakoute</font></a><div style="color:rgb(34,34,34)">Organizer @Daydream Casablanca && NOVATARD FTC#24950 Lead Coder</div><div style="color:rgb(34,34,34)"><a href="https://4f9eb20f.streaklinks.com/CkB8OkIqKmF1XgZXCQmn-rol/https%3A%2F%2Fdaydream.hackclub.com%2F" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://4f9eb20f.streaklinks.com/CkB8OkIqKmF1XgZXCQmn-rol/https%253A%252F%252Fdaydream.hackclub.com%252F&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw06bzM06NOrFiUX3kfynhWJ"><img width="420" height="137" src="https://ci3.googleusercontent.com/mail-sig/AIorK4xwFXn300c83xshdSN00Wp9yWgz72n1P31GBqb_hJACa3Oqv01nxuZIXHogMNLwmbGQDiqGVY3qC33n" alt="https://daydream.hackclub.com/" class="CToWUd" data-bit="iit"><br></a></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)">W:&nbsp;<a href="https://daydream.hackclub.com/" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://daydream.hackclub.com/&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw1M_5uncUUx0PQtwAcPLWCt"><font color="#a64d79">daydream.hackclub.com</font></a><br></div><div><div style="color:rgb(34,34,34)">T: +212 625734075</div><div><font color="#222222">E:&nbsp;</font><a href="mailto:hafsaelidrissi2009@gmail.com" target="_blank"><font color="#a64d79">daydream.casablanca@gmail.<wbr>com</font></a></div></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><font color="#444444">Daydream Casablanca is fiscally sponsored by&nbsp;</font><a href="https://4f9eb20f.streaklinks.com/CkB8OkIc3H0D0h2QUAH8ob-3/https%3A%2F%2Fthe.hackfoundation.org%2F" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://4f9eb20f.streaklinks.com/CkB8OkIc3H0D0h2QUAH8ob-3/https%253A%252F%252Fthe.hackfoundation.org%252F&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw0dHSwgsHXuInPMoi11akdb"><font color="#a64d79"><b>The Hack Foundation</b></font></a><font color="#444444">&nbsp;(d.b.a. Hack Club), a 501(c)(3) nonprofit (EIN: 81-2908499).</font></div></div>
             </body>
             </html>""",
             'SIGNED_NDA':"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
             <meta charset='utf-8'>
             </head>
             <body>
             <div id="main_div" style="text-align:center;  background: radial-gradient(circle at top left,     #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) top left, radial-gradient(circle at top right,    #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) top right, radial-gradient(circle at bottom left,  #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) bottom left, radial-gradient(circle at bottom right, #c0e5fb 0%, #fbecc6 50%, #e79ec4 80%) bottom right; background-size: 50% 50%; background-repeat: no-repeat; color:black; font-family:'Helvetica', sans-serif; font-size:20px;border-radius:5px; margin:0; width:100%; height:auto;">             <h1>Hi there {fullname} !</h1>
             <br/>
             <br/>
             <p>Hope you're doing great. Present the QR code below at Ecole Centrale's entrance to get in and participate in Daydream Casablanca 2025 ! Looking forward to seeing you there !</p>
             </div>
             <div dir="ltr" style="font-size:11px;font-family:'Helvetica', sans-serif;font-weight:bold;"><font>Best regards,</font><a href="https://github.com/Sak-288" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79">Amine Sakoute</font></a><div style="color:rgb(34,34,34)">Organizer @Daydream Casablanca && NOVATARD FTC#24950 Lead Coder</div><div style="color:rgb(34,34,34)"><a href="https://4f9eb20f.streaklinks.com/CkB8OkIqKmF1XgZXCQmn-rol/https%3A%2F%2Fdaydream.hackclub.com%2F" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://4f9eb20f.streaklinks.com/CkB8OkIqKmF1XgZXCQmn-rol/https%253A%252F%252Fdaydream.hackclub.com%252F&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw06bzM06NOrFiUX3kfynhWJ"><img width="420" height="137" src="https://ci3.googleusercontent.com/mail-sig/AIorK4xwFXn300c83xshdSN00Wp9yWgz72n1P31GBqb_hJACa3Oqv01nxuZIXHogMNLwmbGQDiqGVY3qC33n" alt="https://daydream.hackclub.com/" class="CToWUd" data-bit="iit"><br></a></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)">W:&nbsp;<a href="https://daydream.hackclub.com/" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://daydream.hackclub.com/&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw1M_5uncUUx0PQtwAcPLWCt"><font color="#a64d79">daydream.hackclub.com</font></a><br></div><div><div style="color:rgb(34,34,34)">T: +212 625734075</div><div><font color="#222222">E:&nbsp;</font><a href="mailto:hafsaelidrissi2009@gmail.com" target="_blank"><font color="#a64d79">daydream.casablanca@gmail.<wbr>com</font></a></div></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><font color="#444444">Daydream Casablanca is fiscally sponsored by&nbsp;</font><a href="https://4f9eb20f.streaklinks.com/CkB8OkIc3H0D0h2QUAH8ob-3/https%3A%2F%2Fthe.hackfoundation.org%2F" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://4f9eb20f.streaklinks.com/CkB8OkIc3H0D0h2QUAH8ob-3/https%253A%252F%252Fthe.hackfoundation.org%252F&amp;source=gmail&amp;ust=1756814241116000&amp;usg=AOvVaw0dHSwgsHXuInPMoi11akdb"><font color="#a64d79"><b>The Hack Foundation</b></font></a><font color="#444444">&nbsp;(d.b.a. Hack Club), a 501(c)(3) nonprofit (EIN: 81-2908499).</font></div></div>
             </body>
             </html>""".format(**locals())}
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

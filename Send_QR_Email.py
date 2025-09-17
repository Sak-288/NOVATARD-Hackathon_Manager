# Email Stuff Preparation
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Airtable_API_GetData import *
from email.mime.image import MIMEImage

# QR Code Stuff Preparation
from Generate_Entry_QRCode import *

sender_email = "casablanca@daydream.hackclub.com"
app_password = os.environ['GMAIL_APP_PASSWORD']

def sendEmail(receiver_email, subject, plain, html):
    # Outer container: HTML + inline images
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    message.attach(plain)
    message.attach(html)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)

# Iterating over each participant && checking if they've signed the NDA
for table in daydream_table.iterate():
    for participant in table:
        # Getting their info
        fullname = participant['fields']['Name'] + " " + participant['fields']['Surname']
        email = participant['fields']['Email']
        # QR Code Stuff
        prt_id = participant['fields']['Id']
        prt_accessCode = generate_qrcode(WB_PUBLIC_URL, prt_id)
        # Initializing every email_content, I know there's a better solution somewhere, just testing for the sake of personalization
        plain_bodies={'NOT_SIGNED':f"""Hi there {fullname}!
Hope you're doing great. Just a friendly reminder to sign the NDA in the Hackclub form. If you don't, then you won't be able to participate to the evenement, and that would be sad. 
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.

CLICK on the attachment below !""".format(fullname=fullname), 'SIGNED_NDA':f"""Hi there {fullname}! 
Hope you're doing great. Present the QR code below at Ecole Centrale's entrance to get in and participate in Daydream Casablanca 2025 ! Looking forward to seeing you there !
Best regards, Amine Sakoute | Organizer @Daydream Casablanca 2025.""".format(fullname=fullname)}

        html_bodies={'NOT_SIGNED':"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
                     <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <meta charset='utf-8'>
             </head>
             <body>
             <div style="color:black;align-items:flex-start; justify-content:space-between; background:radial-gradient(circle at top left,#c0e5fb 0%,#fbecc6 100%) top left,radial-gradient(circle at top right,#c0e5fb 0%,#fbecc6 100%) top right,radial-gradient(circle at bottom left,#c0e5fb 0%,#fbecc6 100%) bottom left,radial-gradient(circle at bottom right,#c0e5fb 0%,#fbecc6 100%) bottom right; background-repeat:no-repeat; color:black; font-family:'Helvetica',sans-serif; font-size:16px; border-radius:5px; margin:0;width:95%; height:50%; padding:15px;">
             <h1 style="margin:0 0 px 0; padding:0;text-decoration:underlined;text-align:center;">Hi there {fullname} !</h1>
            <div style="display:inline-block;white-space:pre-wrap; text-align:start; font-family:Helvetica,sans-serif;margin-left:15px;font-weight:bold;">Hope you're doing great.
Just a friendly reminder to sign the NDA in the Hackclub form.
If you don't, then you won't be able to
participate to the evenement, and that would be sad.
CLICK on the LINK on the right -->
</div>
             </div>
            <br/>
            <div dir="ltr" style="font-size:13px;font-family:'Helvetica', sans-serif;"><font>Best regards, </font><a href="https://github.com/Sak-288" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>Amine Sakoute</b></font></a><div style="color:rgb(34,34,34)"><b>Organizer @Daydream Casablanca && NOVATARD FTC#24950 Lead Coder</b></div><div style="color:rgb(34,34,34)"><a href="https://daydream.hackclub.com/casablanca" target="_blank"><br/><img width="420" height="137" src="https://ci3.googleusercontent.com/mail-sig/AIorK4xwFXn300c83xshdSN00Wp9yWgz72n1P31GBqb_hJACa3Oqv01nxuZIXHogMNLwmbGQDiqGVY3qC33n" alt="https://daydream.hackclub.com/casablanca" class="CToWUd" data-bit="iit"><br></a></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><b>W:</b>&nbsp;<a href="https://daydream.hackclub.com/casablanca" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>daydream.hackclub.com/casablanca</b></font></a><br></div><div><div style="color:rgb(34,34,34)"><b>T:</b> <b>+212 625734075</b></div><div><b>E:</b>&nbsp;<a href="mailto:casablanca@daydream.hackclub.com" target="_blank"><font color="#a64d79"><b>casablanca@daydream.hackclub.com</b></font></a></div></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><font color="#444444">Daydream Casablanca is fiscally sponsored by&nbsp;</font><a href="https://the.hackfoundation.org/" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>The Hack Foundation</b></font></a><font color="#444444">&nbsp;(d.b.a. Hack Club), a 501(c)(3) nonprofit (EIN: 81-2908499).</font></div></div>
             </body>
             </html>""".format(fullname=fullname),
             'SIGNED_NDA':"""
             <!DOCTYPE html>
             <html lang="en">
             <head>
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <meta charset='utf-8'>
             </head>
             <body>
             <div style="color:black;align-items:flex-start; justify-content:space-between; background:radial-gradient(circle at top left,#c0e5fb 0%,#fbecc6 100%) top left,radial-gradient(circle at top right,#c0e5fb 0%,#fbecc6 100%) top right,radial-gradient(circle at bottom left,#c0e5fb 0%,#fbecc6 100%) bottom left,radial-gradient(circle at bottom right,#c0e5fb 0%,#fbecc6 100%) bottom right; background-repeat:no-repeat; color:black; font-family:'Helvetica',sans-serif; font-size:16px; border-radius:5px; margin:0; width:95%; height:50%; padding:15px;">
            <h1 style="font-color:black;margin:0 0 px 0; padding:0;text-decoration:underlined;text-align:center;">Hi there {fullname} !</h1>
             <div style="display:table; width:100%; margin-top:-10px;">
            <!-- Texte -->
            <div style="display:table-cell; width:70%; text-align:start; vertical-align:middle; font-weight:bold; white-space:pre-wrap;">
            Hope you're doing great.  
            Present the QR code on the right at Ecole Centrale's entrance 
            to get in and participate in Daydream Casablanca 2025!  
            Looking forward to seeing you there.
            </div>
            <!-- QR Code -->
            <div style="display:table-cell; width:30%; text-align:end; vertical-align:middle;">
            <img src="cid:qrcode" alt="QR Code" style="height:150px; width:150px; border-radius:5px; margin-right:60px"/>
            </div>
            </div>
            </div>
             </div>
             <br/>
             <div dir="ltr" style="font-size:13px;font-family:'Helvetica', sans-serif;"><font>Best regards, </font><a href="https://github.com/Sak-288" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>Amine Sakoute</b></font></a><div style="color:rgb(34,34,34)"><b>Organizer @Daydream Casablanca && NOVATARD FTC#24950 Lead Coder</b></div><div style="color:rgb(34,34,34)"><a href="https://daydream.hackclub.com/casablanca" target="_blank"><br/><img width="420" height="137" src="https://ci3.googleusercontent.com/mail-sig/AIorK4xwFXn300c83xshdSN00Wp9yWgz72n1P31GBqb_hJACa3Oqv01nxuZIXHogMNLwmbGQDiqGVY3qC33n" alt="https://daydream.hackclub.com/casablanca" class="CToWUd" data-bit="iit"><br></a></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><b>W:</b>&nbsp;<a href="https://daydream.hackclub.com/casablanca" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>daydream.hackclub.com/casablanca</b></font></a><br></div><div><div style="color:rgb(34,34,34)"><b>T:</b> <b>+212 625734075</b></div><div><b>E:</b>&nbsp;<a href="mailto:casablanca@daydream.hackclub.com" target="_blank"><font color="#a64d79"><b>casablanca@daydream.hackclub.com</b></font></a></div></div><div style="color:rgb(34,34,34)"><br></div><div style="color:rgb(34,34,34)"><font color="#444444">Daydream Casablanca is fiscally sponsored by&nbsp;</font><a href="https://the.hackfoundation.org/" style="color:rgb(17,85,204)" target="_blank"><font color="#a64d79"><b>The Hack Foundation</b></font></a><font color="#444444">&nbsp;(d.b.a. Hack Club), a 501(c)(3) nonprofit (EIN: 81-2908499).</font></div></div>
             </body>
             </html>""".format(fullname=fullname, prt_accessCode=prt_accessCode)}
        try:
            signed = participant['fields']['Signed']
            # If checkbox is not ticked --> NULL, so...
        except:
            signed = False
        # Sending the QR Code + Reminding participants to sign the NDA
        if signed is False:
            pass
        else:
            # Passing the actual email contents : Plain Text && HTML
            plain_content = MIMEText(plain_bodies['SIGNED_NDA'], "plain")
            html_content = MIMEText(html_bodies['SIGNED_NDA'], "html")
            sendEmail(receiver_email=email, subject="IMPROTANT - Click here to get your ticket !",  plain=plain_content, html=html_content)
        

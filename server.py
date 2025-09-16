from flask import Flask, request, render_template_string
import requests, os
from Airtable_API_GetData import *
import subprocess

app = Flask(__name__)

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_TEST_API_KEY")

HTML_PARTICIPANT = """
<!DOCTYPE html>
<html>
<head>  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Participant Info</title><link rel="icon" type="image/png" href="https://www.dropbox.com/scl/fi/9tyxp466h915yhionvuxw/cat.ico?rlkey=tsxs01aqis0fs5nz8o0wtv7dx&e=2&st=66xk2y9t&raw=1"></head>
<body style="position:relative;text-align:center;font-weight:bold;color:black;align-items:flex-start; justify-content:space-between; background:radial-gradient(circle at top left,#c0e5fb 0%,#fbecc6 100%) top left,radial-gradient(circle at top right,#c0e5fb 0%,#fbecc6 100%) top right,radial-gradient(circle at bottom left,#c0e5fb 0%,#fbecc6 100%) bottom left,radial-gradient(circle at bottom right,#c0e5fb 0%,#fbecc6 100%) bottom right; background-repeat:repeat; color:black; font-family:'Orbitron',sans-serif; font-size:16px;">
<h1 style="text-decoration:underline;">Participant Info</h1>
{% if info %}
<div id="info_div" style="margin-top:13px;position:absolute;left:50%; transform:translate(-50%, 0%); width:30%; height:auto; background-color:white; border-radius:5px;">
<p>Id : {{ info['Id'] }}</p>
<p>Surname : {{ info['Surname'] }}</p>
<p>Name : {{ info['Name'] }}</p>
<p>Age : {{ info['Age'] }}</p>
<p>Attendance Status : {{ info['Present'] }}</p>
</div>
{% else %}
<p>No participant found.</p>
{% endif %}
</body>
</html>
"""

HTML_ADMIN = """
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <meta charset="utf-8">
    <title>Admin Page</title>
    <link rel="icon" type="image/png" href="https://www.dropbox.com/s/abcd1234/cat.ico?raw=1">
    <style>
        body {
            margin: 0;
            font-family: 'Orbitron', sans-serif;
            font-size: 20px;
            color: white;
            background-image: url('https://www.dropbox.com/scl/fi/pnaqqe6eezluq8dvtqyli/STARRY.gif?rlkey=o9uuej8oy0qtd174lwww5kmll&st=0woppfiv&raw=1');
            background-repeat: repeat;
            background-position: center;
            position: relative;
            font-weight:bold;
            background-color:black;
        }

        #cmd_div {
            background-color:darkgreen;
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            width: 60%;
            border-radius: 3px;
            padding: 20px;
            text-align: center;
            z-index: 10;
            color: black;
        }

        #cmd_div button {
            padding: 10px 20px;
            font-size: 18px;
            margin: 10px 0;
            cursor: pointer;
            font-weight:bold;
            background-color:blue;
            color:white;
        }

        #ifr_div {
        background-color:darkgreen;
            margin-top: 40px;
            width: 100%;
            padding: 0 5%;
            box-sizing: border-box;
            color:white;
        }

        #ifr_div h2 {
            color: white;
            margin-top: 40px;
            margin-bottom: 10px;
        }

        #ifr_div iframe {
        # background-color:darkgreen;
            width: 100%;
            min-height: 533px;
            border: 1px solid #ccc;
            background: transparent;
        }
    </style>
</head>
<body>

    <div id="cmd_div">
        <p>Send Email to participants to remind them to sign NDA</p>
        <button id="NDA">Send Reminder</button>
        <p>Send Email to participants to give them QR Code Ticket</p>
        <button id="Ticket">Send Ticket</button>
    </div>

    <div id="ifr_div">
        <h2>Hackathon Attendance Sheet</h2>
        <iframe class="airtable-embed" src="https://airtable.com/embed/app5RiAfXsKWSZ67p/shrhKFeNFWUey4Czi"></iframe>

        <h2>Workshop Form Links (to send on GC)</h2>
        <iframe class="airtable-embed" src="https://airtable.com/embed/appZtJBlfY1irfrsL/shraqDjqXiy2k8qTw"></iframe>

        <h2>Workshop 1</h2>
        <iframe class="airtable-embed" src="https://airtable.com/embed/appOpZNn2wGbMvRtk/shrg2WyfzqdgFSPAf"></iframe>

        <h2>Workshop 2</h2>
        <iframe class="airtable-embed" src="https://airtable.com/embed/appSpKDqiOkDkX4BR/shri9U4rCkRoJnOHL"></iframe>

        <h2>Workshop 3</h2>
        <iframe class="airtable-embed" src="https://airtable.com/embed/appefUBAo1M3ATiye/shrSDC3RH5jpGtSXB"></iframe>
    </div>

    <script>
        // Button triggers Flask endpoint to run NDA script
        document.getElementById("NDA").onclick = () => {
            fetch("/run-nda", { method: "POST" });
        };

        // Button triggers Flask endpoint to run Ticket script
        document.getElementById("Ticket").onclick = () => {
            fetch("/run-ticket", { method: "POST" });
        };

        // Parallax Effect for dynamic background
        (function() {
            document.addEventListener("mousemove", parallax_body);
            const elem = document.querySelector("body");

            function parallax_body(e) {
                let _w = window.innerWidth;
                let _h = window.innerHeight;
                let _mouseX = e.clientX;
                let _mouseY = e.clientY;

                let offset_coeff = 0.005;
                let bg_Xoffset = -(_mouseX - _w/2) * offset_coeff;
                let bg_Yoffset = -(_mouseY - _h/2) * offset_coeff * -1.75;

                elem.style.backgroundPosition = `${bg_Xoffset}% ${bg_Yoffset}%`;
            }
        })();
    </script>

</body>
</html>
"""


@app.route("/info")
def home():
    id = request.args.get("id")
    if not id:
        return render_template_string(HTML_PARTICIPANT, info=None)

    id = int(id)
    html_data = None
    for table in daydream_table.iterate():
        for participant in table:
            # Getting the info from airtable
            if participant['fields']['Id'] == id:
                html_data = participant['fields']
                # Sending the info about ATTENDANCE
                update_data = {
                    "fields": {
                        "Present": True
                    }
                }
                url = BASE_URL + f"{BASE_ID}/{TABLE_ID}/{participant['fields']['Rec']}"
                response = requests.patch(url, json=update_data, headers=HEADERS)

                break
        if html_data:
            break

    return render_template_string(HTML_PARTICIPANT, info=html_data)

@app.route("/admin")
def admin_page():
    return render_template_string(HTML_ADMIN)

# Run NDA script
@app.route("/run-nda", methods=["POST"])
def run_nda():
    subprocess.Popen(["python", "Send_NDA_Email.py"])
    return "", 204  # 204 = No Content

# Run Ticket script
@app.route("/run-ticket", methods=["POST"])
def run_ticket():
    subprocess.Popen(["python", "Send_Ticket_Email.py"])
    return "", 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

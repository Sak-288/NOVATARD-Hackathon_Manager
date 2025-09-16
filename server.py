from flask import Flask, request, render_template_string
import requests, os
from Airtable_API_GetData import *

app = Flask(__name__)

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_TEST_API_KEY")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Participant Info</title></head>
<body style="text-align:center;font-weight:bold;color:black;align-items:flex-start; justify-content:space-between; background:radial-gradient(circle at top left,#c0e5fb 0%,#fbecc6 100%) top left,radial-gradient(circle at top right,#c0e5fb 0%,#fbecc6 100%) top right,radial-gradient(circle at bottom left,#c0e5fb 0%,#fbecc6 100%) bottom left,radial-gradient(circle at bottom right,#c0e5fb 0%,#fbecc6 100%) bottom right; background-repeat:repeat; color:black; font-family:'Helvetica',sans-serif; font-size:16px;">
<h1>Participant Info</h1>
{% if info %}
<p>Id : {{ info['Id'] }}</p>
<p>Surname : {{ info['Surname'] }}</p>
<p>Name : {{ info['Name'] }}</p>
<p>Age : {{ info['Age'] }}</p>
{% else %}
<p>No participant found.</p>
{% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    id = request.args.get("id")
    if not id:
        return render_template_string(HTML_TEMPLATE, info=None)

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

    return render_template_string(HTML_TEMPLATE, info=html_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

import requests
from send_email import send_email

topic = ""
#go to url for api key
api_key = ""
url = f""

request = requests.get(url)

#get a dictionary of data
content = request.json()

body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Todays News " + body + article["title"] + "\n" + article["description]"] + "\n" + article[url] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
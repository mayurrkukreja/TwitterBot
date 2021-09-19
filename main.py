import json
import time
from requests.models import Response
import tweepy
import requests
# Api authorization
auth = tweepy.OAuthHandler("Cgsfem33XmmiuZJYtmJhYI7pd", "H25Rh3TVqr5BJqK0tkxjQUWndMDEC5yKjD1cWLNrZ4ydZVWG6I")
auth.set_access_token("1436527230746718209-9xpPbumOQqxL022Y2wf1gXyI1f5b8h", "5vGk9RDabz996AY8jZcxta3fO3bgHYDh5OIIP9cDN0tUm")

# Create an API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful!")
except:
    print("Error during Authentication!")

def scheduler():
    time.sleep(3)
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    res = json.loads(response.text)
    print(res)
    api.update_status(res['content'])

scheduler()

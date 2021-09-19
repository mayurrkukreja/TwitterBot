import logging
import time
import requests
import json
import schedule
import tweepy
from time import sleep 

# API authorization
auth = tweepy.OAuthHandler("rQRXP6L2eLbSvnwkI5TYwLgro", "VQdYvlyYDfpmZHJgIUOYLW6T0dhjkr4oE97cBygaswc7dcK2ve")
auth.set_access_token("844280085167296512-Q2zXATvYf75fp02EMEy7EFNTd9Y8MQD","Jl9Z0gvgjUzIDS8MS7ydV9LgHtzmDXC90PcNeZgQN5OBJ")
api = tweepy.API(auth)

#API verification
try:
    api.verify_credentials()
    print("Authentication successful!");
except:
    print("Error during Authentication.")

# Get User
user = api.get_user('mayurkukreja26')
print(user.screen_name)
# user's followers count
print(user.followers_count)


# logger = logging.getLogger()
# logging.basicConfig(level=logging.INFO)
# logger.setLevel(logging.INFO)

def scheduler():
    time.sleep(3)
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    res = json.loads(response.text)
    print(res)
    api.update_status(res['content']) 

scheduler()


# Automation

#schedule.every().day.at("02:56").do(scheduler, "Done @ 02:56")
#while True:
    #schedule.run_pending()
    #time.sleep(40)

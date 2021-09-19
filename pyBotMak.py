import requests
import json
import tweepy
from time import sleep 
from credentials import *
from config import *
import logging
import credentials

auth = tweepy.OAuthHandler("rQRXP6L2eLbSvnwkI5TYwLgro", "VQdYvlyYDfpmZHJgIUOYLW6T0dhjkr4oE97cBygaswc7dcK2ve")
auth.set_access_token("844280085167296512-Q2zXATvYf75fp02EMEy7EFNTd9Y8MQD","Jl9Z0gvgjUzIDS8MS7ydV9LgHtzmDXC90PcNeZgQN5OBJ")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication successful!");
except:
    print("Error during Authentication.")

api.update_status('Testing twitter bot :)')
#Get user
user = api.get_user('mayurkukreja26')
# User name
print(user.screen_name)
#user's followers count
print(user.followers_count)


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

def  get_quote():
    URL = "https:api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        logger.info('Error calling api')

    res = json.loads(response.text)
    #print(res)
    #return res['content'] + "-" + res['author']





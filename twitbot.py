import tweepy as tp
import time
import os

# Interacts with the Twitter API providing the consumer_key & access_token

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

# Utilizes OAuth to interact with the API using tp(tweepy)

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Moves to the folder in the operating system
os.chdir('wolves')


# For every image in the folder it posts to the specified twitter account every 60 seconds
for wolf_image in os.listdir('.'):
    api.update_with_media(wolf_image)
    time.sleep(60)

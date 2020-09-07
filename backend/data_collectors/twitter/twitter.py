import os, requests, json
from mongoengine import connect
from models import *
import tweepy
try:
    connection
except NameError:
    connection = connect("finsocial", host=os.environ['DB_URI'])

API_KEY=os.environ['API_KEY']
API_KEY_SECRET=os.environ['API_KEY_SECRET']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def lambda_handler(event, context):

    twitter_users = TwitterUsers.objects()
    for user in twitter_users:
        # for status in tweepy.Cursor(api.user_timeline, screen_name='@nicolasmarcwee', tweet_mode="extended").items():
        for status in api.user_timeline(screen_name=f'@{user.username}'):
            r = requests.get(f"https://publish.twitter.com/oembed?url=https://twitter.com/{user.username}/status/{status.id}")
            my_json = r.content.decode('utf8')
            data = json.loads(my_json)
            new_twitter = Twitter.objects(url=data['url']).update_one(set__version=data['version'], set__author_url=data['author_url'], set__author_name=data['author_name'], set__html=data['html'], set__provider_url=data['provider_url'], set__provider_name=data['provider_name'], set__text=status.text, upsert=True)
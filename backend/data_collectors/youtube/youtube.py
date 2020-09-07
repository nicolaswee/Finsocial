import os, requests, json
from mongoengine import connect
from models import *
from youtube_search import YoutubeSearch
try:
    connection
except NameError:
    connection = connect("finsocial", host=os.environ['DB_URI'])

def lambda_handler(event, context):

    youtube_users = YoutubeUsers.objects()
    for user in youtube_users:
        youtubes = json.loads(YoutubeSearch(user.username, max_results=20).to_json())
        for data in youtubes['videos']:
            new_youtube = Youtube.objects(url_suffix=data['url_suffix']).update_one(set__title=data['title'], set__long_desc=data['long_desc'], set__channel=data['channel'], set__duration=str(data['duration']), set__views=str(data['views']), set__provider_name="Youtube", upsert=True)
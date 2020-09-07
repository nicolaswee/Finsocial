import os, requests, json
from mongoengine import connect
from models import *
from TikTokApi import TikTokApi
try:
    connection
except NameError:
    connection = connect("finsocial", host=os.environ['DB_URI'])

api = TikTokApi()

def lambda_handler(event, context):

    tiktok_users = TikTokUsers.objects()
    for user in tiktok_users:
        tiktoks = api.byUsername(user.username)
        for tiktok in tiktoks:
            r = requests.get(f"https://www.tiktok.com/oembed?url=https://www.tiktok.com/@{user.username}/video/{tiktok['id']}")
            if r.content != b'{"status_msg":"Something went wrong"}':
                my_json = r.content.decode('utf8')
                data = json.loads(my_json)
                new_tiktok = TikTok.objects(video_id=tiktok['id']).update_one(set__version=data['version'], set__title=data['title'], set__author_url=data['author_url'], set__author_name=data['author_name'], set__html=data['html'], set__thumbnail_url=data['thumbnail_url'], set__provider_url=data['provider_url'], set__provider_name=data['provider_name'], upsert=True)
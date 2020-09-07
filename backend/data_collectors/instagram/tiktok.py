import os, requests, json
from mongoengine import connect
from models import *
try:
    connection
except NameError:
    connection = connect("finsocial", host=os.environ['DB_URI'])

def lambda_handler(event, context):

    instagram_users = InstagramUsers.objects()
    for user in instagram_users:
        r = requests.get(f"https://api.instagram.com/oembed?url=https://www.instagram.com/p/{user}/")
        my_json = r.content.decode('utf8')
        data = json.loads(my_json)
        new_instagram = Instagram.objects(image_id=user).update_one(set__version=data['version'], set__title=data['title'], set__author_url=data['author_url'], set__author_name=data['author_name'], set__author_id=str(data['author_id']), set__media_id=data['media_id'], set__html=data['html'], set__thumbnail_url=data['thumbnail_url'], set__provider_url=data['provider_url'], set__provider_name=data['provider_name'], upsert=True)
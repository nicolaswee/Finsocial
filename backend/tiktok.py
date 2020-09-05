import os, requests, json
from mongoengine import connect
from models import *
from TikTokApi import TikTokApi



api = TikTokApi()

tiktok_users = TikTokUsers.objects()
for user in tiktok_users:
    tiktoks = api.byUsername(user.username)
    for tiktok in tiktoks:
        r = requests.get(f"https://www.tiktok.com/oembed?url=https://www.tiktok.com/@{user.username}/video/{tiktok['id']}")
        my_json = r.content.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        new_tiktok = TikTok(version=data['version'], title=data['title'], author_url=data['author_url'], author_name=data['author_name'], html=data['html'], thumbnail_url=data['thumbnail_url'], provider_url=data['provider_url'], provider_name=data['provider_name']).update(version=data['version'], title=data['title'], author_url=data['author_url'], author_name=data['author_name'], html=data['html'], thumbnail_url=data['thumbnail_url'], provider_url=data['provider_url'], provider_name=data['provider_name'])
        new_tiktok.save()
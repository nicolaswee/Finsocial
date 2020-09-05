from mongoengine import Document
from mongoengine.fields import (
    StringField
)

class TikTokUsers(Document):

    username = StringField()

    meta = {
        "collection": "tiktok_users"
    }

class TikTok(Document):

    version = StringField()
    title = StringField()
    author_url = StringField()
    author_name = StringField()
    html = StringField()
    thumbnail_url = StringField()
    provider_url = StringField()
    provider_name = StringField()

    meta = {
        "collection": "tiktok"
    }
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
    video_id = StringField()
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

class TwitterUsers(Document):

    username = StringField()

    meta = {
        "collection": "twitter_users"
    }

class Twitter(Document):

    version = StringField()
    url = StringField()
    author_url = StringField()
    author_name = StringField()
    html = StringField()
    provider_url = StringField()
    provider_name = StringField()
    text = StringField()

    meta = {
        "collection": "twitter"
    }

class YoutubeUsers(Document):

    username = StringField()

    meta = {
        "collection": "youtube_users"
    }

class Youtube(Document):

    title = StringField()
    url_suffix = StringField()
    long_desc = StringField()
    channel = StringField()
    duration = StringField()
    views = StringField()
    provider_name = StringField()

    meta = {
        "collection": "youtube"
    }

class InstagramUsers(Document):

    username = StringField()

    meta = {
        "collection": "instagram_users"
    }

class Instagram(Document):

    version = StringField()
    image_id = StringField()
    title = StringField()
    author_url = StringField()
    author_name = StringField()
    author_id = StringField()
    media_id = StringField()
    html = StringField()
    thumbnail_url = StringField()
    provider_url = StringField()
    provider_name = StringField()

    meta = {
        "collection": "instagram"
    }
import os, sys, json, random
from flask import Flask, jsonify, request
from flask_cors import CORS
from bson import ObjectId
from dotenv import load_dotenv
from mongoengine import connect
from models import *
from youtube_search import YoutubeSearch

app = Flask(__name__)
load_dotenv()
CORS(app)
connection = connect("finsocial", host=os.getenv('DB_URL'))

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/get_socials',methods=['GET'])
def get_socials():

    data = []
    data += TikTok.objects.aggregate({"$sample": {"size": 5}})
    data += Twitter.objects.aggregate({"$sample": {"size": 5}})
    data += Youtube.objects.aggregate({"$sample": {"size": 5}})
    data += Instagram.objects.aggregate({"$sample": {"size": 5}})
    random.shuffle(data)

    return JSONEncoder().encode({"data": data}), 200

@app.route('/get_related_news',methods=['GET'])
def get_related_news():

    data = []
    tweets = Twitter.objects.aggregate({"$match": {"author_name": "Financial Times"}},{"$sample": {"size": 5}})

    for tweet in tweets:
        youtubes = json.loads(YoutubeSearch(tweet['text'], max_results=3).to_json())
        data += [{"tweet": tweet, "youtubes": youtubes['videos']}]

    return JSONEncoder().encode({"data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
# Replace this function with code to fetch Instagram comments using access_token, instagram_id, and media_id
import requests
import time
import datetime

class InstagramComments:
    # Constructor to save id, text and time of comment
    def __init__(self, id, text, time):
        self.fb_id = id
        self.text = text
        self.creation_time = time
        self.sentiment_score = -1
        self.magnitude = -1

def fetch_instagram_comments(access_token, media_id):

    # define the instagram end point to get the comments
    instagram_media_comments = f'https://graph.facebook.com/v14.0/{media_id}/comments?access_token={access_token}'

    # make the call to request the comments
    response = requests.get(instagram_media_comments)

    if not response:
        return None

    # get the json response
    data = response.json()

    # To return all the response object
    # return data

    comments_list = data['data']
    comments = []
    for comment in comments_list:
        id = comment['id']
        text = comment['text']
        time = comment['timestamp']
        #convert date string like "2022-11-13T17:40:33+0000" to unix time stamp
        time = time.mktime(datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S+0000").timetuple())
        obj = InstagramComments(id, text, time)
        comments.append(obj)

    return comments

import os

import pymongo
from dotenv import load_dotenv

from swagger_server.controllers.fetch_comments import InstagramComments

load_dotenv()

# Connect to MongoDB
hostname = os.getenv('MONGO_DB_NAME')
port = int(os.getenv('MONGO_DB_PORT'))
username = os.getenv('MONGO_DB_USERNAME')
password = os.getenv('MONGO_DB_PASSWORD')
client = pymongo.MongoClient(hostname, port, username=username, password=password)

db = client['zebra']
collection = db['user1']
sentiment_data = db['comment_sentiment_data']  # collection name
sentiment_data.create_index([("media_id", pymongo.ASCENDING)], unique=True, name="media_id_index")


# Convert comments objects to a list of dictionaries for storage
def convert_comments(comments):
    comments_list = []
    for comment in comments:
        comment_dict = {'fb_id': comment.fb_id, 'text': comment.text, 'creation_time': comment.creation_time,
                        'sentiment_score': comment.sentiment_score, 'magnitude': comment.magnitude}
        comments_list.append(comment_dict)
    return comments_list


# Convert list of dictionaries to comments objects for analysis
def convert_to_comments(comments):
    comments_list = []
    for comment in comments:
        print(comment)
        comment_obj = InstagramComments(comment['fb_id'], comment['text'], comment['creation_time'],
                                        comment['sentiment_score'], comment['magnitude'])
        comments_list.append(comment_obj)
    return comments_list


def store_comments(media_id, comments):
    comments = convert_comments(comments)
    # check if the media id exists
    media = sentiment_data.find_one({'media_id': media_id})

    if media:
        print("media exists")
    else:
        print("media does not exist")
        # preparing new sentiment data
        data = {
            'media_id': media_id,
        }

        # inserting new sentiment data
        sentiment_data.insert_one(data)

    print("Updating comments")
    # unset all old comments and push new list of comments
    update_query = {
        '$set': {'comments': comments}
    }
    # updating the media id with the new analysis
    sentiment_data.update_one({'media_id': media_id}, update_query)

    return comments


def get_all_data(media_id=""):  # get all the analyzed data for the media id

    # fetch the data for the media id
    media = sentiment_data.find_one({'media_id': media_id})

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # pull the data field from the fetched result
    data = media.get('comments', [])
    data = convert_to_comments(data)
    return data


def get_latest_data(media_id=""):  # get the last analyzed data for the media id

    # fetch the data for the media id
    media = sentiment_data.find_one({'media_id': media_id})

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # pull the data field from the fetched result
    data = media.get('comments', [])
    # check to see if the fetched array has data and return the latest/last analysis
    if len(data) > 0:
        return convert_to_comments([data[0]])
    data = convert_to_comments(data)
    return data


def get_data_range(media_id="", start="", end=""):
    # convert the start string to int
    start = int(start)

    # convert the end string to int
    end = int(end)

    # Define the query to find documents by media_id
    query = {
        'media_id': media_id
    }

    # Find the document based on the media_id
    media = sentiment_data.find_one(query)

    # check if media exists
    if not media:
        return {"error": "Unable to retrieve data"}

    # Initialize an empty list to store selected data objects
    selected_data = []

    if media:
        # Get the 'data' array from the document
        data_array = media.get('comments', [])

        # Loop through the 'data' array and select objects with dates in the specified range
        for data_item in data_array:
            date_str = data_item.get('creation_time')
            if date_str:
                date = int(date_str)
                if int(start) <= date <= int(end):
                    selected_data.append(data_item)
    selected_data = convert_to_comments(selected_data)
    return selected_data

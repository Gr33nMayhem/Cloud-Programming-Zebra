import connexion
import six

from swagger_server.controllers.analyze_comments import analyze_sentiments, get_average_magnitude
from swagger_server.controllers.data_model import store_comments, get_all_data, get_latest_data, get_data_range
from swagger_server.controllers.fetch_comments import fetch_instagram_comments
from swagger_server.models import RetrieveAllForMediaSentimentScores
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def create_response_from_comments(media_id, comments):
    average_magnitude = get_average_magnitude(comments)
    analyzeSentimentScores_list = []
    for comment in comments:
        item = RetrieveAllForMediaSentimentScores(id=comment.fb_id, text=comment.text, score=comment.sentiment_score,
                                                  _date=comment.creation_time)
        analyzeSentimentScores_list.append(item)
    response = InlineResponse200(id=media_id, average_magnitude=average_magnitude,
                                 sentiment_scores=analyzeSentimentScores_list)

    return response


def get_analysis_all_get(media_id=None):  # noqa: E501
    """get_analysis_all_get

    get all the comment analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_all(media_id)


def get_analysis_all_post(media_id=None):  # noqa: E501
    """get_analysis_all_post

    get all the comment analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_all(media_id)


def get_analysis_all(media_id):

    comments = get_all_data(media_id)
    return create_response_from_comments(media_id, comments)


def get_analysis_latest_get(media_id=None):  # noqa: E501
    """get_analysis_latest_get

    get latest comments with analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_latest(media_id)


def get_analysis_latest_post(media_id=None):  # noqa: E501
    """get_analysis_latest_post

    get latest comments with analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_latest(media_id)


def get_analysis_latest(media_id):
    comments = get_latest_data(media_id)
    return create_response_from_comments(media_id, comments)


def get_analysis_range_get(media_id=None, start_time=0, end_time=0):  # noqa: E501
    """get_analysis_range_get

    get latest comments with analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str
    :param start_time: start time of comments range
    :type start_time: int
    :param end_time: end time of comments range
    :type end_time: int

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_range(media_id, start_time, end_time)


def get_analysis_range_post(media_id=None, start_time=0, end_time=0):  # noqa: E501
    """get_analysis_range_post

    get latest comments with analysis for the media # noqa: E501

    :param media_id: media ID for which comments are returned
    :type media_id: str
    :param start_time: start time of comments range
    :type start_time: int
    :param end_time: end time of comments range
    :type end_time: int

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return get_analysis_range(media_id, start_time, end_time)


def get_analysis_range(media_id, start_time, end_time):
    comments = get_data_range(media_id, start_time, end_time)
    return create_response_from_comments(media_id, comments)


def retrieve_all_for_media_get(access_token=None, media_id=None):  # noqa: E501
    """retrieve_all_for_media_get

    fetch comments for a media and analyze it # noqa: E501

    :param access_token: access token for the instagram account
    :type access_token: str
    :param media_id: media ID for which comments need analysis
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return retrieve_all(access_token, media_id)


def retrieve_all_for_media_post(access_token=None, media_id=None):  # noqa: E501
    """retrieve_all_for_media_post

    fetch comments for a media and analyze it # noqa: E501

    :param access_token: access token for the instagram account
    :type access_token: str
    :param media_id: media ID for which comments need analysis
    :type media_id: str

    :rtype: List[InlineResponse200]
    """
    if media_id is None:
        return InlineResponse200(media_id, 0, [])
    return retrieve_all(access_token, media_id)


def retrieve_all(access_token, media_id):
    # Fetch instagram comments
    comments = fetch_instagram_comments(access_token, media_id)
    comments = analyze_sentiments(comments)
    average_magnitude = get_average_magnitude(comments)
    analyzeSentimentScores_list = []
    for comment in comments:
        item = RetrieveAllForMediaSentimentScores(id=comment.fb_id, text=comment.text, score=comment.sentiment_score,
                                                  _date=comment.creation_time)
        analyzeSentimentScores_list.append(item)
    store_comments(media_id, comments)
    response = InlineResponse200(id=media_id, average_magnitude=average_magnitude,
                                 sentiment_scores=analyzeSentimentScores_list)

    return response

import connexion
import six

from swagger_server.controllers.analyze_comments import analyze_sentiments, get_average_magnitude
from swagger_server.controllers.data_model import store_comments
from swagger_server.controllers.fetch_comments import fetch_instagram_comments
from swagger_server.models import AnalyzeSentimentScores
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def analyze_get(access_token=None, media_id=None):  # noqa: E501
    """analyze_get

    fetch a comment and analyse sentiment # noqa: E501

    :param access_token: access token for the instagram account
    :type access_token: str
    :param media_id: media ID for which comments need analysis
    :type media_id: str

    :rtype: List[InlineResponse200]
    """

    # Fetch instagram comments
    comments = fetch_instagram_comments(access_token, media_id)
    comments = analyze_sentiments(comments)
    average_magnitude = get_average_magnitude(comments)
    analyzeSentimentScores_list = []
    for comment in comments:
        item = AnalyzeSentimentScores(id=comment.fb_id, text=comment.text, score=comment.sentiment_score,
                                      _date=comment.creation_time)
        analyzeSentimentScores_list.append(item)
    store_comments(analyzeSentimentScores_list)
    response = InlineResponse200(id=media_id, average_magnitude=average_magnitude,
                                 sentiment_scores=analyzeSentimentScores_list)

    return response

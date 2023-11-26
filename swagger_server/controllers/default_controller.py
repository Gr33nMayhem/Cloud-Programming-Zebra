import connexion
import six

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
    return 'do some magic!'

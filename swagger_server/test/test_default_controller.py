# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_analyze_get(self):
        """Test case for analyze_get

        
        """
        query_string = [('access_token', 'access_token_example'),
                        ('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/analyze',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

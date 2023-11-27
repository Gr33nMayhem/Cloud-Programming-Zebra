# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_analysis_all_get(self):
        """Test case for get_analysis_all_get

        
        """
        query_string = [('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_all',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analysis_all_post(self):
        """Test case for get_analysis_all_post

        
        """
        query_string = [('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_all',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analysis_latest_get(self):
        """Test case for get_analysis_latest_get

        
        """
        query_string = [('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_latest',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analysis_latest_post(self):
        """Test case for get_analysis_latest_post

        
        """
        query_string = [('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_latest',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analysis_range_get(self):
        """Test case for get_analysis_range_get

        
        """
        query_string = [('media_id', 'media_id_example'),
                        ('start_time', 56),
                        ('end_time', 56)]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_range',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analysis_range_post(self):
        """Test case for get_analysis_range_post

        
        """
        query_string = [('media_id', 'media_id_example'),
                        ('start_time', 56),
                        ('end_time', 56)]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/get_analysis_range',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_all_for_media_get(self):
        """Test case for retrieve_all_for_media_get

        
        """
        query_string = [('access_token', 'access_token_example'),
                        ('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/retrieve_all_for_media',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_all_for_media_post(self):
        """Test case for retrieve_all_for_media_post

        
        """
        query_string = [('access_token', 'access_token_example'),
                        ('media_id', 'media_id_example')]
        response = self.client.open(
            '/GR33NMAYHEM_1/Project-Zebra/0.1/retrieve_all_for_media',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

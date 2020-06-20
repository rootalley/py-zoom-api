# coding: utf-8

"""
    Zoom API

    The Zoom API allows developers to safely and securely access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [Authorization Guide](https://marketplace.zoom.us/docs/guides/authorization/credentials). All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance you can list all users on an account via `https://api.zoom.us/v2/users/`.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: developersupport@zoom.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.tracking_field_api import TrackingFieldApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrackingFieldApi(unittest.TestCase):
    """TrackingFieldApi unit test stubs"""

    def setUp(self):
        self.api = api.tracking_field_api.TrackingFieldApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_trackingfield_create(self):
        """Test case for trackingfield_create

        Create a Tracking Field  # noqa: E501
        """
        pass

    def test_trackingfield_delete(self):
        """Test case for trackingfield_delete

        Delete a Tracking Field  # noqa: E501
        """
        pass

    def test_trackingfield_get(self):
        """Test case for trackingfield_get

        Get a Tracking Field  # noqa: E501
        """
        pass

    def test_trackingfield_list(self):
        """Test case for trackingfield_list

        List Tracking Fields  # noqa: E501
        """
        pass

    def test_trackingfield_update(self):
        """Test case for trackingfield_update

        Update a Tracking Field  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

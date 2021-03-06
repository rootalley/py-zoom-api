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
from api.devices_api import DevicesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_create(self):
        """Test case for device_create

        Create a H.323/SIP Device  # noqa: E501
        """
        pass

    def test_device_delete(self):
        """Test case for device_delete

        Delete a H.323/SIP Device  # noqa: E501
        """
        pass

    def test_device_list(self):
        """Test case for device_list

        List H.323/SIP Devices  # noqa: E501
        """
        pass

    def test_device_update(self):
        """Test case for device_update

        Update a H.323/SIP Device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

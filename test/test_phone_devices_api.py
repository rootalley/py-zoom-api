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
from api.phone_devices_api import PhoneDevicesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPhoneDevicesApi(unittest.TestCase):
    """PhoneDevicesApi unit test stubs"""

    def setUp(self):
        self.api = api.phone_devices_api.PhoneDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_phone_device(self):
        """Test case for add_phone_device

        Add a Device  # noqa: E501
        """
        pass

    def test_delete_a_device(self):
        """Test case for delete_a_device

        Delete a Device  # noqa: E501
        """
        pass

    def test_get_a_device(self):
        """Test case for get_a_device

        Get Device Details  # noqa: E501
        """
        pass

    def test_list_phone_devices(self):
        """Test case for list_phone_devices

        List Devices  # noqa: E501
        """
        pass

    def test_update_a_device(self):
        """Test case for update_a_device

        Update a Device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

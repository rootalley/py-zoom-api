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
from api.phone_blocked_list_api import PhoneBlockedListApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPhoneBlockedListApi(unittest.TestCase):
    """PhoneBlockedListApi unit test stubs"""

    def setUp(self):
        self.api = api.phone_blocked_list_api.PhoneBlockedListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_anumber_to_blocked_list(self):
        """Test case for add_anumber_to_blocked_list

        Create a Blocked List  # noqa: E501
        """
        pass

    def test_delete_a_blocked_list(self):
        """Test case for delete_a_blocked_list

        Delete a Blocked List  # noqa: E501
        """
        pass

    def test_get_a_blocked_list(self):
        """Test case for get_a_blocked_list

        Get Blocked List Details  # noqa: E501
        """
        pass

    def test_list_blocked_list(self):
        """Test case for list_blocked_list

        List Blocked Lists  # noqa: E501
        """
        pass

    def test_update_blocked_list(self):
        """Test case for update_blocked_list

        Update a Blocked List  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

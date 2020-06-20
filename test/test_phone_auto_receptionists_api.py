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
from api.phone_auto_receptionists_api import PhoneAutoReceptionistsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPhoneAutoReceptionistsApi(unittest.TestCase):
    """PhoneAutoReceptionistsApi unit test stubs"""

    def setUp(self):
        self.api = api.phone_auto_receptionists_api.PhoneAutoReceptionistsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_auto_receptionist(self):
        """Test case for add_auto_receptionist

        Add an Auto Receptionist  # noqa: E501
        """
        pass

    def test_assign_phone_numbers_auto_receptionist(self):
        """Test case for assign_phone_numbers_auto_receptionist

        Assign Phone Numbers  # noqa: E501
        """
        pass

    def test_unassign_a_phone_num_auto_receptionist(self):
        """Test case for unassign_a_phone_num_auto_receptionist

        Unassign a Phone Number  # noqa: E501
        """
        pass

    def test_unassign_all_phone_nums_auto_receptionist(self):
        """Test case for unassign_all_phone_nums_auto_receptionist

        Unassign all Phone Numbers  # noqa: E501
        """
        pass

    def test_update_auto_receptionist(self):
        """Test case for update_auto_receptionist

        Update Auto Receptionist Details   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from api.roles_api import RolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_role_members(self):
        """Test case for add_role_members

        Assign a Role to Members  # noqa: E501
        """
        pass

    def test_create_role(self):
        """Test case for create_role

        Create a Role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete a Role  # noqa: E501
        """
        pass

    def test_get_role_information(self):
        """Test case for get_role_information

        Get Role Information  # noqa: E501
        """
        pass

    def test_role_member_delete(self):
        """Test case for role_member_delete

        Unassign a Member's Role  # noqa: E501
        """
        pass

    def test_role_members(self):
        """Test case for role_members

        List Members in a Role  # noqa: E501
        """
        pass

    def test_roles(self):
        """Test case for roles

        List Roles  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Role Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

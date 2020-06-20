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
from api.sip_phone_api import SIPPhoneApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSIPPhoneApi(unittest.TestCase):
    """SIPPhoneApi unit test stubs"""

    def setUp(self):
        self.api = api.sip_phone_api.SIPPhoneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sip_phone(self):
        """Test case for create_sip_phone

        Create SIP Phone  # noqa: E501
        """
        pass

    def test_delete_sip_phone(self):
        """Test case for delete_sip_phone

        Delete SIP Phone  # noqa: E501
        """
        pass

    def test_list_sip_phones(self):
        """Test case for list_sip_phones

        List SIP Phones  # noqa: E501
        """
        pass

    def test_update_sip_phone(self):
        """Test case for update_sip_phone

        Update SIP Phone  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
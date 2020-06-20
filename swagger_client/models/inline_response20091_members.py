# coding: utf-8

"""
    Zoom API

    The Zoom API allows developers to safely and securely access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [Authorization Guide](https://marketplace.zoom.us/docs/guides/authorization/credentials). All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance you can list all users on an account via `https://api.zoom.us/v2/users/`.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: developersupport@zoom.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse20091Members(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'users': 'list[InlineResponse20091MembersUsers]',
        'common_area_phones': 'list[InlineResponse20091MembersCommonAreaPhones]'
    }

    attribute_map = {
        'users': 'users',
        'common_area_phones': 'common_area_phones'
    }

    def __init__(self, users=None, common_area_phones=None):  # noqa: E501
        """InlineResponse20091Members - a model defined in Swagger"""  # noqa: E501
        self._users = None
        self._common_area_phones = None
        self.discriminator = None
        if users is not None:
            self.users = users
        if common_area_phones is not None:
            self.common_area_phones = common_area_phones

    @property
    def users(self):
        """Gets the users of this InlineResponse20091Members.  # noqa: E501


        :return: The users of this InlineResponse20091Members.  # noqa: E501
        :rtype: list[InlineResponse20091MembersUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this InlineResponse20091Members.


        :param users: The users of this InlineResponse20091Members.  # noqa: E501
        :type: list[InlineResponse20091MembersUsers]
        """

        self._users = users

    @property
    def common_area_phones(self):
        """Gets the common_area_phones of this InlineResponse20091Members.  # noqa: E501


        :return: The common_area_phones of this InlineResponse20091Members.  # noqa: E501
        :rtype: list[InlineResponse20091MembersCommonAreaPhones]
        """
        return self._common_area_phones

    @common_area_phones.setter
    def common_area_phones(self, common_area_phones):
        """Sets the common_area_phones of this InlineResponse20091Members.


        :param common_area_phones: The common_area_phones of this InlineResponse20091Members.  # noqa: E501
        :type: list[InlineResponse20091MembersCommonAreaPhones]
        """

        self._common_area_phones = common_area_phones

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20091Members, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20091Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class GroupMember(object):
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
        'id': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'type': 'type'
    }

    def __init__(self, id=None, email=None, first_name=None, last_name=None, type=None):  # noqa: E501
        """GroupMember - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this GroupMember.  # noqa: E501

        User ID.  # noqa: E501

        :return: The id of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupMember.

        User ID.  # noqa: E501

        :param id: The id of this GroupMember.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this GroupMember.  # noqa: E501

        User email.  # noqa: E501

        :return: The email of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GroupMember.

        User email.  # noqa: E501

        :param email: The email of this GroupMember.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this GroupMember.  # noqa: E501

        User first name.  # noqa: E501

        :return: The first_name of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this GroupMember.

        User first name.  # noqa: E501

        :param first_name: The first_name of this GroupMember.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this GroupMember.  # noqa: E501

        User last name.  # noqa: E501

        :return: The last_name of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this GroupMember.

        User last name.  # noqa: E501

        :param last_name: The last_name of this GroupMember.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def type(self):
        """Gets the type of this GroupMember.  # noqa: E501

        User type.<br> `1` - Basic<br> `2` - Licensed<br>  `3` - On-prem  # noqa: E501

        :return: The type of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupMember.

        User type.<br> `1` - Basic<br> `2` - Licensed<br>  `3` - On-prem  # noqa: E501

        :param type: The type of this GroupMember.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if issubclass(GroupMember, dict):
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
        if not isinstance(other, GroupMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

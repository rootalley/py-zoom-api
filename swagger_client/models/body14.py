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


class Body14(object):
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
        'name': 'str',
        'type': 'int',
        'members': 'list[ChatusersmechannelsMembers]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'members': 'members'
    }

    def __init__(self, name=None, type=None, members=None):  # noqa: E501
        """Body14 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._members = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if members is not None:
            self.members = members

    @property
    def name(self):
        """Gets the name of this Body14.  # noqa: E501

        Name of the channel.  # noqa: E501

        :return: The name of this Body14.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body14.

        Name of the channel.  # noqa: E501

        :param name: The name of this Body14.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Body14.  # noqa: E501

        Type of the channel. The value can be one of the following:<br> `1`: Private channel. In this type of channel, members must be invited to join a channel.<br> `2`: Private channel with members that belong to one Zoom account. Members in this channel should be invited and the members should be from the same organization.<br> `3`: Public channel. Anyone can search for this channel and join the channel.<br> `4`: New chat. This is an instant channel which can be created by adding members to a new chat.   # noqa: E501

        :return: The type of this Body14.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body14.

        Type of the channel. The value can be one of the following:<br> `1`: Private channel. In this type of channel, members must be invited to join a channel.<br> `2`: Private channel with members that belong to one Zoom account. Members in this channel should be invited and the members should be from the same organization.<br> `3`: Public channel. Anyone can search for this channel and join the channel.<br> `4`: New chat. This is an instant channel which can be created by adding members to a new chat.   # noqa: E501

        :param type: The type of this Body14.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def members(self):
        """Gets the members of this Body14.  # noqa: E501

        Member(s) to include in the channel. A max of 5 members can be added to the channel at once with this API.  # noqa: E501

        :return: The members of this Body14.  # noqa: E501
        :rtype: list[ChatusersmechannelsMembers]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Body14.

        Member(s) to include in the channel. A max of 5 members can be added to the channel at once with this API.  # noqa: E501

        :param members: The members of this Body14.  # noqa: E501
        :type: list[ChatusersmechannelsMembers]
        """

        self._members = members

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
        if issubclass(Body14, dict):
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
        if not isinstance(other, Body14):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

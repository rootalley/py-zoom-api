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


class Body12(object):
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
        'message': 'str',
        'to_contact': 'str',
        'to_channel': 'str'
    }

    attribute_map = {
        'message': 'message',
        'to_contact': 'to_contact',
        'to_channel': 'to_channel'
    }

    def __init__(self, message=None, to_contact=None, to_channel=None):  # noqa: E501
        """Body12 - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._to_contact = None
        self._to_channel = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if to_contact is not None:
            self.to_contact = to_contact
        if to_channel is not None:
            self.to_channel = to_channel

    @property
    def message(self):
        """Gets the message of this Body12.  # noqa: E501

        The edited message.  # noqa: E501

        :return: The message of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Body12.

        The edited message.  # noqa: E501

        :param message: The message of this Body12.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def to_contact(self):
        """Gets the to_contact of this Body12.  # noqa: E501

        The email address of the contact to whom the message was sent.<br> You must provide either `to_contact` or `to_channel` parameter in the API request.  # noqa: E501

        :return: The to_contact of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._to_contact

    @to_contact.setter
    def to_contact(self, to_contact):
        """Sets the to_contact of this Body12.

        The email address of the contact to whom the message was sent.<br> You must provide either `to_contact` or `to_channel` parameter in the API request.  # noqa: E501

        :param to_contact: The to_contact of this Body12.  # noqa: E501
        :type: str
        """

        self._to_contact = to_contact

    @property
    def to_channel(self):
        """Gets the to_channel of this Body12.  # noqa: E501

        The Channel ID of the channel where you sent the message.<br>You must provide either `to_contact` or `to_channel` parameter in the API request.  Channel ID can be retrieved from List User's Channels API.   # noqa: E501

        :return: The to_channel of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._to_channel

    @to_channel.setter
    def to_channel(self, to_channel):
        """Sets the to_channel of this Body12.

        The Channel ID of the channel where you sent the message.<br>You must provide either `to_contact` or `to_channel` parameter in the API request.  Channel ID can be retrieved from List User's Channels API.   # noqa: E501

        :param to_channel: The to_channel of this Body12.  # noqa: E501
        :type: str
        """

        self._to_channel = to_channel

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
        if issubclass(Body12, dict):
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
        if not isinstance(other, Body12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

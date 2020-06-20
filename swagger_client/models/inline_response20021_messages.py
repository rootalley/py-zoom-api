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


class InlineResponse20021Messages(object):
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
        'sender': 'str',
        'date_time': 'datetime',
        'action': 'str',
        'action_time': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'sender': 'sender',
        'date_time': 'date_time',
        'action': 'action',
        'action_time': 'action_time'
    }

    def __init__(self, message=None, sender=None, date_time=None, action=None, action_time=None):  # noqa: E501
        """InlineResponse20021Messages - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._sender = None
        self._date_time = None
        self._action = None
        self._action_time = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if sender is not None:
            self.sender = sender
        if date_time is not None:
            self.date_time = date_time
        if action is not None:
            self.action = action
        if action_time is not None:
            self.action_time = action_time

    @property
    def message(self):
        """Gets the message of this InlineResponse20021Messages.  # noqa: E501

        IM chat message content.  # noqa: E501

        :return: The message of this InlineResponse20021Messages.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse20021Messages.

        IM chat message content.  # noqa: E501

        :param message: The message of this InlineResponse20021Messages.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def sender(self):
        """Gets the sender of this InlineResponse20021Messages.  # noqa: E501

        IM chat message sender.  # noqa: E501

        :return: The sender of this InlineResponse20021Messages.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this InlineResponse20021Messages.

        IM chat message sender.  # noqa: E501

        :param sender: The sender of this InlineResponse20021Messages.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse20021Messages.  # noqa: E501

        IM chat message sent time.  # noqa: E501

        :return: The date_time of this InlineResponse20021Messages.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse20021Messages.

        IM chat message sent time.  # noqa: E501

        :param date_time: The date_time of this InlineResponse20021Messages.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def action(self):
        """Gets the action of this InlineResponse20021Messages.  # noqa: E501

        IM chat message action.  # noqa: E501

        :return: The action of this InlineResponse20021Messages.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InlineResponse20021Messages.

        IM chat message action.  # noqa: E501

        :param action: The action of this InlineResponse20021Messages.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def action_time(self):
        """Gets the action_time of this InlineResponse20021Messages.  # noqa: E501

        Action time.  # noqa: E501

        :return: The action_time of this InlineResponse20021Messages.  # noqa: E501
        :rtype: datetime
        """
        return self._action_time

    @action_time.setter
    def action_time(self, action_time):
        """Sets the action_time of this InlineResponse20021Messages.

        Action time.  # noqa: E501

        :param action_time: The action_time of this InlineResponse20021Messages.  # noqa: E501
        :type: datetime
        """

        self._action_time = action_time

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
        if issubclass(InlineResponse20021Messages, dict):
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
        if not isinstance(other, InlineResponse20021Messages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

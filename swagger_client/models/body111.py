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


class Body111(object):
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
        'robot_jid': 'str',
        'user_jid': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'robot_jid': 'robot_jid',
        'user_jid': 'user_jid',
        'account_id': 'account_id'
    }

    def __init__(self, robot_jid=None, user_jid=None, account_id=None):  # noqa: E501
        """Body111 - a model defined in Swagger"""  # noqa: E501
        self._robot_jid = None
        self._user_jid = None
        self._account_id = None
        self.discriminator = None
        self.robot_jid = robot_jid
        if user_jid is not None:
            self.user_jid = user_jid
        self.account_id = account_id

    @property
    def robot_jid(self):
        """Gets the robot_jid of this Body111.  # noqa: E501

        The BotJID found in the Chat Subscription Section on the Features page of your App Dashboard.  # noqa: E501

        :return: The robot_jid of this Body111.  # noqa: E501
        :rtype: str
        """
        return self._robot_jid

    @robot_jid.setter
    def robot_jid(self, robot_jid):
        """Sets the robot_jid of this Body111.

        The BotJID found in the Chat Subscription Section on the Features page of your App Dashboard.  # noqa: E501

        :param robot_jid: The robot_jid of this Body111.  # noqa: E501
        :type: str
        """
        if robot_jid is None:
            raise ValueError("Invalid value for `robot_jid`, must not be `None`")  # noqa: E501

        self._robot_jid = robot_jid

    @property
    def user_jid(self):
        """Gets the user_jid of this Body111.  # noqa: E501

        The UserJID of the user on whose behalf the message is being sent. Used to prevent members of a channel from getting notifications that were set up by a user who has left the channel.  # noqa: E501

        :return: The user_jid of this Body111.  # noqa: E501
        :rtype: str
        """
        return self._user_jid

    @user_jid.setter
    def user_jid(self, user_jid):
        """Sets the user_jid of this Body111.

        The UserJID of the user on whose behalf the message is being sent. Used to prevent members of a channel from getting notifications that were set up by a user who has left the channel.  # noqa: E501

        :param user_jid: The user_jid of this Body111.  # noqa: E501
        :type: str
        """

        self._user_jid = user_jid

    @property
    def account_id(self):
        """Gets the account_id of this Body111.  # noqa: E501

        The AccountID of the Zoom account to which the message was sent. Retrieve this from the Chatbot request sent to your server as shown in the example [here]( https://marketplace.zoom.us/docs/guides/chatbots/sending-messages).  # noqa: E501

        :return: The account_id of this Body111.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Body111.

        The AccountID of the Zoom account to which the message was sent. Retrieve this from the Chatbot request sent to your server as shown in the example [here]( https://marketplace.zoom.us/docs/guides/chatbots/sending-messages).  # noqa: E501

        :param account_id: The account_id of this Body111.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if issubclass(Body111, dict):
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
        if not isinstance(other, Body111):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

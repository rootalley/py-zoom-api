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


class Body107(object):
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
        'to_jid': 'str',
        'account_id': 'str',
        'content': 'object',
        'visible_to_user': 'str',
        'user_jid': 'str',
        'is_markdown_support': 'bool'
    }

    attribute_map = {
        'robot_jid': 'robot_jid',
        'to_jid': 'to_jid',
        'account_id': 'account_id',
        'content': 'content',
        'visible_to_user': 'visible_to_user',
        'user_jid': 'user_jid',
        'is_markdown_support': 'is_markdown_support'
    }

    def __init__(self, robot_jid=None, to_jid=None, account_id=None, content=None, visible_to_user=None, user_jid=None, is_markdown_support=None):  # noqa: E501
        """Body107 - a model defined in Swagger"""  # noqa: E501
        self._robot_jid = None
        self._to_jid = None
        self._account_id = None
        self._content = None
        self._visible_to_user = None
        self._user_jid = None
        self._is_markdown_support = None
        self.discriminator = None
        self.robot_jid = robot_jid
        self.to_jid = to_jid
        self.account_id = account_id
        self.content = content
        if visible_to_user is not None:
            self.visible_to_user = visible_to_user
        if user_jid is not None:
            self.user_jid = user_jid
        if is_markdown_support is not None:
            self.is_markdown_support = is_markdown_support

    @property
    def robot_jid(self):
        """Gets the robot_jid of this Body107.  # noqa: E501

        Robot JID created when enabling chatbot features on your marketplace app.  # noqa: E501

        :return: The robot_jid of this Body107.  # noqa: E501
        :rtype: str
        """
        return self._robot_jid

    @robot_jid.setter
    def robot_jid(self, robot_jid):
        """Sets the robot_jid of this Body107.

        Robot JID created when enabling chatbot features on your marketplace app.  # noqa: E501

        :param robot_jid: The robot_jid of this Body107.  # noqa: E501
        :type: str
        """
        if robot_jid is None:
            raise ValueError("Invalid value for `robot_jid`, must not be `None`")  # noqa: E501

        self._robot_jid = robot_jid

    @property
    def to_jid(self):
        """Gets the to_jid of this Body107.  # noqa: E501

        Unique JID of reciever. Can be a group or user.  # noqa: E501

        :return: The to_jid of this Body107.  # noqa: E501
        :rtype: str
        """
        return self._to_jid

    @to_jid.setter
    def to_jid(self, to_jid):
        """Sets the to_jid of this Body107.

        Unique JID of reciever. Can be a group or user.  # noqa: E501

        :param to_jid: The to_jid of this Body107.  # noqa: E501
        :type: str
        """
        if to_jid is None:
            raise ValueError("Invalid value for `to_jid`, must not be `None`")  # noqa: E501

        self._to_jid = to_jid

    @property
    def account_id(self):
        """Gets the account_id of this Body107.  # noqa: E501

        Account ID of the authorized account.  # noqa: E501

        :return: The account_id of this Body107.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Body107.

        Account ID of the authorized account.  # noqa: E501

        :param account_id: The account_id of this Body107.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def content(self):
        """Gets the content of this Body107.  # noqa: E501

        JSON template describing how the message should be displayed for the user. For more information please see our [\"Send Message\" templates](https://marketplace.zoom.us/docs/guides/chatbots/sending-messages#example-request).  # noqa: E501

        :return: The content of this Body107.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Body107.

        JSON template describing how the message should be displayed for the user. For more information please see our [\"Send Message\" templates](https://marketplace.zoom.us/docs/guides/chatbots/sending-messages#example-request).  # noqa: E501

        :param content: The content of this Body107.  # noqa: E501
        :type: object
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def visible_to_user(self):
        """Gets the visible_to_user of this Body107.  # noqa: E501

        **Optional**<br>Allow a Chatbot to send a message to a group channel, but have only one designated person in that group channel see the message by providing the person's UserID in this field.  # noqa: E501

        :return: The visible_to_user of this Body107.  # noqa: E501
        :rtype: str
        """
        return self._visible_to_user

    @visible_to_user.setter
    def visible_to_user(self, visible_to_user):
        """Sets the visible_to_user of this Body107.

        **Optional**<br>Allow a Chatbot to send a message to a group channel, but have only one designated person in that group channel see the message by providing the person's UserID in this field.  # noqa: E501

        :param visible_to_user: The visible_to_user of this Body107.  # noqa: E501
        :type: str
        """

        self._visible_to_user = visible_to_user

    @property
    def user_jid(self):
        """Gets the user_jid of this Body107.  # noqa: E501

        **Optional**<br> The UserJID of the user on whose behalf the message is being sent. Use this field to prevent members of a channel from getting notifications that were set up by a user who has left the channel.  # noqa: E501

        :return: The user_jid of this Body107.  # noqa: E501
        :rtype: str
        """
        return self._user_jid

    @user_jid.setter
    def user_jid(self, user_jid):
        """Sets the user_jid of this Body107.

        **Optional**<br> The UserJID of the user on whose behalf the message is being sent. Use this field to prevent members of a channel from getting notifications that were set up by a user who has left the channel.  # noqa: E501

        :param user_jid: The user_jid of this Body107.  # noqa: E501
        :type: str
        """

        self._user_jid = user_jid

    @property
    def is_markdown_support(self):
        """Gets the is_markdown_support of this Body107.  # noqa: E501

        **Optional**<br> Applies the markdown parser to your chatbot message if the value of this field is set to `true`.<br> To learn more, refer to the Chatbot message [markdown reference](https://marketplace.zoom.us/docs/guides/chatbots/customizing-messages/message-with-markdown).  # noqa: E501

        :return: The is_markdown_support of this Body107.  # noqa: E501
        :rtype: bool
        """
        return self._is_markdown_support

    @is_markdown_support.setter
    def is_markdown_support(self, is_markdown_support):
        """Sets the is_markdown_support of this Body107.

        **Optional**<br> Applies the markdown parser to your chatbot message if the value of this field is set to `true`.<br> To learn more, refer to the Chatbot message [markdown reference](https://marketplace.zoom.us/docs/guides/chatbots/customizing-messages/message-with-markdown).  # noqa: E501

        :param is_markdown_support: The is_markdown_support of this Body107.  # noqa: E501
        :type: bool
        """

        self._is_markdown_support = is_markdown_support

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
        if issubclass(Body107, dict):
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
        if not isinstance(other, Body107):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

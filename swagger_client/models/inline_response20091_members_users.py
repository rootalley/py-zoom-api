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


class InlineResponse20091MembersUsers(object):
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
        'name': 'str',
        'level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'level': 'level'
    }

    def __init__(self, id=None, name=None, level=None):  # noqa: E501
        """InlineResponse20091MembersUsers - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._level = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level

    @property
    def id(self):
        """Gets the id of this InlineResponse20091MembersUsers.  # noqa: E501

        User ID: Unique Identifier of the user.  # noqa: E501

        :return: The id of this InlineResponse20091MembersUsers.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20091MembersUsers.

        User ID: Unique Identifier of the user.  # noqa: E501

        :param id: The id of this InlineResponse20091MembersUsers.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20091MembersUsers.  # noqa: E501

        Name of the user.  # noqa: E501

        :return: The name of this InlineResponse20091MembersUsers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20091MembersUsers.

        Name of the user.  # noqa: E501

        :param name: The name of this InlineResponse20091MembersUsers.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def level(self):
        """Gets the level of this InlineResponse20091MembersUsers.  # noqa: E501

        Level of the user. The value can be one of the following:<br> `manager`: A call queue manager has the privilege to change call queue settings, policy settings and manage recordings and voicemail inbox. There can only be one manager for each call queue.<br><br> `user`: Regular user without the privileges of a manager.  # noqa: E501

        :return: The level of this InlineResponse20091MembersUsers.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this InlineResponse20091MembersUsers.

        Level of the user. The value can be one of the following:<br> `manager`: A call queue manager has the privilege to change call queue settings, policy settings and manage recordings and voicemail inbox. There can only be one manager for each call queue.<br><br> `user`: Regular user without the privileges of a manager.  # noqa: E501

        :param level: The level of this InlineResponse20091MembersUsers.  # noqa: E501
        :type: str
        """
        allowed_values = ["manager", "user"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

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
        if issubclass(InlineResponse20091MembersUsers, dict):
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
        if not isinstance(other, InlineResponse20091MembersUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

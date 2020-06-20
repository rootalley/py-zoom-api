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


class InlineResponse2013(object):
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
        'ids': 'list[str]',
        'added_at': 'datetime'
    }

    attribute_map = {
        'ids': 'ids',
        'added_at': 'added_at'
    }

    def __init__(self, ids=None, added_at=None):  # noqa: E501
        """InlineResponse2013 - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._added_at = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids
        if added_at is not None:
            self.added_at = added_at

    @property
    def ids(self):
        """Gets the ids of this InlineResponse2013.  # noqa: E501

        Member Ids of the members.  # noqa: E501

        :return: The ids of this InlineResponse2013.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this InlineResponse2013.

        Member Ids of the members.  # noqa: E501

        :param ids: The ids of this InlineResponse2013.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def added_at(self):
        """Gets the added_at of this InlineResponse2013.  # noqa: E501

        The date and time at which the member(s) are added to the channe.  # noqa: E501

        :return: The added_at of this InlineResponse2013.  # noqa: E501
        :rtype: datetime
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at):
        """Sets the added_at of this InlineResponse2013.

        The date and time at which the member(s) are added to the channe.  # noqa: E501

        :param added_at: The added_at of this InlineResponse2013.  # noqa: E501
        :type: datetime
        """

        self._added_at = added_at

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
        if issubclass(InlineResponse2013, dict):
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
        if not isinstance(other, InlineResponse2013):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
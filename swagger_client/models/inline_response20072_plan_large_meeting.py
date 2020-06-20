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


class InlineResponse20072PlanLargeMeeting(object):
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
        'type': 'str',
        'hosts': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'type': 'type',
        'hosts': 'hosts',
        'usage': 'usage'
    }

    def __init__(self, type=None, hosts=None, usage=None):  # noqa: E501
        """InlineResponse20072PlanLargeMeeting - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._hosts = None
        self._usage = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if hosts is not None:
            self.hosts = hosts
        if usage is not None:
            self.usage = usage

    @property
    def type(self):
        """Gets the type of this InlineResponse20072PlanLargeMeeting.  # noqa: E501

        Large meeting Plan Type  # noqa: E501

        :return: The type of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20072PlanLargeMeeting.

        Large meeting Plan Type  # noqa: E501

        :param type: The type of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def hosts(self):
        """Gets the hosts of this InlineResponse20072PlanLargeMeeting.  # noqa: E501

        Number of hosts in this plan.   # noqa: E501

        :return: The hosts of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :rtype: int
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this InlineResponse20072PlanLargeMeeting.

        Number of hosts in this plan.   # noqa: E501

        :param hosts: The hosts of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :type: int
        """

        self._hosts = hosts

    @property
    def usage(self):
        """Gets the usage of this InlineResponse20072PlanLargeMeeting.  # noqa: E501

        Number of usages for this account plan.  # noqa: E501

        :return: The usage of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this InlineResponse20072PlanLargeMeeting.

        Number of usages for this account plan.  # noqa: E501

        :param usage: The usage of this InlineResponse20072PlanLargeMeeting.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if issubclass(InlineResponse20072PlanLargeMeeting, dict):
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
        if not isinstance(other, InlineResponse20072PlanLargeMeeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

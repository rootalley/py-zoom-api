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


class InlineResponse20072PlanRecording(object):
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
        'free_storage': 'str',
        'free_storage_usage': 'str',
        'plan_storage': 'str',
        'plan_storage_usage': 'str',
        'plan_storage_exceed': 'str'
    }

    attribute_map = {
        'type': 'type',
        'free_storage': 'free_storage',
        'free_storage_usage': 'free_storage_usage',
        'plan_storage': 'plan_storage',
        'plan_storage_usage': 'plan_storage_usage',
        'plan_storage_exceed': 'plan_storage_exceed'
    }

    def __init__(self, type=None, free_storage=None, free_storage_usage=None, plan_storage=None, plan_storage_usage=None, plan_storage_exceed=None):  # noqa: E501
        """InlineResponse20072PlanRecording - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._free_storage = None
        self._free_storage_usage = None
        self._plan_storage = None
        self._plan_storage_usage = None
        self._plan_storage_exceed = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if free_storage is not None:
            self.free_storage = free_storage
        if free_storage_usage is not None:
            self.free_storage_usage = free_storage_usage
        if plan_storage is not None:
            self.plan_storage = plan_storage
        if plan_storage_usage is not None:
            self.plan_storage_usage = plan_storage_usage
        if plan_storage_exceed is not None:
            self.plan_storage_exceed = plan_storage_exceed

    @property
    def type(self):
        """Gets the type of this InlineResponse20072PlanRecording.  # noqa: E501

        Recording plan type.  # noqa: E501

        :return: The type of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20072PlanRecording.

        Recording plan type.  # noqa: E501

        :param type: The type of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def free_storage(self):
        """Gets the free_storage of this InlineResponse20072PlanRecording.  # noqa: E501

        Recording free storage.  # noqa: E501

        :return: The free_storage of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._free_storage

    @free_storage.setter
    def free_storage(self, free_storage):
        """Sets the free_storage of this InlineResponse20072PlanRecording.

        Recording free storage.  # noqa: E501

        :param free_storage: The free_storage of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._free_storage = free_storage

    @property
    def free_storage_usage(self):
        """Gets the free_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501

        Amount of free storage used.  # noqa: E501

        :return: The free_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._free_storage_usage

    @free_storage_usage.setter
    def free_storage_usage(self, free_storage_usage):
        """Sets the free_storage_usage of this InlineResponse20072PlanRecording.

        Amount of free storage used.  # noqa: E501

        :param free_storage_usage: The free_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._free_storage_usage = free_storage_usage

    @property
    def plan_storage(self):
        """Gets the plan_storage of this InlineResponse20072PlanRecording.  # noqa: E501

        Recording plan storage.  # noqa: E501

        :return: The plan_storage of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._plan_storage

    @plan_storage.setter
    def plan_storage(self, plan_storage):
        """Sets the plan_storage of this InlineResponse20072PlanRecording.

        Recording plan storage.  # noqa: E501

        :param plan_storage: The plan_storage of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._plan_storage = plan_storage

    @property
    def plan_storage_usage(self):
        """Gets the plan_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501

        Recording storage usage.  # noqa: E501

        :return: The plan_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._plan_storage_usage

    @plan_storage_usage.setter
    def plan_storage_usage(self, plan_storage_usage):
        """Sets the plan_storage_usage of this InlineResponse20072PlanRecording.

        Recording storage usage.  # noqa: E501

        :param plan_storage_usage: The plan_storage_usage of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._plan_storage_usage = plan_storage_usage

    @property
    def plan_storage_exceed(self):
        """Gets the plan_storage_exceed of this InlineResponse20072PlanRecording.  # noqa: E501


        :return: The plan_storage_exceed of this InlineResponse20072PlanRecording.  # noqa: E501
        :rtype: str
        """
        return self._plan_storage_exceed

    @plan_storage_exceed.setter
    def plan_storage_exceed(self, plan_storage_exceed):
        """Sets the plan_storage_exceed of this InlineResponse20072PlanRecording.


        :param plan_storage_exceed: The plan_storage_exceed of this InlineResponse20072PlanRecording.  # noqa: E501
        :type: str
        """

        self._plan_storage_exceed = plan_storage_exceed

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
        if issubclass(InlineResponse20072PlanRecording, dict):
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
        if not isinstance(other, InlineResponse20072PlanRecording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
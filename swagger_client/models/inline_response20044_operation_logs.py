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


class InlineResponse20044OperationLogs(object):
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
        'time': 'datetime',
        'operator': 'str',
        'category_type': 'str',
        'action': 'str',
        'operation_detail': 'str'
    }

    attribute_map = {
        'time': 'time',
        'operator': 'operator',
        'category_type': 'category_type',
        'action': 'action',
        'operation_detail': 'operation_detail'
    }

    def __init__(self, time=None, operator=None, category_type=None, action=None, operation_detail=None):  # noqa: E501
        """InlineResponse20044OperationLogs - a model defined in Swagger"""  # noqa: E501
        self._time = None
        self._operator = None
        self._category_type = None
        self._action = None
        self._operation_detail = None
        self.discriminator = None
        if time is not None:
            self.time = time
        if operator is not None:
            self.operator = operator
        if category_type is not None:
            self.category_type = category_type
        if action is not None:
            self.action = action
        if operation_detail is not None:
            self.operation_detail = operation_detail

    @property
    def time(self):
        """Gets the time of this InlineResponse20044OperationLogs.  # noqa: E501

        The time at which the operation was performed.  # noqa: E501

        :return: The time of this InlineResponse20044OperationLogs.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20044OperationLogs.

        The time at which the operation was performed.  # noqa: E501

        :param time: The time of this InlineResponse20044OperationLogs.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def operator(self):
        """Gets the operator of this InlineResponse20044OperationLogs.  # noqa: E501

        The user who performed the operation.  # noqa: E501

        :return: The operator of this InlineResponse20044OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this InlineResponse20044OperationLogs.

        The user who performed the operation.  # noqa: E501

        :param operator: The operator of this InlineResponse20044OperationLogs.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def category_type(self):
        """Gets the category_type of this InlineResponse20044OperationLogs.  # noqa: E501

        Category type  # noqa: E501

        :return: The category_type of this InlineResponse20044OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this InlineResponse20044OperationLogs.

        Category type  # noqa: E501

        :param category_type: The category_type of this InlineResponse20044OperationLogs.  # noqa: E501
        :type: str
        """

        self._category_type = category_type

    @property
    def action(self):
        """Gets the action of this InlineResponse20044OperationLogs.  # noqa: E501

        Action  # noqa: E501

        :return: The action of this InlineResponse20044OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InlineResponse20044OperationLogs.

        Action  # noqa: E501

        :param action: The action of this InlineResponse20044OperationLogs.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def operation_detail(self):
        """Gets the operation_detail of this InlineResponse20044OperationLogs.  # noqa: E501

        Operation detail  # noqa: E501

        :return: The operation_detail of this InlineResponse20044OperationLogs.  # noqa: E501
        :rtype: str
        """
        return self._operation_detail

    @operation_detail.setter
    def operation_detail(self, operation_detail):
        """Sets the operation_detail of this InlineResponse20044OperationLogs.

        Operation detail  # noqa: E501

        :param operation_detail: The operation_detail of this InlineResponse20044OperationLogs.  # noqa: E501
        :type: str
        """

        self._operation_detail = operation_detail

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
        if issubclass(InlineResponse20044OperationLogs, dict):
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
        if not isinstance(other, InlineResponse20044OperationLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

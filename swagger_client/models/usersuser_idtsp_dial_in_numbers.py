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


class UsersuserIdtspDialInNumbers(object):
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
        'code': 'str',
        'number': 'str',
        'type': 'str',
        'country_label': 'str'
    }

    attribute_map = {
        'code': 'code',
        'number': 'number',
        'type': 'type',
        'country_label': 'country_label'
    }

    def __init__(self, code=None, number=None, type=None, country_label=None):  # noqa: E501
        """UsersuserIdtspDialInNumbers - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._number = None
        self._type = None
        self._country_label = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type
        if country_label is not None:
            self.country_label = country_label

    @property
    def code(self):
        """Gets the code of this UsersuserIdtspDialInNumbers.  # noqa: E501

        Country code.  # noqa: E501

        :return: The code of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UsersuserIdtspDialInNumbers.

        Country code.  # noqa: E501

        :param code: The code of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def number(self):
        """Gets the number of this UsersuserIdtspDialInNumbers.  # noqa: E501

        Dial-in number: length is less than 16.  # noqa: E501

        :return: The number of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this UsersuserIdtspDialInNumbers.

        Dial-in number: length is less than 16.  # noqa: E501

        :param number: The number of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def type(self):
        """Gets the type of this UsersuserIdtspDialInNumbers.  # noqa: E501

        Dial-in number types:<br>`toll` - Toll number.<br>`tollfree` -Toll free number.<br> `media_link` - Media link.  # noqa: E501

        :return: The type of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UsersuserIdtspDialInNumbers.

        Dial-in number types:<br>`toll` - Toll number.<br>`tollfree` -Toll free number.<br> `media_link` - Media link.  # noqa: E501

        :param type: The type of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :type: str
        """
        allowed_values = ["toll", "tollfree", "media_link"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def country_label(self):
        """Gets the country_label of this UsersuserIdtspDialInNumbers.  # noqa: E501

        Country Label, if passed, will display in place of code.  # noqa: E501

        :return: The country_label of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :rtype: str
        """
        return self._country_label

    @country_label.setter
    def country_label(self, country_label):
        """Sets the country_label of this UsersuserIdtspDialInNumbers.

        Country Label, if passed, will display in place of code.  # noqa: E501

        :param country_label: The country_label of this UsersuserIdtspDialInNumbers.  # noqa: E501
        :type: str
        """

        self._country_label = country_label

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
        if issubclass(UsersuserIdtspDialInNumbers, dict):
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
        if not isinstance(other, UsersuserIdtspDialInNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

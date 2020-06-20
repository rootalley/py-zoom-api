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


class InlineResponse20082(object):
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
        'total_records': 'int',
        'phone_numbers': 'list[InlineResponse20082PhoneNumbers]'
    }

    attribute_map = {
        'total_records': 'total_records',
        'phone_numbers': 'phone_numbers'
    }

    def __init__(self, total_records=None, phone_numbers=None):  # noqa: E501
        """InlineResponse20082 - a model defined in Swagger"""  # noqa: E501
        self._total_records = None
        self._phone_numbers = None
        self.discriminator = None
        if total_records is not None:
            self.total_records = total_records
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponse20082.  # noqa: E501

        Total number of records returned.  # noqa: E501

        :return: The total_records of this InlineResponse20082.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponse20082.

        Total number of records returned.  # noqa: E501

        :param total_records: The total_records of this InlineResponse20082.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse20082.  # noqa: E501


        :return: The phone_numbers of this InlineResponse20082.  # noqa: E501
        :rtype: list[InlineResponse20082PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse20082.


        :param phone_numbers: The phone_numbers of this InlineResponse20082.  # noqa: E501
        :type: list[InlineResponse20082PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

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
        if issubclass(InlineResponse20082, dict):
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
        if not isinstance(other, InlineResponse20082):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

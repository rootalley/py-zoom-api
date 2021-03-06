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


class Body183(object):
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
        'match_type': 'str',
        'phone_number': 'str',
        'block_type': 'str',
        'status': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'match_type': 'match_type',
        'phone_number': 'phone_number',
        'block_type': 'block_type',
        'status': 'status',
        'comment': 'comment'
    }

    def __init__(self, match_type=None, phone_number=None, block_type=None, status=None, comment=None):  # noqa: E501
        """Body183 - a model defined in Swagger"""  # noqa: E501
        self._match_type = None
        self._phone_number = None
        self._block_type = None
        self._status = None
        self._comment = None
        self.discriminator = None
        if match_type is not None:
            self.match_type = match_type
        if phone_number is not None:
            self.phone_number = phone_number
        if block_type is not None:
            self.block_type = block_type
        if status is not None:
            self.status = status
        if comment is not None:
            self.comment = comment

    @property
    def match_type(self):
        """Gets the match_type of this Body183.  # noqa: E501

        Specify the match type for the blocked list. The values can be one of the following:<br><br> `phoneNumber`: Choose this option (Phone Number Match) if you want to block a specific phone number. Then, in the `phone_number` field, provide the phone number along with the country code.<br><br> `prefix`: Choose this option (Prefix Match) if you want to block all numbers with a specific country code and area code. Next, in the `phone_number` field, enter a country code as part of the prefix. For example, entering 1907 blocks numbers with country code 1 and area code 907.  # noqa: E501

        :return: The match_type of this Body183.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this Body183.

        Specify the match type for the blocked list. The values can be one of the following:<br><br> `phoneNumber`: Choose this option (Phone Number Match) if you want to block a specific phone number. Then, in the `phone_number` field, provide the phone number along with the country code.<br><br> `prefix`: Choose this option (Prefix Match) if you want to block all numbers with a specific country code and area code. Next, in the `phone_number` field, enter a country code as part of the prefix. For example, entering 1907 blocks numbers with country code 1 and area code 907.  # noqa: E501

        :param match_type: The match_type of this Body183.  # noqa: E501
        :type: str
        """
        allowed_values = ["phoneNumber", "prefix"]  # noqa: E501
        if match_type not in allowed_values:
            raise ValueError(
                "Invalid value for `match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(match_type, allowed_values)
            )

        self._match_type = match_type

    @property
    def phone_number(self):
        """Gets the phone_number of this Body183.  # noqa: E501

        The phone number to be blocked if you passed \"phoneNumber\" as the value for the `match_type` field. If you passed \"prefix\" as the value for the `match_type` field, provide the prefix of the phone number here including the country code. For example, entering 1905 blocks numbers with country code 1 and area code 905.   # noqa: E501

        :return: The phone_number of this Body183.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Body183.

        The phone number to be blocked if you passed \"phoneNumber\" as the value for the `match_type` field. If you passed \"prefix\" as the value for the `match_type` field, provide the prefix of the phone number here including the country code. For example, entering 1905 blocks numbers with country code 1 and area code 905.   # noqa: E501

        :param phone_number: The phone_number of this Body183.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def block_type(self):
        """Gets the block_type of this Body183.  # noqa: E501

        State whether you want the block type to be inbound or outbound.<br> `inbound`: Pass this value to prevent the blocked number or prefix from calling in to phone users.<br> `outbound`: Pass this value to prevent phone users from calling the blocked number or prefix.  # noqa: E501

        :return: The block_type of this Body183.  # noqa: E501
        :rtype: str
        """
        return self._block_type

    @block_type.setter
    def block_type(self, block_type):
        """Sets the block_type of this Body183.

        State whether you want the block type to be inbound or outbound.<br> `inbound`: Pass this value to prevent the blocked number or prefix from calling in to phone users.<br> `outbound`: Pass this value to prevent phone users from calling the blocked number or prefix.  # noqa: E501

        :param block_type: The block_type of this Body183.  # noqa: E501
        :type: str
        """
        allowed_values = ["inbound", "outbound"]  # noqa: E501
        if block_type not in allowed_values:
            raise ValueError(
                "Invalid value for `block_type` ({0}), must be one of {1}"  # noqa: E501
                .format(block_type, allowed_values)
            )

        self._block_type = block_type

    @property
    def status(self):
        """Gets the status of this Body183.  # noqa: E501

        Enable or disable the blocking. One of the following values are allowed:<br> `active`: Keep the blocking active.<br> `inactive`: Disable the blocking.  # noqa: E501

        :return: The status of this Body183.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body183.

        Enable or disable the blocking. One of the following values are allowed:<br> `active`: Keep the blocking active.<br> `inactive`: Disable the blocking.  # noqa: E501

        :param status: The status of this Body183.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def comment(self):
        """Gets the comment of this Body183.  # noqa: E501

        Provide a comment to help you identify the blocked number or prefix.  # noqa: E501

        :return: The comment of this Body183.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body183.

        Provide a comment to help you identify the blocked number or prefix.  # noqa: E501

        :param comment: The comment of this Body183.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(Body183, dict):
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
        if not isinstance(other, Body183):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

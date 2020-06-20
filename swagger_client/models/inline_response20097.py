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


class InlineResponse20097(object):
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
        'next_page_token': 'str',
        'page_size': 'int',
        'total_records': 'int',
        'blocked_list': 'list[InlineResponse20097BlockedList]'
    }

    attribute_map = {
        'next_page_token': 'next_page_token',
        'page_size': 'page_size',
        'total_records': 'total_records',
        'blocked_list': 'blocked_list'
    }

    def __init__(self, next_page_token=None, page_size=None, total_records=None, blocked_list=None):  # noqa: E501
        """InlineResponse20097 - a model defined in Swagger"""  # noqa: E501
        self._next_page_token = None
        self._page_size = None
        self._total_records = None
        self._blocked_list = None
        self.discriminator = None
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if page_size is not None:
            self.page_size = page_size
        if total_records is not None:
            self.total_records = total_records
        if blocked_list is not None:
            self.blocked_list = blocked_list

    @property
    def next_page_token(self):
        """Gets the next_page_token of this InlineResponse20097.  # noqa: E501

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :return: The next_page_token of this InlineResponse20097.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this InlineResponse20097.

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :param next_page_token: The next_page_token of this InlineResponse20097.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def page_size(self):
        """Gets the page_size of this InlineResponse20097.  # noqa: E501

        The total number of records returned from a single API call.  # noqa: E501

        :return: The page_size of this InlineResponse20097.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineResponse20097.

        The total number of records returned from a single API call.  # noqa: E501

        :param page_size: The page_size of this InlineResponse20097.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_records(self):
        """Gets the total_records of this InlineResponse20097.  # noqa: E501

        The total number of records found for this query.  # noqa: E501

        :return: The total_records of this InlineResponse20097.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this InlineResponse20097.

        The total number of records found for this query.  # noqa: E501

        :param total_records: The total_records of this InlineResponse20097.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def blocked_list(self):
        """Gets the blocked_list of this InlineResponse20097.  # noqa: E501


        :return: The blocked_list of this InlineResponse20097.  # noqa: E501
        :rtype: list[InlineResponse20097BlockedList]
        """
        return self._blocked_list

    @blocked_list.setter
    def blocked_list(self, blocked_list):
        """Sets the blocked_list of this InlineResponse20097.


        :param blocked_list: The blocked_list of this InlineResponse20097.  # noqa: E501
        :type: list[InlineResponse20097BlockedList]
        """

        self._blocked_list = blocked_list

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
        if issubclass(InlineResponse20097, dict):
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
        if not isinstance(other, InlineResponse20097):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

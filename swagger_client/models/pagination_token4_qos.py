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


class PaginationToken4Qos(object):
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
        'page_count': 'int',
        'page_size': 'int',
        'total_records': 'int',
        'next_page_token': 'str'
    }

    attribute_map = {
        'page_count': 'page_count',
        'page_size': 'page_size',
        'total_records': 'total_records',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, page_count=None, page_size=None, total_records=None, next_page_token=None):  # noqa: E501
        """PaginationToken4Qos - a model defined in Swagger"""  # noqa: E501
        self._page_count = None
        self._page_size = None
        self._total_records = None
        self._next_page_token = None
        self.discriminator = None
        if page_count is not None:
            self.page_count = page_count
        if page_size is not None:
            self.page_size = page_size
        if total_records is not None:
            self.total_records = total_records
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def page_count(self):
        """Gets the page_count of this PaginationToken4Qos.  # noqa: E501

        The number of pages returned for the request made.  # noqa: E501

        :return: The page_count of this PaginationToken4Qos.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this PaginationToken4Qos.

        The number of pages returned for the request made.  # noqa: E501

        :param page_count: The page_count of this PaginationToken4Qos.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def page_size(self):
        """Gets the page_size of this PaginationToken4Qos.  # noqa: E501

        The number of items per page.  # noqa: E501

        :return: The page_size of this PaginationToken4Qos.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PaginationToken4Qos.

        The number of items per page.  # noqa: E501

        :param page_size: The page_size of this PaginationToken4Qos.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_records(self):
        """Gets the total_records of this PaginationToken4Qos.  # noqa: E501

        The number of all records available across pages.  # noqa: E501

        :return: The total_records of this PaginationToken4Qos.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this PaginationToken4Qos.

        The number of all records available across pages.  # noqa: E501

        :param total_records: The total_records of this PaginationToken4Qos.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def next_page_token(self):
        """Gets the next_page_token of this PaginationToken4Qos.  # noqa: E501

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :return: The next_page_token of this PaginationToken4Qos.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this PaginationToken4Qos.

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes.  # noqa: E501

        :param next_page_token: The next_page_token of this PaginationToken4Qos.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if issubclass(PaginationToken4Qos, dict):
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
        if not isinstance(other, PaginationToken4Qos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
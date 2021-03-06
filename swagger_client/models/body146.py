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


class Body146(object):
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
        'structures': 'list[str]'
    }

    attribute_map = {
        'structures': 'structures'
    }

    def __init__(self, structures=None):  # noqa: E501
        """Body146 - a model defined in Swagger"""  # noqa: E501
        self._structures = None
        self.discriminator = None
        if structures is not None:
            self.structures = structures

    @property
    def structures(self):
        """Gets the structures of this Body146.  # noqa: E501

        Location Structure. The value can be either one or a combination of the following strings separated by comma: `country`, `state`, `city`, `campus`, `building`, `floor`  # noqa: E501

        :return: The structures of this Body146.  # noqa: E501
        :rtype: list[str]
        """
        return self._structures

    @structures.setter
    def structures(self, structures):
        """Sets the structures of this Body146.

        Location Structure. The value can be either one or a combination of the following strings separated by comma: `country`, `state`, `city`, `campus`, `building`, `floor`  # noqa: E501

        :param structures: The structures of this Body146.  # noqa: E501
        :type: list[str]
        """

        self._structures = structures

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
        if issubclass(Body146, dict):
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
        if not isinstance(other, Body146):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

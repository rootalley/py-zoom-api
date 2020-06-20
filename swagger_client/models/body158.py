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


class Body158(object):
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
        'location_id': 'str'
    }

    attribute_map = {
        'location_id': 'location_id'
    }

    def __init__(self, location_id=None):  # noqa: E501
        """Body158 - a model defined in Swagger"""  # noqa: E501
        self._location_id = None
        self.discriminator = None
        if location_id is not None:
            self.location_id = location_id

    @property
    def location_id(self):
        """Gets the location_id of this Body158.  # noqa: E501

        Location ID of the location where Zoom Room is to be assigned. This can be retrieved from the `id` property in the response of [List Zoom Rooms Locations](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) API.  # noqa: E501

        :return: The location_id of this Body158.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Body158.

        Location ID of the location where Zoom Room is to be assigned. This can be retrieved from the `id` property in the response of [List Zoom Rooms Locations](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) API.  # noqa: E501

        :param location_id: The location_id of this Body158.  # noqa: E501
        :type: str
        """

        self._location_id = location_id

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
        if issubclass(Body158, dict):
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
        if not isinstance(other, Body158):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

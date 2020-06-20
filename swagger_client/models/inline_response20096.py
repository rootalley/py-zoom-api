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


class InlineResponse20096(object):
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
        'id': 'str',
        'name': 'str',
        'device_type': 'str',
        'mac_address': 'str',
        'status': 'str',
        'site': 'InlineResponse20095Site'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'device_type': 'device_type',
        'mac_address': 'mac_address',
        'status': 'status',
        'site': 'site'
    }

    def __init__(self, id=None, name=None, device_type=None, mac_address=None, status=None, site=None):  # noqa: E501
        """InlineResponse20096 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._device_type = None
        self._mac_address = None
        self._status = None
        self._site = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if device_type is not None:
            self.device_type = device_type
        if mac_address is not None:
            self.mac_address = mac_address
        if status is not None:
            self.status = status
        if site is not None:
            self.site = site

    @property
    def id(self):
        """Gets the id of this InlineResponse20096.  # noqa: E501

        Unique Identifier of the common area phone.  # noqa: E501

        :return: The id of this InlineResponse20096.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20096.

        Unique Identifier of the common area phone.  # noqa: E501

        :param id: The id of this InlineResponse20096.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20096.  # noqa: E501

        Display name of the common area phone.  # noqa: E501

        :return: The name of this InlineResponse20096.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20096.

        Display name of the common area phone.  # noqa: E501

        :param name: The name of this InlineResponse20096.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_type(self):
        """Gets the device_type of this InlineResponse20096.  # noqa: E501

        Type of device (manufacturer name + model name).  # noqa: E501

        :return: The device_type of this InlineResponse20096.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InlineResponse20096.

        Type of device (manufacturer name + model name).  # noqa: E501

        :param device_type: The device_type of this InlineResponse20096.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def mac_address(self):
        """Gets the mac_address of this InlineResponse20096.  # noqa: E501

         Mac address or serial number.  # noqa: E501

        :return: The mac_address of this InlineResponse20096.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this InlineResponse20096.

         Mac address or serial number.  # noqa: E501

        :param mac_address: The mac_address of this InlineResponse20096.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def status(self):
        """Gets the status of this InlineResponse20096.  # noqa: E501

        Status of the common area phone. It can be either `online` or `offline`.  # noqa: E501

        :return: The status of this InlineResponse20096.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20096.

        Status of the common area phone. It can be either `online` or `offline`.  # noqa: E501

        :param status: The status of this InlineResponse20096.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def site(self):
        """Gets the site of this InlineResponse20096.  # noqa: E501


        :return: The site of this InlineResponse20096.  # noqa: E501
        :rtype: InlineResponse20095Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse20096.


        :param site: The site of this InlineResponse20096.  # noqa: E501
        :type: InlineResponse20095Site
        """

        self._site = site

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
        if issubclass(InlineResponse20096, dict):
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
        if not isinstance(other, InlineResponse20096):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

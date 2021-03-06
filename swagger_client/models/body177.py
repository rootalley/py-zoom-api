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


class Body177(object):
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
        'site_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'extension_number': 'int',
        'mac_address': 'str',
        'type': 'str',
        'model': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'display_name': 'display_name',
        'description': 'description',
        'extension_number': 'extension_number',
        'mac_address': 'mac_address',
        'type': 'type',
        'model': 'model',
        'time_zone': 'time_zone'
    }

    def __init__(self, site_id=None, display_name=None, description=None, extension_number=None, mac_address=None, type=None, model=None, time_zone=None):  # noqa: E501
        """Body177 - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._display_name = None
        self._description = None
        self._extension_number = None
        self._mac_address = None
        self._type = None
        self._model = None
        self._time_zone = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        self.display_name = display_name
        if description is not None:
            self.description = description
        self.extension_number = extension_number
        self.mac_address = mac_address
        self.type = type
        if model is not None:
            self.model = model
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def site_id(self):
        """Gets the site_id of this Body177.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from List Sites API.  # noqa: E501

        :return: The site_id of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Body177.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from List Sites API.  # noqa: E501

        :param site_id: The site_id of this Body177.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def display_name(self):
        """Gets the display_name of this Body177.  # noqa: E501

        Display name of the Common area phone.  # noqa: E501

        :return: The display_name of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Body177.

        Display name of the Common area phone.  # noqa: E501

        :param display_name: The display_name of this Body177.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Body177.  # noqa: E501

        Description for the common area phone.  # noqa: E501

        :return: The description of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body177.

        Description for the common area phone.  # noqa: E501

        :param description: The description of this Body177.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extension_number(self):
        """Gets the extension_number of this Body177.  # noqa: E501

        Extension number assigned to the common area phone. If site code is enabled, provide the short extension number instead.  # noqa: E501

        :return: The extension_number of this Body177.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this Body177.

        Extension number assigned to the common area phone. If site code is enabled, provide the short extension number instead.  # noqa: E501

        :param extension_number: The extension_number of this Body177.  # noqa: E501
        :type: int
        """
        if extension_number is None:
            raise ValueError("Invalid value for `extension_number`, must not be `None`")  # noqa: E501

        self._extension_number = extension_number

    @property
    def mac_address(self):
        """Gets the mac_address of this Body177.  # noqa: E501

        Mac Address (serial number) of the common area desk phone. These examples show the formats supported: `64-16-7f-37-90-92` or `64167f379092`  # noqa: E501

        :return: The mac_address of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Body177.

        Mac Address (serial number) of the common area desk phone. These examples show the formats supported: `64-16-7f-37-90-92` or `64167f379092`  # noqa: E501

        :param mac_address: The mac_address of this Body177.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def type(self):
        """Gets the type of this Body177.  # noqa: E501

        Phone device manufacturer name. Refer to the \"Manufacturer Name\" field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table.  # noqa: E501

        :return: The type of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body177.

        Phone device manufacturer name. Refer to the \"Manufacturer Name\" field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table.  # noqa: E501

        :param type: The type of this Body177.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def model(self):
        """Gets the model of this Body177.  # noqa: E501

        Device Model name. Refer to the \"Model Name\" field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table.  # noqa: E501

        :return: The model of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Body177.

        Device Model name. Refer to the \"Model Name\" field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table.  # noqa: E501

        :param model: The model of this Body177.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def time_zone(self):
        """Gets the time_zone of this Body177.  # noqa: E501

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area phone.  # noqa: E501

        :return: The time_zone of this Body177.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Body177.

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area phone.  # noqa: E501

        :param time_zone: The time_zone of this Body177.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

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
        if issubclass(Body177, dict):
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
        if not isinstance(other, Body177):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

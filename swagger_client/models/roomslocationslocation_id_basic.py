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


class RoomslocationslocationIdBasic(object):
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
        'name': 'str',
        'description_': 'str',
        'timezone': 'str',
        'address': 'str',
        'support_email': 'str',
        'support_phone': 'str',
        'room_passcode': 'str',
        'required_code_to_ext': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description_': 'description ',
        'timezone': 'timezone',
        'address': 'address',
        'support_email': 'support_email',
        'support_phone': 'support_phone',
        'room_passcode': 'room_passcode',
        'required_code_to_ext': 'required_code_to_ext'
    }

    def __init__(self, name=None, description_=None, timezone=None, address=None, support_email=None, support_phone=None, room_passcode=None, required_code_to_ext=None):  # noqa: E501
        """RoomslocationslocationIdBasic - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description_ = None
        self._timezone = None
        self._address = None
        self._support_email = None
        self._support_phone = None
        self._room_passcode = None
        self._required_code_to_ext = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description_ is not None:
            self.description_ = description_
        if timezone is not None:
            self.timezone = timezone
        if address is not None:
            self.address = address
        if support_email is not None:
            self.support_email = support_email
        if support_phone is not None:
            self.support_phone = support_phone
        if room_passcode is not None:
            self.room_passcode = room_passcode
        if required_code_to_ext is not None:
            self.required_code_to_ext = required_code_to_ext

    @property
    def name(self):
        """Gets the name of this RoomslocationslocationIdBasic.  # noqa: E501

        Name of the location type.  # noqa: E501

        :return: The name of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoomslocationslocationIdBasic.

        Name of the location type.  # noqa: E501

        :param name: The name of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description_(self):
        """Gets the description_ of this RoomslocationslocationIdBasic.  # noqa: E501

        Description about the location.  # noqa: E501

        :return: The description_ of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._description_

    @description_.setter
    def description_(self, description_):
        """Sets the description_ of this RoomslocationslocationIdBasic.

        Description about the location.  # noqa: E501

        :param description_: The description_ of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._description_ = description_

    @property
    def timezone(self):
        """Gets the timezone of this RoomslocationslocationIdBasic.  # noqa: E501

        Timezone (can only be updated for location type - city).  # noqa: E501

        :return: The timezone of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this RoomslocationslocationIdBasic.

        Timezone (can only be updated for location type - city).  # noqa: E501

        :param timezone: The timezone of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def address(self):
        """Gets the address of this RoomslocationslocationIdBasic.  # noqa: E501

        Address. Can only be updated for Campus and Building.  # noqa: E501

        :return: The address of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RoomslocationslocationIdBasic.

        Address. Can only be updated for Campus and Building.  # noqa: E501

        :param address: The address of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def support_email(self):
        """Gets the support_email of this RoomslocationslocationIdBasic.  # noqa: E501

        The email address to be used for reporting Zoom Room issues.   # noqa: E501

        :return: The support_email of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._support_email

    @support_email.setter
    def support_email(self, support_email):
        """Sets the support_email of this RoomslocationslocationIdBasic.

        The email address to be used for reporting Zoom Room issues.   # noqa: E501

        :param support_email: The support_email of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._support_email = support_email

    @property
    def support_phone(self):
        """Gets the support_phone of this RoomslocationslocationIdBasic.  # noqa: E501

        The phone number to be used for reporting Zoom Room issues.   # noqa: E501

        :return: The support_phone of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._support_phone

    @support_phone.setter
    def support_phone(self, support_phone):
        """Sets the support_phone of this RoomslocationslocationIdBasic.

        The phone number to be used for reporting Zoom Room issues.   # noqa: E501

        :param support_phone: The support_phone of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._support_phone = support_phone

    @property
    def room_passcode(self):
        """Gets the room_passcode of this RoomslocationslocationIdBasic.  # noqa: E501

        1-16 digit number or characters that is used to secure your Zoom Rooms application.  # noqa: E501

        :return: The room_passcode of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: str
        """
        return self._room_passcode

    @room_passcode.setter
    def room_passcode(self, room_passcode):
        """Sets the room_passcode of this RoomslocationslocationIdBasic.

        1-16 digit number or characters that is used to secure your Zoom Rooms application.  # noqa: E501

        :param room_passcode: The room_passcode of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: str
        """

        self._room_passcode = room_passcode

    @property
    def required_code_to_ext(self):
        """Gets the required_code_to_ext of this RoomslocationslocationIdBasic.  # noqa: E501

        Require code to exit out of your Zoom Rooms application to switch between other apps.   # noqa: E501

        :return: The required_code_to_ext of this RoomslocationslocationIdBasic.  # noqa: E501
        :rtype: bool
        """
        return self._required_code_to_ext

    @required_code_to_ext.setter
    def required_code_to_ext(self, required_code_to_ext):
        """Sets the required_code_to_ext of this RoomslocationslocationIdBasic.

        Require code to exit out of your Zoom Rooms application to switch between other apps.   # noqa: E501

        :param required_code_to_ext: The required_code_to_ext of this RoomslocationslocationIdBasic.  # noqa: E501
        :type: bool
        """

        self._required_code_to_ext = required_code_to_ext

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
        if issubclass(RoomslocationslocationIdBasic, dict):
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
        if not isinstance(other, RoomslocationslocationIdBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

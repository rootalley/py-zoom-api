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


class InlineResponse2002Rooms(object):
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
        'activation_code': 'str',
        'status': 'str',
        'room_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'activation_code': 'activation_code',
        'status': 'status',
        'room_id': 'room_id'
    }

    def __init__(self, id=None, name=None, activation_code=None, status=None, room_id=None):  # noqa: E501
        """InlineResponse2002Rooms - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._activation_code = None
        self._status = None
        self._room_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if activation_code is not None:
            self.activation_code = activation_code
        if status is not None:
            self.status = status
        if room_id is not None:
            self.room_id = room_id

    @property
    def id(self):
        """Gets the id of this InlineResponse2002Rooms.  # noqa: E501

        Unique Identifier for the Zoom Room.  # noqa: E501

        :return: The id of this InlineResponse2002Rooms.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2002Rooms.

        Unique Identifier for the Zoom Room.  # noqa: E501

        :param id: The id of this InlineResponse2002Rooms.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2002Rooms.  # noqa: E501

        Name of the Zoom Room.  # noqa: E501

        :return: The name of this InlineResponse2002Rooms.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2002Rooms.

        Name of the Zoom Room.  # noqa: E501

        :param name: The name of this InlineResponse2002Rooms.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def activation_code(self):
        """Gets the activation_code of this InlineResponse2002Rooms.  # noqa: E501

        Activation Code is the code that is used to complete the setup of the Zoom Room.  # noqa: E501

        :return: The activation_code of this InlineResponse2002Rooms.  # noqa: E501
        :rtype: str
        """
        return self._activation_code

    @activation_code.setter
    def activation_code(self, activation_code):
        """Sets the activation_code of this InlineResponse2002Rooms.

        Activation Code is the code that is used to complete the setup of the Zoom Room.  # noqa: E501

        :param activation_code: The activation_code of this InlineResponse2002Rooms.  # noqa: E501
        :type: str
        """

        self._activation_code = activation_code

    @property
    def status(self):
        """Gets the status of this InlineResponse2002Rooms.  # noqa: E501

        Status of the Zoom Room.  # noqa: E501

        :return: The status of this InlineResponse2002Rooms.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2002Rooms.

        Status of the Zoom Room.  # noqa: E501

        :param status: The status of this InlineResponse2002Rooms.  # noqa: E501
        :type: str
        """
        allowed_values = ["Offline", "Available", "InMeeting", "UnderConstruction"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def room_id(self):
        """Gets the room_id of this InlineResponse2002Rooms.  # noqa: E501

        Globally unique identifier of the Zoom Room. Use this ID for the **Dashboard Zoom Room APIs**.  # noqa: E501

        :return: The room_id of this InlineResponse2002Rooms.  # noqa: E501
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this InlineResponse2002Rooms.

        Globally unique identifier of the Zoom Room. Use this ID for the **Dashboard Zoom Room APIs**.  # noqa: E501

        :param room_id: The room_id of this InlineResponse2002Rooms.  # noqa: E501
        :type: str
        """

        self._room_id = room_id

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
        if issubclass(InlineResponse2002Rooms, dict):
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
        if not isinstance(other, InlineResponse2002Rooms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
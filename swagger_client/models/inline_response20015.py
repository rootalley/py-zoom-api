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


class InlineResponse20015(object):
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
        'plan_base': 'Body29',
        'plan_zoom_rooms': 'AccountPlansPlanZoomRooms',
        'plan_room_connector': 'AccountPlansPlanZoomRooms',
        'plan_large_meeting': 'list[AccountPlansPlanZoomRooms]',
        'plan_webinar': 'list[AccountPlansPlanZoomRooms]',
        'plan_recording': 'str',
        'plan_audio': 'AccountPlansPlanAudio',
        'plan_phone': 'PhonePlan1'
    }

    attribute_map = {
        'plan_base': 'plan_base',
        'plan_zoom_rooms': 'plan_zoom_rooms',
        'plan_room_connector': 'plan_room_connector',
        'plan_large_meeting': 'plan_large_meeting',
        'plan_webinar': 'plan_webinar',
        'plan_recording': 'plan_recording',
        'plan_audio': 'plan_audio',
        'plan_phone': 'plan_phone'
    }

    def __init__(self, plan_base=None, plan_zoom_rooms=None, plan_room_connector=None, plan_large_meeting=None, plan_webinar=None, plan_recording=None, plan_audio=None, plan_phone=None):  # noqa: E501
        """InlineResponse20015 - a model defined in Swagger"""  # noqa: E501
        self._plan_base = None
        self._plan_zoom_rooms = None
        self._plan_room_connector = None
        self._plan_large_meeting = None
        self._plan_webinar = None
        self._plan_recording = None
        self._plan_audio = None
        self._plan_phone = None
        self.discriminator = None
        self.plan_base = plan_base
        if plan_zoom_rooms is not None:
            self.plan_zoom_rooms = plan_zoom_rooms
        if plan_room_connector is not None:
            self.plan_room_connector = plan_room_connector
        if plan_large_meeting is not None:
            self.plan_large_meeting = plan_large_meeting
        if plan_webinar is not None:
            self.plan_webinar = plan_webinar
        if plan_recording is not None:
            self.plan_recording = plan_recording
        if plan_audio is not None:
            self.plan_audio = plan_audio
        if plan_phone is not None:
            self.plan_phone = plan_phone

    @property
    def plan_base(self):
        """Gets the plan_base of this InlineResponse20015.  # noqa: E501


        :return: The plan_base of this InlineResponse20015.  # noqa: E501
        :rtype: Body29
        """
        return self._plan_base

    @plan_base.setter
    def plan_base(self, plan_base):
        """Sets the plan_base of this InlineResponse20015.


        :param plan_base: The plan_base of this InlineResponse20015.  # noqa: E501
        :type: Body29
        """
        if plan_base is None:
            raise ValueError("Invalid value for `plan_base`, must not be `None`")  # noqa: E501

        self._plan_base = plan_base

    @property
    def plan_zoom_rooms(self):
        """Gets the plan_zoom_rooms of this InlineResponse20015.  # noqa: E501


        :return: The plan_zoom_rooms of this InlineResponse20015.  # noqa: E501
        :rtype: AccountPlansPlanZoomRooms
        """
        return self._plan_zoom_rooms

    @plan_zoom_rooms.setter
    def plan_zoom_rooms(self, plan_zoom_rooms):
        """Sets the plan_zoom_rooms of this InlineResponse20015.


        :param plan_zoom_rooms: The plan_zoom_rooms of this InlineResponse20015.  # noqa: E501
        :type: AccountPlansPlanZoomRooms
        """

        self._plan_zoom_rooms = plan_zoom_rooms

    @property
    def plan_room_connector(self):
        """Gets the plan_room_connector of this InlineResponse20015.  # noqa: E501


        :return: The plan_room_connector of this InlineResponse20015.  # noqa: E501
        :rtype: AccountPlansPlanZoomRooms
        """
        return self._plan_room_connector

    @plan_room_connector.setter
    def plan_room_connector(self, plan_room_connector):
        """Sets the plan_room_connector of this InlineResponse20015.


        :param plan_room_connector: The plan_room_connector of this InlineResponse20015.  # noqa: E501
        :type: AccountPlansPlanZoomRooms
        """

        self._plan_room_connector = plan_room_connector

    @property
    def plan_large_meeting(self):
        """Gets the plan_large_meeting of this InlineResponse20015.  # noqa: E501

        Additional large meeting Plans.  # noqa: E501

        :return: The plan_large_meeting of this InlineResponse20015.  # noqa: E501
        :rtype: list[AccountPlansPlanZoomRooms]
        """
        return self._plan_large_meeting

    @plan_large_meeting.setter
    def plan_large_meeting(self, plan_large_meeting):
        """Sets the plan_large_meeting of this InlineResponse20015.

        Additional large meeting Plans.  # noqa: E501

        :param plan_large_meeting: The plan_large_meeting of this InlineResponse20015.  # noqa: E501
        :type: list[AccountPlansPlanZoomRooms]
        """

        self._plan_large_meeting = plan_large_meeting

    @property
    def plan_webinar(self):
        """Gets the plan_webinar of this InlineResponse20015.  # noqa: E501

        Additional webinar plans.  # noqa: E501

        :return: The plan_webinar of this InlineResponse20015.  # noqa: E501
        :rtype: list[AccountPlansPlanZoomRooms]
        """
        return self._plan_webinar

    @plan_webinar.setter
    def plan_webinar(self, plan_webinar):
        """Sets the plan_webinar of this InlineResponse20015.

        Additional webinar plans.  # noqa: E501

        :param plan_webinar: The plan_webinar of this InlineResponse20015.  # noqa: E501
        :type: list[AccountPlansPlanZoomRooms]
        """

        self._plan_webinar = plan_webinar

    @property
    def plan_recording(self):
        """Gets the plan_recording of this InlineResponse20015.  # noqa: E501

        Additional cloud recording plan.  # noqa: E501

        :return: The plan_recording of this InlineResponse20015.  # noqa: E501
        :rtype: str
        """
        return self._plan_recording

    @plan_recording.setter
    def plan_recording(self, plan_recording):
        """Sets the plan_recording of this InlineResponse20015.

        Additional cloud recording plan.  # noqa: E501

        :param plan_recording: The plan_recording of this InlineResponse20015.  # noqa: E501
        :type: str
        """

        self._plan_recording = plan_recording

    @property
    def plan_audio(self):
        """Gets the plan_audio of this InlineResponse20015.  # noqa: E501


        :return: The plan_audio of this InlineResponse20015.  # noqa: E501
        :rtype: AccountPlansPlanAudio
        """
        return self._plan_audio

    @plan_audio.setter
    def plan_audio(self, plan_audio):
        """Sets the plan_audio of this InlineResponse20015.


        :param plan_audio: The plan_audio of this InlineResponse20015.  # noqa: E501
        :type: AccountPlansPlanAudio
        """

        self._plan_audio = plan_audio

    @property
    def plan_phone(self):
        """Gets the plan_phone of this InlineResponse20015.  # noqa: E501


        :return: The plan_phone of this InlineResponse20015.  # noqa: E501
        :rtype: PhonePlan1
        """
        return self._plan_phone

    @plan_phone.setter
    def plan_phone(self, plan_phone):
        """Sets the plan_phone of this InlineResponse20015.


        :param plan_phone: The plan_phone of this InlineResponse20015.  # noqa: E501
        :type: PhonePlan1
        """

        self._plan_phone = plan_phone

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
        if issubclass(InlineResponse20015, dict):
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
        if not isinstance(other, InlineResponse20015):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

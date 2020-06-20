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


class AccountSettingsZoomRooms(object):
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
        'upcoming_meeting_alert': 'bool',
        'start_airplay_manually': 'bool',
        'weekly_system_restart': 'bool',
        'list_meetings_with_calendar': 'bool',
        'zr_post_meeting_feedback': 'bool',
        'ultrasonic': 'bool',
        'force_private_meeting': 'bool',
        'hide_host_information': 'bool',
        'cmr_for_instant_meeting': 'bool',
        'auto_start_stop_scheduled_meetings': 'bool'
    }

    attribute_map = {
        'upcoming_meeting_alert': 'upcoming_meeting_alert',
        'start_airplay_manually': 'start_airplay_manually',
        'weekly_system_restart': 'weekly_system_restart',
        'list_meetings_with_calendar': 'list_meetings_with_calendar',
        'zr_post_meeting_feedback': 'zr_post_meeting_feedback',
        'ultrasonic': 'ultrasonic',
        'force_private_meeting': 'force_private_meeting',
        'hide_host_information': 'hide_host_information',
        'cmr_for_instant_meeting': 'cmr_for_instant_meeting',
        'auto_start_stop_scheduled_meetings': 'auto_start_stop_scheduled_meetings'
    }

    def __init__(self, upcoming_meeting_alert=None, start_airplay_manually=None, weekly_system_restart=None, list_meetings_with_calendar=None, zr_post_meeting_feedback=None, ultrasonic=None, force_private_meeting=None, hide_host_information=None, cmr_for_instant_meeting=None, auto_start_stop_scheduled_meetings=None):  # noqa: E501
        """AccountSettingsZoomRooms - a model defined in Swagger"""  # noqa: E501
        self._upcoming_meeting_alert = None
        self._start_airplay_manually = None
        self._weekly_system_restart = None
        self._list_meetings_with_calendar = None
        self._zr_post_meeting_feedback = None
        self._ultrasonic = None
        self._force_private_meeting = None
        self._hide_host_information = None
        self._cmr_for_instant_meeting = None
        self._auto_start_stop_scheduled_meetings = None
        self.discriminator = None
        if upcoming_meeting_alert is not None:
            self.upcoming_meeting_alert = upcoming_meeting_alert
        if start_airplay_manually is not None:
            self.start_airplay_manually = start_airplay_manually
        if weekly_system_restart is not None:
            self.weekly_system_restart = weekly_system_restart
        if list_meetings_with_calendar is not None:
            self.list_meetings_with_calendar = list_meetings_with_calendar
        if zr_post_meeting_feedback is not None:
            self.zr_post_meeting_feedback = zr_post_meeting_feedback
        if ultrasonic is not None:
            self.ultrasonic = ultrasonic
        if force_private_meeting is not None:
            self.force_private_meeting = force_private_meeting
        if hide_host_information is not None:
            self.hide_host_information = hide_host_information
        if cmr_for_instant_meeting is not None:
            self.cmr_for_instant_meeting = cmr_for_instant_meeting
        if auto_start_stop_scheduled_meetings is not None:
            self.auto_start_stop_scheduled_meetings = auto_start_stop_scheduled_meetings

    @property
    def upcoming_meeting_alert(self):
        """Gets the upcoming_meeting_alert of this AccountSettingsZoomRooms.  # noqa: E501

        Upcoming meeting alert.  # noqa: E501

        :return: The upcoming_meeting_alert of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._upcoming_meeting_alert

    @upcoming_meeting_alert.setter
    def upcoming_meeting_alert(self, upcoming_meeting_alert):
        """Sets the upcoming_meeting_alert of this AccountSettingsZoomRooms.

        Upcoming meeting alert.  # noqa: E501

        :param upcoming_meeting_alert: The upcoming_meeting_alert of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._upcoming_meeting_alert = upcoming_meeting_alert

    @property
    def start_airplay_manually(self):
        """Gets the start_airplay_manually of this AccountSettingsZoomRooms.  # noqa: E501

        Start AirPlay service manually.  # noqa: E501

        :return: The start_airplay_manually of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._start_airplay_manually

    @start_airplay_manually.setter
    def start_airplay_manually(self, start_airplay_manually):
        """Sets the start_airplay_manually of this AccountSettingsZoomRooms.

        Start AirPlay service manually.  # noqa: E501

        :param start_airplay_manually: The start_airplay_manually of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._start_airplay_manually = start_airplay_manually

    @property
    def weekly_system_restart(self):
        """Gets the weekly_system_restart of this AccountSettingsZoomRooms.  # noqa: E501

        Weekly system restart.  # noqa: E501

        :return: The weekly_system_restart of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._weekly_system_restart

    @weekly_system_restart.setter
    def weekly_system_restart(self, weekly_system_restart):
        """Sets the weekly_system_restart of this AccountSettingsZoomRooms.

        Weekly system restart.  # noqa: E501

        :param weekly_system_restart: The weekly_system_restart of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._weekly_system_restart = weekly_system_restart

    @property
    def list_meetings_with_calendar(self):
        """Gets the list_meetings_with_calendar of this AccountSettingsZoomRooms.  # noqa: E501

        Display meeting list with calendar integration.  # noqa: E501

        :return: The list_meetings_with_calendar of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._list_meetings_with_calendar

    @list_meetings_with_calendar.setter
    def list_meetings_with_calendar(self, list_meetings_with_calendar):
        """Sets the list_meetings_with_calendar of this AccountSettingsZoomRooms.

        Display meeting list with calendar integration.  # noqa: E501

        :param list_meetings_with_calendar: The list_meetings_with_calendar of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._list_meetings_with_calendar = list_meetings_with_calendar

    @property
    def zr_post_meeting_feedback(self):
        """Gets the zr_post_meeting_feedback of this AccountSettingsZoomRooms.  # noqa: E501

        Zoom Room post meeting feedback.  # noqa: E501

        :return: The zr_post_meeting_feedback of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._zr_post_meeting_feedback

    @zr_post_meeting_feedback.setter
    def zr_post_meeting_feedback(self, zr_post_meeting_feedback):
        """Sets the zr_post_meeting_feedback of this AccountSettingsZoomRooms.

        Zoom Room post meeting feedback.  # noqa: E501

        :param zr_post_meeting_feedback: The zr_post_meeting_feedback of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._zr_post_meeting_feedback = zr_post_meeting_feedback

    @property
    def ultrasonic(self):
        """Gets the ultrasonic of this AccountSettingsZoomRooms.  # noqa: E501

        Automatic direct sharing using an ultrasonic proximity signal.  # noqa: E501

        :return: The ultrasonic of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._ultrasonic

    @ultrasonic.setter
    def ultrasonic(self, ultrasonic):
        """Sets the ultrasonic of this AccountSettingsZoomRooms.

        Automatic direct sharing using an ultrasonic proximity signal.  # noqa: E501

        :param ultrasonic: The ultrasonic of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._ultrasonic = ultrasonic

    @property
    def force_private_meeting(self):
        """Gets the force_private_meeting of this AccountSettingsZoomRooms.  # noqa: E501

        Shift all meetings to private.  # noqa: E501

        :return: The force_private_meeting of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._force_private_meeting

    @force_private_meeting.setter
    def force_private_meeting(self, force_private_meeting):
        """Sets the force_private_meeting of this AccountSettingsZoomRooms.

        Shift all meetings to private.  # noqa: E501

        :param force_private_meeting: The force_private_meeting of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._force_private_meeting = force_private_meeting

    @property
    def hide_host_information(self):
        """Gets the hide_host_information of this AccountSettingsZoomRooms.  # noqa: E501

        Hide host and meeting ID from private meetings.  # noqa: E501

        :return: The hide_host_information of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._hide_host_information

    @hide_host_information.setter
    def hide_host_information(self, hide_host_information):
        """Sets the hide_host_information of this AccountSettingsZoomRooms.

        Hide host and meeting ID from private meetings.  # noqa: E501

        :param hide_host_information: The hide_host_information of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._hide_host_information = hide_host_information

    @property
    def cmr_for_instant_meeting(self):
        """Gets the cmr_for_instant_meeting of this AccountSettingsZoomRooms.  # noqa: E501

        Cloud recording for instant meetings.  # noqa: E501

        :return: The cmr_for_instant_meeting of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._cmr_for_instant_meeting

    @cmr_for_instant_meeting.setter
    def cmr_for_instant_meeting(self, cmr_for_instant_meeting):
        """Sets the cmr_for_instant_meeting of this AccountSettingsZoomRooms.

        Cloud recording for instant meetings.  # noqa: E501

        :param cmr_for_instant_meeting: The cmr_for_instant_meeting of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._cmr_for_instant_meeting = cmr_for_instant_meeting

    @property
    def auto_start_stop_scheduled_meetings(self):
        """Gets the auto_start_stop_scheduled_meetings of this AccountSettingsZoomRooms.  # noqa: E501

        Automatic start and stop for scheduled meetings.  # noqa: E501

        :return: The auto_start_stop_scheduled_meetings of this AccountSettingsZoomRooms.  # noqa: E501
        :rtype: bool
        """
        return self._auto_start_stop_scheduled_meetings

    @auto_start_stop_scheduled_meetings.setter
    def auto_start_stop_scheduled_meetings(self, auto_start_stop_scheduled_meetings):
        """Sets the auto_start_stop_scheduled_meetings of this AccountSettingsZoomRooms.

        Automatic start and stop for scheduled meetings.  # noqa: E501

        :param auto_start_stop_scheduled_meetings: The auto_start_stop_scheduled_meetings of this AccountSettingsZoomRooms.  # noqa: E501
        :type: bool
        """

        self._auto_start_stop_scheduled_meetings = auto_start_stop_scheduled_meetings

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
        if issubclass(AccountSettingsZoomRooms, dict):
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
        if not isinstance(other, AccountSettingsZoomRooms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

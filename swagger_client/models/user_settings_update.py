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


class UserSettingsUpdate(object):
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
        'schedule_meeting': 'UserSettingsMeetingSettings',
        'in_meeting': 'UserSettingsMeetingSettings1',
        'email_notification': 'UserSettingsNotificationSettings',
        'recording': 'UserSettingsRecordingSettings',
        'telephony': 'UserSettingsMeetingSettings2',
        'feature': 'UserSettingsFeatureSettings1',
        'tsp': 'UserSettingsTSPSettings'
    }

    attribute_map = {
        'schedule_meeting': 'schedule_meeting',
        'in_meeting': 'in_meeting',
        'email_notification': 'email_notification',
        'recording': 'recording',
        'telephony': 'telephony',
        'feature': 'feature',
        'tsp': 'tsp'
    }

    def __init__(self, schedule_meeting=None, in_meeting=None, email_notification=None, recording=None, telephony=None, feature=None, tsp=None):  # noqa: E501
        """UserSettingsUpdate - a model defined in Swagger"""  # noqa: E501
        self._schedule_meeting = None
        self._in_meeting = None
        self._email_notification = None
        self._recording = None
        self._telephony = None
        self._feature = None
        self._tsp = None
        self.discriminator = None
        if schedule_meeting is not None:
            self.schedule_meeting = schedule_meeting
        if in_meeting is not None:
            self.in_meeting = in_meeting
        if email_notification is not None:
            self.email_notification = email_notification
        if recording is not None:
            self.recording = recording
        if telephony is not None:
            self.telephony = telephony
        if feature is not None:
            self.feature = feature
        if tsp is not None:
            self.tsp = tsp

    @property
    def schedule_meeting(self):
        """Gets the schedule_meeting of this UserSettingsUpdate.  # noqa: E501


        :return: The schedule_meeting of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsMeetingSettings
        """
        return self._schedule_meeting

    @schedule_meeting.setter
    def schedule_meeting(self, schedule_meeting):
        """Sets the schedule_meeting of this UserSettingsUpdate.


        :param schedule_meeting: The schedule_meeting of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsMeetingSettings
        """

        self._schedule_meeting = schedule_meeting

    @property
    def in_meeting(self):
        """Gets the in_meeting of this UserSettingsUpdate.  # noqa: E501


        :return: The in_meeting of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsMeetingSettings1
        """
        return self._in_meeting

    @in_meeting.setter
    def in_meeting(self, in_meeting):
        """Sets the in_meeting of this UserSettingsUpdate.


        :param in_meeting: The in_meeting of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsMeetingSettings1
        """

        self._in_meeting = in_meeting

    @property
    def email_notification(self):
        """Gets the email_notification of this UserSettingsUpdate.  # noqa: E501


        :return: The email_notification of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsNotificationSettings
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this UserSettingsUpdate.


        :param email_notification: The email_notification of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsNotificationSettings
        """

        self._email_notification = email_notification

    @property
    def recording(self):
        """Gets the recording of this UserSettingsUpdate.  # noqa: E501


        :return: The recording of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsRecordingSettings
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        """Sets the recording of this UserSettingsUpdate.


        :param recording: The recording of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsRecordingSettings
        """

        self._recording = recording

    @property
    def telephony(self):
        """Gets the telephony of this UserSettingsUpdate.  # noqa: E501


        :return: The telephony of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsMeetingSettings2
        """
        return self._telephony

    @telephony.setter
    def telephony(self, telephony):
        """Sets the telephony of this UserSettingsUpdate.


        :param telephony: The telephony of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsMeetingSettings2
        """

        self._telephony = telephony

    @property
    def feature(self):
        """Gets the feature of this UserSettingsUpdate.  # noqa: E501


        :return: The feature of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsFeatureSettings1
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this UserSettingsUpdate.


        :param feature: The feature of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsFeatureSettings1
        """

        self._feature = feature

    @property
    def tsp(self):
        """Gets the tsp of this UserSettingsUpdate.  # noqa: E501


        :return: The tsp of this UserSettingsUpdate.  # noqa: E501
        :rtype: UserSettingsTSPSettings
        """
        return self._tsp

    @tsp.setter
    def tsp(self, tsp):
        """Sets the tsp of this UserSettingsUpdate.


        :param tsp: The tsp of this UserSettingsUpdate.  # noqa: E501
        :type: UserSettingsTSPSettings
        """

        self._tsp = tsp

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
        if issubclass(UserSettingsUpdate, dict):
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
        if not isinstance(other, UserSettingsUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

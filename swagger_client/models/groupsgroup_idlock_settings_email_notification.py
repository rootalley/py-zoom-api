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


class GroupsgroupIdlockSettingsEmailNotification(object):
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
        'cloud_recording_available_reminder': 'bool',
        'jbh_reminder': 'bool',
        'cancel_meeting_reminder': 'bool',
        'alternative_host_reminder': 'bool',
        'schedule_for_host_reminder': 'bool'
    }

    attribute_map = {
        'cloud_recording_available_reminder': 'cloud_recording_available_reminder',
        'jbh_reminder': 'jbh_reminder',
        'cancel_meeting_reminder': 'cancel_meeting_reminder',
        'alternative_host_reminder': 'alternative_host_reminder',
        'schedule_for_host_reminder': 'schedule_for_host_reminder'
    }

    def __init__(self, cloud_recording_available_reminder=None, jbh_reminder=None, cancel_meeting_reminder=None, alternative_host_reminder=None, schedule_for_host_reminder=None):  # noqa: E501
        """GroupsgroupIdlockSettingsEmailNotification - a model defined in Swagger"""  # noqa: E501
        self._cloud_recording_available_reminder = None
        self._jbh_reminder = None
        self._cancel_meeting_reminder = None
        self._alternative_host_reminder = None
        self._schedule_for_host_reminder = None
        self.discriminator = None
        if cloud_recording_available_reminder is not None:
            self.cloud_recording_available_reminder = cloud_recording_available_reminder
        if jbh_reminder is not None:
            self.jbh_reminder = jbh_reminder
        if cancel_meeting_reminder is not None:
            self.cancel_meeting_reminder = cancel_meeting_reminder
        if alternative_host_reminder is not None:
            self.alternative_host_reminder = alternative_host_reminder
        if schedule_for_host_reminder is not None:
            self.schedule_for_host_reminder = schedule_for_host_reminder

    @property
    def cloud_recording_available_reminder(self):
        """Gets the cloud_recording_available_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501

        Notify host when cloud recording is available.  # noqa: E501

        :return: The cloud_recording_available_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording_available_reminder

    @cloud_recording_available_reminder.setter
    def cloud_recording_available_reminder(self, cloud_recording_available_reminder):
        """Sets the cloud_recording_available_reminder of this GroupsgroupIdlockSettingsEmailNotification.

        Notify host when cloud recording is available.  # noqa: E501

        :param cloud_recording_available_reminder: The cloud_recording_available_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :type: bool
        """

        self._cloud_recording_available_reminder = cloud_recording_available_reminder

    @property
    def jbh_reminder(self):
        """Gets the jbh_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501

        Notify host when participants join the meeting before them.  # noqa: E501

        :return: The jbh_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._jbh_reminder

    @jbh_reminder.setter
    def jbh_reminder(self, jbh_reminder):
        """Sets the jbh_reminder of this GroupsgroupIdlockSettingsEmailNotification.

        Notify host when participants join the meeting before them.  # noqa: E501

        :param jbh_reminder: The jbh_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :type: bool
        """

        self._jbh_reminder = jbh_reminder

    @property
    def cancel_meeting_reminder(self):
        """Gets the cancel_meeting_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501

        Notify host and participants when the meeting is cancelled.  # noqa: E501

        :return: The cancel_meeting_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_meeting_reminder

    @cancel_meeting_reminder.setter
    def cancel_meeting_reminder(self, cancel_meeting_reminder):
        """Sets the cancel_meeting_reminder of this GroupsgroupIdlockSettingsEmailNotification.

        Notify host and participants when the meeting is cancelled.  # noqa: E501

        :param cancel_meeting_reminder: The cancel_meeting_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :type: bool
        """

        self._cancel_meeting_reminder = cancel_meeting_reminder

    @property
    def alternative_host_reminder(self):
        """Gets the alternative_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501

        Notify the alternative host who is set or removed.  # noqa: E501

        :return: The alternative_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._alternative_host_reminder

    @alternative_host_reminder.setter
    def alternative_host_reminder(self, alternative_host_reminder):
        """Sets the alternative_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.

        Notify the alternative host who is set or removed.  # noqa: E501

        :param alternative_host_reminder: The alternative_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :type: bool
        """

        self._alternative_host_reminder = alternative_host_reminder

    @property
    def schedule_for_host_reminder(self):
        """Gets the schedule_for_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501

        Notify the host there is a meeting is scheduled, rescheduled, or cancelled.  # noqa: E501

        :return: The schedule_for_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :rtype: bool
        """
        return self._schedule_for_host_reminder

    @schedule_for_host_reminder.setter
    def schedule_for_host_reminder(self, schedule_for_host_reminder):
        """Sets the schedule_for_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.

        Notify the host there is a meeting is scheduled, rescheduled, or cancelled.  # noqa: E501

        :param schedule_for_host_reminder: The schedule_for_host_reminder of this GroupsgroupIdlockSettingsEmailNotification.  # noqa: E501
        :type: bool
        """

        self._schedule_for_host_reminder = schedule_for_host_reminder

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
        if issubclass(GroupsgroupIdlockSettingsEmailNotification, dict):
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
        if not isinstance(other, GroupsgroupIdlockSettingsEmailNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

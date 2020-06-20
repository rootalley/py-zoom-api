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


class AccountSettingsIntegration(object):
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
        'google_calendar': 'bool',
        'google_drive': 'bool',
        'dropbox': 'bool',
        'box': 'bool',
        'microsoft_one_drive': 'bool',
        'kubi': 'bool'
    }

    attribute_map = {
        'google_calendar': 'google_calendar',
        'google_drive': 'google_drive',
        'dropbox': 'dropbox',
        'box': 'box',
        'microsoft_one_drive': 'microsoft_one_drive',
        'kubi': 'kubi'
    }

    def __init__(self, google_calendar=None, google_drive=None, dropbox=None, box=None, microsoft_one_drive=None, kubi=None):  # noqa: E501
        """AccountSettingsIntegration - a model defined in Swagger"""  # noqa: E501
        self._google_calendar = None
        self._google_drive = None
        self._dropbox = None
        self._box = None
        self._microsoft_one_drive = None
        self._kubi = None
        self.discriminator = None
        if google_calendar is not None:
            self.google_calendar = google_calendar
        if google_drive is not None:
            self.google_drive = google_drive
        if dropbox is not None:
            self.dropbox = dropbox
        if box is not None:
            self.box = box
        if microsoft_one_drive is not None:
            self.microsoft_one_drive = microsoft_one_drive
        if kubi is not None:
            self.kubi = kubi

    @property
    def google_calendar(self):
        """Gets the google_calendar of this AccountSettingsIntegration.  # noqa: E501

        Enable meetings to be scheduled using Google Calendar.  # noqa: E501

        :return: The google_calendar of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._google_calendar

    @google_calendar.setter
    def google_calendar(self, google_calendar):
        """Sets the google_calendar of this AccountSettingsIntegration.

        Enable meetings to be scheduled using Google Calendar.  # noqa: E501

        :param google_calendar: The google_calendar of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._google_calendar = google_calendar

    @property
    def google_drive(self):
        """Gets the google_drive of this AccountSettingsIntegration.  # noqa: E501

        Enable users who join a meeting from their mobile device to share content from their Google Drive.  # noqa: E501

        :return: The google_drive of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._google_drive

    @google_drive.setter
    def google_drive(self, google_drive):
        """Sets the google_drive of this AccountSettingsIntegration.

        Enable users who join a meeting from their mobile device to share content from their Google Drive.  # noqa: E501

        :param google_drive: The google_drive of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._google_drive = google_drive

    @property
    def dropbox(self):
        """Gets the dropbox of this AccountSettingsIntegration.  # noqa: E501

        Enable users who join a meeting from their mobile device to share content from their Dropbox account.  # noqa: E501

        :return: The dropbox of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._dropbox

    @dropbox.setter
    def dropbox(self, dropbox):
        """Sets the dropbox of this AccountSettingsIntegration.

        Enable users who join a meeting from their mobile device to share content from their Dropbox account.  # noqa: E501

        :param dropbox: The dropbox of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._dropbox = dropbox

    @property
    def box(self):
        """Gets the box of this AccountSettingsIntegration.  # noqa: E501

        Enable users who join a meeting from their mobile device to share content from their Box account.  # noqa: E501

        :return: The box of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this AccountSettingsIntegration.

        Enable users who join a meeting from their mobile device to share content from their Box account.  # noqa: E501

        :param box: The box of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._box = box

    @property
    def microsoft_one_drive(self):
        """Gets the microsoft_one_drive of this AccountSettingsIntegration.  # noqa: E501

        Enable users who join a meeting from their mobile device to share content from their Microsoft OneDrive account.  # noqa: E501

        :return: The microsoft_one_drive of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._microsoft_one_drive

    @microsoft_one_drive.setter
    def microsoft_one_drive(self, microsoft_one_drive):
        """Sets the microsoft_one_drive of this AccountSettingsIntegration.

        Enable users who join a meeting from their mobile device to share content from their Microsoft OneDrive account.  # noqa: E501

        :param microsoft_one_drive: The microsoft_one_drive of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._microsoft_one_drive = microsoft_one_drive

    @property
    def kubi(self):
        """Gets the kubi of this AccountSettingsIntegration.  # noqa: E501

        Enable users to control a connected Kubi device from within a Zoom meeting.  # noqa: E501

        :return: The kubi of this AccountSettingsIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._kubi

    @kubi.setter
    def kubi(self, kubi):
        """Sets the kubi of this AccountSettingsIntegration.

        Enable users to control a connected Kubi device from within a Zoom meeting.  # noqa: E501

        :param kubi: The kubi of this AccountSettingsIntegration.  # noqa: E501
        :type: bool
        """

        self._kubi = kubi

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
        if issubclass(AccountSettingsIntegration, dict):
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
        if not isinstance(other, AccountSettingsIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

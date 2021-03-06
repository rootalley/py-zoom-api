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


class UserSettingsFeatureSettings(object):
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
        'meeting_capacity': 'int',
        'large_meeting': 'bool',
        'large_meeting_capacity': 'int',
        'webinar': 'bool',
        'webinar_capacity': 'int',
        'cn_meeting': 'bool',
        'in_meeting': 'bool',
        'zoom_phone': 'bool'
    }

    attribute_map = {
        'meeting_capacity': 'meeting_capacity',
        'large_meeting': 'large_meeting',
        'large_meeting_capacity': 'large_meeting_capacity',
        'webinar': 'webinar',
        'webinar_capacity': 'webinar_capacity',
        'cn_meeting': 'cn_meeting',
        'in_meeting': 'in_meeting',
        'zoom_phone': 'zoom_phone'
    }

    def __init__(self, meeting_capacity=None, large_meeting=None, large_meeting_capacity=None, webinar=None, webinar_capacity=None, cn_meeting=None, in_meeting=None, zoom_phone=None):  # noqa: E501
        """UserSettingsFeatureSettings - a model defined in Swagger"""  # noqa: E501
        self._meeting_capacity = None
        self._large_meeting = None
        self._large_meeting_capacity = None
        self._webinar = None
        self._webinar_capacity = None
        self._cn_meeting = None
        self._in_meeting = None
        self._zoom_phone = None
        self.discriminator = None
        if meeting_capacity is not None:
            self.meeting_capacity = meeting_capacity
        if large_meeting is not None:
            self.large_meeting = large_meeting
        if large_meeting_capacity is not None:
            self.large_meeting_capacity = large_meeting_capacity
        if webinar is not None:
            self.webinar = webinar
        if webinar_capacity is not None:
            self.webinar_capacity = webinar_capacity
        if cn_meeting is not None:
            self.cn_meeting = cn_meeting
        if in_meeting is not None:
            self.in_meeting = in_meeting
        if zoom_phone is not None:
            self.zoom_phone = zoom_phone

    @property
    def meeting_capacity(self):
        """Gets the meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501

        User’s meeting capacity.  # noqa: E501

        :return: The meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: int
        """
        return self._meeting_capacity

    @meeting_capacity.setter
    def meeting_capacity(self, meeting_capacity):
        """Sets the meeting_capacity of this UserSettingsFeatureSettings.

        User’s meeting capacity.  # noqa: E501

        :param meeting_capacity: The meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :type: int
        """

        self._meeting_capacity = meeting_capacity

    @property
    def large_meeting(self):
        """Gets the large_meeting of this UserSettingsFeatureSettings.  # noqa: E501

        Large meeting feature.  # noqa: E501

        :return: The large_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: bool
        """
        return self._large_meeting

    @large_meeting.setter
    def large_meeting(self, large_meeting):
        """Sets the large_meeting of this UserSettingsFeatureSettings.

        Large meeting feature.  # noqa: E501

        :param large_meeting: The large_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :type: bool
        """

        self._large_meeting = large_meeting

    @property
    def large_meeting_capacity(self):
        """Gets the large_meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501

        Large meeting capacity: can be 500 or 1000, depending on if the user has a large meeting capacity plan subscription or not.  # noqa: E501

        :return: The large_meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: int
        """
        return self._large_meeting_capacity

    @large_meeting_capacity.setter
    def large_meeting_capacity(self, large_meeting_capacity):
        """Sets the large_meeting_capacity of this UserSettingsFeatureSettings.

        Large meeting capacity: can be 500 or 1000, depending on if the user has a large meeting capacity plan subscription or not.  # noqa: E501

        :param large_meeting_capacity: The large_meeting_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :type: int
        """

        self._large_meeting_capacity = large_meeting_capacity

    @property
    def webinar(self):
        """Gets the webinar of this UserSettingsFeatureSettings.  # noqa: E501

        Webinar feature.  # noqa: E501

        :return: The webinar of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: bool
        """
        return self._webinar

    @webinar.setter
    def webinar(self, webinar):
        """Sets the webinar of this UserSettingsFeatureSettings.

        Webinar feature.  # noqa: E501

        :param webinar: The webinar of this UserSettingsFeatureSettings.  # noqa: E501
        :type: bool
        """

        self._webinar = webinar

    @property
    def webinar_capacity(self):
        """Gets the webinar_capacity of this UserSettingsFeatureSettings.  # noqa: E501

        Webinar capacity: can be 100, 500, 1000, 3000, 5000 or 10000, depending on if the user has a webinar capacity plan subscription or not.  # noqa: E501

        :return: The webinar_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: int
        """
        return self._webinar_capacity

    @webinar_capacity.setter
    def webinar_capacity(self, webinar_capacity):
        """Sets the webinar_capacity of this UserSettingsFeatureSettings.

        Webinar capacity: can be 100, 500, 1000, 3000, 5000 or 10000, depending on if the user has a webinar capacity plan subscription or not.  # noqa: E501

        :param webinar_capacity: The webinar_capacity of this UserSettingsFeatureSettings.  # noqa: E501
        :type: int
        """

        self._webinar_capacity = webinar_capacity

    @property
    def cn_meeting(self):
        """Gets the cn_meeting of this UserSettingsFeatureSettings.  # noqa: E501

        CN meeting feature.  # noqa: E501

        :return: The cn_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: bool
        """
        return self._cn_meeting

    @cn_meeting.setter
    def cn_meeting(self, cn_meeting):
        """Sets the cn_meeting of this UserSettingsFeatureSettings.

        CN meeting feature.  # noqa: E501

        :param cn_meeting: The cn_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :type: bool
        """

        self._cn_meeting = cn_meeting

    @property
    def in_meeting(self):
        """Gets the in_meeting of this UserSettingsFeatureSettings.  # noqa: E501

        IN meeting feature.  # noqa: E501

        :return: The in_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: bool
        """
        return self._in_meeting

    @in_meeting.setter
    def in_meeting(self, in_meeting):
        """Sets the in_meeting of this UserSettingsFeatureSettings.

        IN meeting feature.  # noqa: E501

        :param in_meeting: The in_meeting of this UserSettingsFeatureSettings.  # noqa: E501
        :type: bool
        """

        self._in_meeting = in_meeting

    @property
    def zoom_phone(self):
        """Gets the zoom_phone of this UserSettingsFeatureSettings.  # noqa: E501

        Zoom phone feature.  # noqa: E501

        :return: The zoom_phone of this UserSettingsFeatureSettings.  # noqa: E501
        :rtype: bool
        """
        return self._zoom_phone

    @zoom_phone.setter
    def zoom_phone(self, zoom_phone):
        """Sets the zoom_phone of this UserSettingsFeatureSettings.

        Zoom phone feature.  # noqa: E501

        :param zoom_phone: The zoom_phone of this UserSettingsFeatureSettings.  # noqa: E501
        :type: bool
        """

        self._zoom_phone = zoom_phone

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
        if issubclass(UserSettingsFeatureSettings, dict):
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
        if not isinstance(other, UserSettingsFeatureSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

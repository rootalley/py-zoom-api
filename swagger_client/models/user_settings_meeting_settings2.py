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


class UserSettingsMeetingSettings2(object):
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
        'third_party_audio': 'bool',
        'audio_conference_info': 'str',
        'show_international_numbers_link': 'bool'
    }

    attribute_map = {
        'third_party_audio': 'third_party_audio',
        'audio_conference_info': 'audio_conference_info',
        'show_international_numbers_link': 'show_international_numbers_link'
    }

    def __init__(self, third_party_audio=None, audio_conference_info='', show_international_numbers_link=None):  # noqa: E501
        """UserSettingsMeetingSettings2 - a model defined in Swagger"""  # noqa: E501
        self._third_party_audio = None
        self._audio_conference_info = None
        self._show_international_numbers_link = None
        self.discriminator = None
        if third_party_audio is not None:
            self.third_party_audio = third_party_audio
        if audio_conference_info is not None:
            self.audio_conference_info = audio_conference_info
        if show_international_numbers_link is not None:
            self.show_international_numbers_link = show_international_numbers_link

    @property
    def third_party_audio(self):
        """Gets the third_party_audio of this UserSettingsMeetingSettings2.  # noqa: E501

        Third party audio conference.  # noqa: E501

        :return: The third_party_audio of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._third_party_audio

    @third_party_audio.setter
    def third_party_audio(self, third_party_audio):
        """Sets the third_party_audio of this UserSettingsMeetingSettings2.

        Third party audio conference.  # noqa: E501

        :param third_party_audio: The third_party_audio of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._third_party_audio = third_party_audio

    @property
    def audio_conference_info(self):
        """Gets the audio_conference_info of this UserSettingsMeetingSettings2.  # noqa: E501

        Third party audio conference info.  # noqa: E501

        :return: The audio_conference_info of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: str
        """
        return self._audio_conference_info

    @audio_conference_info.setter
    def audio_conference_info(self, audio_conference_info):
        """Sets the audio_conference_info of this UserSettingsMeetingSettings2.

        Third party audio conference info.  # noqa: E501

        :param audio_conference_info: The audio_conference_info of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: str
        """

        self._audio_conference_info = audio_conference_info

    @property
    def show_international_numbers_link(self):
        """Gets the show_international_numbers_link of this UserSettingsMeetingSettings2.  # noqa: E501

        Show the international numbers link on the invitation email.  # noqa: E501

        :return: The show_international_numbers_link of this UserSettingsMeetingSettings2.  # noqa: E501
        :rtype: bool
        """
        return self._show_international_numbers_link

    @show_international_numbers_link.setter
    def show_international_numbers_link(self, show_international_numbers_link):
        """Sets the show_international_numbers_link of this UserSettingsMeetingSettings2.

        Show the international numbers link on the invitation email.  # noqa: E501

        :param show_international_numbers_link: The show_international_numbers_link of this UserSettingsMeetingSettings2.  # noqa: E501
        :type: bool
        """

        self._show_international_numbers_link = show_international_numbers_link

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
        if issubclass(UserSettingsMeetingSettings2, dict):
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
        if not isinstance(other, UserSettingsMeetingSettings2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

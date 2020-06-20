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


class TSPGlobalDialInURLSetting(object):
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
        'audio_url': 'str'
    }

    attribute_map = {
        'audio_url': 'audio_url'
    }

    def __init__(self, audio_url=None):  # noqa: E501
        """TSPGlobalDialInURLSetting - a model defined in Swagger"""  # noqa: E501
        self._audio_url = None
        self.discriminator = None
        if audio_url is not None:
            self.audio_url = audio_url

    @property
    def audio_url(self):
        """Gets the audio_url of this TSPGlobalDialInURLSetting.  # noqa: E501

        The global dial-in URL for a TSP enabled account. The URL must be valid with a max-length of 512 characters.  # noqa: E501

        :return: The audio_url of this TSPGlobalDialInURLSetting.  # noqa: E501
        :rtype: str
        """
        return self._audio_url

    @audio_url.setter
    def audio_url(self, audio_url):
        """Sets the audio_url of this TSPGlobalDialInURLSetting.

        The global dial-in URL for a TSP enabled account. The URL must be valid with a max-length of 512 characters.  # noqa: E501

        :param audio_url: The audio_url of this TSPGlobalDialInURLSetting.  # noqa: E501
        :type: str
        """

        self._audio_url = audio_url

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
        if issubclass(TSPGlobalDialInURLSetting, dict):
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
        if not isinstance(other, TSPGlobalDialInURLSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

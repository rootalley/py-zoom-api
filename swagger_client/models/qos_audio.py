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


class QOSAudio(object):
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
        'bitrate': 'str',
        'latency': 'str',
        'jitter': 'str',
        'avg_loss': 'str',
        'max_loss': 'str'
    }

    attribute_map = {
        'bitrate': 'bitrate',
        'latency': 'latency',
        'jitter': 'jitter',
        'avg_loss': 'avg_loss',
        'max_loss': 'max_loss'
    }

    def __init__(self, bitrate=None, latency=None, jitter=None, avg_loss=None, max_loss=None):  # noqa: E501
        """QOSAudio - a model defined in Swagger"""  # noqa: E501
        self._bitrate = None
        self._latency = None
        self._jitter = None
        self._avg_loss = None
        self._max_loss = None
        self.discriminator = None
        if bitrate is not None:
            self.bitrate = bitrate
        if latency is not None:
            self.latency = latency
        if jitter is not None:
            self.jitter = jitter
        if avg_loss is not None:
            self.avg_loss = avg_loss
        if max_loss is not None:
            self.max_loss = max_loss

    @property
    def bitrate(self):
        """Gets the bitrate of this QOSAudio.  # noqa: E501

        Bitrate:  the number of bits per second that can be transmitted along a digital network.  # noqa: E501

        :return: The bitrate of this QOSAudio.  # noqa: E501
        :rtype: str
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this QOSAudio.

        Bitrate:  the number of bits per second that can be transmitted along a digital network.  # noqa: E501

        :param bitrate: The bitrate of this QOSAudio.  # noqa: E501
        :type: str
        """

        self._bitrate = bitrate

    @property
    def latency(self):
        """Gets the latency of this QOSAudio.  # noqa: E501

        Latency: The amount of time it takes for a pack to travel from one point to another. In Zoom's case, an audio, video, or screen share packet.  # noqa: E501

        :return: The latency of this QOSAudio.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this QOSAudio.

        Latency: The amount of time it takes for a pack to travel from one point to another. In Zoom's case, an audio, video, or screen share packet.  # noqa: E501

        :param latency: The latency of this QOSAudio.  # noqa: E501
        :type: str
        """

        self._latency = latency

    @property
    def jitter(self):
        """Gets the jitter of this QOSAudio.  # noqa: E501

        Jitter:  the variation in the delay of received packets.  # noqa: E501

        :return: The jitter of this QOSAudio.  # noqa: E501
        :rtype: str
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this QOSAudio.

        Jitter:  the variation in the delay of received packets.  # noqa: E501

        :param jitter: The jitter of this QOSAudio.  # noqa: E501
        :type: str
        """

        self._jitter = jitter

    @property
    def avg_loss(self):
        """Gets the avg_loss of this QOSAudio.  # noqa: E501

        Average loss: the average amount of packet loss, that is the percentage of packets that fail to arrive at their destination.  # noqa: E501

        :return: The avg_loss of this QOSAudio.  # noqa: E501
        :rtype: str
        """
        return self._avg_loss

    @avg_loss.setter
    def avg_loss(self, avg_loss):
        """Sets the avg_loss of this QOSAudio.

        Average loss: the average amount of packet loss, that is the percentage of packets that fail to arrive at their destination.  # noqa: E501

        :param avg_loss: The avg_loss of this QOSAudio.  # noqa: E501
        :type: str
        """

        self._avg_loss = avg_loss

    @property
    def max_loss(self):
        """Gets the max_loss of this QOSAudio.  # noqa: E501

        Max loss: the max amount of packet loss, that is the max percentage of packets that fail to arrive at their destination.  # noqa: E501

        :return: The max_loss of this QOSAudio.  # noqa: E501
        :rtype: str
        """
        return self._max_loss

    @max_loss.setter
    def max_loss(self, max_loss):
        """Sets the max_loss of this QOSAudio.

        Max loss: the max amount of packet loss, that is the max percentage of packets that fail to arrive at their destination.  # noqa: E501

        :param max_loss: The max_loss of this QOSAudio.  # noqa: E501
        :type: str
        """

        self._max_loss = max_loss

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
        if issubclass(QOSAudio, dict):
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
        if not isinstance(other, QOSAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

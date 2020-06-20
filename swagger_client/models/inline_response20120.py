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


class InlineResponse20120(object):
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
        'registrant_id': 'str',
        'id': 'str',
        'topic': 'str',
        'start_time': 'datetime',
        'join_url': 'str'
    }

    attribute_map = {
        'registrant_id': 'registrant_id',
        'id': 'id',
        'topic': 'topic',
        'start_time': 'start_time',
        'join_url': 'join_url'
    }

    def __init__(self, registrant_id=None, id=None, topic=None, start_time=None, join_url=None):  # noqa: E501
        """InlineResponse20120 - a model defined in Swagger"""  # noqa: E501
        self._registrant_id = None
        self._id = None
        self._topic = None
        self._start_time = None
        self._join_url = None
        self.discriminator = None
        if registrant_id is not None:
            self.registrant_id = registrant_id
        if id is not None:
            self.id = id
        if topic is not None:
            self.topic = topic
        if start_time is not None:
            self.start_time = start_time
        if join_url is not None:
            self.join_url = join_url

    @property
    def registrant_id(self):
        """Gets the registrant_id of this InlineResponse20120.  # noqa: E501

        Registrant ID  # noqa: E501

        :return: The registrant_id of this InlineResponse20120.  # noqa: E501
        :rtype: str
        """
        return self._registrant_id

    @registrant_id.setter
    def registrant_id(self, registrant_id):
        """Sets the registrant_id of this InlineResponse20120.

        Registrant ID  # noqa: E501

        :param registrant_id: The registrant_id of this InlineResponse20120.  # noqa: E501
        :type: str
        """

        self._registrant_id = registrant_id

    @property
    def id(self):
        """Gets the id of this InlineResponse20120.  # noqa: E501

        Webinar ID  # noqa: E501

        :return: The id of this InlineResponse20120.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20120.

        Webinar ID  # noqa: E501

        :param id: The id of this InlineResponse20120.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def topic(self):
        """Gets the topic of this InlineResponse20120.  # noqa: E501

        Topic  # noqa: E501

        :return: The topic of this InlineResponse20120.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this InlineResponse20120.

        Topic  # noqa: E501

        :param topic: The topic of this InlineResponse20120.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20120.  # noqa: E501

        Start time  # noqa: E501

        :return: The start_time of this InlineResponse20120.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20120.

        Start time  # noqa: E501

        :param start_time: The start_time of this InlineResponse20120.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def join_url(self):
        """Gets the join_url of this InlineResponse20120.  # noqa: E501

        Unique URL for this registrant to join the Webinar. This URL should only be shared with the registrant for whom the API request was made.  # noqa: E501

        :return: The join_url of this InlineResponse20120.  # noqa: E501
        :rtype: str
        """
        return self._join_url

    @join_url.setter
    def join_url(self, join_url):
        """Sets the join_url of this InlineResponse20120.

        Unique URL for this registrant to join the Webinar. This URL should only be shared with the registrant for whom the API request was made.  # noqa: E501

        :param join_url: The join_url of this InlineResponse20120.  # noqa: E501
        :type: str
        """

        self._join_url = join_url

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
        if issubclass(InlineResponse20120, dict):
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
        if not isinstance(other, InlineResponse20120):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
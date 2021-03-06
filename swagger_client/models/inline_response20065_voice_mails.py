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


class InlineResponse20065VoiceMails(object):
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
        'id': 'str',
        'date_time': 'str',
        'download_url': 'str',
        'duration': 'str',
        'caller_number': 'str',
        'caller_number_type': 'str',
        'caller_name': 'str',
        'callee_number': 'str',
        'callee_number_type': 'str',
        'callee_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'date_time': 'date_time',
        'download_url': 'download_url',
        'duration': 'duration',
        'caller_number': 'caller_number',
        'caller_number_type': 'caller_number_type',
        'caller_name': 'caller_name',
        'callee_number': 'callee_number',
        'callee_number_type': 'callee_number_type',
        'callee_name': 'callee_name',
        'status': 'status'
    }

    def __init__(self, id=None, date_time=None, download_url=None, duration=None, caller_number=None, caller_number_type=None, caller_name=None, callee_number=None, callee_number_type=None, callee_name=None, status=None):  # noqa: E501
        """InlineResponse20065VoiceMails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_time = None
        self._download_url = None
        self._duration = None
        self._caller_number = None
        self._caller_number_type = None
        self._caller_name = None
        self._callee_number = None
        self._callee_number_type = None
        self._callee_name = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if date_time is not None:
            self.date_time = date_time
        if download_url is not None:
            self.download_url = download_url
        if duration is not None:
            self.duration = duration
        if caller_number is not None:
            self.caller_number = caller_number
        if caller_number_type is not None:
            self.caller_number_type = caller_number_type
        if caller_name is not None:
            self.caller_name = caller_name
        if callee_number is not None:
            self.callee_number = callee_number
        if callee_number_type is not None:
            self.callee_number_type = callee_number_type
        if callee_name is not None:
            self.callee_name = callee_name
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this InlineResponse20065VoiceMails.  # noqa: E501

        Id of voice mail  # noqa: E501

        :return: The id of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20065VoiceMails.

        Id of voice mail  # noqa: E501

        :param id: The id of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse20065VoiceMails.  # noqa: E501

        Date the voice mail started  # noqa: E501

        :return: The date_time of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse20065VoiceMails.

        Date the voice mail started  # noqa: E501

        :param date_time: The date_time of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._date_time = date_time

    @property
    def download_url(self):
        """Gets the download_url of this InlineResponse20065VoiceMails.  # noqa: E501

        Download url of attachment  # noqa: E501

        :return: The download_url of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this InlineResponse20065VoiceMails.

        Download url of attachment  # noqa: E501

        :param download_url: The download_url of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20065VoiceMails.  # noqa: E501

        Duration of the voice mail  # noqa: E501

        :return: The duration of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20065VoiceMails.

        Duration of the voice mail  # noqa: E501

        :param duration: The duration of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def caller_number(self):
        """Gets the caller_number of this InlineResponse20065VoiceMails.  # noqa: E501

        Number of caller   # noqa: E501

        :return: The caller_number of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._caller_number

    @caller_number.setter
    def caller_number(self, caller_number):
        """Sets the caller_number of this InlineResponse20065VoiceMails.

        Number of caller   # noqa: E501

        :param caller_number: The caller_number of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._caller_number = caller_number

    @property
    def caller_number_type(self):
        """Gets the caller_number_type of this InlineResponse20065VoiceMails.  # noqa: E501

        Type of caller's number. 1 - internal | 2 - external  # noqa: E501

        :return: The caller_number_type of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._caller_number_type

    @caller_number_type.setter
    def caller_number_type(self, caller_number_type):
        """Sets the caller_number_type of this InlineResponse20065VoiceMails.

        Type of caller's number. 1 - internal | 2 - external  # noqa: E501

        :param caller_number_type: The caller_number_type of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._caller_number_type = caller_number_type

    @property
    def caller_name(self):
        """Gets the caller_name of this InlineResponse20065VoiceMails.  # noqa: E501

        Contact name of caller  # noqa: E501

        :return: The caller_name of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """Sets the caller_name of this InlineResponse20065VoiceMails.

        Contact name of caller  # noqa: E501

        :param caller_name: The caller_name of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._caller_name = caller_name

    @property
    def callee_number(self):
        """Gets the callee_number of this InlineResponse20065VoiceMails.  # noqa: E501

        Number of callee  # noqa: E501

        :return: The callee_number of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._callee_number

    @callee_number.setter
    def callee_number(self, callee_number):
        """Sets the callee_number of this InlineResponse20065VoiceMails.

        Number of callee  # noqa: E501

        :param callee_number: The callee_number of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._callee_number = callee_number

    @property
    def callee_number_type(self):
        """Gets the callee_number_type of this InlineResponse20065VoiceMails.  # noqa: E501

        Type of callee's number. 1 - internal | 2 - external  # noqa: E501

        :return: The callee_number_type of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._callee_number_type

    @callee_number_type.setter
    def callee_number_type(self, callee_number_type):
        """Sets the callee_number_type of this InlineResponse20065VoiceMails.

        Type of callee's number. 1 - internal | 2 - external  # noqa: E501

        :param callee_number_type: The callee_number_type of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._callee_number_type = callee_number_type

    @property
    def callee_name(self):
        """Gets the callee_name of this InlineResponse20065VoiceMails.  # noqa: E501

        Contact name of callee  # noqa: E501

        :return: The callee_name of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._callee_name

    @callee_name.setter
    def callee_name(self, callee_name):
        """Sets the callee_name of this InlineResponse20065VoiceMails.

        Contact name of callee  # noqa: E501

        :param callee_name: The callee_name of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """

        self._callee_name = callee_name

    @property
    def status(self):
        """Gets the status of this InlineResponse20065VoiceMails.  # noqa: E501

        Status of the voice mail. Can be either 'read' or 'unread'  # noqa: E501

        :return: The status of this InlineResponse20065VoiceMails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20065VoiceMails.

        Status of the voice mail. Can be either 'read' or 'unread'  # noqa: E501

        :param status: The status of this InlineResponse20065VoiceMails.  # noqa: E501
        :type: str
        """
        allowed_values = ["read", "unread"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(InlineResponse20065VoiceMails, dict):
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
        if not isinstance(other, InlineResponse20065VoiceMails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

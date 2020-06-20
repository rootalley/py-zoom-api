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


class InlineResponse20039(object):
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
        'uuid': 'str',
        'id': 'int',
        'type': 'int',
        'topic': 'str',
        'user_name': 'str',
        'user_email': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'duration': 'int',
        'total_minutes': 'int',
        'participants_count': 'int',
        'tracking_fields': 'list[InlineResponse20036TrackingFields]',
        'dept': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'id': 'id',
        'type': 'type',
        'topic': 'topic',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration',
        'total_minutes': 'total_minutes',
        'participants_count': 'participants_count',
        'tracking_fields': 'tracking_fields',
        'dept': 'dept'
    }

    def __init__(self, uuid=None, id=None, type=None, topic=None, user_name=None, user_email=None, start_time=None, end_time=None, duration=None, total_minutes=None, participants_count=None, tracking_fields=None, dept=None):  # noqa: E501
        """InlineResponse20039 - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._id = None
        self._type = None
        self._topic = None
        self._user_name = None
        self._user_email = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._total_minutes = None
        self._participants_count = None
        self._tracking_fields = None
        self._dept = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if topic is not None:
            self.topic = topic
        if user_name is not None:
            self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if participants_count is not None:
            self.participants_count = participants_count
        if tracking_fields is not None:
            self.tracking_fields = tracking_fields
        if dept is not None:
            self.dept = dept

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20039.  # noqa: E501

        Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.  # noqa: E501

        :return: The uuid of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20039.

        Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.  # noqa: E501

        :param uuid: The uuid of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def id(self):
        """Gets the id of this InlineResponse20039.  # noqa: E501

        [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in \"**long**\" format(represented as int64 data type in JSON), also known as the meeting number.  # noqa: E501

        :return: The id of this InlineResponse20039.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20039.

        [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in \"**long**\" format(represented as int64 data type in JSON), also known as the meeting number.  # noqa: E501

        :param id: The id of this InlineResponse20039.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InlineResponse20039.  # noqa: E501

        Meeting type.  # noqa: E501

        :return: The type of this InlineResponse20039.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20039.

        Meeting type.  # noqa: E501

        :param type: The type of this InlineResponse20039.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def topic(self):
        """Gets the topic of this InlineResponse20039.  # noqa: E501

        Meeting topic.  # noqa: E501

        :return: The topic of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this InlineResponse20039.

        Meeting topic.  # noqa: E501

        :param topic: The topic of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def user_name(self):
        """Gets the user_name of this InlineResponse20039.  # noqa: E501

        User display name.  # noqa: E501

        :return: The user_name of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InlineResponse20039.

        User display name.  # noqa: E501

        :param user_name: The user_name of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this InlineResponse20039.  # noqa: E501

        User email.  # noqa: E501

        :return: The user_email of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this InlineResponse20039.

        User email.  # noqa: E501

        :param user_email: The user_email of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20039.  # noqa: E501

        Meeting start time.  # noqa: E501

        :return: The start_time of this InlineResponse20039.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20039.

        Meeting start time.  # noqa: E501

        :param start_time: The start_time of this InlineResponse20039.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InlineResponse20039.  # noqa: E501

        Meeting end time.  # noqa: E501

        :return: The end_time of this InlineResponse20039.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InlineResponse20039.

        Meeting end time.  # noqa: E501

        :param end_time: The end_time of this InlineResponse20039.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20039.  # noqa: E501

        Meeting duration.  # noqa: E501

        :return: The duration of this InlineResponse20039.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20039.

        Meeting duration.  # noqa: E501

        :param duration: The duration of this InlineResponse20039.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def total_minutes(self):
        """Gets the total_minutes of this InlineResponse20039.  # noqa: E501

        Number of Webinar minutes. This represents the total amount of Webinar minutes attended by each participant including the host, for a Webinar hosted by the user. For instance if there were one host(named A) and one participant(named B) in a Webinar, the value of total_minutes would be calculated as below:  **total_minutes** = Total Webinar Attendance Minutes of A + Total Webinar Attendance Minutes of B  # noqa: E501

        :return: The total_minutes of this InlineResponse20039.  # noqa: E501
        :rtype: int
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this InlineResponse20039.

        Number of Webinar minutes. This represents the total amount of Webinar minutes attended by each participant including the host, for a Webinar hosted by the user. For instance if there were one host(named A) and one participant(named B) in a Webinar, the value of total_minutes would be calculated as below:  **total_minutes** = Total Webinar Attendance Minutes of A + Total Webinar Attendance Minutes of B  # noqa: E501

        :param total_minutes: The total_minutes of this InlineResponse20039.  # noqa: E501
        :type: int
        """

        self._total_minutes = total_minutes

    @property
    def participants_count(self):
        """Gets the participants_count of this InlineResponse20039.  # noqa: E501

        Number of meeting participants.  # noqa: E501

        :return: The participants_count of this InlineResponse20039.  # noqa: E501
        :rtype: int
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """Sets the participants_count of this InlineResponse20039.

        Number of meeting participants.  # noqa: E501

        :param participants_count: The participants_count of this InlineResponse20039.  # noqa: E501
        :type: int
        """

        self._participants_count = participants_count

    @property
    def tracking_fields(self):
        """Gets the tracking_fields of this InlineResponse20039.  # noqa: E501

        Tracking fields.  # noqa: E501

        :return: The tracking_fields of this InlineResponse20039.  # noqa: E501
        :rtype: list[InlineResponse20036TrackingFields]
        """
        return self._tracking_fields

    @tracking_fields.setter
    def tracking_fields(self, tracking_fields):
        """Sets the tracking_fields of this InlineResponse20039.

        Tracking fields.  # noqa: E501

        :param tracking_fields: The tracking_fields of this InlineResponse20039.  # noqa: E501
        :type: list[InlineResponse20036TrackingFields]
        """

        self._tracking_fields = tracking_fields

    @property
    def dept(self):
        """Gets the dept of this InlineResponse20039.  # noqa: E501

        Department of the host.  # noqa: E501

        :return: The dept of this InlineResponse20039.  # noqa: E501
        :rtype: str
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this InlineResponse20039.

        Department of the host.  # noqa: E501

        :param dept: The dept of this InlineResponse20039.  # noqa: E501
        :type: str
        """

        self._dept = dept

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
        if issubclass(InlineResponse20039, dict):
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
        if not isinstance(other, InlineResponse20039):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

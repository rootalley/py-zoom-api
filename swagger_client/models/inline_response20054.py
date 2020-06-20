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


class InlineResponse20054(object):
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
        'agenda': 'str',
        'created_at': 'datetime',
        'duration': 'int',
        'host_id': 'str',
        'id': 'int',
        'join_url': 'str',
        'occurrences': 'list[MeetingInfoOccurrences]',
        'password': 'str',
        'recurrence': 'RecurrenceWebinar',
        'settings': 'SessionWebinarSettings',
        'start_time': 'datetime',
        'start_url': 'str',
        'timezone': 'str',
        'topic': 'str',
        'tracking_fields': 'list[MeetingTrackingFields]',
        'type': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'agenda': 'agenda',
        'created_at': 'created_at',
        'duration': 'duration',
        'host_id': 'host_id',
        'id': 'id',
        'join_url': 'join_url',
        'occurrences': 'occurrences',
        'password': 'password',
        'recurrence': 'recurrence',
        'settings': 'settings',
        'start_time': 'start_time',
        'start_url': 'start_url',
        'timezone': 'timezone',
        'topic': 'topic',
        'tracking_fields': 'tracking_fields',
        'type': 'type',
        'uuid': 'uuid'
    }

    def __init__(self, agenda=None, created_at=None, duration=None, host_id=None, id=None, join_url=None, occurrences=None, password=None, recurrence=None, settings=None, start_time=None, start_url=None, timezone=None, topic=None, tracking_fields=None, type=None, uuid=None):  # noqa: E501
        """InlineResponse20054 - a model defined in Swagger"""  # noqa: E501
        self._agenda = None
        self._created_at = None
        self._duration = None
        self._host_id = None
        self._id = None
        self._join_url = None
        self._occurrences = None
        self._password = None
        self._recurrence = None
        self._settings = None
        self._start_time = None
        self._start_url = None
        self._timezone = None
        self._topic = None
        self._tracking_fields = None
        self._type = None
        self._uuid = None
        self.discriminator = None
        if agenda is not None:
            self.agenda = agenda
        if created_at is not None:
            self.created_at = created_at
        if duration is not None:
            self.duration = duration
        if host_id is not None:
            self.host_id = host_id
        if id is not None:
            self.id = id
        if join_url is not None:
            self.join_url = join_url
        if occurrences is not None:
            self.occurrences = occurrences
        if password is not None:
            self.password = password
        if recurrence is not None:
            self.recurrence = recurrence
        if settings is not None:
            self.settings = settings
        if start_time is not None:
            self.start_time = start_time
        if start_url is not None:
            self.start_url = start_url
        if timezone is not None:
            self.timezone = timezone
        if topic is not None:
            self.topic = topic
        if tracking_fields is not None:
            self.tracking_fields = tracking_fields
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid

    @property
    def agenda(self):
        """Gets the agenda of this InlineResponse20054.  # noqa: E501

        Webinar agenda.  # noqa: E501

        :return: The agenda of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._agenda

    @agenda.setter
    def agenda(self, agenda):
        """Sets the agenda of this InlineResponse20054.

        Webinar agenda.  # noqa: E501

        :param agenda: The agenda of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._agenda = agenda

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20054.  # noqa: E501

        Create time.  # noqa: E501

        :return: The created_at of this InlineResponse20054.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20054.

        Create time.  # noqa: E501

        :param created_at: The created_at of this InlineResponse20054.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20054.  # noqa: E501

        Webinar duration.  # noqa: E501

        :return: The duration of this InlineResponse20054.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20054.

        Webinar duration.  # noqa: E501

        :param duration: The duration of this InlineResponse20054.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def host_id(self):
        """Gets the host_id of this InlineResponse20054.  # noqa: E501

        ID of the user set as host of webinar.  # noqa: E501

        :return: The host_id of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this InlineResponse20054.

        ID of the user set as host of webinar.  # noqa: E501

        :param host_id: The host_id of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def id(self):
        """Gets the id of this InlineResponse20054.  # noqa: E501

        Webinar ID in \"**long**\" format(represented as int64 data type in JSON), also known as the webinar number.  # noqa: E501

        :return: The id of this InlineResponse20054.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20054.

        Webinar ID in \"**long**\" format(represented as int64 data type in JSON), also known as the webinar number.  # noqa: E501

        :param id: The id of this InlineResponse20054.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def join_url(self):
        """Gets the join_url of this InlineResponse20054.  # noqa: E501

        URL to join the Webinar. This URL should only be shared with the users who should be invited to the Webinar.  # noqa: E501

        :return: The join_url of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._join_url

    @join_url.setter
    def join_url(self, join_url):
        """Sets the join_url of this InlineResponse20054.

        URL to join the Webinar. This URL should only be shared with the users who should be invited to the Webinar.  # noqa: E501

        :param join_url: The join_url of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._join_url = join_url

    @property
    def occurrences(self):
        """Gets the occurrences of this InlineResponse20054.  # noqa: E501

        Array of occurrence objects.  # noqa: E501

        :return: The occurrences of this InlineResponse20054.  # noqa: E501
        :rtype: list[MeetingInfoOccurrences]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this InlineResponse20054.

        Array of occurrence objects.  # noqa: E501

        :param occurrences: The occurrences of this InlineResponse20054.  # noqa: E501
        :type: list[MeetingInfoOccurrences]
        """

        self._occurrences = occurrences

    @property
    def password(self):
        """Gets the password of this InlineResponse20054.  # noqa: E501

        Webinar password.   If \"Require a password when scheduling new meetings\" setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the password field will be autogenerated for the Webinar in the response even if it is not provided in the API request. <br><br> **Note:** If the account owner or the admin has configured [minimum password requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the password value provided here must meet those requirements. <br><br>If the requirements are enabled, you can view those requirements by calling either the [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings) or the  [Get Account Settings](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) API.         # noqa: E501

        :return: The password of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineResponse20054.

        Webinar password.   If \"Require a password when scheduling new meetings\" setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the password field will be autogenerated for the Webinar in the response even if it is not provided in the API request. <br><br> **Note:** If the account owner or the admin has configured [minimum password requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the password value provided here must meet those requirements. <br><br>If the requirements are enabled, you can view those requirements by calling either the [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings) or the  [Get Account Settings](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) API.         # noqa: E501

        :param password: The password of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def recurrence(self):
        """Gets the recurrence of this InlineResponse20054.  # noqa: E501


        :return: The recurrence of this InlineResponse20054.  # noqa: E501
        :rtype: RecurrenceWebinar
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this InlineResponse20054.


        :param recurrence: The recurrence of this InlineResponse20054.  # noqa: E501
        :type: RecurrenceWebinar
        """

        self._recurrence = recurrence

    @property
    def settings(self):
        """Gets the settings of this InlineResponse20054.  # noqa: E501


        :return: The settings of this InlineResponse20054.  # noqa: E501
        :rtype: SessionWebinarSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this InlineResponse20054.


        :param settings: The settings of this InlineResponse20054.  # noqa: E501
        :type: SessionWebinarSettings
        """

        self._settings = settings

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20054.  # noqa: E501

        Webinar start time in GMT/UTC.  # noqa: E501

        :return: The start_time of this InlineResponse20054.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20054.

        Webinar start time in GMT/UTC.  # noqa: E501

        :param start_time: The start_time of this InlineResponse20054.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def start_url(self):
        """Gets the start_url of this InlineResponse20054.  # noqa: E501

        <br><aside>The <code>start_url</code> of a Webinar is a URL using which a host or an alternative host can start the Webinar. This URL should only be used by the host of the meeting and should not be shared with anyone other than the host of the Webinar.   The expiration time for the <code>start_url</code> field listed in the response of [Create a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarcreate) is two hours for all regular users.    For users created using the <code>custCreate</code> option via the [Create Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usercreate) API, the expiration time of the <code>start_url</code> field is 90 days.   For security reasons, to retrieve the latest value for the <code>start_url</code> field programmatically (after expiry), you must call the [Retrieve a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinar) and refer to the value of the <code>start_url</code> field in the response.</aside><br><br><br>  # noqa: E501

        :return: The start_url of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._start_url

    @start_url.setter
    def start_url(self, start_url):
        """Sets the start_url of this InlineResponse20054.

        <br><aside>The <code>start_url</code> of a Webinar is a URL using which a host or an alternative host can start the Webinar. This URL should only be used by the host of the meeting and should not be shared with anyone other than the host of the Webinar.   The expiration time for the <code>start_url</code> field listed in the response of [Create a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarcreate) is two hours for all regular users.    For users created using the <code>custCreate</code> option via the [Create Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usercreate) API, the expiration time of the <code>start_url</code> field is 90 days.   For security reasons, to retrieve the latest value for the <code>start_url</code> field programmatically (after expiry), you must call the [Retrieve a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinar) and refer to the value of the <code>start_url</code> field in the response.</aside><br><br><br>  # noqa: E501

        :param start_url: The start_url of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._start_url = start_url

    @property
    def timezone(self):
        """Gets the timezone of this InlineResponse20054.  # noqa: E501

        Time zone to format start_time.  # noqa: E501

        :return: The timezone of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InlineResponse20054.

        Time zone to format start_time.  # noqa: E501

        :param timezone: The timezone of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def topic(self):
        """Gets the topic of this InlineResponse20054.  # noqa: E501

        Webinar topic.  # noqa: E501

        :return: The topic of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this InlineResponse20054.

        Webinar topic.  # noqa: E501

        :param topic: The topic of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def tracking_fields(self):
        """Gets the tracking_fields of this InlineResponse20054.  # noqa: E501

        Tracking fields  # noqa: E501

        :return: The tracking_fields of this InlineResponse20054.  # noqa: E501
        :rtype: list[MeetingTrackingFields]
        """
        return self._tracking_fields

    @tracking_fields.setter
    def tracking_fields(self, tracking_fields):
        """Sets the tracking_fields of this InlineResponse20054.

        Tracking fields  # noqa: E501

        :param tracking_fields: The tracking_fields of this InlineResponse20054.  # noqa: E501
        :type: list[MeetingTrackingFields]
        """

        self._tracking_fields = tracking_fields

    @property
    def type(self):
        """Gets the type of this InlineResponse20054.  # noqa: E501

        Webinar Types:<br>`5` - Webinar.<br>`6` - Recurring webinar with no fixed time.<br>`9` - Recurring webinar with a fixed time.  # noqa: E501

        :return: The type of this InlineResponse20054.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20054.

        Webinar Types:<br>`5` - Webinar.<br>`6` - Recurring webinar with no fixed time.<br>`9` - Recurring webinar with a fixed time.  # noqa: E501

        :param type: The type of this InlineResponse20054.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20054.  # noqa: E501

        Unique Webinar ID. Each Webinar instance will generate its own Webinar UUID (i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). You can retrieve a list of UUIDs from past Webinar instances using [this API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/pastwebinars). Please double encode your UUID when using it for API calls if the UUID begins with a '/'or contains '//' in it.    # noqa: E501

        :return: The uuid of this InlineResponse20054.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20054.

        Unique Webinar ID. Each Webinar instance will generate its own Webinar UUID (i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). You can retrieve a list of UUIDs from past Webinar instances using [this API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/pastwebinars). Please double encode your UUID when using it for API calls if the UUID begins with a '/'or contains '//' in it.    # noqa: E501

        :param uuid: The uuid of this InlineResponse20054.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(InlineResponse20054, dict):
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
        if not isinstance(other, InlineResponse20054):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

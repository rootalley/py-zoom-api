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


class AccountSettingsScheduleMeeting(object):
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
        'host_video': 'bool',
        'participant_video': 'bool',
        'audio_type': 'str',
        'join_before_host': 'bool',
        'enforce_login': 'bool',
        'enforce_login_with_domains': 'bool',
        'enforce_login_domains': 'str',
        'not_store_meeting_topic': 'bool',
        'force_pmi_jbh_password': 'bool',
        'use_pmi_for_scheduled_meetings': 'bool',
        'use_pmi_for_instant_meetings': 'bool',
        'require_password_for_scheduling_new_meetings': 'bool',
        'require_password_for_scheduled_meetings': 'bool',
        'require_password_for_instant_meetings': 'bool',
        'require_password_for_pmi_meetings': 'str',
        'meeting_password_requirement': 'AccountSettingsScheduleMeetingMeetingPasswordRequirement',
        'personal_meeting': 'bool'
    }

    attribute_map = {
        'host_video': 'host_video',
        'participant_video': 'participant_video',
        'audio_type': 'audio_type',
        'join_before_host': 'join_before_host',
        'enforce_login': 'enforce_login',
        'enforce_login_with_domains': 'enforce_login_with_domains',
        'enforce_login_domains': 'enforce_login_domains',
        'not_store_meeting_topic': 'not_store_meeting_topic',
        'force_pmi_jbh_password': 'force_pmi_jbh_password',
        'use_pmi_for_scheduled_meetings': 'use_pmi_for_scheduled_meetings',
        'use_pmi_for_instant_meetings': 'use_pmi_for_instant_meetings',
        'require_password_for_scheduling_new_meetings': 'require_password_for_scheduling_new_meetings',
        'require_password_for_scheduled_meetings': 'require_password_for_scheduled_meetings',
        'require_password_for_instant_meetings': 'require_password_for_instant_meetings',
        'require_password_for_pmi_meetings': 'require_password_for_pmi_meetings',
        'meeting_password_requirement': 'meeting_password_requirement',
        'personal_meeting': 'personal_meeting'
    }

    def __init__(self, host_video=None, participant_video=None, audio_type='both', join_before_host=None, enforce_login=None, enforce_login_with_domains=None, enforce_login_domains=None, not_store_meeting_topic=None, force_pmi_jbh_password=None, use_pmi_for_scheduled_meetings=None, use_pmi_for_instant_meetings=None, require_password_for_scheduling_new_meetings=None, require_password_for_scheduled_meetings=None, require_password_for_instant_meetings=None, require_password_for_pmi_meetings=None, meeting_password_requirement=None, personal_meeting=None):  # noqa: E501
        """AccountSettingsScheduleMeeting - a model defined in Swagger"""  # noqa: E501
        self._host_video = None
        self._participant_video = None
        self._audio_type = None
        self._join_before_host = None
        self._enforce_login = None
        self._enforce_login_with_domains = None
        self._enforce_login_domains = None
        self._not_store_meeting_topic = None
        self._force_pmi_jbh_password = None
        self._use_pmi_for_scheduled_meetings = None
        self._use_pmi_for_instant_meetings = None
        self._require_password_for_scheduling_new_meetings = None
        self._require_password_for_scheduled_meetings = None
        self._require_password_for_instant_meetings = None
        self._require_password_for_pmi_meetings = None
        self._meeting_password_requirement = None
        self._personal_meeting = None
        self.discriminator = None
        if host_video is not None:
            self.host_video = host_video
        if participant_video is not None:
            self.participant_video = participant_video
        if audio_type is not None:
            self.audio_type = audio_type
        if join_before_host is not None:
            self.join_before_host = join_before_host
        if enforce_login is not None:
            self.enforce_login = enforce_login
        if enforce_login_with_domains is not None:
            self.enforce_login_with_domains = enforce_login_with_domains
        if enforce_login_domains is not None:
            self.enforce_login_domains = enforce_login_domains
        if not_store_meeting_topic is not None:
            self.not_store_meeting_topic = not_store_meeting_topic
        if force_pmi_jbh_password is not None:
            self.force_pmi_jbh_password = force_pmi_jbh_password
        if use_pmi_for_scheduled_meetings is not None:
            self.use_pmi_for_scheduled_meetings = use_pmi_for_scheduled_meetings
        if use_pmi_for_instant_meetings is not None:
            self.use_pmi_for_instant_meetings = use_pmi_for_instant_meetings
        if require_password_for_scheduling_new_meetings is not None:
            self.require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings
        if require_password_for_scheduled_meetings is not None:
            self.require_password_for_scheduled_meetings = require_password_for_scheduled_meetings
        if require_password_for_instant_meetings is not None:
            self.require_password_for_instant_meetings = require_password_for_instant_meetings
        if require_password_for_pmi_meetings is not None:
            self.require_password_for_pmi_meetings = require_password_for_pmi_meetings
        if meeting_password_requirement is not None:
            self.meeting_password_requirement = meeting_password_requirement
        if personal_meeting is not None:
            self.personal_meeting = personal_meeting

    @property
    def host_video(self):
        """Gets the host_video of this AccountSettingsScheduleMeeting.  # noqa: E501

        Start meetings with the host video on.  # noqa: E501

        :return: The host_video of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._host_video

    @host_video.setter
    def host_video(self, host_video):
        """Sets the host_video of this AccountSettingsScheduleMeeting.

        Start meetings with the host video on.  # noqa: E501

        :param host_video: The host_video of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._host_video = host_video

    @property
    def participant_video(self):
        """Gets the participant_video of this AccountSettingsScheduleMeeting.  # noqa: E501

        Start meetings with the participant video on. Participants can change this setting during the meeting.  # noqa: E501

        :return: The participant_video of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._participant_video

    @participant_video.setter
    def participant_video(self, participant_video):
        """Sets the participant_video of this AccountSettingsScheduleMeeting.

        Start meetings with the participant video on. Participants can change this setting during the meeting.  # noqa: E501

        :param participant_video: The participant_video of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._participant_video = participant_video

    @property
    def audio_type(self):
        """Gets the audio_type of this AccountSettingsScheduleMeeting.  # noqa: E501

        Determine how participants can join the audio portion of the meeting.<br>`both` - Telephony and VoIP.<br>`telephony` - Audio PSTN telephony only.<br>`voip` - VoIP only.<br>`thirdParty` - 3rd party audio conference.  # noqa: E501

        :return: The audio_type of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: str
        """
        return self._audio_type

    @audio_type.setter
    def audio_type(self, audio_type):
        """Sets the audio_type of this AccountSettingsScheduleMeeting.

        Determine how participants can join the audio portion of the meeting.<br>`both` - Telephony and VoIP.<br>`telephony` - Audio PSTN telephony only.<br>`voip` - VoIP only.<br>`thirdParty` - 3rd party audio conference.  # noqa: E501

        :param audio_type: The audio_type of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: str
        """
        allowed_values = ["both", "telephony", "voip", "thirdParty"]  # noqa: E501
        if audio_type not in allowed_values:
            raise ValueError(
                "Invalid value for `audio_type` ({0}), must be one of {1}"  # noqa: E501
                .format(audio_type, allowed_values)
            )

        self._audio_type = audio_type

    @property
    def join_before_host(self):
        """Gets the join_before_host of this AccountSettingsScheduleMeeting.  # noqa: E501

        Allow participants to join the meeting before the host arrives.  # noqa: E501

        :return: The join_before_host of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._join_before_host

    @join_before_host.setter
    def join_before_host(self, join_before_host):
        """Sets the join_before_host of this AccountSettingsScheduleMeeting.

        Allow participants to join the meeting before the host arrives.  # noqa: E501

        :param join_before_host: The join_before_host of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._join_before_host = join_before_host

    @property
    def enforce_login(self):
        """Gets the enforce_login of this AccountSettingsScheduleMeeting.  # noqa: E501

        Only Zoom users who are signed in can join meetings.  # noqa: E501

        :return: The enforce_login of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_login

    @enforce_login.setter
    def enforce_login(self, enforce_login):
        """Sets the enforce_login of this AccountSettingsScheduleMeeting.

        Only Zoom users who are signed in can join meetings.  # noqa: E501

        :param enforce_login: The enforce_login of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._enforce_login = enforce_login

    @property
    def enforce_login_with_domains(self):
        """Gets the enforce_login_with_domains of this AccountSettingsScheduleMeeting.  # noqa: E501

        Only signed in users with a specific domain can join meetings.  # noqa: E501

        :return: The enforce_login_with_domains of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_login_with_domains

    @enforce_login_with_domains.setter
    def enforce_login_with_domains(self, enforce_login_with_domains):
        """Sets the enforce_login_with_domains of this AccountSettingsScheduleMeeting.

        Only signed in users with a specific domain can join meetings.  # noqa: E501

        :param enforce_login_with_domains: The enforce_login_with_domains of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._enforce_login_with_domains = enforce_login_with_domains

    @property
    def enforce_login_domains(self):
        """Gets the enforce_login_domains of this AccountSettingsScheduleMeeting.  # noqa: E501

        Only signed in users with a specified domain can join the meeting.   # noqa: E501

        :return: The enforce_login_domains of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: str
        """
        return self._enforce_login_domains

    @enforce_login_domains.setter
    def enforce_login_domains(self, enforce_login_domains):
        """Sets the enforce_login_domains of this AccountSettingsScheduleMeeting.

        Only signed in users with a specified domain can join the meeting.   # noqa: E501

        :param enforce_login_domains: The enforce_login_domains of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: str
        """

        self._enforce_login_domains = enforce_login_domains

    @property
    def not_store_meeting_topic(self):
        """Gets the not_store_meeting_topic of this AccountSettingsScheduleMeeting.  # noqa: E501

        Always display \"Zoom Meeting\" as the meeting topic.  # noqa: E501

        :return: The not_store_meeting_topic of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._not_store_meeting_topic

    @not_store_meeting_topic.setter
    def not_store_meeting_topic(self, not_store_meeting_topic):
        """Sets the not_store_meeting_topic of this AccountSettingsScheduleMeeting.

        Always display \"Zoom Meeting\" as the meeting topic.  # noqa: E501

        :param not_store_meeting_topic: The not_store_meeting_topic of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._not_store_meeting_topic = not_store_meeting_topic

    @property
    def force_pmi_jbh_password(self):
        """Gets the force_pmi_jbh_password of this AccountSettingsScheduleMeeting.  # noqa: E501

        Require a password for Personal Meetings if attendees can join before host.  # noqa: E501

        :return: The force_pmi_jbh_password of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._force_pmi_jbh_password

    @force_pmi_jbh_password.setter
    def force_pmi_jbh_password(self, force_pmi_jbh_password):
        """Sets the force_pmi_jbh_password of this AccountSettingsScheduleMeeting.

        Require a password for Personal Meetings if attendees can join before host.  # noqa: E501

        :param force_pmi_jbh_password: The force_pmi_jbh_password of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._force_pmi_jbh_password = force_pmi_jbh_password

    @property
    def use_pmi_for_scheduled_meetings(self):
        """Gets the use_pmi_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Use Personal Meeting ID (PMI) when scheduling a meeting   # noqa: E501

        :return: The use_pmi_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi_for_scheduled_meetings

    @use_pmi_for_scheduled_meetings.setter
    def use_pmi_for_scheduled_meetings(self, use_pmi_for_scheduled_meetings):
        """Sets the use_pmi_for_scheduled_meetings of this AccountSettingsScheduleMeeting.

        Use Personal Meeting ID (PMI) when scheduling a meeting   # noqa: E501

        :param use_pmi_for_scheduled_meetings: The use_pmi_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._use_pmi_for_scheduled_meetings = use_pmi_for_scheduled_meetings

    @property
    def use_pmi_for_instant_meetings(self):
        """Gets the use_pmi_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Use Personal Meeting ID (PMI) when starting an instant meeting   # noqa: E501

        :return: The use_pmi_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi_for_instant_meetings

    @use_pmi_for_instant_meetings.setter
    def use_pmi_for_instant_meetings(self, use_pmi_for_instant_meetings):
        """Sets the use_pmi_for_instant_meetings of this AccountSettingsScheduleMeeting.

        Use Personal Meeting ID (PMI) when starting an instant meeting   # noqa: E501

        :param use_pmi_for_instant_meetings: The use_pmi_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._use_pmi_for_instant_meetings = use_pmi_for_instant_meetings

    @property
    def require_password_for_scheduling_new_meetings(self):
        """Gets the require_password_for_scheduling_new_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Require a password when scheduling new meetings. This setting applies for regular meetings that do not use PMI. If enabled, a password will be generated while a host schedules a new meeting and participants will be required to enter the password before they can join the meeting. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.  # noqa: E501

        :return: The require_password_for_scheduling_new_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduling_new_meetings

    @require_password_for_scheduling_new_meetings.setter
    def require_password_for_scheduling_new_meetings(self, require_password_for_scheduling_new_meetings):
        """Sets the require_password_for_scheduling_new_meetings of this AccountSettingsScheduleMeeting.

        Require a password when scheduling new meetings. This setting applies for regular meetings that do not use PMI. If enabled, a password will be generated while a host schedules a new meeting and participants will be required to enter the password before they can join the meeting. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.  # noqa: E501

        :param require_password_for_scheduling_new_meetings: The require_password_for_scheduling_new_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduling_new_meetings = require_password_for_scheduling_new_meetings

    @property
    def require_password_for_scheduled_meetings(self):
        """Gets the require_password_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Require a password for meetings which have already been scheduled   # noqa: E501

        :return: The require_password_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_scheduled_meetings

    @require_password_for_scheduled_meetings.setter
    def require_password_for_scheduled_meetings(self, require_password_for_scheduled_meetings):
        """Sets the require_password_for_scheduled_meetings of this AccountSettingsScheduleMeeting.

        Require a password for meetings which have already been scheduled   # noqa: E501

        :param require_password_for_scheduled_meetings: The require_password_for_scheduled_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_scheduled_meetings = require_password_for_scheduled_meetings

    @property
    def require_password_for_instant_meetings(self):
        """Gets the require_password_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Require a password for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :return: The require_password_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._require_password_for_instant_meetings

    @require_password_for_instant_meetings.setter
    def require_password_for_instant_meetings(self, require_password_for_instant_meetings):
        """Sets the require_password_for_instant_meetings of this AccountSettingsScheduleMeeting.

        Require a password for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :param require_password_for_instant_meetings: The require_password_for_instant_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._require_password_for_instant_meetings = require_password_for_instant_meetings

    @property
    def require_password_for_pmi_meetings(self):
        """Gets the require_password_for_pmi_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501

        Require a password for a meeting held using Personal Meeting ID (PMI) This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :return: The require_password_for_pmi_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: str
        """
        return self._require_password_for_pmi_meetings

    @require_password_for_pmi_meetings.setter
    def require_password_for_pmi_meetings(self, require_password_for_pmi_meetings):
        """Sets the require_password_for_pmi_meetings of this AccountSettingsScheduleMeeting.

        Require a password for a meeting held using Personal Meeting ID (PMI) This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.   # noqa: E501

        :param require_password_for_pmi_meetings: The require_password_for_pmi_meetings of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: str
        """
        allowed_values = ["jbh_only", "all", "none"]  # noqa: E501
        if require_password_for_pmi_meetings not in allowed_values:
            raise ValueError(
                "Invalid value for `require_password_for_pmi_meetings` ({0}), must be one of {1}"  # noqa: E501
                .format(require_password_for_pmi_meetings, allowed_values)
            )

        self._require_password_for_pmi_meetings = require_password_for_pmi_meetings

    @property
    def meeting_password_requirement(self):
        """Gets the meeting_password_requirement of this AccountSettingsScheduleMeeting.  # noqa: E501


        :return: The meeting_password_requirement of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: AccountSettingsScheduleMeetingMeetingPasswordRequirement
        """
        return self._meeting_password_requirement

    @meeting_password_requirement.setter
    def meeting_password_requirement(self, meeting_password_requirement):
        """Sets the meeting_password_requirement of this AccountSettingsScheduleMeeting.


        :param meeting_password_requirement: The meeting_password_requirement of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: AccountSettingsScheduleMeetingMeetingPasswordRequirement
        """

        self._meeting_password_requirement = meeting_password_requirement

    @property
    def personal_meeting(self):
        """Gets the personal_meeting of this AccountSettingsScheduleMeeting.  # noqa: E501

        Personal Meeting Setting.<br><br> `true`: Indicates that the **\"Enable Personal Meeting ID\"** setting is turned on. Users can choose to use personal meeting ID for their meetings. <br><br> `false`: Indicates that the **\"Enable Personal Meeting ID\"** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **\"Elevate to Zoom Meeting\"** on desk phone will be disabled.     # noqa: E501

        :return: The personal_meeting of this AccountSettingsScheduleMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._personal_meeting

    @personal_meeting.setter
    def personal_meeting(self, personal_meeting):
        """Sets the personal_meeting of this AccountSettingsScheduleMeeting.

        Personal Meeting Setting.<br><br> `true`: Indicates that the **\"Enable Personal Meeting ID\"** setting is turned on. Users can choose to use personal meeting ID for their meetings. <br><br> `false`: Indicates that the **\"Enable Personal Meeting ID\"** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **\"Elevate to Zoom Meeting\"** on desk phone will be disabled.     # noqa: E501

        :param personal_meeting: The personal_meeting of this AccountSettingsScheduleMeeting.  # noqa: E501
        :type: bool
        """

        self._personal_meeting = personal_meeting

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
        if issubclass(AccountSettingsScheduleMeeting, dict):
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
        if not isinstance(other, AccountSettingsScheduleMeeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

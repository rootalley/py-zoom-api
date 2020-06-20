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


class UsersuserIdmeetingsSettings(object):
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
        'cn_meeting': 'bool',
        'in_meeting': 'bool',
        'join_before_host': 'bool',
        'mute_upon_entry': 'bool',
        'watermark': 'bool',
        'use_pmi': 'bool',
        'approval_type': 'int',
        'registration_type': 'int',
        'audio': 'str',
        'auto_recording': 'str',
        'alternative_hosts': 'str',
        'close_registration': 'bool',
        'waiting_room': 'bool',
        'global_dial_in_countries': 'list[str]',
        'contact_name': 'str',
        'contact_email': 'str',
        'registrants_email_notification': 'bool',
        'meeting_authentication': 'bool',
        'authentication_option': 'str',
        'authentication_domains': 'str',
        'additional_data_center_regions': 'list[str]'
    }

    attribute_map = {
        'host_video': 'host_video',
        'participant_video': 'participant_video',
        'cn_meeting': 'cn_meeting',
        'in_meeting': 'in_meeting',
        'join_before_host': 'join_before_host',
        'mute_upon_entry': 'mute_upon_entry',
        'watermark': 'watermark',
        'use_pmi': 'use_pmi',
        'approval_type': 'approval_type',
        'registration_type': 'registration_type',
        'audio': 'audio',
        'auto_recording': 'auto_recording',
        'alternative_hosts': 'alternative_hosts',
        'close_registration': 'close_registration',
        'waiting_room': 'waiting_room',
        'global_dial_in_countries': 'global_dial_in_countries',
        'contact_name': 'contact_name',
        'contact_email': 'contact_email',
        'registrants_email_notification': 'registrants_email_notification',
        'meeting_authentication': 'meeting_authentication',
        'authentication_option': 'authentication_option',
        'authentication_domains': 'authentication_domains',
        'additional_data_center_regions': 'additional_data_center_regions'
    }

    def __init__(self, host_video=None, participant_video=None, cn_meeting=False, in_meeting=False, join_before_host=False, mute_upon_entry=False, watermark=False, use_pmi=False, approval_type=None, registration_type=None, audio='both', auto_recording='none', alternative_hosts=None, close_registration=False, waiting_room=None, global_dial_in_countries=None, contact_name=None, contact_email=None, registrants_email_notification=None, meeting_authentication=None, authentication_option=None, authentication_domains=None, additional_data_center_regions=None):  # noqa: E501
        """UsersuserIdmeetingsSettings - a model defined in Swagger"""  # noqa: E501
        self._host_video = None
        self._participant_video = None
        self._cn_meeting = None
        self._in_meeting = None
        self._join_before_host = None
        self._mute_upon_entry = None
        self._watermark = None
        self._use_pmi = None
        self._approval_type = None
        self._registration_type = None
        self._audio = None
        self._auto_recording = None
        self._alternative_hosts = None
        self._close_registration = None
        self._waiting_room = None
        self._global_dial_in_countries = None
        self._contact_name = None
        self._contact_email = None
        self._registrants_email_notification = None
        self._meeting_authentication = None
        self._authentication_option = None
        self._authentication_domains = None
        self._additional_data_center_regions = None
        self.discriminator = None
        if host_video is not None:
            self.host_video = host_video
        if participant_video is not None:
            self.participant_video = participant_video
        if cn_meeting is not None:
            self.cn_meeting = cn_meeting
        if in_meeting is not None:
            self.in_meeting = in_meeting
        if join_before_host is not None:
            self.join_before_host = join_before_host
        if mute_upon_entry is not None:
            self.mute_upon_entry = mute_upon_entry
        if watermark is not None:
            self.watermark = watermark
        if use_pmi is not None:
            self.use_pmi = use_pmi
        if approval_type is not None:
            self.approval_type = approval_type
        if registration_type is not None:
            self.registration_type = registration_type
        if audio is not None:
            self.audio = audio
        if auto_recording is not None:
            self.auto_recording = auto_recording
        if alternative_hosts is not None:
            self.alternative_hosts = alternative_hosts
        if close_registration is not None:
            self.close_registration = close_registration
        if waiting_room is not None:
            self.waiting_room = waiting_room
        if global_dial_in_countries is not None:
            self.global_dial_in_countries = global_dial_in_countries
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_email is not None:
            self.contact_email = contact_email
        if registrants_email_notification is not None:
            self.registrants_email_notification = registrants_email_notification
        if meeting_authentication is not None:
            self.meeting_authentication = meeting_authentication
        if authentication_option is not None:
            self.authentication_option = authentication_option
        if authentication_domains is not None:
            self.authentication_domains = authentication_domains
        if additional_data_center_regions is not None:
            self.additional_data_center_regions = additional_data_center_regions

    @property
    def host_video(self):
        """Gets the host_video of this UsersuserIdmeetingsSettings.  # noqa: E501

        Start video when the host joins the meeting.  # noqa: E501

        :return: The host_video of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._host_video

    @host_video.setter
    def host_video(self, host_video):
        """Sets the host_video of this UsersuserIdmeetingsSettings.

        Start video when the host joins the meeting.  # noqa: E501

        :param host_video: The host_video of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._host_video = host_video

    @property
    def participant_video(self):
        """Gets the participant_video of this UsersuserIdmeetingsSettings.  # noqa: E501

        Start video when participants join the meeting.  # noqa: E501

        :return: The participant_video of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._participant_video

    @participant_video.setter
    def participant_video(self, participant_video):
        """Sets the participant_video of this UsersuserIdmeetingsSettings.

        Start video when participants join the meeting.  # noqa: E501

        :param participant_video: The participant_video of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._participant_video = participant_video

    @property
    def cn_meeting(self):
        """Gets the cn_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501

        Host meeting in China.  # noqa: E501

        :return: The cn_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._cn_meeting

    @cn_meeting.setter
    def cn_meeting(self, cn_meeting):
        """Sets the cn_meeting of this UsersuserIdmeetingsSettings.

        Host meeting in China.  # noqa: E501

        :param cn_meeting: The cn_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._cn_meeting = cn_meeting

    @property
    def in_meeting(self):
        """Gets the in_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501

        Host meeting in India.  # noqa: E501

        :return: The in_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._in_meeting

    @in_meeting.setter
    def in_meeting(self, in_meeting):
        """Sets the in_meeting of this UsersuserIdmeetingsSettings.

        Host meeting in India.  # noqa: E501

        :param in_meeting: The in_meeting of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._in_meeting = in_meeting

    @property
    def join_before_host(self):
        """Gets the join_before_host of this UsersuserIdmeetingsSettings.  # noqa: E501

        Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings.  # noqa: E501

        :return: The join_before_host of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._join_before_host

    @join_before_host.setter
    def join_before_host(self, join_before_host):
        """Sets the join_before_host of this UsersuserIdmeetingsSettings.

        Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings.  # noqa: E501

        :param join_before_host: The join_before_host of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._join_before_host = join_before_host

    @property
    def mute_upon_entry(self):
        """Gets the mute_upon_entry of this UsersuserIdmeetingsSettings.  # noqa: E501

        Mute participants upon entry.  # noqa: E501

        :return: The mute_upon_entry of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._mute_upon_entry

    @mute_upon_entry.setter
    def mute_upon_entry(self, mute_upon_entry):
        """Sets the mute_upon_entry of this UsersuserIdmeetingsSettings.

        Mute participants upon entry.  # noqa: E501

        :param mute_upon_entry: The mute_upon_entry of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._mute_upon_entry = mute_upon_entry

    @property
    def watermark(self):
        """Gets the watermark of this UsersuserIdmeetingsSettings.  # noqa: E501

        Add watermark when viewing a shared screen.  # noqa: E501

        :return: The watermark of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """Sets the watermark of this UsersuserIdmeetingsSettings.

        Add watermark when viewing a shared screen.  # noqa: E501

        :param watermark: The watermark of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._watermark = watermark

    @property
    def use_pmi(self):
        """Gets the use_pmi of this UsersuserIdmeetingsSettings.  # noqa: E501

        Use Personal Meeting ID instead of an automatically generated meeting ID. It can only be used for scheduled meetings, instant meetings and recurring meetings with no fixed time.  # noqa: E501

        :return: The use_pmi of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_pmi

    @use_pmi.setter
    def use_pmi(self, use_pmi):
        """Sets the use_pmi of this UsersuserIdmeetingsSettings.

        Use Personal Meeting ID instead of an automatically generated meeting ID. It can only be used for scheduled meetings, instant meetings and recurring meetings with no fixed time.  # noqa: E501

        :param use_pmi: The use_pmi of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._use_pmi = use_pmi

    @property
    def approval_type(self):
        """Gets the approval_type of this UsersuserIdmeetingsSettings.  # noqa: E501

        `0` - Automatically approve.<br>`1` - Manually approve.<br>`2` - No registration required.  # noqa: E501

        :return: The approval_type of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this UsersuserIdmeetingsSettings.

        `0` - Automatically approve.<br>`1` - Manually approve.<br>`2` - No registration required.  # noqa: E501

        :param approval_type: The approval_type of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: int
        """

        self._approval_type = approval_type

    @property
    def registration_type(self):
        """Gets the registration_type of this UsersuserIdmeetingsSettings.  # noqa: E501

        Registration type. Used for recurring meeting with fixed time only. <br>`1` Attendees register once and can attend any of the occurrences.<br>`2` Attendees need to register for each occurrence to attend.<br>`3` Attendees register once and can choose one or more occurrences to attend.  # noqa: E501

        :return: The registration_type of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._registration_type

    @registration_type.setter
    def registration_type(self, registration_type):
        """Sets the registration_type of this UsersuserIdmeetingsSettings.

        Registration type. Used for recurring meeting with fixed time only. <br>`1` Attendees register once and can attend any of the occurrences.<br>`2` Attendees need to register for each occurrence to attend.<br>`3` Attendees register once and can choose one or more occurrences to attend.  # noqa: E501

        :param registration_type: The registration_type of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: int
        """

        self._registration_type = registration_type

    @property
    def audio(self):
        """Gets the audio of this UsersuserIdmeetingsSettings.  # noqa: E501

        Determine how participants can join the audio portion of the meeting.<br>`both` - Both Telephony and VoIP.<br>`telephony` - Telephony only.<br>`voip` - VoIP only.  # noqa: E501

        :return: The audio of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this UsersuserIdmeetingsSettings.

        Determine how participants can join the audio portion of the meeting.<br>`both` - Both Telephony and VoIP.<br>`telephony` - Telephony only.<br>`voip` - VoIP only.  # noqa: E501

        :param audio: The audio of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["both", "telephony", "voip"]  # noqa: E501
        if audio not in allowed_values:
            raise ValueError(
                "Invalid value for `audio` ({0}), must be one of {1}"  # noqa: E501
                .format(audio, allowed_values)
            )

        self._audio = audio

    @property
    def auto_recording(self):
        """Gets the auto_recording of this UsersuserIdmeetingsSettings.  # noqa: E501

        Automatic recording:<br>`local` - Record on local.<br>`cloud` -  Record on cloud.<br>`none` - Disabled.  # noqa: E501

        :return: The auto_recording of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._auto_recording

    @auto_recording.setter
    def auto_recording(self, auto_recording):
        """Sets the auto_recording of this UsersuserIdmeetingsSettings.

        Automatic recording:<br>`local` - Record on local.<br>`cloud` -  Record on cloud.<br>`none` - Disabled.  # noqa: E501

        :param auto_recording: The auto_recording of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["local", "cloud", "none"]  # noqa: E501
        if auto_recording not in allowed_values:
            raise ValueError(
                "Invalid value for `auto_recording` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_recording, allowed_values)
            )

        self._auto_recording = auto_recording

    @property
    def alternative_hosts(self):
        """Gets the alternative_hosts of this UsersuserIdmeetingsSettings.  # noqa: E501

        Alternative host's emails or IDs: multiple values separated by a comma.  # noqa: E501

        :return: The alternative_hosts of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._alternative_hosts

    @alternative_hosts.setter
    def alternative_hosts(self, alternative_hosts):
        """Sets the alternative_hosts of this UsersuserIdmeetingsSettings.

        Alternative host's emails or IDs: multiple values separated by a comma.  # noqa: E501

        :param alternative_hosts: The alternative_hosts of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """

        self._alternative_hosts = alternative_hosts

    @property
    def close_registration(self):
        """Gets the close_registration of this UsersuserIdmeetingsSettings.  # noqa: E501

        Close registration after event date  # noqa: E501

        :return: The close_registration of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._close_registration

    @close_registration.setter
    def close_registration(self, close_registration):
        """Sets the close_registration of this UsersuserIdmeetingsSettings.

        Close registration after event date  # noqa: E501

        :param close_registration: The close_registration of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._close_registration = close_registration

    @property
    def waiting_room(self):
        """Gets the waiting_room of this UsersuserIdmeetingsSettings.  # noqa: E501

        Enable waiting room  # noqa: E501

        :return: The waiting_room of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._waiting_room

    @waiting_room.setter
    def waiting_room(self, waiting_room):
        """Sets the waiting_room of this UsersuserIdmeetingsSettings.

        Enable waiting room  # noqa: E501

        :param waiting_room: The waiting_room of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._waiting_room = waiting_room

    @property
    def global_dial_in_countries(self):
        """Gets the global_dial_in_countries of this UsersuserIdmeetingsSettings.  # noqa: E501

        List of global dial-in countries  # noqa: E501

        :return: The global_dial_in_countries of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._global_dial_in_countries

    @global_dial_in_countries.setter
    def global_dial_in_countries(self, global_dial_in_countries):
        """Sets the global_dial_in_countries of this UsersuserIdmeetingsSettings.

        List of global dial-in countries  # noqa: E501

        :param global_dial_in_countries: The global_dial_in_countries of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._global_dial_in_countries = global_dial_in_countries

    @property
    def contact_name(self):
        """Gets the contact_name of this UsersuserIdmeetingsSettings.  # noqa: E501

        Contact name for registration  # noqa: E501

        :return: The contact_name of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this UsersuserIdmeetingsSettings.

        Contact name for registration  # noqa: E501

        :param contact_name: The contact_name of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_email(self):
        """Gets the contact_email of this UsersuserIdmeetingsSettings.  # noqa: E501

        Contact email for registration  # noqa: E501

        :return: The contact_email of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this UsersuserIdmeetingsSettings.

        Contact email for registration  # noqa: E501

        :param contact_email: The contact_email of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def registrants_email_notification(self):
        """Gets the registrants_email_notification of this UsersuserIdmeetingsSettings.  # noqa: E501

        Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.  # noqa: E501

        :return: The registrants_email_notification of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._registrants_email_notification

    @registrants_email_notification.setter
    def registrants_email_notification(self, registrants_email_notification):
        """Sets the registrants_email_notification of this UsersuserIdmeetingsSettings.

        Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.  # noqa: E501

        :param registrants_email_notification: The registrants_email_notification of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._registrants_email_notification = registrants_email_notification

    @property
    def meeting_authentication(self):
        """Gets the meeting_authentication of this UsersuserIdmeetingsSettings.  # noqa: E501

        Only [authenticated](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) users can join meeting if the value of this field is set to `true`.  # noqa: E501

        :return: The meeting_authentication of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._meeting_authentication

    @meeting_authentication.setter
    def meeting_authentication(self, meeting_authentication):
        """Sets the meeting_authentication of this UsersuserIdmeetingsSettings.

        Only [authenticated](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) users can join meeting if the value of this field is set to `true`.  # noqa: E501

        :param meeting_authentication: The meeting_authentication of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: bool
        """

        self._meeting_authentication = meeting_authentication

    @property
    def authentication_option(self):
        """Gets the authentication_option of this UsersuserIdmeetingsSettings.  # noqa: E501

        Specify the authentication type for users to join a meeting with`meeting_authentication` setting set to `true`. The value of this field can be retrieved from the `id` field within `authentication_options` array in the response of [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings).  # noqa: E501

        :return: The authentication_option of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_option

    @authentication_option.setter
    def authentication_option(self, authentication_option):
        """Sets the authentication_option of this UsersuserIdmeetingsSettings.

        Specify the authentication type for users to join a meeting with`meeting_authentication` setting set to `true`. The value of this field can be retrieved from the `id` field within `authentication_options` array in the response of [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings).  # noqa: E501

        :param authentication_option: The authentication_option of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """

        self._authentication_option = authentication_option

    @property
    def authentication_domains(self):
        """Gets the authentication_domains of this UsersuserIdmeetingsSettings.  # noqa: E501

        Meeting authentication domains. This option, allows you to specify the rule so that Zoom users, whose email address contains a certain domain, can join the meeting. You can either provide multiple domains, using a comma in between and/or use a wildcard for listing domains.  # noqa: E501

        :return: The authentication_domains of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_domains

    @authentication_domains.setter
    def authentication_domains(self, authentication_domains):
        """Sets the authentication_domains of this UsersuserIdmeetingsSettings.

        Meeting authentication domains. This option, allows you to specify the rule so that Zoom users, whose email address contains a certain domain, can join the meeting. You can either provide multiple domains, using a comma in between and/or use a wildcard for listing domains.  # noqa: E501

        :param authentication_domains: The authentication_domains of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: str
        """

        self._authentication_domains = authentication_domains

    @property
    def additional_data_center_regions(self):
        """Gets the additional_data_center_regions of this UsersuserIdmeetingsSettings.  # noqa: E501

        Enable additional [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) for this meeting. Provide the value in the form of array of country code(s) for the countries which are available as data center regions in the [account settings](https://zoom.us/account/setting) but have been opt out of in the user settings. For instance, let's say that in your account settings, the data center regions that have been selected are Europe, Honkong, Australia, India, Latin America, Japan, China, United States,and Canada. The complete list of available data center regions for your account is: [\"EU\", \"HK\", \"AU\", \"IN\", \"LA\", \"TY\", \"CN\", \"US\", \"CA\"]. In [user settings](https://zoom.us/profile/setting), you have opted out of India(IN) and Japan(TY) for meeting and webinar traffic routing. If you would like, you can still include India and Japan as additional data centers for this meeting using this field. To include India and Japan as additional data center regions, you would provide [\"IN\", \"TY\"] as the value.  # noqa: E501

        :return: The additional_data_center_regions of this UsersuserIdmeetingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_data_center_regions

    @additional_data_center_regions.setter
    def additional_data_center_regions(self, additional_data_center_regions):
        """Sets the additional_data_center_regions of this UsersuserIdmeetingsSettings.

        Enable additional [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) for this meeting. Provide the value in the form of array of country code(s) for the countries which are available as data center regions in the [account settings](https://zoom.us/account/setting) but have been opt out of in the user settings. For instance, let's say that in your account settings, the data center regions that have been selected are Europe, Honkong, Australia, India, Latin America, Japan, China, United States,and Canada. The complete list of available data center regions for your account is: [\"EU\", \"HK\", \"AU\", \"IN\", \"LA\", \"TY\", \"CN\", \"US\", \"CA\"]. In [user settings](https://zoom.us/profile/setting), you have opted out of India(IN) and Japan(TY) for meeting and webinar traffic routing. If you would like, you can still include India and Japan as additional data centers for this meeting using this field. To include India and Japan as additional data center regions, you would provide [\"IN\", \"TY\"] as the value.  # noqa: E501

        :param additional_data_center_regions: The additional_data_center_regions of this UsersuserIdmeetingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._additional_data_center_regions = additional_data_center_regions

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
        if issubclass(UsersuserIdmeetingsSettings, dict):
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
        if not isinstance(other, UsersuserIdmeetingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
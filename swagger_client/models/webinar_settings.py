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


class WebinarSettings(object):
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
        'panelists_video': 'bool',
        'practice_session': 'bool',
        'hd_video': 'bool',
        'approval_type': 'int',
        'registration_type': 'int',
        'audio': 'str',
        'auto_recording': 'str',
        'enforce_login': 'bool',
        'enforce_login_domains': 'str',
        'alternative_hosts': 'str',
        'close_registration': 'bool',
        'show_share_button': 'bool',
        'allow_multiple_devices': 'bool',
        'on_demand': 'bool',
        'global_dial_in_countries': 'list[str]',
        'contact_name': 'str',
        'contact_email': 'str',
        'registrants_confirmation_email': 'bool',
        'registrants_restrict_number': 'int',
        'notify_registrants': 'bool',
        'post_webinar_survey': 'bool',
        'survey_url': 'str',
        'registrants_email_notification': 'bool',
        'meeting_authentication': 'bool',
        'authentication_option': 'str',
        'authentication_domains': 'str',
        'authentication_name': 'str'
    }

    attribute_map = {
        'host_video': 'host_video',
        'panelists_video': 'panelists_video',
        'practice_session': 'practice_session',
        'hd_video': 'hd_video',
        'approval_type': 'approval_type',
        'registration_type': 'registration_type',
        'audio': 'audio',
        'auto_recording': 'auto_recording',
        'enforce_login': 'enforce_login',
        'enforce_login_domains': 'enforce_login_domains',
        'alternative_hosts': 'alternative_hosts',
        'close_registration': 'close_registration',
        'show_share_button': 'show_share_button',
        'allow_multiple_devices': 'allow_multiple_devices',
        'on_demand': 'on_demand',
        'global_dial_in_countries': 'global_dial_in_countries',
        'contact_name': 'contact_name',
        'contact_email': 'contact_email',
        'registrants_confirmation_email': 'registrants_confirmation_email',
        'registrants_restrict_number': 'registrants_restrict_number',
        'notify_registrants': 'notify_registrants',
        'post_webinar_survey': 'post_webinar_survey',
        'survey_url': 'survey_url',
        'registrants_email_notification': 'registrants_email_notification',
        'meeting_authentication': 'meeting_authentication',
        'authentication_option': 'authentication_option',
        'authentication_domains': 'authentication_domains',
        'authentication_name': 'authentication_name'
    }

    def __init__(self, host_video=None, panelists_video=None, practice_session=False, hd_video=False, approval_type=None, registration_type=None, audio='both', auto_recording='none', enforce_login=None, enforce_login_domains=None, alternative_hosts=None, close_registration=None, show_share_button=None, allow_multiple_devices=None, on_demand=False, global_dial_in_countries=None, contact_name=None, contact_email=None, registrants_confirmation_email=None, registrants_restrict_number=None, notify_registrants=None, post_webinar_survey=None, survey_url=None, registrants_email_notification=None, meeting_authentication=None, authentication_option=None, authentication_domains=None, authentication_name=None):  # noqa: E501
        """WebinarSettings - a model defined in Swagger"""  # noqa: E501
        self._host_video = None
        self._panelists_video = None
        self._practice_session = None
        self._hd_video = None
        self._approval_type = None
        self._registration_type = None
        self._audio = None
        self._auto_recording = None
        self._enforce_login = None
        self._enforce_login_domains = None
        self._alternative_hosts = None
        self._close_registration = None
        self._show_share_button = None
        self._allow_multiple_devices = None
        self._on_demand = None
        self._global_dial_in_countries = None
        self._contact_name = None
        self._contact_email = None
        self._registrants_confirmation_email = None
        self._registrants_restrict_number = None
        self._notify_registrants = None
        self._post_webinar_survey = None
        self._survey_url = None
        self._registrants_email_notification = None
        self._meeting_authentication = None
        self._authentication_option = None
        self._authentication_domains = None
        self._authentication_name = None
        self.discriminator = None
        if host_video is not None:
            self.host_video = host_video
        if panelists_video is not None:
            self.panelists_video = panelists_video
        if practice_session is not None:
            self.practice_session = practice_session
        if hd_video is not None:
            self.hd_video = hd_video
        if approval_type is not None:
            self.approval_type = approval_type
        if registration_type is not None:
            self.registration_type = registration_type
        if audio is not None:
            self.audio = audio
        if auto_recording is not None:
            self.auto_recording = auto_recording
        if enforce_login is not None:
            self.enforce_login = enforce_login
        if enforce_login_domains is not None:
            self.enforce_login_domains = enforce_login_domains
        if alternative_hosts is not None:
            self.alternative_hosts = alternative_hosts
        if close_registration is not None:
            self.close_registration = close_registration
        if show_share_button is not None:
            self.show_share_button = show_share_button
        if allow_multiple_devices is not None:
            self.allow_multiple_devices = allow_multiple_devices
        if on_demand is not None:
            self.on_demand = on_demand
        if global_dial_in_countries is not None:
            self.global_dial_in_countries = global_dial_in_countries
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_email is not None:
            self.contact_email = contact_email
        if registrants_confirmation_email is not None:
            self.registrants_confirmation_email = registrants_confirmation_email
        if registrants_restrict_number is not None:
            self.registrants_restrict_number = registrants_restrict_number
        if notify_registrants is not None:
            self.notify_registrants = notify_registrants
        if post_webinar_survey is not None:
            self.post_webinar_survey = post_webinar_survey
        if survey_url is not None:
            self.survey_url = survey_url
        if registrants_email_notification is not None:
            self.registrants_email_notification = registrants_email_notification
        if meeting_authentication is not None:
            self.meeting_authentication = meeting_authentication
        if authentication_option is not None:
            self.authentication_option = authentication_option
        if authentication_domains is not None:
            self.authentication_domains = authentication_domains
        if authentication_name is not None:
            self.authentication_name = authentication_name

    @property
    def host_video(self):
        """Gets the host_video of this WebinarSettings.  # noqa: E501

        Start video when host joins webinar.  # noqa: E501

        :return: The host_video of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._host_video

    @host_video.setter
    def host_video(self, host_video):
        """Sets the host_video of this WebinarSettings.

        Start video when host joins webinar.  # noqa: E501

        :param host_video: The host_video of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._host_video = host_video

    @property
    def panelists_video(self):
        """Gets the panelists_video of this WebinarSettings.  # noqa: E501

        Start video when panelists join webinar.  # noqa: E501

        :return: The panelists_video of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._panelists_video

    @panelists_video.setter
    def panelists_video(self, panelists_video):
        """Sets the panelists_video of this WebinarSettings.

        Start video when panelists join webinar.  # noqa: E501

        :param panelists_video: The panelists_video of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._panelists_video = panelists_video

    @property
    def practice_session(self):
        """Gets the practice_session of this WebinarSettings.  # noqa: E501

        Enable practice session.  # noqa: E501

        :return: The practice_session of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._practice_session

    @practice_session.setter
    def practice_session(self, practice_session):
        """Sets the practice_session of this WebinarSettings.

        Enable practice session.  # noqa: E501

        :param practice_session: The practice_session of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._practice_session = practice_session

    @property
    def hd_video(self):
        """Gets the hd_video of this WebinarSettings.  # noqa: E501

        Default to HD video.  # noqa: E501

        :return: The hd_video of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hd_video

    @hd_video.setter
    def hd_video(self, hd_video):
        """Sets the hd_video of this WebinarSettings.

        Default to HD video.  # noqa: E501

        :param hd_video: The hd_video of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._hd_video = hd_video

    @property
    def approval_type(self):
        """Gets the approval_type of this WebinarSettings.  # noqa: E501

        `0` - Automatically approve.<br>`1` - Manually approve.<br>`2` - No registration required.  # noqa: E501

        :return: The approval_type of this WebinarSettings.  # noqa: E501
        :rtype: int
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this WebinarSettings.

        `0` - Automatically approve.<br>`1` - Manually approve.<br>`2` - No registration required.  # noqa: E501

        :param approval_type: The approval_type of this WebinarSettings.  # noqa: E501
        :type: int
        """

        self._approval_type = approval_type

    @property
    def registration_type(self):
        """Gets the registration_type of this WebinarSettings.  # noqa: E501

        Registration types. Only used for recurring webinars with a fixed time.<br>`1` - Attendees register once and can attend any of the webinar sessions.<br>`2` - Attendees need to register for each session in order to attend.<br>`3` - Attendees register once and can choose one or more sessions to attend.  # noqa: E501

        :return: The registration_type of this WebinarSettings.  # noqa: E501
        :rtype: int
        """
        return self._registration_type

    @registration_type.setter
    def registration_type(self, registration_type):
        """Sets the registration_type of this WebinarSettings.

        Registration types. Only used for recurring webinars with a fixed time.<br>`1` - Attendees register once and can attend any of the webinar sessions.<br>`2` - Attendees need to register for each session in order to attend.<br>`3` - Attendees register once and can choose one or more sessions to attend.  # noqa: E501

        :param registration_type: The registration_type of this WebinarSettings.  # noqa: E501
        :type: int
        """

        self._registration_type = registration_type

    @property
    def audio(self):
        """Gets the audio of this WebinarSettings.  # noqa: E501

        Determine how participants can join the audio portion of the webinar.  # noqa: E501

        :return: The audio of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this WebinarSettings.

        Determine how participants can join the audio portion of the webinar.  # noqa: E501

        :param audio: The audio of this WebinarSettings.  # noqa: E501
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
        """Gets the auto_recording of this WebinarSettings.  # noqa: E501

        Automatic recording:<br>`local` - Record on local.<br>`cloud` -  Record on cloud.<br>`none` - Disabled.  # noqa: E501

        :return: The auto_recording of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._auto_recording

    @auto_recording.setter
    def auto_recording(self, auto_recording):
        """Sets the auto_recording of this WebinarSettings.

        Automatic recording:<br>`local` - Record on local.<br>`cloud` -  Record on cloud.<br>`none` - Disabled.  # noqa: E501

        :param auto_recording: The auto_recording of this WebinarSettings.  # noqa: E501
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
    def enforce_login(self):
        """Gets the enforce_login of this WebinarSettings.  # noqa: E501

        Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**  <br><br>As an alternative, use the \"meeting_authentication\", \"authentication_option\" and \"authentication_domains\" fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the Webinar.  # noqa: E501

        :return: The enforce_login of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_login

    @enforce_login.setter
    def enforce_login(self, enforce_login):
        """Sets the enforce_login of this WebinarSettings.

        Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**  <br><br>As an alternative, use the \"meeting_authentication\", \"authentication_option\" and \"authentication_domains\" fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the Webinar.  # noqa: E501

        :param enforce_login: The enforce_login of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._enforce_login = enforce_login

    @property
    def enforce_login_domains(self):
        """Gets the enforce_login_domains of this WebinarSettings.  # noqa: E501

        Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**  <br><br>As an alternative, use the \"meeting_authentication\", \"authentication_option\" and \"authentication_domains\" fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the Webinar.  # noqa: E501

        :return: The enforce_login_domains of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._enforce_login_domains

    @enforce_login_domains.setter
    def enforce_login_domains(self, enforce_login_domains):
        """Sets the enforce_login_domains of this WebinarSettings.

        Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**  <br><br>As an alternative, use the \"meeting_authentication\", \"authentication_option\" and \"authentication_domains\" fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the Webinar.  # noqa: E501

        :param enforce_login_domains: The enforce_login_domains of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._enforce_login_domains = enforce_login_domains

    @property
    def alternative_hosts(self):
        """Gets the alternative_hosts of this WebinarSettings.  # noqa: E501

        Alternative host emails or IDs. Multiple values separated by comma.  # noqa: E501

        :return: The alternative_hosts of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._alternative_hosts

    @alternative_hosts.setter
    def alternative_hosts(self, alternative_hosts):
        """Sets the alternative_hosts of this WebinarSettings.

        Alternative host emails or IDs. Multiple values separated by comma.  # noqa: E501

        :param alternative_hosts: The alternative_hosts of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._alternative_hosts = alternative_hosts

    @property
    def close_registration(self):
        """Gets the close_registration of this WebinarSettings.  # noqa: E501

        Close registration after event date.  # noqa: E501

        :return: The close_registration of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._close_registration

    @close_registration.setter
    def close_registration(self, close_registration):
        """Sets the close_registration of this WebinarSettings.

        Close registration after event date.  # noqa: E501

        :param close_registration: The close_registration of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._close_registration = close_registration

    @property
    def show_share_button(self):
        """Gets the show_share_button of this WebinarSettings.  # noqa: E501

        Show social share buttons on the registration page.  # noqa: E501

        :return: The show_share_button of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_share_button

    @show_share_button.setter
    def show_share_button(self, show_share_button):
        """Sets the show_share_button of this WebinarSettings.

        Show social share buttons on the registration page.  # noqa: E501

        :param show_share_button: The show_share_button of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._show_share_button = show_share_button

    @property
    def allow_multiple_devices(self):
        """Gets the allow_multiple_devices of this WebinarSettings.  # noqa: E501

        Allow attendees to join from multiple devices.  # noqa: E501

        :return: The allow_multiple_devices of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_devices

    @allow_multiple_devices.setter
    def allow_multiple_devices(self, allow_multiple_devices):
        """Sets the allow_multiple_devices of this WebinarSettings.

        Allow attendees to join from multiple devices.  # noqa: E501

        :param allow_multiple_devices: The allow_multiple_devices of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._allow_multiple_devices = allow_multiple_devices

    @property
    def on_demand(self):
        """Gets the on_demand of this WebinarSettings.  # noqa: E501

        Make the webinar on-demand  # noqa: E501

        :return: The on_demand of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._on_demand

    @on_demand.setter
    def on_demand(self, on_demand):
        """Sets the on_demand of this WebinarSettings.

        Make the webinar on-demand  # noqa: E501

        :param on_demand: The on_demand of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._on_demand = on_demand

    @property
    def global_dial_in_countries(self):
        """Gets the global_dial_in_countries of this WebinarSettings.  # noqa: E501

        List of global dial-in countries  # noqa: E501

        :return: The global_dial_in_countries of this WebinarSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._global_dial_in_countries

    @global_dial_in_countries.setter
    def global_dial_in_countries(self, global_dial_in_countries):
        """Sets the global_dial_in_countries of this WebinarSettings.

        List of global dial-in countries  # noqa: E501

        :param global_dial_in_countries: The global_dial_in_countries of this WebinarSettings.  # noqa: E501
        :type: list[str]
        """

        self._global_dial_in_countries = global_dial_in_countries

    @property
    def contact_name(self):
        """Gets the contact_name of this WebinarSettings.  # noqa: E501

        Contact name for registration  # noqa: E501

        :return: The contact_name of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this WebinarSettings.

        Contact name for registration  # noqa: E501

        :param contact_name: The contact_name of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_email(self):
        """Gets the contact_email of this WebinarSettings.  # noqa: E501

        Contact email for registration  # noqa: E501

        :return: The contact_email of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this WebinarSettings.

        Contact email for registration  # noqa: E501

        :param contact_email: The contact_email of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def registrants_confirmation_email(self):
        """Gets the registrants_confirmation_email of this WebinarSettings.  # noqa: E501

        Send confirmation email to registrants  # noqa: E501

        :return: The registrants_confirmation_email of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._registrants_confirmation_email

    @registrants_confirmation_email.setter
    def registrants_confirmation_email(self, registrants_confirmation_email):
        """Sets the registrants_confirmation_email of this WebinarSettings.

        Send confirmation email to registrants  # noqa: E501

        :param registrants_confirmation_email: The registrants_confirmation_email of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._registrants_confirmation_email = registrants_confirmation_email

    @property
    def registrants_restrict_number(self):
        """Gets the registrants_restrict_number of this WebinarSettings.  # noqa: E501

        Restrict number of registrants for a webinar. By default, it is set to `0`. A `0` value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number.  # noqa: E501

        :return: The registrants_restrict_number of this WebinarSettings.  # noqa: E501
        :rtype: int
        """
        return self._registrants_restrict_number

    @registrants_restrict_number.setter
    def registrants_restrict_number(self, registrants_restrict_number):
        """Sets the registrants_restrict_number of this WebinarSettings.

        Restrict number of registrants for a webinar. By default, it is set to `0`. A `0` value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number.  # noqa: E501

        :param registrants_restrict_number: The registrants_restrict_number of this WebinarSettings.  # noqa: E501
        :type: int
        """

        self._registrants_restrict_number = registrants_restrict_number

    @property
    def notify_registrants(self):
        """Gets the notify_registrants of this WebinarSettings.  # noqa: E501

        Send notification email to registrants when the host updates a webinar.  # noqa: E501

        :return: The notify_registrants of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._notify_registrants

    @notify_registrants.setter
    def notify_registrants(self, notify_registrants):
        """Sets the notify_registrants of this WebinarSettings.

        Send notification email to registrants when the host updates a webinar.  # noqa: E501

        :param notify_registrants: The notify_registrants of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._notify_registrants = notify_registrants

    @property
    def post_webinar_survey(self):
        """Gets the post_webinar_survey of this WebinarSettings.  # noqa: E501

        Zoom will open a survey page in attendees' browsers after leaving the webinar  # noqa: E501

        :return: The post_webinar_survey of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._post_webinar_survey

    @post_webinar_survey.setter
    def post_webinar_survey(self, post_webinar_survey):
        """Sets the post_webinar_survey of this WebinarSettings.

        Zoom will open a survey page in attendees' browsers after leaving the webinar  # noqa: E501

        :param post_webinar_survey: The post_webinar_survey of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._post_webinar_survey = post_webinar_survey

    @property
    def survey_url(self):
        """Gets the survey_url of this WebinarSettings.  # noqa: E501

        Survey url for post webinar survey  # noqa: E501

        :return: The survey_url of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._survey_url

    @survey_url.setter
    def survey_url(self, survey_url):
        """Sets the survey_url of this WebinarSettings.

        Survey url for post webinar survey  # noqa: E501

        :param survey_url: The survey_url of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._survey_url = survey_url

    @property
    def registrants_email_notification(self):
        """Gets the registrants_email_notification of this WebinarSettings.  # noqa: E501

        Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.  # noqa: E501

        :return: The registrants_email_notification of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._registrants_email_notification

    @registrants_email_notification.setter
    def registrants_email_notification(self, registrants_email_notification):
        """Sets the registrants_email_notification of this WebinarSettings.

        Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.  # noqa: E501

        :param registrants_email_notification: The registrants_email_notification of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._registrants_email_notification = registrants_email_notification

    @property
    def meeting_authentication(self):
        """Gets the meeting_authentication of this WebinarSettings.  # noqa: E501

        `true`- Only authenticated users can join Webinar.  # noqa: E501

        :return: The meeting_authentication of this WebinarSettings.  # noqa: E501
        :rtype: bool
        """
        return self._meeting_authentication

    @meeting_authentication.setter
    def meeting_authentication(self, meeting_authentication):
        """Sets the meeting_authentication of this WebinarSettings.

        `true`- Only authenticated users can join Webinar.  # noqa: E501

        :param meeting_authentication: The meeting_authentication of this WebinarSettings.  # noqa: E501
        :type: bool
        """

        self._meeting_authentication = meeting_authentication

    @property
    def authentication_option(self):
        """Gets the authentication_option of this WebinarSettings.  # noqa: E501

        Webinar authentication option id.  # noqa: E501

        :return: The authentication_option of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_option

    @authentication_option.setter
    def authentication_option(self, authentication_option):
        """Sets the authentication_option of this WebinarSettings.

        Webinar authentication option id.  # noqa: E501

        :param authentication_option: The authentication_option of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._authentication_option = authentication_option

    @property
    def authentication_domains(self):
        """Gets the authentication_domains of this WebinarSettings.  # noqa: E501

        If user has configured [\"Sign Into Zoom with Specified Domains\"](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.  # noqa: E501

        :return: The authentication_domains of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_domains

    @authentication_domains.setter
    def authentication_domains(self, authentication_domains):
        """Sets the authentication_domains of this WebinarSettings.

        If user has configured [\"Sign Into Zoom with Specified Domains\"](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.  # noqa: E501

        :param authentication_domains: The authentication_domains of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._authentication_domains = authentication_domains

    @property
    def authentication_name(self):
        """Gets the authentication_name of this WebinarSettings.  # noqa: E501

        Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).  # noqa: E501

        :return: The authentication_name of this WebinarSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_name

    @authentication_name.setter
    def authentication_name(self, authentication_name):
        """Sets the authentication_name of this WebinarSettings.

        Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).  # noqa: E501

        :param authentication_name: The authentication_name of this WebinarSettings.  # noqa: E501
        :type: str
        """

        self._authentication_name = authentication_name

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
        if issubclass(WebinarSettings, dict):
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
        if not isinstance(other, WebinarSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

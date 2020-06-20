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


class AccountsaccountIdlockSettingsInMeeting(object):
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
        'e2e_encryption': 'bool',
        'chat': 'bool',
        'private_chat': 'bool',
        'auto_saving_chat': 'bool',
        'entry_exit_chime': 'str',
        'feedback': 'bool',
        'post_meeting_feedback': 'bool',
        'co_host': 'bool',
        'polling': 'bool',
        'attendee_on_hold': 'bool',
        'show_meeting_control_toolbar': 'bool',
        'allow_show_zoom_windows': 'bool',
        'annotation': 'bool',
        'whiteboard': 'bool',
        'remote_control': 'bool',
        'webinar_question_answer': 'bool',
        'anonymous_question_answer': 'bool',
        'breakout_room': 'bool',
        'closed_caption': 'bool',
        'far_end_camera_control': 'bool',
        'group_hd': 'bool',
        'virtual_background': 'bool',
        'alert_guest_join': 'bool',
        'auto_answer': 'bool',
        'sending_default_email_invites': 'bool',
        'use_html_format_email': 'bool',
        'dscp_marking': 'bool',
        'stereo_audio': 'bool',
        'original_audio': 'bool',
        'screen_sharing': 'bool',
        'custom_data_center_regions': 'bool'
    }

    attribute_map = {
        'e2e_encryption': 'e2e_encryption',
        'chat': 'chat',
        'private_chat': 'private_chat',
        'auto_saving_chat': 'auto_saving_chat',
        'entry_exit_chime': 'entry_exit_chime',
        'feedback': 'feedback',
        'post_meeting_feedback': 'post_meeting_feedback',
        'co_host': 'co_host',
        'polling': 'polling',
        'attendee_on_hold': 'attendee_on_hold',
        'show_meeting_control_toolbar': 'show_meeting_control_toolbar',
        'allow_show_zoom_windows': 'allow_show_zoom_windows',
        'annotation': 'annotation',
        'whiteboard': 'whiteboard',
        'remote_control': 'remote_control',
        'webinar_question_answer': 'webinar_question_answer',
        'anonymous_question_answer': 'anonymous_question_answer',
        'breakout_room': 'breakout_room',
        'closed_caption': 'closed_caption',
        'far_end_camera_control': 'far_end_camera_control',
        'group_hd': 'group_hd',
        'virtual_background': 'virtual_background',
        'alert_guest_join': 'alert_guest_join',
        'auto_answer': 'auto_answer',
        'sending_default_email_invites': 'sending_default_email_invites',
        'use_html_format_email': 'use_html_format_email',
        'dscp_marking': 'dscp_marking',
        'stereo_audio': 'stereo_audio',
        'original_audio': 'original_audio',
        'screen_sharing': 'screen_sharing',
        'custom_data_center_regions': 'custom_data_center_regions'
    }

    def __init__(self, e2e_encryption=None, chat=None, private_chat=None, auto_saving_chat=None, entry_exit_chime=None, feedback=None, post_meeting_feedback=None, co_host=None, polling=None, attendee_on_hold=None, show_meeting_control_toolbar=None, allow_show_zoom_windows=None, annotation=None, whiteboard=None, remote_control=None, webinar_question_answer=None, anonymous_question_answer=None, breakout_room=None, closed_caption=None, far_end_camera_control=None, group_hd=None, virtual_background=None, alert_guest_join=None, auto_answer=None, sending_default_email_invites=None, use_html_format_email=None, dscp_marking=None, stereo_audio=None, original_audio=None, screen_sharing=None, custom_data_center_regions=None):  # noqa: E501
        """AccountsaccountIdlockSettingsInMeeting - a model defined in Swagger"""  # noqa: E501
        self._e2e_encryption = None
        self._chat = None
        self._private_chat = None
        self._auto_saving_chat = None
        self._entry_exit_chime = None
        self._feedback = None
        self._post_meeting_feedback = None
        self._co_host = None
        self._polling = None
        self._attendee_on_hold = None
        self._show_meeting_control_toolbar = None
        self._allow_show_zoom_windows = None
        self._annotation = None
        self._whiteboard = None
        self._remote_control = None
        self._webinar_question_answer = None
        self._anonymous_question_answer = None
        self._breakout_room = None
        self._closed_caption = None
        self._far_end_camera_control = None
        self._group_hd = None
        self._virtual_background = None
        self._alert_guest_join = None
        self._auto_answer = None
        self._sending_default_email_invites = None
        self._use_html_format_email = None
        self._dscp_marking = None
        self._stereo_audio = None
        self._original_audio = None
        self._screen_sharing = None
        self._custom_data_center_regions = None
        self.discriminator = None
        if e2e_encryption is not None:
            self.e2e_encryption = e2e_encryption
        if chat is not None:
            self.chat = chat
        if private_chat is not None:
            self.private_chat = private_chat
        if auto_saving_chat is not None:
            self.auto_saving_chat = auto_saving_chat
        if entry_exit_chime is not None:
            self.entry_exit_chime = entry_exit_chime
        if feedback is not None:
            self.feedback = feedback
        if post_meeting_feedback is not None:
            self.post_meeting_feedback = post_meeting_feedback
        if co_host is not None:
            self.co_host = co_host
        if polling is not None:
            self.polling = polling
        if attendee_on_hold is not None:
            self.attendee_on_hold = attendee_on_hold
        if show_meeting_control_toolbar is not None:
            self.show_meeting_control_toolbar = show_meeting_control_toolbar
        if allow_show_zoom_windows is not None:
            self.allow_show_zoom_windows = allow_show_zoom_windows
        if annotation is not None:
            self.annotation = annotation
        if whiteboard is not None:
            self.whiteboard = whiteboard
        if remote_control is not None:
            self.remote_control = remote_control
        if webinar_question_answer is not None:
            self.webinar_question_answer = webinar_question_answer
        if anonymous_question_answer is not None:
            self.anonymous_question_answer = anonymous_question_answer
        if breakout_room is not None:
            self.breakout_room = breakout_room
        if closed_caption is not None:
            self.closed_caption = closed_caption
        if far_end_camera_control is not None:
            self.far_end_camera_control = far_end_camera_control
        if group_hd is not None:
            self.group_hd = group_hd
        if virtual_background is not None:
            self.virtual_background = virtual_background
        if alert_guest_join is not None:
            self.alert_guest_join = alert_guest_join
        if auto_answer is not None:
            self.auto_answer = auto_answer
        if sending_default_email_invites is not None:
            self.sending_default_email_invites = sending_default_email_invites
        if use_html_format_email is not None:
            self.use_html_format_email = use_html_format_email
        if dscp_marking is not None:
            self.dscp_marking = dscp_marking
        if stereo_audio is not None:
            self.stereo_audio = stereo_audio
        if original_audio is not None:
            self.original_audio = original_audio
        if screen_sharing is not None:
            self.screen_sharing = screen_sharing
        if custom_data_center_regions is not None:
            self.custom_data_center_regions = custom_data_center_regions

    @property
    def e2e_encryption(self):
        """Gets the e2e_encryption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Require that all meetings are encrypted using AES.  # noqa: E501

        :return: The e2e_encryption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._e2e_encryption

    @e2e_encryption.setter
    def e2e_encryption(self, e2e_encryption):
        """Sets the e2e_encryption of this AccountsaccountIdlockSettingsInMeeting.

        Require that all meetings are encrypted using AES.  # noqa: E501

        :param e2e_encryption: The e2e_encryption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._e2e_encryption = e2e_encryption

    @property
    def chat(self):
        """Gets the chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow meeting participants to send chat message visible to all participants.  # noqa: E501

        :return: The chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._chat

    @chat.setter
    def chat(self, chat):
        """Sets the chat of this AccountsaccountIdlockSettingsInMeeting.

        Allow meeting participants to send chat message visible to all participants.  # noqa: E501

        :param chat: The chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._chat = chat

    @property
    def private_chat(self):
        """Gets the private_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow meeting participants to send a private 1:1 message to another participant.  # noqa: E501

        :return: The private_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._private_chat

    @private_chat.setter
    def private_chat(self, private_chat):
        """Sets the private_chat of this AccountsaccountIdlockSettingsInMeeting.

        Allow meeting participants to send a private 1:1 message to another participant.  # noqa: E501

        :param private_chat: The private_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._private_chat = private_chat

    @property
    def auto_saving_chat(self):
        """Gets the auto_saving_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Automatically save all in-meeting chats.  # noqa: E501

        :return: The auto_saving_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._auto_saving_chat

    @auto_saving_chat.setter
    def auto_saving_chat(self, auto_saving_chat):
        """Sets the auto_saving_chat of this AccountsaccountIdlockSettingsInMeeting.

        Automatically save all in-meeting chats.  # noqa: E501

        :param auto_saving_chat: The auto_saving_chat of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._auto_saving_chat = auto_saving_chat

    @property
    def entry_exit_chime(self):
        """Gets the entry_exit_chime of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Play sound when participants join or leave.  # noqa: E501

        :return: The entry_exit_chime of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: str
        """
        return self._entry_exit_chime

    @entry_exit_chime.setter
    def entry_exit_chime(self, entry_exit_chime):
        """Sets the entry_exit_chime of this AccountsaccountIdlockSettingsInMeeting.

        Play sound when participants join or leave.  # noqa: E501

        :param entry_exit_chime: The entry_exit_chime of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: str
        """

        self._entry_exit_chime = entry_exit_chime

    @property
    def feedback(self):
        """Gets the feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Enable users to provide feedback to Zoom at the end of the meeting.  # noqa: E501

        :return: The feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this AccountsaccountIdlockSettingsInMeeting.

        Enable users to provide feedback to Zoom at the end of the meeting.  # noqa: E501

        :param feedback: The feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._feedback = feedback

    @property
    def post_meeting_feedback(self):
        """Gets the post_meeting_feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Display end-of-meeting experience feedback survey.  # noqa: E501

        :return: The post_meeting_feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._post_meeting_feedback

    @post_meeting_feedback.setter
    def post_meeting_feedback(self, post_meeting_feedback):
        """Sets the post_meeting_feedback of this AccountsaccountIdlockSettingsInMeeting.

        Display end-of-meeting experience feedback survey.  # noqa: E501

        :param post_meeting_feedback: The post_meeting_feedback of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._post_meeting_feedback = post_meeting_feedback

    @property
    def co_host(self):
        """Gets the co_host of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow the host to add co-hosts. Co-hosts have the same in-meeting controls as the host.  # noqa: E501

        :return: The co_host of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._co_host

    @co_host.setter
    def co_host(self, co_host):
        """Sets the co_host of this AccountsaccountIdlockSettingsInMeeting.

        Allow the host to add co-hosts. Co-hosts have the same in-meeting controls as the host.  # noqa: E501

        :param co_host: The co_host of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._co_host = co_host

    @property
    def polling(self):
        """Gets the polling of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Add 'Polls' to the meeting controls. This allows the host to survey the attendees.  # noqa: E501

        :return: The polling of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._polling

    @polling.setter
    def polling(self, polling):
        """Sets the polling of this AccountsaccountIdlockSettingsInMeeting.

        Add 'Polls' to the meeting controls. This allows the host to survey the attendees.  # noqa: E501

        :param polling: The polling of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._polling = polling

    @property
    def attendee_on_hold(self):
        """Gets the attendee_on_hold of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow hosts to temporarily remove an attendee from the meeting.  # noqa: E501

        :return: The attendee_on_hold of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._attendee_on_hold

    @attendee_on_hold.setter
    def attendee_on_hold(self, attendee_on_hold):
        """Sets the attendee_on_hold of this AccountsaccountIdlockSettingsInMeeting.

        Allow hosts to temporarily remove an attendee from the meeting.  # noqa: E501

        :param attendee_on_hold: The attendee_on_hold of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._attendee_on_hold = attendee_on_hold

    @property
    def show_meeting_control_toolbar(self):
        """Gets the show_meeting_control_toolbar of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Always show meeting controls during a meeting.  # noqa: E501

        :return: The show_meeting_control_toolbar of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._show_meeting_control_toolbar

    @show_meeting_control_toolbar.setter
    def show_meeting_control_toolbar(self, show_meeting_control_toolbar):
        """Sets the show_meeting_control_toolbar of this AccountsaccountIdlockSettingsInMeeting.

        Always show meeting controls during a meeting.  # noqa: E501

        :param show_meeting_control_toolbar: The show_meeting_control_toolbar of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._show_meeting_control_toolbar = show_meeting_control_toolbar

    @property
    def allow_show_zoom_windows(self):
        """Gets the allow_show_zoom_windows of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Show Zoom windows during screen share.  # noqa: E501

        :return: The allow_show_zoom_windows of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._allow_show_zoom_windows

    @allow_show_zoom_windows.setter
    def allow_show_zoom_windows(self, allow_show_zoom_windows):
        """Sets the allow_show_zoom_windows of this AccountsaccountIdlockSettingsInMeeting.

        Show Zoom windows during screen share.  # noqa: E501

        :param allow_show_zoom_windows: The allow_show_zoom_windows of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._allow_show_zoom_windows = allow_show_zoom_windows

    @property
    def annotation(self):
        """Gets the annotation of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow participants to use annotation tools to add information to shared screens.  # noqa: E501

        :return: The annotation of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this AccountsaccountIdlockSettingsInMeeting.

        Allow participants to use annotation tools to add information to shared screens.  # noqa: E501

        :param annotation: The annotation of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._annotation = annotation

    @property
    def whiteboard(self):
        """Gets the whiteboard of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow participants to share a whiteboard that includes annotation tools.  # noqa: E501

        :return: The whiteboard of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._whiteboard

    @whiteboard.setter
    def whiteboard(self, whiteboard):
        """Sets the whiteboard of this AccountsaccountIdlockSettingsInMeeting.

        Allow participants to share a whiteboard that includes annotation tools.  # noqa: E501

        :param whiteboard: The whiteboard of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._whiteboard = whiteboard

    @property
    def remote_control(self):
        """Gets the remote_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        During screen sharing, allow the person who is sharing to let others control the shared content.  # noqa: E501

        :return: The remote_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._remote_control

    @remote_control.setter
    def remote_control(self, remote_control):
        """Sets the remote_control of this AccountsaccountIdlockSettingsInMeeting.

        During screen sharing, allow the person who is sharing to let others control the shared content.  # noqa: E501

        :param remote_control: The remote_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._remote_control = remote_control

    @property
    def webinar_question_answer(self):
        """Gets the webinar_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501


        :return: The webinar_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._webinar_question_answer

    @webinar_question_answer.setter
    def webinar_question_answer(self, webinar_question_answer):
        """Sets the webinar_question_answer of this AccountsaccountIdlockSettingsInMeeting.


        :param webinar_question_answer: The webinar_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._webinar_question_answer = webinar_question_answer

    @property
    def anonymous_question_answer(self):
        """Gets the anonymous_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501


        :return: The anonymous_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous_question_answer

    @anonymous_question_answer.setter
    def anonymous_question_answer(self, anonymous_question_answer):
        """Sets the anonymous_question_answer of this AccountsaccountIdlockSettingsInMeeting.


        :param anonymous_question_answer: The anonymous_question_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._anonymous_question_answer = anonymous_question_answer

    @property
    def breakout_room(self):
        """Gets the breakout_room of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow host to split meeting participants into separate, smaller rooms.  # noqa: E501

        :return: The breakout_room of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._breakout_room

    @breakout_room.setter
    def breakout_room(self, breakout_room):
        """Sets the breakout_room of this AccountsaccountIdlockSettingsInMeeting.

        Allow host to split meeting participants into separate, smaller rooms.  # noqa: E501

        :param breakout_room: The breakout_room of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._breakout_room = breakout_room

    @property
    def closed_caption(self):
        """Gets the closed_caption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow host to type closed captions or assign a participant/third party device to add closed captions.  # noqa: E501

        :return: The closed_caption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._closed_caption

    @closed_caption.setter
    def closed_caption(self, closed_caption):
        """Sets the closed_caption of this AccountsaccountIdlockSettingsInMeeting.

        Allow host to type closed captions or assign a participant/third party device to add closed captions.  # noqa: E501

        :param closed_caption: The closed_caption of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._closed_caption = closed_caption

    @property
    def far_end_camera_control(self):
        """Gets the far_end_camera_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow another user to take control of the camera during a meeting.  # noqa: E501

        :return: The far_end_camera_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._far_end_camera_control

    @far_end_camera_control.setter
    def far_end_camera_control(self, far_end_camera_control):
        """Sets the far_end_camera_control of this AccountsaccountIdlockSettingsInMeeting.

        Allow another user to take control of the camera during a meeting.  # noqa: E501

        :param far_end_camera_control: The far_end_camera_control of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._far_end_camera_control = far_end_camera_control

    @property
    def group_hd(self):
        """Gets the group_hd of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Enable higher quality video for host and participants. This will require more bandwidth.  # noqa: E501

        :return: The group_hd of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._group_hd

    @group_hd.setter
    def group_hd(self, group_hd):
        """Sets the group_hd of this AccountsaccountIdlockSettingsInMeeting.

        Enable higher quality video for host and participants. This will require more bandwidth.  # noqa: E501

        :param group_hd: The group_hd of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._group_hd = group_hd

    @property
    def virtual_background(self):
        """Gets the virtual_background of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Enable virtual background.  # noqa: E501

        :return: The virtual_background of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_background

    @virtual_background.setter
    def virtual_background(self, virtual_background):
        """Sets the virtual_background of this AccountsaccountIdlockSettingsInMeeting.

        Enable virtual background.  # noqa: E501

        :param virtual_background: The virtual_background of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._virtual_background = virtual_background

    @property
    def alert_guest_join(self):
        """Gets the alert_guest_join of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow participants who belong to your account to see that a guest (someone who does not belong to your account) is participating in the meeting/webinar.  # noqa: E501

        :return: The alert_guest_join of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._alert_guest_join

    @alert_guest_join.setter
    def alert_guest_join(self, alert_guest_join):
        """Sets the alert_guest_join of this AccountsaccountIdlockSettingsInMeeting.

        Allow participants who belong to your account to see that a guest (someone who does not belong to your account) is participating in the meeting/webinar.  # noqa: E501

        :param alert_guest_join: The alert_guest_join of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._alert_guest_join = alert_guest_join

    @property
    def auto_answer(self):
        """Gets the auto_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Enable users to see and add contacts to 'auto-answer group' in the contact list on chat. Any call from members of this group will be automatically answered.  # noqa: E501

        :return: The auto_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._auto_answer

    @auto_answer.setter
    def auto_answer(self, auto_answer):
        """Sets the auto_answer of this AccountsaccountIdlockSettingsInMeeting.

        Enable users to see and add contacts to 'auto-answer group' in the contact list on chat. Any call from members of this group will be automatically answered.  # noqa: E501

        :param auto_answer: The auto_answer of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._auto_answer = auto_answer

    @property
    def sending_default_email_invites(self):
        """Gets the sending_default_email_invites of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow users to invite participants by email only by default.  # noqa: E501

        :return: The sending_default_email_invites of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._sending_default_email_invites

    @sending_default_email_invites.setter
    def sending_default_email_invites(self, sending_default_email_invites):
        """Sets the sending_default_email_invites of this AccountsaccountIdlockSettingsInMeeting.

        Allow users to invite participants by email only by default.  # noqa: E501

        :param sending_default_email_invites: The sending_default_email_invites of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._sending_default_email_invites = sending_default_email_invites

    @property
    def use_html_format_email(self):
        """Gets the use_html_format_email of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow  HTML formatting instead of plain text for meeting invitations scheduled with the Outlook plugin.  # noqa: E501

        :return: The use_html_format_email of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._use_html_format_email

    @use_html_format_email.setter
    def use_html_format_email(self, use_html_format_email):
        """Sets the use_html_format_email of this AccountsaccountIdlockSettingsInMeeting.

        Allow  HTML formatting instead of plain text for meeting invitations scheduled with the Outlook plugin.  # noqa: E501

        :param use_html_format_email: The use_html_format_email of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._use_html_format_email = use_html_format_email

    @property
    def dscp_marking(self):
        """Gets the dscp_marking of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow users to select stereo audio during a meeting.  # noqa: E501

        :return: The dscp_marking of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._dscp_marking

    @dscp_marking.setter
    def dscp_marking(self, dscp_marking):
        """Sets the dscp_marking of this AccountsaccountIdlockSettingsInMeeting.

        Allow users to select stereo audio during a meeting.  # noqa: E501

        :param dscp_marking: The dscp_marking of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._dscp_marking = dscp_marking

    @property
    def stereo_audio(self):
        """Gets the stereo_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow users to select stereo audio during a meeting.  # noqa: E501

        :return: The stereo_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._stereo_audio

    @stereo_audio.setter
    def stereo_audio(self, stereo_audio):
        """Sets the stereo_audio of this AccountsaccountIdlockSettingsInMeeting.

        Allow users to select stereo audio during a meeting.  # noqa: E501

        :param stereo_audio: The stereo_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._stereo_audio = stereo_audio

    @property
    def original_audio(self):
        """Gets the original_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow users to select original sound during a meeting.  # noqa: E501

        :return: The original_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._original_audio

    @original_audio.setter
    def original_audio(self, original_audio):
        """Sets the original_audio of this AccountsaccountIdlockSettingsInMeeting.

        Allow users to select original sound during a meeting.  # noqa: E501

        :param original_audio: The original_audio of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._original_audio = original_audio

    @property
    def screen_sharing(self):
        """Gets the screen_sharing of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        Allow host and participants to share their screen or content during meetings.  # noqa: E501

        :return: The screen_sharing of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._screen_sharing

    @screen_sharing.setter
    def screen_sharing(self, screen_sharing):
        """Sets the screen_sharing of this AccountsaccountIdlockSettingsInMeeting.

        Allow host and participants to share their screen or content during meetings.  # noqa: E501

        :param screen_sharing: The screen_sharing of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._screen_sharing = screen_sharing

    @property
    def custom_data_center_regions(self):
        """Gets the custom_data_center_regions of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501

        If set to `true`, account owners and admins on paid accounts can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting their real-time meeting and webinar traffic. These regions can be provided in the `data_center_regions` field in the account settings. If set to `false`, the regions cannot be customized and the default regions will be used.  # noqa: E501

        :return: The custom_data_center_regions of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :rtype: bool
        """
        return self._custom_data_center_regions

    @custom_data_center_regions.setter
    def custom_data_center_regions(self, custom_data_center_regions):
        """Sets the custom_data_center_regions of this AccountsaccountIdlockSettingsInMeeting.

        If set to `true`, account owners and admins on paid accounts can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting their real-time meeting and webinar traffic. These regions can be provided in the `data_center_regions` field in the account settings. If set to `false`, the regions cannot be customized and the default regions will be used.  # noqa: E501

        :param custom_data_center_regions: The custom_data_center_regions of this AccountsaccountIdlockSettingsInMeeting.  # noqa: E501
        :type: bool
        """

        self._custom_data_center_regions = custom_data_center_regions

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
        if issubclass(AccountsaccountIdlockSettingsInMeeting, dict):
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
        if not isinstance(other, AccountsaccountIdlockSettingsInMeeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

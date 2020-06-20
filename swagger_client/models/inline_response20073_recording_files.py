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


class InlineResponse20073RecordingFiles(object):
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
        'recording_start': 'str',
        'recording_end': 'str',
        'file_type': 'str',
        'file_size': 'float',
        'play_url': 'str',
        'download_url': 'str',
        'status': 'str',
        'recording_type': 'str',
        'meeting_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'recording_start': 'recording_start',
        'recording_end': 'recording_end',
        'file_type': 'file_type',
        'file_size': 'file_size',
        'play_url': 'play_url',
        'download_url': 'download_url',
        'status': 'status',
        'recording_type': 'recording_type',
        'meeting_id': 'meeting_id'
    }

    def __init__(self, id=None, recording_start=None, recording_end=None, file_type=None, file_size=None, play_url=None, download_url=None, status=None, recording_type=None, meeting_id=None):  # noqa: E501
        """InlineResponse20073RecordingFiles - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._recording_start = None
        self._recording_end = None
        self._file_type = None
        self._file_size = None
        self._play_url = None
        self._download_url = None
        self._status = None
        self._recording_type = None
        self._meeting_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if recording_start is not None:
            self.recording_start = recording_start
        if recording_end is not None:
            self.recording_end = recording_end
        if file_type is not None:
            self.file_type = file_type
        if file_size is not None:
            self.file_size = file_size
        if play_url is not None:
            self.play_url = play_url
        if download_url is not None:
            self.download_url = download_url
        if status is not None:
            self.status = status
        if recording_type is not None:
            self.recording_type = recording_type
        if meeting_id is not None:
            self.meeting_id = meeting_id

    @property
    def id(self):
        """Gets the id of this InlineResponse20073RecordingFiles.  # noqa: E501

        Recording ID. Identifier for the recording.  # noqa: E501

        :return: The id of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20073RecordingFiles.

        Recording ID. Identifier for the recording.  # noqa: E501

        :param id: The id of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def recording_start(self):
        """Gets the recording_start of this InlineResponse20073RecordingFiles.  # noqa: E501

        The date and time at which the recording started.  # noqa: E501

        :return: The recording_start of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._recording_start

    @recording_start.setter
    def recording_start(self, recording_start):
        """Sets the recording_start of this InlineResponse20073RecordingFiles.

        The date and time at which the recording started.  # noqa: E501

        :param recording_start: The recording_start of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._recording_start = recording_start

    @property
    def recording_end(self):
        """Gets the recording_end of this InlineResponse20073RecordingFiles.  # noqa: E501

        The date and time at which the recording ended.  # noqa: E501

        :return: The recording_end of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._recording_end

    @recording_end.setter
    def recording_end(self, recording_end):
        """Sets the recording_end of this InlineResponse20073RecordingFiles.

        The date and time at which the recording ended.  # noqa: E501

        :param recording_end: The recording_end of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._recording_end = recording_end

    @property
    def file_type(self):
        """Gets the file_type of this InlineResponse20073RecordingFiles.  # noqa: E501

        The recording file type. The value of this field could be one of the following:<br> `MP4`: Video file of the recording.<br>`M4A` Audio-only file of the recording.<br>`TIMELINE`: Timestamp file of the recording.<br> `TRANSCRIPT`: Transcription file of the recording.<br> `CHAT`: A TXT file containing in-meeting chat messages that were sent during the meeting.<br>`CC`: File containing closed captions of the recording.<br><br> A recording file object with file type of either `CC` or `TIMELINE` **does not have** the following properties:<br>  `id`, `status`, `file_size`, `recording_type`, and `play_url`.  # noqa: E501

        :return: The file_type of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this InlineResponse20073RecordingFiles.

        The recording file type. The value of this field could be one of the following:<br> `MP4`: Video file of the recording.<br>`M4A` Audio-only file of the recording.<br>`TIMELINE`: Timestamp file of the recording.<br> `TRANSCRIPT`: Transcription file of the recording.<br> `CHAT`: A TXT file containing in-meeting chat messages that were sent during the meeting.<br>`CC`: File containing closed captions of the recording.<br><br> A recording file object with file type of either `CC` or `TIMELINE` **does not have** the following properties:<br>  `id`, `status`, `file_size`, `recording_type`, and `play_url`.  # noqa: E501

        :param file_type: The file_type of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def file_size(self):
        """Gets the file_size of this InlineResponse20073RecordingFiles.  # noqa: E501

        The size of the recording file in bytes.  # noqa: E501

        :return: The file_size of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: float
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this InlineResponse20073RecordingFiles.

        The size of the recording file in bytes.  # noqa: E501

        :param file_size: The file_size of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: float
        """

        self._file_size = file_size

    @property
    def play_url(self):
        """Gets the play_url of this InlineResponse20073RecordingFiles.  # noqa: E501

        The URL using which recording can be played.  # noqa: E501

        :return: The play_url of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._play_url

    @play_url.setter
    def play_url(self, play_url):
        """Sets the play_url of this InlineResponse20073RecordingFiles.

        The URL using which recording can be played.  # noqa: E501

        :param play_url: The play_url of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._play_url = play_url

    @property
    def download_url(self):
        """Gets the download_url of this InlineResponse20073RecordingFiles.  # noqa: E501

        The URL using which the recording can be downloaded  # noqa: E501

        :return: The download_url of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this InlineResponse20073RecordingFiles.

        The URL using which the recording can be downloaded  # noqa: E501

        :param download_url: The download_url of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def status(self):
        """Gets the status of this InlineResponse20073RecordingFiles.  # noqa: E501

        The status of the recording.   # noqa: E501

        :return: The status of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20073RecordingFiles.

        The status of the recording.   # noqa: E501

        :param status: The status of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """
        allowed_values = ["completed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def recording_type(self):
        """Gets the recording_type of this InlineResponse20073RecordingFiles.  # noqa: E501

        The recording type. The value of this field can be one of the following:<br>`shared_screen_with_speaker_view(CC)`<br>`shared_screen_with_speaker_view`<br>`shared_screen_with_gallery_view`<br>`speaker_view`<br>`gallery_view`<br>`shared_screen`<br>`audio_only`<br>`audio_transcript`<br>`chat_file`<br>`TIMELINE`  # noqa: E501

        :return: The recording_type of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._recording_type

    @recording_type.setter
    def recording_type(self, recording_type):
        """Sets the recording_type of this InlineResponse20073RecordingFiles.

        The recording type. The value of this field can be one of the following:<br>`shared_screen_with_speaker_view(CC)`<br>`shared_screen_with_speaker_view`<br>`shared_screen_with_gallery_view`<br>`speaker_view`<br>`gallery_view`<br>`shared_screen`<br>`audio_only`<br>`audio_transcript`<br>`chat_file`<br>`TIMELINE`  # noqa: E501

        :param recording_type: The recording_type of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._recording_type = recording_type

    @property
    def meeting_id(self):
        """Gets the meeting_id of this InlineResponse20073RecordingFiles.  # noqa: E501

        Universally unique identifier of the meeting instance that was being recorded.  # noqa: E501

        :return: The meeting_id of this InlineResponse20073RecordingFiles.  # noqa: E501
        :rtype: str
        """
        return self._meeting_id

    @meeting_id.setter
    def meeting_id(self, meeting_id):
        """Sets the meeting_id of this InlineResponse20073RecordingFiles.

        Universally unique identifier of the meeting instance that was being recorded.  # noqa: E501

        :param meeting_id: The meeting_id of this InlineResponse20073RecordingFiles.  # noqa: E501
        :type: str
        """

        self._meeting_id = meeting_id

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
        if issubclass(InlineResponse20073RecordingFiles, dict):
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
        if not isinstance(other, InlineResponse20073RecordingFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

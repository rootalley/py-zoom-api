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


class GroupsgroupIdlockSettingsRecording(object):
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
        'local_recording': 'bool',
        'cloud_recording': 'bool',
        'auto_recording': 'str',
        'cloud_recording_download': 'bool',
        'account_user_access_recording': 'bool',
        'host_delete_cloud_recording': 'bool',
        'auto_delete_cmr': 'bool',
        'recording_authentication': 'str'
    }

    attribute_map = {
        'local_recording': 'local_recording',
        'cloud_recording': 'cloud_recording',
        'auto_recording': 'auto_recording',
        'cloud_recording_download': 'cloud_recording_download',
        'account_user_access_recording': 'account_user_access_recording',
        'host_delete_cloud_recording': 'host_delete_cloud_recording',
        'auto_delete_cmr': 'auto_delete_cmr',
        'recording_authentication': 'recording_authentication'
    }

    def __init__(self, local_recording=None, cloud_recording=None, auto_recording=None, cloud_recording_download=None, account_user_access_recording=None, host_delete_cloud_recording=None, auto_delete_cmr=None, recording_authentication=None):  # noqa: E501
        """GroupsgroupIdlockSettingsRecording - a model defined in Swagger"""  # noqa: E501
        self._local_recording = None
        self._cloud_recording = None
        self._auto_recording = None
        self._cloud_recording_download = None
        self._account_user_access_recording = None
        self._host_delete_cloud_recording = None
        self._auto_delete_cmr = None
        self._recording_authentication = None
        self.discriminator = None
        if local_recording is not None:
            self.local_recording = local_recording
        if cloud_recording is not None:
            self.cloud_recording = cloud_recording
        if auto_recording is not None:
            self.auto_recording = auto_recording
        if cloud_recording_download is not None:
            self.cloud_recording_download = cloud_recording_download
        if account_user_access_recording is not None:
            self.account_user_access_recording = account_user_access_recording
        if host_delete_cloud_recording is not None:
            self.host_delete_cloud_recording = host_delete_cloud_recording
        if auto_delete_cmr is not None:
            self.auto_delete_cmr = auto_delete_cmr
        if recording_authentication is not None:
            self.recording_authentication = recording_authentication

    @property
    def local_recording(self):
        """Gets the local_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Allow hosts and participants to record the meeting to a local file.  # noqa: E501

        :return: The local_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._local_recording

    @local_recording.setter
    def local_recording(self, local_recording):
        """Sets the local_recording of this GroupsgroupIdlockSettingsRecording.

        Allow hosts and participants to record the meeting to a local file.  # noqa: E501

        :param local_recording: The local_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._local_recording = local_recording

    @property
    def cloud_recording(self):
        """Gets the cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Allow hosts to record and save the meeting / webinar in the cloud.  # noqa: E501

        :return: The cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording

    @cloud_recording.setter
    def cloud_recording(self, cloud_recording):
        """Sets the cloud_recording of this GroupsgroupIdlockSettingsRecording.

        Allow hosts to record and save the meeting / webinar in the cloud.  # noqa: E501

        :param cloud_recording: The cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._cloud_recording = cloud_recording

    @property
    def auto_recording(self):
        """Gets the auto_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Record meetings automatically as they start.  # noqa: E501

        :return: The auto_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: str
        """
        return self._auto_recording

    @auto_recording.setter
    def auto_recording(self, auto_recording):
        """Sets the auto_recording of this GroupsgroupIdlockSettingsRecording.

        Record meetings automatically as they start.  # noqa: E501

        :param auto_recording: The auto_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: str
        """

        self._auto_recording = auto_recording

    @property
    def cloud_recording_download(self):
        """Gets the cloud_recording_download of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Allow anyone with a link to the cloud recording to download.  # noqa: E501

        :return: The cloud_recording_download of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording_download

    @cloud_recording_download.setter
    def cloud_recording_download(self, cloud_recording_download):
        """Sets the cloud_recording_download of this GroupsgroupIdlockSettingsRecording.

        Allow anyone with a link to the cloud recording to download.  # noqa: E501

        :param cloud_recording_download: The cloud_recording_download of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._cloud_recording_download = cloud_recording_download

    @property
    def account_user_access_recording(self):
        """Gets the account_user_access_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Make cloud recordings accessible to account members only.  # noqa: E501

        :return: The account_user_access_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._account_user_access_recording

    @account_user_access_recording.setter
    def account_user_access_recording(self, account_user_access_recording):
        """Sets the account_user_access_recording of this GroupsgroupIdlockSettingsRecording.

        Make cloud recordings accessible to account members only.  # noqa: E501

        :param account_user_access_recording: The account_user_access_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._account_user_access_recording = account_user_access_recording

    @property
    def host_delete_cloud_recording(self):
        """Gets the host_delete_cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Allow the host to delete the recordings. If this option is disabled, the recordings cannot be deleted by the host and only admin can delete them.  # noqa: E501

        :return: The host_delete_cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._host_delete_cloud_recording

    @host_delete_cloud_recording.setter
    def host_delete_cloud_recording(self, host_delete_cloud_recording):
        """Sets the host_delete_cloud_recording of this GroupsgroupIdlockSettingsRecording.

        Allow the host to delete the recordings. If this option is disabled, the recordings cannot be deleted by the host and only admin can delete them.  # noqa: E501

        :param host_delete_cloud_recording: The host_delete_cloud_recording of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._host_delete_cloud_recording = host_delete_cloud_recording

    @property
    def auto_delete_cmr(self):
        """Gets the auto_delete_cmr of this GroupsgroupIdlockSettingsRecording.  # noqa: E501

        Allow Zoom to automatically delete recordings permanently after a specified number of days.  # noqa: E501

        :return: The auto_delete_cmr of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: bool
        """
        return self._auto_delete_cmr

    @auto_delete_cmr.setter
    def auto_delete_cmr(self, auto_delete_cmr):
        """Sets the auto_delete_cmr of this GroupsgroupIdlockSettingsRecording.

        Allow Zoom to automatically delete recordings permanently after a specified number of days.  # noqa: E501

        :param auto_delete_cmr: The auto_delete_cmr of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: bool
        """

        self._auto_delete_cmr = auto_delete_cmr

    @property
    def recording_authentication(self):
        """Gets the recording_authentication of this GroupsgroupIdlockSettingsRecording.  # noqa: E501


        :return: The recording_authentication of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :rtype: str
        """
        return self._recording_authentication

    @recording_authentication.setter
    def recording_authentication(self, recording_authentication):
        """Sets the recording_authentication of this GroupsgroupIdlockSettingsRecording.


        :param recording_authentication: The recording_authentication of this GroupsgroupIdlockSettingsRecording.  # noqa: E501
        :type: str
        """

        self._recording_authentication = recording_authentication

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
        if issubclass(GroupsgroupIdlockSettingsRecording, dict):
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
        if not isinstance(other, GroupsgroupIdlockSettingsRecording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

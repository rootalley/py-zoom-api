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


class InlineResponse20045(object):
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
        'tsp_provider': 'str',
        'enable': 'bool',
        'dial_in_numbers': 'list[InlineResponse20045DialInNumbers]',
        'tsp_enabled': 'bool',
        'master_account_setting_extended': 'bool',
        'modify_credential_forbidden': 'bool',
        'dial_in_number_unrestricted': 'bool',
        'tsp_bridge': 'str'
    }

    attribute_map = {
        'tsp_provider': 'tsp_provider',
        'enable': 'enable',
        'dial_in_numbers': 'dial_in_numbers',
        'tsp_enabled': 'tsp_enabled',
        'master_account_setting_extended': 'master_account_setting_extended',
        'modify_credential_forbidden': 'modify_credential_forbidden',
        'dial_in_number_unrestricted': 'dial_in_number_unrestricted',
        'tsp_bridge': 'tsp_bridge'
    }

    def __init__(self, tsp_provider=None, enable=None, dial_in_numbers=None, tsp_enabled=None, master_account_setting_extended=None, modify_credential_forbidden=None, dial_in_number_unrestricted=None, tsp_bridge=None):  # noqa: E501
        """InlineResponse20045 - a model defined in Swagger"""  # noqa: E501
        self._tsp_provider = None
        self._enable = None
        self._dial_in_numbers = None
        self._tsp_enabled = None
        self._master_account_setting_extended = None
        self._modify_credential_forbidden = None
        self._dial_in_number_unrestricted = None
        self._tsp_bridge = None
        self.discriminator = None
        if tsp_provider is not None:
            self.tsp_provider = tsp_provider
        if enable is not None:
            self.enable = enable
        if dial_in_numbers is not None:
            self.dial_in_numbers = dial_in_numbers
        if tsp_enabled is not None:
            self.tsp_enabled = tsp_enabled
        if master_account_setting_extended is not None:
            self.master_account_setting_extended = master_account_setting_extended
        if modify_credential_forbidden is not None:
            self.modify_credential_forbidden = modify_credential_forbidden
        if dial_in_number_unrestricted is not None:
            self.dial_in_number_unrestricted = dial_in_number_unrestricted
        if tsp_bridge is not None:
            self.tsp_bridge = tsp_bridge

    @property
    def tsp_provider(self):
        """Gets the tsp_provider of this InlineResponse20045.  # noqa: E501

        Telephony Service Provider.  # noqa: E501

        :return: The tsp_provider of this InlineResponse20045.  # noqa: E501
        :rtype: str
        """
        return self._tsp_provider

    @tsp_provider.setter
    def tsp_provider(self, tsp_provider):
        """Sets the tsp_provider of this InlineResponse20045.

        Telephony Service Provider.  # noqa: E501

        :param tsp_provider: The tsp_provider of this InlineResponse20045.  # noqa: E501
        :type: str
        """

        self._tsp_provider = tsp_provider

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20045.  # noqa: E501

        Enable Telephony Service Provider for account users.  # noqa: E501

        :return: The enable of this InlineResponse20045.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20045.

        Enable Telephony Service Provider for account users.  # noqa: E501

        :param enable: The enable of this InlineResponse20045.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def dial_in_numbers(self):
        """Gets the dial_in_numbers of this InlineResponse20045.  # noqa: E501


        :return: The dial_in_numbers of this InlineResponse20045.  # noqa: E501
        :rtype: list[InlineResponse20045DialInNumbers]
        """
        return self._dial_in_numbers

    @dial_in_numbers.setter
    def dial_in_numbers(self, dial_in_numbers):
        """Sets the dial_in_numbers of this InlineResponse20045.


        :param dial_in_numbers: The dial_in_numbers of this InlineResponse20045.  # noqa: E501
        :type: list[InlineResponse20045DialInNumbers]
        """

        self._dial_in_numbers = dial_in_numbers

    @property
    def tsp_enabled(self):
        """Gets the tsp_enabled of this InlineResponse20045.  # noqa: E501

        Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.  # noqa: E501

        :return: The tsp_enabled of this InlineResponse20045.  # noqa: E501
        :rtype: bool
        """
        return self._tsp_enabled

    @tsp_enabled.setter
    def tsp_enabled(self, tsp_enabled):
        """Sets the tsp_enabled of this InlineResponse20045.

        Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.  # noqa: E501

        :param tsp_enabled: The tsp_enabled of this InlineResponse20045.  # noqa: E501
        :type: bool
        """

        self._tsp_enabled = tsp_enabled

    @property
    def master_account_setting_extended(self):
        """Gets the master_account_setting_extended of this InlineResponse20045.  # noqa: E501

        For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.  # noqa: E501

        :return: The master_account_setting_extended of this InlineResponse20045.  # noqa: E501
        :rtype: bool
        """
        return self._master_account_setting_extended

    @master_account_setting_extended.setter
    def master_account_setting_extended(self, master_account_setting_extended):
        """Sets the master_account_setting_extended of this InlineResponse20045.

        For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.  # noqa: E501

        :param master_account_setting_extended: The master_account_setting_extended of this InlineResponse20045.  # noqa: E501
        :type: bool
        """

        self._master_account_setting_extended = master_account_setting_extended

    @property
    def modify_credential_forbidden(self):
        """Gets the modify_credential_forbidden of this InlineResponse20045.  # noqa: E501

        Control restriction on account users being able to modify their TSP credentials.  # noqa: E501

        :return: The modify_credential_forbidden of this InlineResponse20045.  # noqa: E501
        :rtype: bool
        """
        return self._modify_credential_forbidden

    @modify_credential_forbidden.setter
    def modify_credential_forbidden(self, modify_credential_forbidden):
        """Sets the modify_credential_forbidden of this InlineResponse20045.

        Control restriction on account users being able to modify their TSP credentials.  # noqa: E501

        :param modify_credential_forbidden: The modify_credential_forbidden of this InlineResponse20045.  # noqa: E501
        :type: bool
        """

        self._modify_credential_forbidden = modify_credential_forbidden

    @property
    def dial_in_number_unrestricted(self):
        """Gets the dial_in_number_unrestricted of this InlineResponse20045.  # noqa: E501

        Control restriction on account users adding a TSP number outside of account's dial in numbers.  # noqa: E501

        :return: The dial_in_number_unrestricted of this InlineResponse20045.  # noqa: E501
        :rtype: bool
        """
        return self._dial_in_number_unrestricted

    @dial_in_number_unrestricted.setter
    def dial_in_number_unrestricted(self, dial_in_number_unrestricted):
        """Sets the dial_in_number_unrestricted of this InlineResponse20045.

        Control restriction on account users adding a TSP number outside of account's dial in numbers.  # noqa: E501

        :param dial_in_number_unrestricted: The dial_in_number_unrestricted of this InlineResponse20045.  # noqa: E501
        :type: bool
        """

        self._dial_in_number_unrestricted = dial_in_number_unrestricted

    @property
    def tsp_bridge(self):
        """Gets the tsp_bridge of this InlineResponse20045.  # noqa: E501

        Telephony bridge zone  # noqa: E501

        :return: The tsp_bridge of this InlineResponse20045.  # noqa: E501
        :rtype: str
        """
        return self._tsp_bridge

    @tsp_bridge.setter
    def tsp_bridge(self, tsp_bridge):
        """Sets the tsp_bridge of this InlineResponse20045.

        Telephony bridge zone  # noqa: E501

        :param tsp_bridge: The tsp_bridge of this InlineResponse20045.  # noqa: E501
        :type: str
        """
        allowed_values = ["US_TSP_TB", "EU_TSP_TB"]  # noqa: E501
        if tsp_bridge not in allowed_values:
            raise ValueError(
                "Invalid value for `tsp_bridge` ({0}), must be one of {1}"  # noqa: E501
                .format(tsp_bridge, allowed_values)
            )

        self._tsp_bridge = tsp_bridge

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
        if issubclass(InlineResponse20045, dict):
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
        if not isinstance(other, InlineResponse20045):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

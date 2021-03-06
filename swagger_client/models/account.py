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


class Account(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'password': 'str',
        'options': 'Body23',
        'vanity_url': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'password': 'password',
        'options': 'options',
        'vanity_url': 'vanity_url'
    }

    def __init__(self, first_name=None, last_name=None, email=None, password=None, options=None, vanity_url=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._options = None
        self._vanity_url = None
        self.discriminator = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        if options is not None:
            self.options = options
        if vanity_url is not None:
            self.vanity_url = vanity_url

    @property
    def first_name(self):
        """Gets the first_name of this Account.  # noqa: E501

        User's first name.  # noqa: E501

        :return: The first_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Account.

        User's first name.  # noqa: E501

        :param first_name: The first_name of this Account.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Account.  # noqa: E501

        User's last name.  # noqa: E501

        :return: The last_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Account.

        User's last name.  # noqa: E501

        :param last_name: The last_name of this Account.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Account.  # noqa: E501

        User's email address.  # noqa: E501

        :return: The email of this Account.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Account.

        User's email address.  # noqa: E501

        :param email: The email of this Account.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this Account.  # noqa: E501

        User's password.  # noqa: E501

        :return: The password of this Account.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Account.

        User's password.  # noqa: E501

        :param password: The password of this Account.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def options(self):
        """Gets the options of this Account.  # noqa: E501


        :return: The options of this Account.  # noqa: E501
        :rtype: Body23
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Account.


        :param options: The options of this Account.  # noqa: E501
        :type: Body23
        """

        self._options = options

    @property
    def vanity_url(self):
        """Gets the vanity_url of this Account.  # noqa: E501

        Account Vanity URL  # noqa: E501

        :return: The vanity_url of this Account.  # noqa: E501
        :rtype: str
        """
        return self._vanity_url

    @vanity_url.setter
    def vanity_url(self, vanity_url):
        """Sets the vanity_url of this Account.

        Account Vanity URL  # noqa: E501

        :param vanity_url: The vanity_url of this Account.  # noqa: E501
        :type: str
        """

        self._vanity_url = vanity_url

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

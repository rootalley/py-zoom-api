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


class InlineResponse20090CallQueues(object):
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
        'name': 'str',
        'extension_number': 'int',
        'phone_numbers': 'list[InlineResponse20090PhoneNumbers]',
        'status': 'str',
        'site': 'InlineResponse20090Site'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'extension_number': 'extension_number',
        'phone_numbers': 'phone_numbers',
        'status': 'status',
        'site': 'site'
    }

    def __init__(self, id=None, name=None, extension_number=None, phone_numbers=None, status=None, site=None):  # noqa: E501
        """InlineResponse20090CallQueues - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._extension_number = None
        self._phone_numbers = None
        self._status = None
        self._site = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if extension_number is not None:
            self.extension_number = extension_number
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if status is not None:
            self.status = status
        if site is not None:
            self.site = site

    @property
    def id(self):
        """Gets the id of this InlineResponse20090CallQueues.  # noqa: E501

        Unique Identifier of the Call Queue.  # noqa: E501

        :return: The id of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20090CallQueues.

        Unique Identifier of the Call Queue.  # noqa: E501

        :param id: The id of this InlineResponse20090CallQueues.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20090CallQueues.  # noqa: E501

        Name of the Call Queue.  # noqa: E501

        :return: The name of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20090CallQueues.

        Name of the Call Queue.  # noqa: E501

        :param name: The name of this InlineResponse20090CallQueues.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20090CallQueues.  # noqa: E501

        Extension number assigned to the queue.  # noqa: E501

        :return: The extension_number of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20090CallQueues.

        Extension number assigned to the queue.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20090CallQueues.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse20090CallQueues.  # noqa: E501

        Phone number(s) assigned to the call queue.  # noqa: E501

        :return: The phone_numbers of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: list[InlineResponse20090PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse20090CallQueues.

        Phone number(s) assigned to the call queue.  # noqa: E501

        :param phone_numbers: The phone_numbers of this InlineResponse20090CallQueues.  # noqa: E501
        :type: list[InlineResponse20090PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def status(self):
        """Gets the status of this InlineResponse20090CallQueues.  # noqa: E501

        Status of the Call Queue.<br>`active`: Call queue is enabled and active.<br>`inactive`: Call queue is inactive. Inactive call queues cannot be called but will retain its settings and appear in the [Call Queues](https://zoom.us/pbx/page/telephone/groups#/groups) page.  # noqa: E501

        :return: The status of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20090CallQueues.

        Status of the Call Queue.<br>`active`: Call queue is enabled and active.<br>`inactive`: Call queue is inactive. Inactive call queues cannot be called but will retain its settings and appear in the [Call Queues](https://zoom.us/pbx/page/telephone/groups#/groups) page.  # noqa: E501

        :param status: The status of this InlineResponse20090CallQueues.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def site(self):
        """Gets the site of this InlineResponse20090CallQueues.  # noqa: E501


        :return: The site of this InlineResponse20090CallQueues.  # noqa: E501
        :rtype: InlineResponse20090Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse20090CallQueues.


        :param site: The site of this InlineResponse20090CallQueues.  # noqa: E501
        :type: InlineResponse20090Site
        """

        self._site = site

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
        if issubclass(InlineResponse20090CallQueues, dict):
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
        if not isinstance(other, InlineResponse20090CallQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
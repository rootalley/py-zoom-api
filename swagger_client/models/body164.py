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


class Body164(object):
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
        'name': 'str',
        'description': 'str',
        'site_id': 'str',
        'extension_number': 'int',
        'timezone': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'site_id': 'site_id',
        'extension_number': 'extension_number',
        'timezone': 'timezone',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, site_id=None, extension_number=None, timezone=None, status=None):  # noqa: E501
        """Body164 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._site_id = None
        self._extension_number = None
        self._timezone = None
        self._status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if site_id is not None:
            self.site_id = site_id
        if extension_number is not None:
            self.extension_number = extension_number
        if timezone is not None:
            self.timezone = timezone
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this Body164.  # noqa: E501

        Name of the Call Queue.  # noqa: E501

        :return: The name of this Body164.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body164.

        Name of the Call Queue.  # noqa: E501

        :param name: The name of this Body164.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Body164.  # noqa: E501

        Description for the Call Queue.  # noqa: E501

        :return: The description of this Body164.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body164.

        Description for the Call Queue.  # noqa: E501

        :param description: The description of this Body164.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def site_id(self):
        """Gets the site_id of this Body164.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) where the Call Queue is assigned.  # noqa: E501

        :return: The site_id of this Body164.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Body164.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) where the Call Queue is assigned.  # noqa: E501

        :param site_id: The site_id of this Body164.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def extension_number(self):
        """Gets the extension_number of this Body164.  # noqa: E501

        Phone extension number for the site.<br>  If a site code has been [assigned](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_79ca9c8f-c97b-4486-aa59-d0d9d31a525b) to the site, provide the short extension number instead of the original extension number.  # noqa: E501

        :return: The extension_number of this Body164.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this Body164.

        Phone extension number for the site.<br>  If a site code has been [assigned](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_79ca9c8f-c97b-4486-aa59-d0d9d31a525b) to the site, provide the short extension number instead of the original extension number.  # noqa: E501

        :param extension_number: The extension_number of this Body164.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def timezone(self):
        """Gets the timezone of this Body164.  # noqa: E501

        [Timezone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) of the Call Queue.  # noqa: E501

        :return: The timezone of this Body164.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Body164.

        [Timezone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) of the Call Queue.  # noqa: E501

        :param timezone: The timezone of this Body164.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def status(self):
        """Gets the status of this Body164.  # noqa: E501

        Status of the Call Queue. Allowed values:<br> `active`<br> `inactive`  # noqa: E501

        :return: The status of this Body164.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body164.

        Status of the Call Queue. Allowed values:<br> `active`<br> `inactive`  # noqa: E501

        :param status: The status of this Body164.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(Body164, dict):
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
        if not isinstance(other, Body164):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

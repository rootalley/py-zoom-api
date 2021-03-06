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


class Body128(object):
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
        'action': 'str',
        'type': 'str',
        'reason': 'int',
        'comment': 'str'
    }

    attribute_map = {
        'action': 'action',
        'type': 'type',
        'reason': 'reason',
        'comment': 'comment'
    }

    def __init__(self, action=None, type=None, reason=None, comment=None):  # noqa: E501
        """Body128 - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._type = None
        self._reason = None
        self._comment = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if type is not None:
            self.type = type
        if reason is not None:
            self.reason = reason
        if comment is not None:
            self.comment = comment

    @property
    def action(self):
        """Gets the action of this Body128.  # noqa: E501

        The action that needs to be taken for this sub account. Value must be set to \"cancel\".  # noqa: E501

        :return: The action of this Body128.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Body128.

        The action that needs to be taken for this sub account. Value must be set to \"cancel\".  # noqa: E501

        :param action: The action of this Body128.  # noqa: E501
        :type: str
        """
        allowed_values = ["cancel"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def type(self):
        """Gets the type of this Body128.  # noqa: E501

        Plan [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans).  # noqa: E501

        :return: The type of this Body128.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body128.

        Plan [type](https://marketplace.zoom.us/docs/api-reference/other-references/plans).  # noqa: E501

        :param type: The type of this Body128.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def reason(self):
        """Gets the reason of this Body128.  # noqa: E501

        The reason for the cancellation of plan. Reason options:<br>`1` - Only needed the service occasionally.<br>`2` - Features in the free plan are sufficient.<br>`3` - The plan is too expensive.<br>`4` - Important features are missing.<br>`5` - I need help to better use Zoom.<br> `6` - I bought the wrong product.<br>`7` - I am not satisfied with the product quality.  # noqa: E501

        :return: The reason of this Body128.  # noqa: E501
        :rtype: int
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Body128.

        The reason for the cancellation of plan. Reason options:<br>`1` - Only needed the service occasionally.<br>`2` - Features in the free plan are sufficient.<br>`3` - The plan is too expensive.<br>`4` - Important features are missing.<br>`5` - I need help to better use Zoom.<br> `6` - I bought the wrong product.<br>`7` - I am not satisfied with the product quality.  # noqa: E501

        :param reason: The reason of this Body128.  # noqa: E501
        :type: int
        """

        self._reason = reason

    @property
    def comment(self):
        """Gets the comment of this Body128.  # noqa: E501

        Additional comments about the cancellation decision.  # noqa: E501

        :return: The comment of this Body128.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body128.

        Additional comments about the cancellation decision.  # noqa: E501

        :param comment: The comment of this Body128.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(Body128, dict):
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
        if not isinstance(other, Body128):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

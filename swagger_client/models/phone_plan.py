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


class PhonePlan(object):
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
        'plan_base': 'PhonePlan1PlanBase',
        'plan_calling': 'list[PhonePlan1PlanCalling]',
        'plan_number': 'list[PhonePlan1PlanNumber]'
    }

    attribute_map = {
        'plan_base': 'plan_base',
        'plan_calling': 'plan_calling',
        'plan_number': 'plan_number'
    }

    def __init__(self, plan_base=None, plan_calling=None, plan_number=None):  # noqa: E501
        """PhonePlan - a model defined in Swagger"""  # noqa: E501
        self._plan_base = None
        self._plan_calling = None
        self._plan_number = None
        self.discriminator = None
        if plan_base is not None:
            self.plan_base = plan_base
        if plan_calling is not None:
            self.plan_calling = plan_calling
        if plan_number is not None:
            self.plan_number = plan_number

    @property
    def plan_base(self):
        """Gets the plan_base of this PhonePlan.  # noqa: E501


        :return: The plan_base of this PhonePlan.  # noqa: E501
        :rtype: PhonePlan1PlanBase
        """
        return self._plan_base

    @plan_base.setter
    def plan_base(self, plan_base):
        """Sets the plan_base of this PhonePlan.


        :param plan_base: The plan_base of this PhonePlan.  # noqa: E501
        :type: PhonePlan1PlanBase
        """

        self._plan_base = plan_base

    @property
    def plan_calling(self):
        """Gets the plan_calling of this PhonePlan.  # noqa: E501

        Additional phone calling plans.  # noqa: E501

        :return: The plan_calling of this PhonePlan.  # noqa: E501
        :rtype: list[PhonePlan1PlanCalling]
        """
        return self._plan_calling

    @plan_calling.setter
    def plan_calling(self, plan_calling):
        """Sets the plan_calling of this PhonePlan.

        Additional phone calling plans.  # noqa: E501

        :param plan_calling: The plan_calling of this PhonePlan.  # noqa: E501
        :type: list[PhonePlan1PlanCalling]
        """

        self._plan_calling = plan_calling

    @property
    def plan_number(self):
        """Gets the plan_number of this PhonePlan.  # noqa: E501

        Additional phone number plans.  # noqa: E501

        :return: The plan_number of this PhonePlan.  # noqa: E501
        :rtype: list[PhonePlan1PlanNumber]
        """
        return self._plan_number

    @plan_number.setter
    def plan_number(self, plan_number):
        """Sets the plan_number of this PhonePlan.

        Additional phone number plans.  # noqa: E501

        :param plan_number: The plan_number of this PhonePlan.  # noqa: E501
        :type: list[PhonePlan1PlanNumber]
        """

        self._plan_number = plan_number

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
        if issubclass(PhonePlan, dict):
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
        if not isinstance(other, PhonePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

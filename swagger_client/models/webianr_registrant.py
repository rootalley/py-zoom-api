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


class WebianrRegistrant(object):
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
        'address': 'str',
        'city': 'str',
        'comments': 'str',
        'country': 'str',
        'custom_questions': 'list[MeetingRegistrantCustomQuestions]',
        'email': 'str',
        'first_name': 'str',
        'industry': 'str',
        'job_title': 'str',
        'last_name': 'str',
        'no_of_employees': 'str',
        'org': 'str',
        'phone': 'str',
        'purchasing_time_frame': 'str',
        'role_in_purchase_process': 'str',
        'state': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'comments': 'comments',
        'country': 'country',
        'custom_questions': 'custom_questions',
        'email': 'email',
        'first_name': 'first_name',
        'industry': 'industry',
        'job_title': 'job_title',
        'last_name': 'last_name',
        'no_of_employees': 'no_of_employees',
        'org': 'org',
        'phone': 'phone',
        'purchasing_time_frame': 'purchasing_time_frame',
        'role_in_purchase_process': 'role_in_purchase_process',
        'state': 'state',
        'zip': 'zip'
    }

    def __init__(self, address=None, city=None, comments=None, country=None, custom_questions=None, email=None, first_name=None, industry=None, job_title=None, last_name=None, no_of_employees=None, org=None, phone=None, purchasing_time_frame=None, role_in_purchase_process=None, state=None, zip=None):  # noqa: E501
        """WebianrRegistrant - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._city = None
        self._comments = None
        self._country = None
        self._custom_questions = None
        self._email = None
        self._first_name = None
        self._industry = None
        self._job_title = None
        self._last_name = None
        self._no_of_employees = None
        self._org = None
        self._phone = None
        self._purchasing_time_frame = None
        self._role_in_purchase_process = None
        self._state = None
        self._zip = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if comments is not None:
            self.comments = comments
        if country is not None:
            self.country = country
        if custom_questions is not None:
            self.custom_questions = custom_questions
        self.email = email
        self.first_name = first_name
        if industry is not None:
            self.industry = industry
        if job_title is not None:
            self.job_title = job_title
        if last_name is not None:
            self.last_name = last_name
        if no_of_employees is not None:
            self.no_of_employees = no_of_employees
        if org is not None:
            self.org = org
        if phone is not None:
            self.phone = phone
        if purchasing_time_frame is not None:
            self.purchasing_time_frame = purchasing_time_frame
        if role_in_purchase_process is not None:
            self.role_in_purchase_process = role_in_purchase_process
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip

    @property
    def address(self):
        """Gets the address of this WebianrRegistrant.  # noqa: E501

        Registrant's address.  # noqa: E501

        :return: The address of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this WebianrRegistrant.

        Registrant's address.  # noqa: E501

        :param address: The address of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this WebianrRegistrant.  # noqa: E501

        Registrant's city.  # noqa: E501

        :return: The city of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this WebianrRegistrant.

        Registrant's city.  # noqa: E501

        :param city: The city of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def comments(self):
        """Gets the comments of this WebianrRegistrant.  # noqa: E501

        A field that allows registrants to provide any questions or comments that they might have.  # noqa: E501

        :return: The comments of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WebianrRegistrant.

        A field that allows registrants to provide any questions or comments that they might have.  # noqa: E501

        :param comments: The comments of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def country(self):
        """Gets the country of this WebianrRegistrant.  # noqa: E501

        Registrant's country.  # noqa: E501

        :return: The country of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this WebianrRegistrant.

        Registrant's country.  # noqa: E501

        :param country: The country of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def custom_questions(self):
        """Gets the custom_questions of this WebianrRegistrant.  # noqa: E501

        Custom questions.  # noqa: E501

        :return: The custom_questions of this WebianrRegistrant.  # noqa: E501
        :rtype: list[MeetingRegistrantCustomQuestions]
        """
        return self._custom_questions

    @custom_questions.setter
    def custom_questions(self, custom_questions):
        """Sets the custom_questions of this WebianrRegistrant.

        Custom questions.  # noqa: E501

        :param custom_questions: The custom_questions of this WebianrRegistrant.  # noqa: E501
        :type: list[MeetingRegistrantCustomQuestions]
        """

        self._custom_questions = custom_questions

    @property
    def email(self):
        """Gets the email of this WebianrRegistrant.  # noqa: E501

        A valid email address of the registrant.  # noqa: E501

        :return: The email of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this WebianrRegistrant.

        A valid email address of the registrant.  # noqa: E501

        :param email: The email of this WebianrRegistrant.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this WebianrRegistrant.  # noqa: E501

        Registrant's first name.  # noqa: E501

        :return: The first_name of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this WebianrRegistrant.

        Registrant's first name.  # noqa: E501

        :param first_name: The first_name of this WebianrRegistrant.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def industry(self):
        """Gets the industry of this WebianrRegistrant.  # noqa: E501

        Registrant's Industry.  # noqa: E501

        :return: The industry of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this WebianrRegistrant.

        Registrant's Industry.  # noqa: E501

        :param industry: The industry of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def job_title(self):
        """Gets the job_title of this WebianrRegistrant.  # noqa: E501

        Registrant's job title.  # noqa: E501

        :return: The job_title of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this WebianrRegistrant.

        Registrant's job title.  # noqa: E501

        :param job_title: The job_title of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def last_name(self):
        """Gets the last_name of this WebianrRegistrant.  # noqa: E501

        Registrant's last name.  # noqa: E501

        :return: The last_name of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this WebianrRegistrant.

        Registrant's last name.  # noqa: E501

        :param last_name: The last_name of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def no_of_employees(self):
        """Gets the no_of_employees of this WebianrRegistrant.  # noqa: E501

        Number of Employees:<br>`1-20`<br>`21-50`<br>`51-100`<br>`101-500`<br>`500-1,000`<br>`1,001-5,000`<br>`5,001-10,000`<br>`More than 10,000`  # noqa: E501

        :return: The no_of_employees of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._no_of_employees

    @no_of_employees.setter
    def no_of_employees(self, no_of_employees):
        """Sets the no_of_employees of this WebianrRegistrant.

        Number of Employees:<br>`1-20`<br>`21-50`<br>`51-100`<br>`101-500`<br>`500-1,000`<br>`1,001-5,000`<br>`5,001-10,000`<br>`More than 10,000`  # noqa: E501

        :param no_of_employees: The no_of_employees of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._no_of_employees = no_of_employees

    @property
    def org(self):
        """Gets the org of this WebianrRegistrant.  # noqa: E501

        Registrant's Organization.  # noqa: E501

        :return: The org of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this WebianrRegistrant.

        Registrant's Organization.  # noqa: E501

        :param org: The org of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def phone(self):
        """Gets the phone of this WebianrRegistrant.  # noqa: E501

        Registrant's Phone number.  # noqa: E501

        :return: The phone of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this WebianrRegistrant.

        Registrant's Phone number.  # noqa: E501

        :param phone: The phone of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def purchasing_time_frame(self):
        """Gets the purchasing_time_frame of this WebianrRegistrant.  # noqa: E501

        This field can be included to gauge interest of webinar attendees towards buying your product or service.  Purchasing Time Frame:<br>`Within a month`<br>`1-3 months`<br>`4-6 months`<br>`More than 6 months`<br>`No timeframe`  # noqa: E501

        :return: The purchasing_time_frame of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_time_frame

    @purchasing_time_frame.setter
    def purchasing_time_frame(self, purchasing_time_frame):
        """Sets the purchasing_time_frame of this WebianrRegistrant.

        This field can be included to gauge interest of webinar attendees towards buying your product or service.  Purchasing Time Frame:<br>`Within a month`<br>`1-3 months`<br>`4-6 months`<br>`More than 6 months`<br>`No timeframe`  # noqa: E501

        :param purchasing_time_frame: The purchasing_time_frame of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._purchasing_time_frame = purchasing_time_frame

    @property
    def role_in_purchase_process(self):
        """Gets the role_in_purchase_process of this WebianrRegistrant.  # noqa: E501

        Role in Purchase Process:<br>`Decision Maker`<br>`Evaluator/Recommender`<br>`Influencer`<br>`Not involved`   # noqa: E501

        :return: The role_in_purchase_process of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._role_in_purchase_process

    @role_in_purchase_process.setter
    def role_in_purchase_process(self, role_in_purchase_process):
        """Sets the role_in_purchase_process of this WebianrRegistrant.

        Role in Purchase Process:<br>`Decision Maker`<br>`Evaluator/Recommender`<br>`Influencer`<br>`Not involved`   # noqa: E501

        :param role_in_purchase_process: The role_in_purchase_process of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._role_in_purchase_process = role_in_purchase_process

    @property
    def state(self):
        """Gets the state of this WebianrRegistrant.  # noqa: E501

        Registrant's State/Province.  # noqa: E501

        :return: The state of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WebianrRegistrant.

        Registrant's State/Province.  # noqa: E501

        :param state: The state of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this WebianrRegistrant.  # noqa: E501

        Registrant's Zip/Postal Code.  # noqa: E501

        :return: The zip of this WebianrRegistrant.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this WebianrRegistrant.

        Registrant's Zip/Postal Code.  # noqa: E501

        :param zip: The zip of this WebianrRegistrant.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(WebianrRegistrant, dict):
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
        if not isinstance(other, WebianrRegistrant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

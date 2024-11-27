import pprint
import re  # noqa: F401

import six

class UserDto(object):
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
        'email': 'str',
        'phone': 'str',
        'username': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'id': 'str'
    }

    attribute_map = {
        'email': 'email',
        'phone': 'phone',
        'username': 'username',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'id': 'id'
    }

    def __init__(self, email=None, phone=None, username=None, firstname=None, lastname=None, id=None):  # noqa: E501
        """UserDto - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._phone = None
        self._username = None
        self._firstname = None
        self._lastname = None
        self._id = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if username is not None:
            self.username = username
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if id is not None:
            self.id = id

    @property
    def email(self):
        """Gets the email of this UserDto.  # noqa: E501


        :return: The email of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDto.


        :param email: The email of this UserDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UserDto.  # noqa: E501


        :return: The phone of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserDto.


        :param phone: The phone of this UserDto.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def username(self):
        """Gets the username of this UserDto.  # noqa: E501


        :return: The username of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserDto.


        :param username: The username of this UserDto.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def firstname(self):
        """Gets the firstname of this UserDto.  # noqa: E501


        :return: The firstname of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserDto.


        :param firstname: The firstname of this UserDto.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserDto.  # noqa: E501


        :return: The lastname of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserDto.


        :param lastname: The lastname of this UserDto.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def id(self):
        """Gets the id of this UserDto.  # noqa: E501


        :return: The id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDto.


        :param id: The id of this UserDto.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(UserDto, dict):
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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
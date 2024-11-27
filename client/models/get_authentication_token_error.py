import pprint
import re  # noqa: F401

import six

class GetAuthenticationTokenError(object):
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
        'code': 'AllOfGetAuthenticationTokenErrorCode',
        'type': 'AllOfGetAuthenticationTokenErrorType',
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'code': 'code',
        'type': 'type',
        'values': 'values'
    }

    def __init__(self, code=None, type=None, values=None):  # noqa: E501
        """GetAuthenticationTokenError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._type = None
        self._values = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type
        if values is not None:
            self.values = values

    @property
    def code(self):
        """Gets the code of this GetAuthenticationTokenError.  # noqa: E501


        :return: The code of this GetAuthenticationTokenError.  # noqa: E501
        :rtype: AllOfGetAuthenticationTokenErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetAuthenticationTokenError.


        :param code: The code of this GetAuthenticationTokenError.  # noqa: E501
        :type: AllOfGetAuthenticationTokenErrorCode
        """

        self._code = code

    @property
    def type(self):
        """Gets the type of this GetAuthenticationTokenError.  # noqa: E501

          1 = BusinessLogic  2 = InternalServerError  # noqa: E501

        :return: The type of this GetAuthenticationTokenError.  # noqa: E501
        :rtype: AllOfGetAuthenticationTokenErrorType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetAuthenticationTokenError.

          1 = BusinessLogic  2 = InternalServerError  # noqa: E501

        :param type: The type of this GetAuthenticationTokenError.  # noqa: E501
        :type: AllOfGetAuthenticationTokenErrorType
        """

        self._type = type

    @property
    def values(self):
        """Gets the values of this GetAuthenticationTokenError.  # noqa: E501


        :return: The values of this GetAuthenticationTokenError.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this GetAuthenticationTokenError.


        :param values: The values of this GetAuthenticationTokenError.  # noqa: E501
        :type: dict(str, str)
        """

        self._values = values

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
        if issubclass(GetAuthenticationTokenError, dict):
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
        if not isinstance(other, GetAuthenticationTokenError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

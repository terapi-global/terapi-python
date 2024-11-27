import pprint
import re  # noqa: F401

import six

class RefreshAuthenticationTokenDto(object):
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
        'access_token': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'expires_in': 'expiresIn'
    }

    def __init__(self, access_token=None, expires_in=None):  # noqa: E501
        """RefreshAuthenticationTokenDto - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._expires_in = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in

    @property
    def access_token(self):
        """Gets the access_token of this RefreshAuthenticationTokenDto.  # noqa: E501


        :return: The access_token of this RefreshAuthenticationTokenDto.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RefreshAuthenticationTokenDto.


        :param access_token: The access_token of this RefreshAuthenticationTokenDto.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this RefreshAuthenticationTokenDto.  # noqa: E501


        :return: The expires_in of this RefreshAuthenticationTokenDto.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this RefreshAuthenticationTokenDto.


        :param expires_in: The expires_in of this RefreshAuthenticationTokenDto.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

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
        if issubclass(RefreshAuthenticationTokenDto, dict):
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
        if not isinstance(other, RefreshAuthenticationTokenDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

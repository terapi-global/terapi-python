import pprint
import re  # noqa: F401

import six

class CreateApplicationApiKeyRequestDto(object):
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
        'web_url': 'str',
        'ip_addresses': 'list[str]',
        'application_id': 'str'
    }

    attribute_map = {
        'web_url': 'webUrl',
        'ip_addresses': 'ipAddresses',
        'application_id': 'applicationId'
    }

    def __init__(self, web_url=None, ip_addresses=None, application_id=None):  # noqa: E501
        """CreateApplicationApiKeyRequestDto - a model defined in Swagger"""  # noqa: E501
        self._web_url = None
        self._ip_addresses = None
        self._application_id = None
        self.discriminator = None
        if web_url is not None:
            self.web_url = web_url
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if application_id is not None:
            self.application_id = application_id

    @property
    def web_url(self):
        """Gets the web_url of this CreateApplicationApiKeyRequestDto.  # noqa: E501


        :return: The web_url of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this CreateApplicationApiKeyRequestDto.


        :param web_url: The web_url of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this CreateApplicationApiKeyRequestDto.  # noqa: E501


        :return: The ip_addresses of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this CreateApplicationApiKeyRequestDto.


        :param ip_addresses: The ip_addresses of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def application_id(self):
        """Gets the application_id of this CreateApplicationApiKeyRequestDto.  # noqa: E501


        :return: The application_id of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CreateApplicationApiKeyRequestDto.


        :param application_id: The application_id of this CreateApplicationApiKeyRequestDto.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

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
        if issubclass(CreateApplicationApiKeyRequestDto, dict):
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
        if not isinstance(other, CreateApplicationApiKeyRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
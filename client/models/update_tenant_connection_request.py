import pprint
import re  # noqa: F401

import six

class UpdateTenantConnectionRequest(object):
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
        'dto': 'AllOfUpdateTenantConnectionRequestDto'
    }

    attribute_map = {
        'dto': 'dto'
    }

    def __init__(self, dto=None):  # noqa: E501
        """UpdateTenantConnectionRequest - a model defined in Swagger"""  # noqa: E501
        self._dto = None
        self.discriminator = None
        if dto is not None:
            self.dto = dto

    @property
    def dto(self):
        """Gets the dto of this UpdateTenantConnectionRequest.  # noqa: E501


        :return: The dto of this UpdateTenantConnectionRequest.  # noqa: E501
        :rtype: AllOfUpdateTenantConnectionRequestDto
        """
        return self._dto

    @dto.setter
    def dto(self, dto):
        """Sets the dto of this UpdateTenantConnectionRequest.


        :param dto: The dto of this UpdateTenantConnectionRequest.  # noqa: E501
        :type: AllOfUpdateTenantConnectionRequestDto
        """

        self._dto = dto

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
        if issubclass(UpdateTenantConnectionRequest, dict):
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
        if not isinstance(other, UpdateTenantConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
import pprint
import re  # noqa: F401

import six

class InviteTenantRequestErrorCodes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _20998101 = "20998101"
    _20998102 = "20998102"
    _20998103 = "20998103"
    _20998104 = "20998104"
    _20998105 = "20998105"
    _20998106 = "20998106"
    _20998107 = "20998107"
    _20998108 = "20998108"
    _20998109 = "20998109"
    _20998110 = "20998110"
    _20998111 = "20998111"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """InviteTenantRequestErrorCodes - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(InviteTenantRequestErrorCodes, dict):
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
        if not isinstance(other, InviteTenantRequestErrorCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

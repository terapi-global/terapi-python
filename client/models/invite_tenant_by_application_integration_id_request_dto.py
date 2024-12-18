import pprint
import re  # noqa: F401

import six

class InviteTenantByApplicationIntegrationIdRequestDto(object):
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
        'invited_email_address': 'str',
        'application_integration_id': 'str',
        'is_public_integration': 'bool'
    }

    attribute_map = {
        'invited_email_address': 'invitedEmailAddress',
        'application_integration_id': 'applicationIntegrationId',
        'is_public_integration': 'isPublicIntegration'
    }

    def __init__(self, invited_email_address=None, application_integration_id=None, is_public_integration=None):  # noqa: E501
        """InviteTenantByApplicationIntegrationIdRequestDto - a model defined in Swagger"""  # noqa: E501
        self._invited_email_address = None
        self._application_integration_id = None
        self._is_public_integration = None
        self.discriminator = None
        if invited_email_address is not None:
            self.invited_email_address = invited_email_address
        if application_integration_id is not None:
            self.application_integration_id = application_integration_id
        if is_public_integration is not None:
            self.is_public_integration = is_public_integration

    @property
    def invited_email_address(self):
        """Gets the invited_email_address of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501


        :return: The invited_email_address of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._invited_email_address

    @invited_email_address.setter
    def invited_email_address(self, invited_email_address):
        """Sets the invited_email_address of this InviteTenantByApplicationIntegrationIdRequestDto.


        :param invited_email_address: The invited_email_address of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :type: str
        """

        self._invited_email_address = invited_email_address

    @property
    def application_integration_id(self):
        """Gets the application_integration_id of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501


        :return: The application_integration_id of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._application_integration_id

    @application_integration_id.setter
    def application_integration_id(self, application_integration_id):
        """Sets the application_integration_id of this InviteTenantByApplicationIntegrationIdRequestDto.


        :param application_integration_id: The application_integration_id of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :type: str
        """

        self._application_integration_id = application_integration_id

    @property
    def is_public_integration(self):
        """Gets the is_public_integration of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501


        :return: The is_public_integration of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_integration

    @is_public_integration.setter
    def is_public_integration(self, is_public_integration):
        """Sets the is_public_integration of this InviteTenantByApplicationIntegrationIdRequestDto.


        :param is_public_integration: The is_public_integration of this InviteTenantByApplicationIntegrationIdRequestDto.  # noqa: E501
        :type: bool
        """

        self._is_public_integration = is_public_integration

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
        if issubclass(InviteTenantByApplicationIntegrationIdRequestDto, dict):
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
        if not isinstance(other, InviteTenantByApplicationIntegrationIdRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

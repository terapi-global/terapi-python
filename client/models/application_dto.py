import pprint
import re  # noqa: F401

import six

class ApplicationDto(object):
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
        'name': 'str',
        'description': 'str',
        'category': 'str',
        'official_landing_url': 'str',
        'redirect_base_url': 'str',
        'privacy_policy_url': 'str',
        'end_user_license_agreement_url': 'str',
        'total_integrations': 'int',
        'total_tenants': 'int',
        'total_api_calls': 'int',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'category': 'category',
        'official_landing_url': 'officialLandingUrl',
        'redirect_base_url': 'redirectBaseUrl',
        'privacy_policy_url': 'privacyPolicyUrl',
        'end_user_license_agreement_url': 'endUserLicenseAgreementUrl',
        'total_integrations': 'totalIntegrations',
        'total_tenants': 'totalTenants',
        'total_api_calls': 'totalApiCalls',
        'id': 'id'
    }

    def __init__(self, name=None, description=None, category=None, official_landing_url=None, redirect_base_url=None, privacy_policy_url=None, end_user_license_agreement_url=None, total_integrations=None, total_tenants=None, total_api_calls=None, id=None):  # noqa: E501
        """ApplicationDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._category = None
        self._official_landing_url = None
        self._redirect_base_url = None
        self._privacy_policy_url = None
        self._end_user_license_agreement_url = None
        self._total_integrations = None
        self._total_tenants = None
        self._total_api_calls = None
        self._id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if official_landing_url is not None:
            self.official_landing_url = official_landing_url
        if redirect_base_url is not None:
            self.redirect_base_url = redirect_base_url
        if privacy_policy_url is not None:
            self.privacy_policy_url = privacy_policy_url
        if end_user_license_agreement_url is not None:
            self.end_user_license_agreement_url = end_user_license_agreement_url
        if total_integrations is not None:
            self.total_integrations = total_integrations
        if total_tenants is not None:
            self.total_tenants = total_tenants
        if total_api_calls is not None:
            self.total_api_calls = total_api_calls
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ApplicationDto.  # noqa: E501


        :return: The name of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationDto.


        :param name: The name of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApplicationDto.  # noqa: E501


        :return: The description of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationDto.


        :param description: The description of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this ApplicationDto.  # noqa: E501


        :return: The category of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ApplicationDto.


        :param category: The category of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def official_landing_url(self):
        """Gets the official_landing_url of this ApplicationDto.  # noqa: E501


        :return: The official_landing_url of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._official_landing_url

    @official_landing_url.setter
    def official_landing_url(self, official_landing_url):
        """Sets the official_landing_url of this ApplicationDto.


        :param official_landing_url: The official_landing_url of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._official_landing_url = official_landing_url

    @property
    def redirect_base_url(self):
        """Gets the redirect_base_url of this ApplicationDto.  # noqa: E501


        :return: The redirect_base_url of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._redirect_base_url

    @redirect_base_url.setter
    def redirect_base_url(self, redirect_base_url):
        """Sets the redirect_base_url of this ApplicationDto.


        :param redirect_base_url: The redirect_base_url of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._redirect_base_url = redirect_base_url

    @property
    def privacy_policy_url(self):
        """Gets the privacy_policy_url of this ApplicationDto.  # noqa: E501


        :return: The privacy_policy_url of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._privacy_policy_url

    @privacy_policy_url.setter
    def privacy_policy_url(self, privacy_policy_url):
        """Sets the privacy_policy_url of this ApplicationDto.


        :param privacy_policy_url: The privacy_policy_url of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._privacy_policy_url = privacy_policy_url

    @property
    def end_user_license_agreement_url(self):
        """Gets the end_user_license_agreement_url of this ApplicationDto.  # noqa: E501


        :return: The end_user_license_agreement_url of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._end_user_license_agreement_url

    @end_user_license_agreement_url.setter
    def end_user_license_agreement_url(self, end_user_license_agreement_url):
        """Sets the end_user_license_agreement_url of this ApplicationDto.


        :param end_user_license_agreement_url: The end_user_license_agreement_url of this ApplicationDto.  # noqa: E501
        :type: str
        """

        self._end_user_license_agreement_url = end_user_license_agreement_url

    @property
    def total_integrations(self):
        """Gets the total_integrations of this ApplicationDto.  # noqa: E501


        :return: The total_integrations of this ApplicationDto.  # noqa: E501
        :rtype: int
        """
        return self._total_integrations

    @total_integrations.setter
    def total_integrations(self, total_integrations):
        """Sets the total_integrations of this ApplicationDto.


        :param total_integrations: The total_integrations of this ApplicationDto.  # noqa: E501
        :type: int
        """

        self._total_integrations = total_integrations

    @property
    def total_tenants(self):
        """Gets the total_tenants of this ApplicationDto.  # noqa: E501


        :return: The total_tenants of this ApplicationDto.  # noqa: E501
        :rtype: int
        """
        return self._total_tenants

    @total_tenants.setter
    def total_tenants(self, total_tenants):
        """Sets the total_tenants of this ApplicationDto.


        :param total_tenants: The total_tenants of this ApplicationDto.  # noqa: E501
        :type: int
        """

        self._total_tenants = total_tenants

    @property
    def total_api_calls(self):
        """Gets the total_api_calls of this ApplicationDto.  # noqa: E501


        :return: The total_api_calls of this ApplicationDto.  # noqa: E501
        :rtype: int
        """
        return self._total_api_calls

    @total_api_calls.setter
    def total_api_calls(self, total_api_calls):
        """Sets the total_api_calls of this ApplicationDto.


        :param total_api_calls: The total_api_calls of this ApplicationDto.  # noqa: E501
        :type: int
        """

        self._total_api_calls = total_api_calls

    @property
    def id(self):
        """Gets the id of this ApplicationDto.  # noqa: E501


        :return: The id of this ApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationDto.


        :param id: The id of this ApplicationDto.  # noqa: E501
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
        if issubclass(ApplicationDto, dict):
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
        if not isinstance(other, ApplicationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

import pprint
import re  # noqa: F401

import six

class CategoryDto(object):
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
        'title': 'str',
        'is_parent': 'bool',
        'parent_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'is_parent': 'isParent',
        'parent_id': 'parentId',
        'id': 'id'
    }

    def __init__(self, title=None, is_parent=None, parent_id=None, id=None):  # noqa: E501
        """CategoryDto - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._is_parent = None
        self._parent_id = None
        self._id = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if is_parent is not None:
            self.is_parent = is_parent
        if parent_id is not None:
            self.parent_id = parent_id
        if id is not None:
            self.id = id

    @property
    def title(self):
        """Gets the title of this CategoryDto.  # noqa: E501


        :return: The title of this CategoryDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CategoryDto.


        :param title: The title of this CategoryDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def is_parent(self):
        """Gets the is_parent of this CategoryDto.  # noqa: E501


        :return: The is_parent of this CategoryDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_parent

    @is_parent.setter
    def is_parent(self, is_parent):
        """Sets the is_parent of this CategoryDto.


        :param is_parent: The is_parent of this CategoryDto.  # noqa: E501
        :type: bool
        """

        self._is_parent = is_parent

    @property
    def parent_id(self):
        """Gets the parent_id of this CategoryDto.  # noqa: E501


        :return: The parent_id of this CategoryDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CategoryDto.


        :param parent_id: The parent_id of this CategoryDto.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this CategoryDto.  # noqa: E501


        :return: The id of this CategoryDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryDto.


        :param id: The id of this CategoryDto.  # noqa: E501
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
        if issubclass(CategoryDto, dict):
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
        if not isinstance(other, CategoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

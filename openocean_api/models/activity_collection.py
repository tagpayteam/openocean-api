# coding: utf-8

"""
    OpenOcean-Api

    OpenOcean Swagger API Spec  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openocean_api.configuration import Configuration


class ActivityCollection(object):
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
        'collection_slug': 'str',
        'collection_name': 'str',
        'collection_image': 'str'
    }

    attribute_map = {
        'collection_slug': 'collectionSlug',
        'collection_name': 'collectionName',
        'collection_image': 'collectionImage'
    }

    def __init__(self, collection_slug=None, collection_name=None, collection_image=None, _configuration=None):  # noqa: E501
        """ActivityCollection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collection_slug = None
        self._collection_name = None
        self._collection_image = None
        self.discriminator = None

        self.collection_slug = collection_slug
        self.collection_name = collection_name
        self.collection_image = collection_image

    @property
    def collection_slug(self):
        """Gets the collection_slug of this ActivityCollection.  # noqa: E501

        slug  # noqa: E501

        :return: The collection_slug of this ActivityCollection.  # noqa: E501
        :rtype: str
        """
        return self._collection_slug

    @collection_slug.setter
    def collection_slug(self, collection_slug):
        """Sets the collection_slug of this ActivityCollection.

        slug  # noqa: E501

        :param collection_slug: The collection_slug of this ActivityCollection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_slug is None:
            raise ValueError("Invalid value for `collection_slug`, must not be `None`")  # noqa: E501

        self._collection_slug = collection_slug

    @property
    def collection_name(self):
        """Gets the collection_name of this ActivityCollection.  # noqa: E501

        name  # noqa: E501

        :return: The collection_name of this ActivityCollection.  # noqa: E501
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """Sets the collection_name of this ActivityCollection.

        name  # noqa: E501

        :param collection_name: The collection_name of this ActivityCollection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_name is None:
            raise ValueError("Invalid value for `collection_name`, must not be `None`")  # noqa: E501

        self._collection_name = collection_name

    @property
    def collection_image(self):
        """Gets the collection_image of this ActivityCollection.  # noqa: E501

        image  # noqa: E501

        :return: The collection_image of this ActivityCollection.  # noqa: E501
        :rtype: str
        """
        return self._collection_image

    @collection_image.setter
    def collection_image(self, collection_image):
        """Sets the collection_image of this ActivityCollection.

        image  # noqa: E501

        :param collection_image: The collection_image of this ActivityCollection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_image is None:
            raise ValueError("Invalid value for `collection_image`, must not be `None`")  # noqa: E501

        self._collection_image = collection_image

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
        if issubclass(ActivityCollection, dict):
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
        if not isinstance(other, ActivityCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActivityCollection):
            return True

        return self.to_dict() != other.to_dict()

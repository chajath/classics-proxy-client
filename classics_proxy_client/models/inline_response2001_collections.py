# coding: utf-8

"""
    Classics Proxy API

    Proxy API for fetching Classic Sino-Korean Literature from various corpora  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from classics_proxy_client.configuration import Configuration


class InlineResponse2001Collections(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'authors': 'str',
        'data_id': 'str',
        'title': 'str',
        'zn_title': 'str'
    }

    attribute_map = {
        'authors': 'authors',
        'data_id': 'data_id',
        'title': 'title',
        'zn_title': 'zn_title'
    }

    def __init__(self, authors=None, data_id=None, title=None, zn_title=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001Collections - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authors = None
        self._data_id = None
        self._title = None
        self._zn_title = None
        self.discriminator = None

        if authors is not None:
            self.authors = authors
        if data_id is not None:
            self.data_id = data_id
        if title is not None:
            self.title = title
        if zn_title is not None:
            self.zn_title = zn_title

    @property
    def authors(self):
        """Gets the authors of this InlineResponse2001Collections.  # noqa: E501


        :return: The authors of this InlineResponse2001Collections.  # noqa: E501
        :rtype: str
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this InlineResponse2001Collections.


        :param authors: The authors of this InlineResponse2001Collections.  # noqa: E501
        :type: str
        """

        self._authors = authors

    @property
    def data_id(self):
        """Gets the data_id of this InlineResponse2001Collections.  # noqa: E501


        :return: The data_id of this InlineResponse2001Collections.  # noqa: E501
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """Sets the data_id of this InlineResponse2001Collections.


        :param data_id: The data_id of this InlineResponse2001Collections.  # noqa: E501
        :type: str
        """

        self._data_id = data_id

    @property
    def title(self):
        """Gets the title of this InlineResponse2001Collections.  # noqa: E501


        :return: The title of this InlineResponse2001Collections.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse2001Collections.


        :param title: The title of this InlineResponse2001Collections.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def zn_title(self):
        """Gets the zn_title of this InlineResponse2001Collections.  # noqa: E501


        :return: The zn_title of this InlineResponse2001Collections.  # noqa: E501
        :rtype: str
        """
        return self._zn_title

    @zn_title.setter
    def zn_title(self, zn_title):
        """Sets the zn_title of this InlineResponse2001Collections.


        :param zn_title: The zn_title of this InlineResponse2001Collections.  # noqa: E501
        :type: str
        """

        self._zn_title = zn_title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001Collections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001Collections):
            return True

        return self.to_dict() != other.to_dict()

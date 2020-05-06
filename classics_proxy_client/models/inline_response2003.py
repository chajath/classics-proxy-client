# coding: utf-8

"""
    Classics Proxy API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from classics_proxy_client.configuration import Configuration


class InlineResponse2003(object):
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
        'text': 'str',
        'zn_text': 'str',
        'title': 'str',
        'zn_title': 'str'
    }

    attribute_map = {
        'text': 'text',
        'zn_text': 'zn_text',
        'title': 'title',
        'zn_title': 'zn_title'
    }

    def __init__(self, text=None, zn_text=None, title=None, zn_title=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2003 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._zn_text = None
        self._title = None
        self._zn_title = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if zn_text is not None:
            self.zn_text = zn_text
        if title is not None:
            self.title = title
        if zn_title is not None:
            self.zn_title = zn_title

    @property
    def text(self):
        """Gets the text of this InlineResponse2003.  # noqa: E501


        :return: The text of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InlineResponse2003.


        :param text: The text of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def zn_text(self):
        """Gets the zn_text of this InlineResponse2003.  # noqa: E501


        :return: The zn_text of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._zn_text

    @zn_text.setter
    def zn_text(self, zn_text):
        """Sets the zn_text of this InlineResponse2003.


        :param zn_text: The zn_text of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._zn_text = zn_text

    @property
    def title(self):
        """Gets the title of this InlineResponse2003.  # noqa: E501


        :return: The title of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse2003.


        :param title: The title of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def zn_title(self):
        """Gets the zn_title of this InlineResponse2003.  # noqa: E501


        :return: The zn_title of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._zn_title

    @zn_title.setter
    def zn_title(self, zn_title):
        """Sets the zn_title of this InlineResponse2003.


        :param zn_title: The zn_title of this InlineResponse2003.  # noqa: E501
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    Classics Proxy API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import classics_proxy_client
from classics_proxy_client.models.inline_response200_series import InlineResponse200Series  # noqa: E501
from classics_proxy_client.rest import ApiException

class TestInlineResponse200Series(unittest.TestCase):
    """InlineResponse200Series unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200Series
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = classics_proxy_client.models.inline_response200_series.InlineResponse200Series()  # noqa: E501
        if include_optional :
            return InlineResponse200Series(
                id = '0', 
                name = '0'
            )
        else :
            return InlineResponse200Series(
        )

    def testInlineResponse200Series(self):
        """Test InlineResponse200Series"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Classics Proxy API

    Proxy API for fetching Classic Sino-Korean Literature from various corpora  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from classics_proxy_client.api_client import ApiClient
from classics_proxy_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def itkc_all_text_meta(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_all_text_meta  # noqa: E501

        Recursively list all text nodes under the given `dataId`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_all_text_meta(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.itkc_all_text_meta_with_http_info(series_id, data_id, **kwargs)  # noqa: E501

    def itkc_all_text_meta_with_http_info(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_all_text_meta  # noqa: E501

        Recursively list all text nodes under the given `dataId`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_all_text_meta_with_http_info(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'series_id',
            'data_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method itkc_all_text_meta" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['series_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `series_id` when calling `itkc_all_text_meta`")  # noqa: E501
        # verify the required parameter 'data_id' is set
        if self.api_client.client_side_validation and ('data_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_id` when calling `itkc_all_text_meta`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'series_id' in local_var_params:
            path_params['seriesId'] = local_var_params['series_id']  # noqa: E501
        if 'data_id' in local_var_params:
            path_params['dataId'] = local_var_params['data_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/corpora/itkc/{seriesId}/all_text_meta/{dataId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def itkc_corpora(self, **kwargs):  # noqa: E501
        """itkc_corpora  # noqa: E501

        List all supported itkc corpora  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_corpora(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.itkc_corpora_with_http_info(**kwargs)  # noqa: E501

    def itkc_corpora_with_http_info(self, **kwargs):  # noqa: E501
        """itkc_corpora  # noqa: E501

        List all supported itkc corpora  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_corpora_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse200, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method itkc_corpora" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/corpora/itkc', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def itkc_meta(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_meta  # noqa: E501

        List subsections and articles belonging to the given `dataId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_meta(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.itkc_meta_with_http_info(series_id, data_id, **kwargs)  # noqa: E501

    def itkc_meta_with_http_info(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_meta  # noqa: E501

        List subsections and articles belonging to the given `dataId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_meta_with_http_info(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'series_id',
            'data_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method itkc_meta" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['series_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `series_id` when calling `itkc_meta`")  # noqa: E501
        # verify the required parameter 'data_id' is set
        if self.api_client.client_side_validation and ('data_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_id` when calling `itkc_meta`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'series_id' in local_var_params:
            path_params['seriesId'] = local_var_params['series_id']  # noqa: E501
        if 'data_id' in local_var_params:
            path_params['dataId'] = local_var_params['data_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/corpora/itkc/{seriesId}/meta/{dataId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def itkc_series(self, series_id, **kwargs):  # noqa: E501
        """itkc_series  # noqa: E501

        List all volumns for the corpus  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_series(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.itkc_series_with_http_info(series_id, **kwargs)  # noqa: E501

    def itkc_series_with_http_info(self, series_id, **kwargs):  # noqa: E501
        """itkc_series  # noqa: E501

        List all volumns for the corpus  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_series_with_http_info(series_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'series_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method itkc_series" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['series_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `series_id` when calling `itkc_series`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'series_id' in local_var_params:
            path_params['seriesId'] = local_var_params['series_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/corpora/itkc/{seriesId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def itkc_text(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_text  # noqa: E501

        Get the text content  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_text(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.itkc_text_with_http_info(series_id, data_id, **kwargs)  # noqa: E501

    def itkc_text_with_http_info(self, series_id, data_id, **kwargs):  # noqa: E501
        """itkc_text  # noqa: E501

        Get the text content  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.itkc_text_with_http_info(series_id, data_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str series_id: Id of the corpora from `/corpora/itkc` (required)
        :param str data_id: Id for the node as given in the `data_id` field (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2003, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'series_id',
            'data_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method itkc_text" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'series_id' is set
        if self.api_client.client_side_validation and ('series_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['series_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `series_id` when calling `itkc_text`")  # noqa: E501
        # verify the required parameter 'data_id' is set
        if self.api_client.client_side_validation and ('data_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_id` when calling `itkc_text`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'series_id' in local_var_params:
            path_params['seriesId'] = local_var_params['series_id']  # noqa: E501
        if 'data_id' in local_var_params:
            path_params['dataId'] = local_var_params['data_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/corpora/itkc/{seriesId}/text/{dataId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

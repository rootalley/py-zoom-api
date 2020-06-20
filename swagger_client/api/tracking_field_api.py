# coding: utf-8

"""
    Zoom API

    The Zoom API allows developers to safely and securely access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [Authorization Guide](https://marketplace.zoom.us/docs/guides/authorization/credentials). All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance you can list all users on an account via `https://api.zoom.us/v2/users/`.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: developersupport@zoom.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TrackingFieldApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trackingfield_create(self, body, **kwargs):  # noqa: E501
        """Create a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to create a new tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField body: Tracking Field (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def trackingfield_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to create a new tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField body: Tracking Field (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `trackingfield_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'field' in params:
            form_params.append(('field', params['field']))  # noqa: E501
        if 'required' in params:
            form_params.append(('required', params['required']))  # noqa: E501
        if 'visible' in params:
            form_params.append(('visible', params['visible']))  # noqa: E501
        if 'recommended_values' in params:
            form_params.append(('recommended_values', params['recommended_values']))  # noqa: E501
            collection_formats['recommended_values'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_create(self, field, required, visible, recommended_values, **kwargs):  # noqa: E501
        """Create a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to create a new tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create(field, required, visible, recommended_values, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: (required)
        :param bool required: (required)
        :param bool visible: (required)
        :param list[str] recommended_values: (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_create_with_http_info(field, required, visible, recommended_values, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_create_with_http_info(field, required, visible, recommended_values, **kwargs)  # noqa: E501
            return data

    def trackingfield_create_with_http_info(self, field, required, visible, recommended_values, **kwargs):  # noqa: E501
        """Create a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to create a new tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create_with_http_info(field, required, visible, recommended_values, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: (required)
        :param bool required: (required)
        :param bool visible: (required)
        :param list[str] recommended_values: (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field', 'required', 'visible', 'recommended_values']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `trackingfield_create`")  # noqa: E501
        # verify the required parameter 'required' is set
        if ('required' not in params or
                params['required'] is None):
            raise ValueError("Missing the required parameter `required` when calling `trackingfield_create`")  # noqa: E501
        # verify the required parameter 'visible' is set
        if ('visible' not in params or
                params['visible'] is None):
            raise ValueError("Missing the required parameter `visible` when calling `trackingfield_create`")  # noqa: E501
        # verify the required parameter 'recommended_values' is set
        if ('recommended_values' not in params or
                params['recommended_values'] is None):
            raise ValueError("Missing the required parameter `recommended_values` when calling `trackingfield_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'field' in params:
            form_params.append(('field', params['field']))  # noqa: E501
        if 'required' in params:
            form_params.append(('required', params['required']))  # noqa: E501
        if 'visible' in params:
            form_params.append(('visible', params['visible']))  # noqa: E501
        if 'recommended_values' in params:
            form_params.append(('recommended_values', params['recommended_values']))  # noqa: E501
            collection_formats['recommended_values'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_delete(self, field_id, **kwargs):  # noqa: E501
        """Delete a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to delete a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_delete(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_delete_with_http_info(field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_delete_with_http_info(field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_delete_with_http_info(self, field_id, **kwargs):  # noqa: E501
        """Delete a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to delete a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_delete_with_http_info(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_get(self, field_id, **kwargs):  # noqa: E501
        """Get a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br><br> When scheduling a meeting, the tracking field will be included in the meeting options.<br>Use this API to get information on a tracking field.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_get(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_get_with_http_info(field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_get_with_http_info(field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_get_with_http_info(self, field_id, **kwargs):  # noqa: E501
        """Get a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br><br> When scheduling a meeting, the tracking field will be included in the meeting options.<br>Use this API to get information on a tracking field.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_get_with_http_info(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: InlineResponse2018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_list(self, **kwargs):  # noqa: E501
        """List Tracking Fields  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to list all the tracking fields on your Zoom account.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def trackingfield_list_with_http_info(self, **kwargs):  # noqa: E501
        """List Tracking Fields  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to list all the tracking fields on your Zoom account.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_update(self, body, field_id, **kwargs):  # noqa: E501
        """Update a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to update a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update(body, field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField2 body: (required)
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_update_with_http_info(body, field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_update_with_http_info(body, field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_update_with_http_info(self, body, field_id, **kwargs):  # noqa: E501
        """Update a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to update a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update_with_http_info(body, field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField2 body: (required)
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `trackingfield_update`")  # noqa: E501
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'field' in params:
            form_params.append(('field', params['field']))  # noqa: E501
        if 'required' in params:
            form_params.append(('required', params['required']))  # noqa: E501
        if 'visible' in params:
            form_params.append(('visible', params['visible']))  # noqa: E501
        if 'recommended_values' in params:
            form_params.append(('recommended_values', params['recommended_values']))  # noqa: E501
            collection_formats['recommended_values'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_update(self, field, required, visible, recommended_values, field_id, **kwargs):  # noqa: E501
        """Update a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to update a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update(field, required, visible, recommended_values, field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: (required)
        :param bool required: (required)
        :param bool visible: (required)
        :param list[str] recommended_values: (required)
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_update_with_http_info(field, required, visible, recommended_values, field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_update_with_http_info(field, required, visible, recommended_values, field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_update_with_http_info(self, field, required, visible, recommended_values, field_id, **kwargs):  # noqa: E501
        """Update a Tracking Field  # noqa: E501

        [Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to update a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update_with_http_info(field, required, visible, recommended_values, field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field: (required)
        :param bool required: (required)
        :param bool visible: (required)
        :param list[str] recommended_values: (required)
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field', 'required', 'visible', 'recommended_values', 'field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `trackingfield_update`")  # noqa: E501
        # verify the required parameter 'required' is set
        if ('required' not in params or
                params['required'] is None):
            raise ValueError("Missing the required parameter `required` when calling `trackingfield_update`")  # noqa: E501
        # verify the required parameter 'visible' is set
        if ('visible' not in params or
                params['visible'] is None):
            raise ValueError("Missing the required parameter `visible` when calling `trackingfield_update`")  # noqa: E501
        # verify the required parameter 'recommended_values' is set
        if ('recommended_values' not in params or
                params['recommended_values'] is None):
            raise ValueError("Missing the required parameter `recommended_values` when calling `trackingfield_update`")  # noqa: E501
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'field' in params:
            form_params.append(('field', params['field']))  # noqa: E501
        if 'required' in params:
            form_params.append(('required', params['required']))  # noqa: E501
        if 'visible' in params:
            form_params.append(('visible', params['visible']))  # noqa: E501
        if 'recommended_values' in params:
            form_params.append(('recommended_values', params['recommended_values']))  # noqa: E501
            collection_formats['recommended_values'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

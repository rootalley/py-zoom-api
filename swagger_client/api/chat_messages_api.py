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


class ChatMessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_chat_message(self, message_id, **kwargs):  # noqa: E501
        """Delete a Message  # noqa: E501

        Delete a chat message that you previously sent to a contact or a channel. In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact to whom you sent the message. Use this parameter to delete a message sent to an individual contact in Zoom. * `to_channel`: The channel ID of the channel where you sent the message. Use this parameter to delete a message sent to a channel in Zoom.  <p style=\"background-color:#e1f5fe;color:#01579b;padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chat_message(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID (required)
        :param str to_contact: The userId or email address of a chat contact to whom you previously sent the message.  Note: You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel respectively. 
        :param str to_channel: The channel Id of the channel where you would like to send the message.  You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_chat_message_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_chat_message_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def delete_chat_message_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Delete a Message  # noqa: E501

        Delete a chat message that you previously sent to a contact or a channel. In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact to whom you sent the message. Use this parameter to delete a message sent to an individual contact in Zoom. * `to_channel`: The channel ID of the channel where you sent the message. Use this parameter to delete a message sent to a channel in Zoom.  <p style=\"background-color:#e1f5fe;color:#01579b;padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chat_message_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID (required)
        :param str to_contact: The userId or email address of a chat contact to whom you previously sent the message.  Note: You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel respectively. 
        :param str to_channel: The channel Id of the channel where you would like to send the message.  You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'to_contact', 'to_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_chat_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `delete_chat_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']  # noqa: E501

        query_params = []
        if 'to_contact' in params:
            query_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            query_params.append(('to_channel', params['to_channel']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/chat/users/me/messages/{messageId}', 'DELETE',
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

    def edit_message(self, message_id, **kwargs):  # noqa: E501
        """Update a Message  # noqa: E501

        Each chat message has a unique identifier. Use this API to edit a chat message that you previously sent to either a contact or a channel in Zoom by providing the ID of the message as the value of the `messageId` parameter. The ID can be retrieved from List User's Chat Messages API. Additionally, as a query parameter, you must provide either the **email address** of the contact or the **Channel ID** of the channel where the message was sent.   <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID: Unique Identifier of the message. (required)
        :param Body12 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_message_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_message_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def edit_message_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Update a Message  # noqa: E501

        Each chat message has a unique identifier. Use this API to edit a chat message that you previously sent to either a contact or a channel in Zoom by providing the ID of the message as the value of the `messageId` parameter. The ID can be retrieved from List User's Chat Messages API. Additionally, as a query parameter, you must provide either the **email address** of the contact or the **Channel ID** of the channel where the message was sent.   <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID: Unique Identifier of the message. (required)
        :param Body12 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `edit_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'message' in params:
            form_params.append(('message', params['message']))  # noqa: E501
        if 'to_contact' in params:
            form_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            form_params.append(('to_channel', params['to_channel']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/chat/users/me/messages/{messageId}', 'PUT',
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

    def edit_message(self, message_id, **kwargs):  # noqa: E501
        """Update a Message  # noqa: E501

        Each chat message has a unique identifier. Use this API to edit a chat message that you previously sent to either a contact or a channel in Zoom by providing the ID of the message as the value of the `messageId` parameter. The ID can be retrieved from List User's Chat Messages API. Additionally, as a query parameter, you must provide either the **email address** of the contact or the **Channel ID** of the channel where the message was sent.   <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID: Unique Identifier of the message. (required)
        :param str message:
        :param str to_contact:
        :param str to_channel:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_message_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_message_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def edit_message_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Update a Message  # noqa: E501

        Each chat message has a unique identifier. Use this API to edit a chat message that you previously sent to either a contact or a channel in Zoom by providing the ID of the message as the value of the `messageId` parameter. The ID can be retrieved from List User's Chat Messages API. Additionally, as a query parameter, you must provide either the **email address** of the contact or the **Channel ID** of the channel where the message was sent.   <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`       # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_message_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Message ID: Unique Identifier of the message. (required)
        :param str message:
        :param str to_contact:
        :param str to_channel:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'message', 'to_contact', 'to_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `edit_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'message' in params:
            form_params.append(('message', params['message']))  # noqa: E501
        if 'to_contact' in params:
            form_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            form_params.append(('to_channel', params['to_channel']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth']  # noqa: E501

        return self.api_client.call_api(
            '/chat/users/me/messages/{messageId}', 'PUT',
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

    def get_chat_messages(self, user_id, **kwargs):  # noqa: E501
        """List User's Chat Messages  # noqa: E501

        A Zoom user can have conversations with other Zoom users via chat. Use this API to list the current user's chat messages between the user and an individual contact or a chat channel.<br> In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact with whom the user conversed by sending/receiving messages. * `to_channel`: The channel ID of the channel to/from which the user has sent and/or received messages. <br> **Specify a date** in the `date` query parameter to view messages from that date. If a date is not provided, the default value for the query will be the **current date**.<br> <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"><b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  <br>**Scopes:** `chat_message:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_messages(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str to_contact: The email address of a chat contact with whom the current user chatted. Messages that were sent and/or received between the user and the contact is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel. 
        :param str to_channel: The channel Id of a channel inside which current user had chat converstations. Messages that were sent and/or received between the user and the channel is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel. 
        :param date date_: The query date for which you would like to get the chat messages.
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chat_messages_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chat_messages_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_chat_messages_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List User's Chat Messages  # noqa: E501

        A Zoom user can have conversations with other Zoom users via chat. Use this API to list the current user's chat messages between the user and an individual contact or a chat channel.<br> In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact with whom the user conversed by sending/receiving messages. * `to_channel`: The channel ID of the channel to/from which the user has sent and/or received messages. <br> **Specify a date** in the `date` query parameter to view messages from that date. If a date is not provided, the default value for the query will be the **current date**.<br> <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"><b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  <br>**Scopes:** `chat_message:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_messages_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str to_contact: The email address of a chat contact with whom the current user chatted. Messages that were sent and/or received between the user and the contact is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel. 
        :param str to_channel: The channel Id of a channel inside which current user had chat converstations. Messages that were sent and/or received between the user and the channel is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel. 
        :param date date_: The query date for which you would like to get the chat messages.
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'to_contact', 'to_channel', 'date_', 'page_size', 'next_page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chat_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_chat_messages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []
        if 'to_contact' in params:
            query_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            query_params.append(('to_channel', params['to_channel']))  # noqa: E501
        if 'date_' in params:
            query_params.append(('date ', params['date_']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page_token' in params:
            query_params.append(('next_page_token', params['next_page_token']))  # noqa: E501

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
            '/chat/users/{userId}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def senda_chat_message(self, **kwargs):  # noqa: E501
        """Send a Chat Message  # noqa: E501

        Send chat messages on Zoom to either an individual user who is in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. To send a message to a contact, provide the contact's email address in the `to_contact` field. Similary, to send a message to a channel, provide the Channel Id of the Channel in `to_channel` field.<br>  <br>**Scopes:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b>  <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.senda_chat_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body10 body:
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.senda_chat_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.senda_chat_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def senda_chat_message_with_http_info(self, **kwargs):  # noqa: E501
        """Send a Chat Message  # noqa: E501

        Send chat messages on Zoom to either an individual user who is in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. To send a message to a contact, provide the contact's email address in the `to_contact` field. Similary, to send a message to a channel, provide the Channel Id of the Channel in `to_channel` field.<br>  <br>**Scopes:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b>  <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.senda_chat_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body10 body:
        :return: InlineResponse2011
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
                    " to method senda_chat_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'message' in params:
            form_params.append(('message', params['message']))  # noqa: E501
        if 'to_contact' in params:
            form_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            form_params.append(('to_channel', params['to_channel']))  # noqa: E501

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
            '/chat/users/me/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def senda_chat_message(self, **kwargs):  # noqa: E501
        """Send a Chat Message  # noqa: E501

        Send chat messages on Zoom to either an individual user who is in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. To send a message to a contact, provide the contact's email address in the `to_contact` field. Similary, to send a message to a channel, provide the Channel Id of the Channel in `to_channel` field.<br>  <br>**Scopes:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b>  <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.senda_chat_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message:
        :param str to_contact:
        :param str to_channel:
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.senda_chat_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.senda_chat_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def senda_chat_message_with_http_info(self, **kwargs):  # noqa: E501
        """Send a Chat Message  # noqa: E501

        Send chat messages on Zoom to either an individual user who is in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. To send a message to a contact, provide the contact's email address in the `to_contact` field. Similary, to send a message to a channel, provide the Channel Id of the Channel in `to_channel` field.<br>  <br>**Scopes:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b>  <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.senda_chat_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message:
        :param str to_contact:
        :param str to_channel:
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message', 'to_contact', 'to_channel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method senda_chat_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'message' in params:
            form_params.append(('message', params['message']))  # noqa: E501
        if 'to_contact' in params:
            form_params.append(('to_contact', params['to_contact']))  # noqa: E501
        if 'to_channel' in params:
            form_params.append(('to_channel', params['to_channel']))  # noqa: E501

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
            '/chat/users/me/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

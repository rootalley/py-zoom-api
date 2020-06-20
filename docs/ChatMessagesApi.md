# swagger_client.ChatMessagesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_chat_message**](ChatMessagesApi.md#delete_chat_message) | **DELETE** /chat/users/me/messages/{messageId} | Delete a Message
[**edit_message**](ChatMessagesApi.md#edit_message) | **PUT** /chat/users/me/messages/{messageId} | Update a Message
[**get_chat_messages**](ChatMessagesApi.md#get_chat_messages) | **GET** /chat/users/{userId}/messages | List User&#x27;s Chat Messages
[**senda_chat_message**](ChatMessagesApi.md#senda_chat_message) | **POST** /chat/users/me/messages | Send a Chat Message

# **delete_chat_message**
> delete_chat_message(message_id, to_contact=to_contact, to_channel=to_channel)

Delete a Message

Delete a chat message that you previously sent to a contact or a channel. In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact to whom you sent the message. Use this parameter to delete a message sent to an individual contact in Zoom. * `to_channel`: The channel ID of the channel where you sent the message. Use this parameter to delete a message sent to a channel in Zoom.  <p style=\"background-color:#e1f5fe;color:#01579b;padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatMessagesApi(swagger_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Message ID
to_contact = 'to_contact_example' # str | The userId or email address of a chat contact to whom you previously sent the message.  Note: You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel respectively.  (optional)
to_channel = 'to_channel_example' # str | The channel Id of the channel where you would like to send the message.  You must provide either `to_contact` or `to_channel` as a query parameter to delete a message that was previously sent to either an individual or a chat channel  (optional)

try:
    # Delete a Message
    api_instance.delete_chat_message(message_id, to_contact=to_contact, to_channel=to_channel)
except ApiException as e:
    print("Exception when calling ChatMessagesApi->delete_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID | 
 **to_contact** | **str**| The userId or email address of a chat contact to whom you previously sent the message.  Note: You must provide either &#x60;to_contact&#x60; or &#x60;to_channel&#x60; as a query parameter to delete a message that was previously sent to either an individual or a chat channel respectively.  | [optional] 
 **to_channel** | **str**| The channel Id of the channel where you would like to send the message.  You must provide either &#x60;to_contact&#x60; or &#x60;to_channel&#x60; as a query parameter to delete a message that was previously sent to either an individual or a chat channel  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_message**
> edit_message(message_id, body=body)

Update a Message

Each chat message has a unique identifier. Use this API to edit a chat message that you previously sent to either a contact or a channel in Zoom by providing the ID of the message as the value of the `messageId` parameter. The ID can be retrieved from List User's Chat Messages API. Additionally, as a query parameter, you must provide either the **email address** of the contact or the **Channel ID** of the channel where the message was sent.   <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope:** `chat_message:write` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`     

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatMessagesApi(swagger_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Message ID: Unique Identifier of the message.
body = swagger_client.Body12() # Body12 |  (optional)

try:
    # Update a Message
    api_instance.edit_message(message_id, body=body)
except ApiException as e:
    print("Exception when calling ChatMessagesApi->edit_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Message ID: Unique Identifier of the message. | 
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_messages**
> InlineResponse2006 get_chat_messages(user_id, to_contact=to_contact, to_channel=to_channel, date_=date_, page_size=page_size, next_page_token=next_page_token)

List User's Chat Messages

A Zoom user can have conversations with other Zoom users via chat. Use this API to list the current user's chat messages between the user and an individual contact or a chat channel.<br> In the query parameter, you must provide either of the following:<br> * `to_contact`: The email address of the contact with whom the user conversed by sending/receiving messages. * `to_channel`: The channel ID of the channel to/from which the user has sent and/or received messages. <br> **Specify a date** in the `date` query parameter to view messages from that date. If a date is not provided, the default value for the query will be the **current date**.<br> <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"><b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  <br>**Scopes:** `chat_message:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatMessagesApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
to_contact = 'to_contact_example' # str | The email address of a chat contact with whom the current user chatted. Messages that were sent and/or received between the user and the contact is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel.  (optional)
to_channel = 'to_channel_example' # str | The channel Id of a channel inside which current user had chat converstations. Messages that were sent and/or received between the user and the channel is displayed.  Note: You must provide either `contact` or `channel` as a query parameter to retrieve messages either from an individual or a chat channel.  (optional)
date_ = '2013-10-20' # date | The query date for which you would like to get the chat messages. (optional)
page_size = 10 # int | The number of records returned with a single API call.  (optional) (default to 10)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List User's Chat Messages
    api_response = api_instance.get_chat_messages(user_id, to_contact=to_contact, to_channel=to_channel, date_=date_, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatMessagesApi->get_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **to_contact** | **str**| The email address of a chat contact with whom the current user chatted. Messages that were sent and/or received between the user and the contact is displayed.  Note: You must provide either &#x60;contact&#x60; or &#x60;channel&#x60; as a query parameter to retrieve messages either from an individual or a chat channel.  | [optional] 
 **to_channel** | **str**| The channel Id of a channel inside which current user had chat converstations. Messages that were sent and/or received between the user and the channel is displayed.  Note: You must provide either &#x60;contact&#x60; or &#x60;channel&#x60; as a query parameter to retrieve messages either from an individual or a chat channel.  | [optional] 
 **date_** | **date**| The query date for which you would like to get the chat messages. | [optional] 
 **page_size** | **int**| The number of records returned with a single API call.  | [optional] [default to 10]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **senda_chat_message**
> InlineResponse2011 senda_chat_message(body=body)

Send a Chat Message

Send chat messages on Zoom to either an individual user who is in your contact list or to a [channel](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) of which you are a member. To send a message to a contact, provide the contact's email address in the `to_contact` field. Similary, to send a message to a channel, provide the Channel Id of the Channel in `to_channel` field.<br>  <br>**Scopes:** `chat_message:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b>  <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatMessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body10() # Body10 |  (optional)

try:
    # Send a Chat Message
    api_response = api_instance.senda_chat_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatMessagesApi->senda_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.IMChatApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**im_chat_messages**](IMChatApi.md#im_chat_messages) | **GET** /im/chat/sessions/{sessionId} | Retrieve IM Chat Messages
[**im_chat_sessions**](IMChatApi.md#im_chat_sessions) | **GET** /im/chat/sessions | Get IM Chat Sessions
[**listimmessages**](IMChatApi.md#listimmessages) | **GET** /im/users/{userId}/chat/messages | Get User’s IM Messages
[**sendimmessages**](IMChatApi.md#sendimmessages) | **POST** /im/users/me/chat/messages | Send IM messages

# **im_chat_messages**
> InlineResponse20021 im_chat_messages(session_id, _from, to, page_size=page_size, next_page_token=next_page_token)

Retrieve IM Chat Messages

Retrieve IM chat messages for a specified period of time. <aside>Note: This API only supports oauth2.</aside><br><br>  **Scopes:** `imchat:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

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
api_instance = swagger_client.IMChatApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | IM chat session ID.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Retrieve IM Chat Messages
    api_response = api_instance.im_chat_messages(session_id, _from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMChatApi->im_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| IM chat session ID. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_chat_sessions**
> InlineResponse20020 im_chat_sessions(_from, to, page_size=page_size, next_page_token=next_page_token)

Get IM Chat Sessions

Retrieve IM Chat sessions for a specified period of time. <aside>Note: This API only supports Oauth2.</aside><br>    **Scopes:** `imchat:read, imchat:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = swagger_client.IMChatApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get IM Chat Sessions
    api_response = api_instance.im_chat_sessions(_from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMChatApi->im_chat_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listimmessages**
> InlineResponse20060 listimmessages(user_id, chat_user=chat_user, channel=channel, _date=_date, page_size=page_size, next_page_token=next_page_token)

Get User’s IM Messages

Get IM Chat messages for a specified period of time. <aside>Note: This API only supports Oauth2.</aside><br><br> **Scopes:** `imchat:read`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>   

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
api_instance = swagger_client.IMChatApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address.
chat_user = 'chat_user_example' # str | Chat user's ID or email address. (optional)
channel = 'channel_example' # str | IM Channel's ID. (optional)
_date = '_date_example' # str | IM message's query date time, format as yyyy-MM-dd. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get User’s IM Messages
    api_response = api_instance.listimmessages(user_id, chat_user=chat_user, channel=channel, _date=_date, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMChatApi->listimmessages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address. | 
 **chat_user** | **str**| Chat user&#x27;s ID or email address. | [optional] 
 **channel** | **str**| IM Channel&#x27;s ID. | [optional] 
 **_date** | **str**| IM message&#x27;s query date time, format as yyyy-MM-dd. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendimmessages**
> InlineResponse20122 sendimmessages(body=body, chat_user=chat_user)

Send IM messages

Send chat message to a user. <aside>Note: This API only supports OAuth 2.0.</aside><br><br>**Scope:** `imchat:write`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.IMChatApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body117() # Body117 |  (optional)
chat_user = 'chat_user_example' # str | The email address (registered with Zoom) or the userId of the chat user. (optional)

try:
    # Send IM messages
    api_response = api_instance.sendimmessages(body=body, chat_user=chat_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMChatApi->sendimmessages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body117**](Body117.md)|  | [optional] 
 **chat_user** | **str**| The email address (registered with Zoom) or the userId of the chat user. | [optional] 

### Return type

[**InlineResponse20122**](InlineResponse20122.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


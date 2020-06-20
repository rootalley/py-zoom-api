# swagger_client.ChatbotMessagesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_a_chatbot_message**](ChatbotMessagesApi.md#delete_a_chatbot_message) | **DELETE** /im/chat/messages/{message_id} | Delete a Chatbot Message
[**edit_chatbot_message**](ChatbotMessagesApi.md#edit_chatbot_message) | **PUT** /im/chat/messages/{message_id} | Edit a Chatbot Message
[**sendchatbot**](ChatbotMessagesApi.md#sendchatbot) | **POST** /im/chat/messages | Send Chatbot Messages

# **delete_a_chatbot_message**
> InlineResponse20058 delete_a_chatbot_message(message_id, body=body)

Delete a Chatbot Message

Delete a message that was sent by your chatbot app.<br><br> **Scopes:** `imchat:bot`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>**Authorization Flow**: Client Credentials Flow<br><br>To get authorized, make a POST request to `/oauth/token` endpoint with grant type as `client_credentials`. <br>Use `https://api.zoom.us/oauth/token?grant_type=client_credentials` as the endpoint for the request.  You will need to send your ClientID and Secret as a Basic base64 encoded AUthorization header. Ex. `Basic base64Encode({client_id}:{client_sceret})`<br><br> Next, use the token received (access_token) as a bearer token while making the DELETE /im/chat/messages/{message_id} request to delete a message.<br><br> Learn more about how to authotize chatbots in the [Chatbot Authorization](https://marketplace.zoom.us/docs/guides/chatbots/authorization) guide.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatbotMessagesApi(swagger_client.ApiClient(configuration))
message_id = 'message_id_example' # str | 
body = swagger_client.Body111() # Body111 |  (optional)

try:
    # Delete a Chatbot Message
    api_response = api_instance.delete_a_chatbot_message(message_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatbotMessagesApi->delete_a_chatbot_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 
 **body** | [**Body111**](Body111.md)|  | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_chatbot_message**
> InlineResponse20057 edit_chatbot_message(message_id, body=body)

Edit a Chatbot Message

Edit a message that was [sent](https://marketplace.zoom.us/docs/api-reference/zoom-api/im-chat/sendchatbot) by your Chatbot app.<br> After sending a message using the Send Chatbot Message API, you must store the messageId returned in the response so that you can make edits to the associated message using this API.  **Scope:** `imchat:bot`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Authorization Flow**: Client Credentials Flow<br><br> To get authorized, make a POST request to `/oauth/token` endpoint with grant type as `client_credentials`. <br>Use `https://api.zoom.us/oauth/token?grant_type=client_credentials` as the endpoint for the request.  You will need to send your ClientID and Secret as a Basic base64 encoded AUthorization header. Ex. `Basic base64Encode({client_id}:{client_sceret})`<br><br> Next, use the token received (access_token) as a bearer token while making the PUT /im/chat/messages/{message_id} request to edit a chatbot message.<br><br> Learn more about how to authotize chatbots in the [Chatbot Authorization](https://marketplace.zoom.us/docs/guides/chatbots/authorization) guide.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatbotMessagesApi(swagger_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Unique Identifier of the message that needs to be updated. This should be retrieved from the response of [Send Chatbot Message API](https://marketplace.zoom.us/docs/api-reference/zoom-api/im-chat/sendchatbot).
body = swagger_client.Body109() # Body109 |  (optional)

try:
    # Edit a Chatbot Message
    api_response = api_instance.edit_chatbot_message(message_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatbotMessagesApi->edit_chatbot_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique Identifier of the message that needs to be updated. This should be retrieved from the response of [Send Chatbot Message API](https://marketplace.zoom.us/docs/api-reference/zoom-api/im-chat/sendchatbot). | 
 **body** | [**Body109**](Body109.md)|  | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendchatbot**
> sendchatbot(body=body)

Send Chatbot Messages

Send chatbot messages from your marketplace chatbot app.<br><br> **Scopes:** `imchat:bot`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Authorization Flow**: Client Credentials Flow<br><br> To get authorized, make a POST request to `/oauth/token` endpoint with grant type as `client_credentials`. <br>Use `https://api.zoom.us/oauth/token?grant_type=client_credentials` as the endpoint for the request.  You will need to send your ClientID and Secret as a Basic base64 encoded AUthorization header. Ex. `Basic base64Encode({client_id}:{client_sceret})`<br><br> Next, use the token recieved (access_token) as a bearer token while making the POST /im/chat/messages request to send chatbot messages.<br><br> Learn more about how to authorize chatbots in the [Chatbot Authorization](https://marketplace.zoom.us/docs/guides/chatbots/authorization) guide.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChatbotMessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body107() # Body107 |  (optional)

try:
    # Send Chatbot Messages
    api_instance.sendchatbot(body=body)
except ApiException as e:
    print("Exception when calling ChatbotMessagesApi->sendchatbot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body107**](Body107.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


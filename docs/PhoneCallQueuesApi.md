# swagger_client.PhoneCallQueuesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_call_queue**](PhoneCallQueuesApi.md#add_members_to_call_queue) | **POST** /phone/call_queues/{callQueueId}/members | Add Members to a Call Queue
[**assign_phone_to_call_queue**](PhoneCallQueuesApi.md#assign_phone_to_call_queue) | **POST** /phone/call_queues/{callQueueId}/phone_numbers | Assign Numbers to a Call Queue
[**change_call_queue_manager**](PhoneCallQueuesApi.md#change_call_queue_manager) | **PUT** /phone/call_queues/{callQueueId}/manager | Change Call Queue Manager
[**create_call_queue**](PhoneCallQueuesApi.md#create_call_queue) | **POST** /phone/call_queues | Create a Call Queue
[**delete_a_call_queue**](PhoneCallQueuesApi.md#delete_a_call_queue) | **DELETE** /phone/call_queues/{callQueueId} | Delete a Call Queue
[**get_a_call_queue**](PhoneCallQueuesApi.md#get_a_call_queue) | **GET** /phone/call_queues/{callQueueId} | Get Call Queue Details
[**get_call_queue_recordings**](PhoneCallQueuesApi.md#get_call_queue_recordings) | **GET** /phone/call_queues/{callQueueId}/recordings | Get Call Queue Recordings
[**list_call_queues**](PhoneCallQueuesApi.md#list_call_queues) | **GET** /phone/call_queues | List Call Queues
[**un_assign_phone_num_call_queue**](PhoneCallQueuesApi.md#un_assign_phone_num_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/phone_numbers/{phoneNumberId} | Unassign a Phone Number
[**unassign_a_phone_num_call_queue**](PhoneCallQueuesApi.md#unassign_a_phone_num_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/phone_numbers | Unassign all Phone Numbers
[**unassign_all_members**](PhoneCallQueuesApi.md#unassign_all_members) | **DELETE** /phone/call_queues/{callQueueId}/members | Unassign all Members
[**unassign_member_from_call_queue**](PhoneCallQueuesApi.md#unassign_member_from_call_queue) | **DELETE** /phone/call_queues/{callQueueId}/members/{memberId} | Unassign a Member
[**update_call_queue**](PhoneCallQueuesApi.md#update_call_queue) | **PATCH** /phone/call_queues/{callQueueId} | Update Call Queue Details

# **add_members_to_call_queue**
> object add_members_to_call_queue(call_queue_id, body=body)

Add Members to a Call Queue

Add phone users and/or [common area phones](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) as members to a specific Call Queue.<br><br> **Prerequisites:**<br> * Pro or higher account plan. * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue.
body = swagger_client.Body167() # Body167 |  (optional)

try:
    # Add Members to a Call Queue
    api_response = api_instance.add_members_to_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->add_members_to_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. | 
 **body** | [**Body167**](Body167.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_to_call_queue**
> object assign_phone_to_call_queue(call_queue_id, body=body)

Assign Numbers to a Call Queue

After [buying phone number(s)](https://support.zoom.us/hc/en-us/articles/360020808292#h_007ec8c2-0914-4265-8351-96ab23efa3ad), you can assign it, allowing callers to directly dial a number to reach a [call queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues).<br><br> **Prerequisites:**<br> * Pro or higher account plan. * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue.
body = swagger_client.Body165() # Body165 |  (optional)

try:
    # Assign Numbers to a Call Queue
    api_response = api_instance.assign_phone_to_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->assign_phone_to_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. | 
 **body** | [**Body165**](Body165.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_call_queue_manager**
> object change_call_queue_manager(call_queue_id, body=body)

Change Call Queue Manager

A call queue manager has the privileges to maanage the call queue's voicemail inbox and recordings, change all call queue settings and call queue policy settings.<br><br> Use this API to to set another phone user as the [call queue manager](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues#h_db06854b-e6a3-4afe-ba15-baf58f31f90c). **Prerequisites:**<br> * Pro or higher account plan. * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue.
body = swagger_client.Body169() # Body169 |  (optional)

try:
    # Change Call Queue Manager
    api_response = api_instance.change_call_queue_manager(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->change_call_queue_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. | 
 **body** | [**Body169**](Body169.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_call_queue**
> InlineResponse20123 create_call_queue(body=body)

Create a Call Queue

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.<br> Use this API to [create a call queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues#h_e81faeeb-9184-429a-aaea-df49ff5ff413).<br> You can add phone users or common area phones to call queues.  **Prerequisites:**<br> * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body161() # Body161 |  (optional)

try:
    # Create a Call Queue
    api_response = api_instance.create_call_queue(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->create_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body161**](Body161.md)|  | [optional] 

### Return type

[**InlineResponse20123**](InlineResponse20123.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_call_queue**
> object delete_a_call_queue(call_queue_id)

Delete a Call Queue

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.<br> Use this API to delete a Call Queue.<br>  **Prerequisites:**<br> * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the call queue.

try:
    # Delete a Call Queue
    api_response = api_instance.delete_a_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->delete_a_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the call queue. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_call_queue**
> InlineResponse20091 get_a_call_queue(call_queue_id)

Get Call Queue Details

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.<br> Use this API to get information on a specific Call Queue.<br><br>  **Prerequisites:**<br> * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue. This can be retrieved from [List Call Queues API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-call-queues/listcallqueues).

try:
    # Get Call Queue Details
    api_response = api_instance.get_a_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->get_a_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. This can be retrieved from [List Call Queues API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-call-queues/listcallqueues). | 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_queue_recordings**
> InlineResponse200100 get_call_queue_recordings(call_queue_id, page_size=page_size, next_page_token=next_page_token)

Get Call Queue Recordings

Use this API to view [call recordings](https://support.zoom.us/hc/en-us/articles/360038521091#h_cbc9f2a3-e06c-4daa-83d4-ddbceef9c77b) from the call queue.<br><br> **Prerequisites:**<br> * Pro or higher account with Zoom Phone license. * [Automatic call recordings](https://support.zoom.us/hc/en-us/articles/360033511872#h_fcb297bb-14e8-4094-91ca-dc61e1a18734) must be enabled in the Policy Settings for call queues. <br> **Scope:** `phone:read:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`    

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Call Queue Recordings
    api_response = api_instance.get_call_queue_recordings(call_queue_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->get_call_queue_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_queues**
> InlineResponse20090 list_call_queues(next_page_token=next_page_token, page_size=page_size)

List Call Queues

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.<br> Use this API to list Call queues.<br><br> **Prerequisites:**<br> * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned from a single API call. (optional) (default to 30)

try:
    # List Call Queues
    api_response = api_instance.list_call_queues(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->list_call_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned from a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_assign_phone_num_call_queue**
> object un_assign_phone_num_call_queue(call_queue_id, phone_number_id)

Unassign a Phone Number

After assigning a phone number, you can unbind it if you don't want it to be assigned to a [Call Queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues). Use this API to unbind a phone number from a Call Queue. After successful unbinding, the number will appear in the [Unassigned tab](https://zoom.us/signin#/numbers/unassigned).<br><br> **Prerequisites:** * Pro or higher account palan * Account owner or admin permissions * Zoom Phone license <br> **Scopes:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue. This can be retrieved from the List Call Queues API.
phone_number_id = 'phone_number_id_example' # str | Unique Identifier of the Phone Number. 

try:
    # Unassign a Phone Number
    api_response = api_instance.un_assign_phone_num_call_queue(call_queue_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->un_assign_phone_num_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. This can be retrieved from the List Call Queues API. | 
 **phone_number_id** | **str**| Unique Identifier of the Phone Number.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_a_phone_num_call_queue**
> object unassign_a_phone_num_call_queue(call_queue_id)

Unassign all Phone Numbers

Use this API to unbind all phone numbers that are assigned to a [Call Queue](https://support.zoom.us/hc/en-us/articles/360021524831-Managing-Call-Queues) After successful unbinding, the numbers will appear in the [Unassigned tab](https://zoom.us/signin#/numbers/unassigned).<br> If you only need to unassign a specific phone number, use the Unassign a Phone Number API instead. <br> **Prerequisites:** * Pro or higher account palan * Account owner or admin permissions * Zoom Phone license <br> **Scopes:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue. This can be retrieved from List Call Queues API.

try:
    # Unassign all Phone Numbers
    api_response = api_instance.unassign_a_phone_num_call_queue(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->unassign_a_phone_num_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. This can be retrieved from List Call Queues API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_all_members**
> object unassign_all_members(call_queue_id)

Unassign all Members

Use this API to remove all members from a Call Queue who were previously assigned to that Call Queue. The members could be phone users or [common area phones](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones). **Prerequisites:**<br> * Pro or higher account plan. * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | 

try:
    # Unassign all Members
    api_response = api_instance.unassign_all_members(call_queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->unassign_all_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_member_from_call_queue**
> object unassign_member_from_call_queue(call_queue_id, member_id)

Unassign a Member

Use this API to remove a member from a Call Queue who was previously added to that Call Queue. The member could be a phone user or a [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones). A member who is a Call Queue Manager cannot be unassigned from the Call Queue using this API.  **Prerequisites:**<br> * Pro or higher account plan. * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue from which the member needs to be unassigned.
member_id = 'member_id_example' # str | Unique Identifier of the member who needs to be unassigned.

try:
    # Unassign a Member
    api_response = api_instance.unassign_member_from_call_queue(call_queue_id, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->unassign_member_from_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue from which the member needs to be unassigned. | 
 **member_id** | **str**| Unique Identifier of the member who needs to be unassigned. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_queue**
> object update_call_queue(call_queue_id, body=body)

Update Call Queue Details

Call queues allow you to route incoming calls to a group of users. For instance, you can use call queues to route calls to various departments in your organization such as sales, engineering, billing, customer service etc.<br> Use this API to update information of a specific Call Queue.<br>  **Prerequisites:**<br> * Pro, Business, or Education account * Account owner or admin permissions * Zoom Phone license<br> **Scopes:** `phone:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.PhoneCallQueuesApi(swagger_client.ApiClient(configuration))
call_queue_id = 'call_queue_id_example' # str | Unique Identifier of the Call Queue.
body = swagger_client.Body163() # Body163 |  (optional)

try:
    # Update Call Queue Details
    api_response = api_instance.update_call_queue(call_queue_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneCallQueuesApi->update_call_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_queue_id** | **str**| Unique Identifier of the Call Queue. | 
 **body** | [**Body163**](Body163.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


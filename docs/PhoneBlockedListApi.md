# swagger_client.PhoneBlockedListApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_anumber_to_blocked_list**](PhoneBlockedListApi.md#add_anumber_to_blocked_list) | **POST** /phone/blocked_list | Create a Blocked List
[**delete_a_blocked_list**](PhoneBlockedListApi.md#delete_a_blocked_list) | **DELETE** /phone/blocked_list/{blockedListId} | Delete a Blocked List
[**get_a_blocked_list**](PhoneBlockedListApi.md#get_a_blocked_list) | **GET** /phone/blocked_list/{blockedListId} | Get Blocked List Details
[**list_blocked_list**](PhoneBlockedListApi.md#list_blocked_list) | **GET** /phone/blocked_list | List Blocked Lists
[**update_blocked_list**](PhoneBlockedListApi.md#update_blocked_list) | **PATCH** /phone/blocked_list/{blockedListId} | Update a Blocked List

# **add_anumber_to_blocked_list**
> InlineResponse20125 add_anumber_to_blocked_list(body=body)

Create a Blocked List

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available.<br>Use this API to create a blocked list and add a number to that blocked list.<br> **Prerequisites:** * Pro or higher account plan with Zoom phone license<br> **Scope:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneBlockedListApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body180() # Body180 |  (optional)

try:
    # Create a Blocked List
    api_response = api_instance.add_anumber_to_blocked_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneBlockedListApi->add_anumber_to_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body180**](Body180.md)|  | [optional] 

### Return type

[**InlineResponse20125**](InlineResponse20125.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_blocked_list**
> object delete_a_blocked_list(blocked_list_id)

Delete a Blocked List

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). <br>Use this API to delete a blocked list and therefore removing the associated number from the blocked list. The number will be unblocked after the deletion.<br> **Prerequisites:** * Pro or higher account plan with Zoom phone license<br> **Scope:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneBlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique Identifier of the blocked list. This can be retrieved from the List Blocked List API.

try:
    # Delete a Blocked List
    api_response = api_instance.delete_a_blocked_list(blocked_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneBlockedListApi->delete_a_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique Identifier of the blocked list. This can be retrieved from the List Blocked List API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_blocked_list**
> InlineResponse20098 get_a_blocked_list(blocked_list_id)

Get Blocked List Details

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available.<br>Use this API to get information about a specific blocked list.<br> **Prerequisites:** * Pro or higher account plan with Zoom phone license<br> **Scope:** `phone:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneBlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique Identifier of the blocked list.

try:
    # Get Blocked List Details
    api_response = api_instance.get_a_blocked_list(blocked_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneBlockedListApi->get_a_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique Identifier of the blocked list. | 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocked_list**
> InlineResponse20097 list_blocked_list(next_page_token=next_page_token, page_size=page_size)

List Blocked Lists

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available.<br>Use this API to list all the blocked lists in an acccount.<br> **Prerequisites:** * Pro or higher account plan with Zoom phone license<br> **Scope:** `phone:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.PhoneBlockedListApi(swagger_client.ApiClient(configuration))
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)

try:
    # List Blocked Lists
    api_response = api_instance.list_blocked_list(next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneBlockedListApi->list_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blocked_list**
> object update_blocked_list(blocked_list_id, body=body)

Update a Blocked List

A Zoom account owner or a user with admin privilege can block phone numbers for phone users in an account. Blocked numbers can be inbound (numbers will be blocked from calling in) and outbound (phone users in your account won't be able to dial those numbers). Blocked callers will hear a generic message stating that the person they are calling is not available.<br>Use this API to update information on the blocked list.<br> **Prerequisites:** * Pro or higher account plan with Zoom phone license<br> **Scope:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneBlockedListApi(swagger_client.ApiClient(configuration))
blocked_list_id = 'blocked_list_id_example' # str | Unique Identifier for the blocked list.
body = swagger_client.Body182() # Body182 |  (optional)

try:
    # Update a Blocked List
    api_response = api_instance.update_blocked_list(blocked_list_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneBlockedListApi->update_blocked_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_list_id** | **str**| Unique Identifier for the blocked list. | 
 **body** | [**Body182**](Body182.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


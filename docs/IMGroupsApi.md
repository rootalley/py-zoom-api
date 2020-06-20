# swagger_client.IMGroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**im_group**](IMGroupsApi.md#im_group) | **GET** /im/groups/{groupId} | Retrieve an IM Directory Group
[**im_group_create**](IMGroupsApi.md#im_group_create) | **POST** /im/groups | Create an IM Directory Group
[**im_group_delete**](IMGroupsApi.md#im_group_delete) | **DELETE** /im/groups/{groupId} | Delete an IM Directory Group
[**im_group_members**](IMGroupsApi.md#im_group_members) | **GET** /im/groups/{groupId}/members | List IM Directory Group Members
[**im_group_members_create**](IMGroupsApi.md#im_group_members_create) | **POST** /im/groups/{groupId}/members | Add IM Directory Group Members
[**im_group_members_delete**](IMGroupsApi.md#im_group_members_delete) | **DELETE** /im/groups/{groupId}/members/{memberId} | Delete an IM Directory Group Member
[**im_group_update**](IMGroupsApi.md#im_group_update) | **PATCH** /im/groups/{groupId} | Update an IM Directory Group
[**im_groups**](IMGroupsApi.md#im_groups) | **GET** /im/groups | List IM Directory Groups

# **im_group**
> InlineResponse20019 im_group(group_id)

Retrieve an IM Directory Group

Retrieve an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.<br><br> Scopes: `imgroup:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Retrieve an IM Directory Group
    api_response = api_instance.im_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_create**
> im_group_create(body)

Create an IM Directory Group

Create an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.<br><br> **Scopes**: `imgroup:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body40() # Body40 | 

try:
    # Create an IM Directory Group
    api_instance.im_group_create(body)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body40**](Body40.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml, new

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_delete**
> im_group_delete(group_id)

Delete an IM Directory Group

Delete an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.<br><br> Scopes: `imgroup:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Delete an IM Directory Group
    api_instance.im_group_delete(group_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_members**
> GroupMemberList im_group_members(group_id, page_size=page_size, page_number=page_number)

List IM Directory Group Members

List the members of an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).<br><br> **Scope:** `imgroup:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List IM Directory Group Members
    api_response = api_instance.im_group_members(group_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**GroupMemberList**](GroupMemberList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_members_create**
> im_group_members_create(body, group_id)

Add IM Directory Group Members

Add members to an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.<br><br> **Scope:** `imgroup:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body44() # Body44 | 
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Add IM Directory Group Members
    api_instance.im_group_members_create(body, group_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body44**](Body44.md)|  | 
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_members_delete**
> im_group_members_delete(group_id, member_id)

Delete an IM Directory Group Member

Delete a member from an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under an account.<br><br> Scopes: `imgroup:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).
member_id = 'member_id_example' # str | The member ID.

try:
    # Delete an IM Directory Group Member
    api_instance.im_group_members_delete(group_id, member_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 
 **member_id** | **str**| The member ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_group_update**
> im_group_update(body, group_id)

Update an IM Directory Group

Update an [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) under your account.<br><br> **Scopes**: `imgroup:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body42() # Body42 | 
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Update an IM Directory Group
    api_instance.im_group_update(body, group_id)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body42**](Body42.md)|  | 
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **im_groups**
> IMGroupList im_groups()

List IM Directory Groups

List [IM directory groups](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management).<br><br> **Scopes**: `imgroup:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.IMGroupsApi(swagger_client.ApiClient(configuration))

try:
    # List IM Directory Groups
    api_response = api_instance.im_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IMGroupsApi->im_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IMGroupList**](IMGroupList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


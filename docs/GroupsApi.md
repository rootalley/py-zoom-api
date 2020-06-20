# swagger_client.GroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_lock_settings**](GroupsApi.md#get_group_lock_settings) | **GET** /groups/{groupId}/lock_settings | Get Locked Settings
[**get_group_settings**](GroupsApi.md#get_group_settings) | **GET** /groups/{groupId}/settings | Get a Group&#x27;s Settings
[**group**](GroupsApi.md#group) | **GET** /groups/{groupId} | Get a Group
[**group_create**](GroupsApi.md#group_create) | **POST** /groups | Create a Group
[**group_delete**](GroupsApi.md#group_delete) | **DELETE** /groups/{groupId} | Delete a Group
[**group_locked_settings**](GroupsApi.md#group_locked_settings) | **PATCH** /groups/{groupId}/lock_settings | Update Locked Settings
[**group_members**](GroupsApi.md#group_members) | **GET** /groups/{groupId}/members | List Group Members 
[**group_members_create**](GroupsApi.md#group_members_create) | **POST** /groups/{groupId}/members | Add Group Members
[**group_members_delete**](GroupsApi.md#group_members_delete) | **DELETE** /groups/{groupId}/members/{memberId} | Delete a Group Member
[**group_update**](GroupsApi.md#group_update) | **PATCH** /groups/{groupId} | Update a Group
[**groups**](GroupsApi.md#groups) | **GET** /groups | List Groups
[**update_a_group_member**](GroupsApi.md#update_a_group_member) | **PATCH** /groups/{groupId}/members/{memberId} | Update a Group Member
[**update_group_settings**](GroupsApi.md#update_group_settings) | **PATCH** /groups/{groupId}/settings | Update a Group&#x27;s Settings

# **get_group_lock_settings**
> InlineResponse20069 get_group_lock_settings(group_id)

Get Locked Settings

Retrieve a [group's](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) locked settings. If you lock a setting, the group members will not be able to modify it individually. <p style=\"background-color:#FEEFB3; color:#9F6000\"><br>Note:</b> The `force_pmi_jbh_password` field under meeting settings is planned to be deprecated on September 22, 2019. This field will be replaced by another field that will provide the same functionality.</p>  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Id of the group.

try:
    # Get Locked Settings
    api_response = api_instance.get_group_lock_settings(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_lock_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group. | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_settings**
> object get_group_settings(group_id, option=option)

Get a Group's Settings

Get settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
option = 'option_example' # str | `meeting_authentication`: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.<br>`recording_authentication`: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. (optional)

try:
    # Get a Group's Settings
    api_response = api_instance.get_group_settings(group_id, option=option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **option** | **str**| &#x60;meeting_authentication&#x60;: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.&lt;br&gt;&#x60;recording_authentication&#x60;: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group**
> InlineResponse20017 group(group_id)

Get a Group

Get a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Get a Group
    api_response = api_instance.group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create**
> group_create(body)

Create a Group

Create a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.<br> **Scopes**: `group:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body32() # Body32 | 

try:
    # Create a Group
    api_instance.group_create(body)
except ApiException as e:
    print("Exception when calling GroupsApi->group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete**
> group_delete(group_id)

Delete a Group

Delete a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Delete a Group
    api_instance.group_delete(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_delete: %s\n" % e)
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

# **group_locked_settings**
> object group_locked_settings(group_id, body=body)

Update Locked Settings

Update a [group's](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) locked settings. If you lock a setting, the group members will not be able to modify it individually. <p style=\"background-color:#FEEFB3; color:#9F6000\"><br>Note:</b> The `force_pmi_jbh_password` field under meeting settings is planned to be deprecated on September 22, 2019. This field will be replaced by another field that will provide the same functionality.</p>  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The Id of the group.
body = swagger_client.Body129() # Body129 |  (optional)

try:
    # Update Locked Settings
    api_response = api_instance.group_locked_settings(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_locked_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The Id of the group. | 
 **body** | [**Body129**](Body129.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members**
> InlineResponse20018 group_members(group_id, page_size=page_size, page_number=page_number)

List Group Members 

List the members of a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Group Members 
    api_response = api_instance.group_members(group_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members_create**
> group_members_create(body, group_id)

Add Group Members

Add members to a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body36() # Body36 | 
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Add Group Members
    api_instance.group_members_create(body, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body36**](Body36.md)|  | 
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members_delete**
> group_members_delete(group_id, member_id)

Delete a Group Member

Delete a member from a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) in a Zoom account.  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).
member_id = 'member_id_example' # str | The member ID.

try:
    # Delete a Group Member
    api_instance.group_members_delete(group_id, member_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_members_delete: %s\n" % e)
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

# **group_update**
> group_update(body, group_id)

Update a Group

Update a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro, Business, or Education account<br> **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body34() # Body34 | 
group_id = 'group_id_example' # str | The group ID.<br> Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups).

try:
    # Update a Group
    api_instance.group_update(body, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body34**](Body34.md)|  | 
 **group_id** | **str**| The group ID.&lt;br&gt; Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups). | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups**
> InlineResponse20016 groups()

List Groups

List [groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.<br> **Scopes**: `group:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))

try:
    # List Groups
    api_response = api_instance.groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_group_member**
> object update_a_group_member(group_id, member_id, body=body)

Update a Group Member

If a user is a member in multiple groups, you can [set a primary group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-#h_d07c7dcd-4fd8-485a-b5fe-a322e8d21c09) for the user. The group member will use the primary group's settings by default. However, if settings are locked in other groups, those settings will continue to be locked for that user. By default, the primary group is the first group that user is added to.<br><br> Use this API to perform either of the following tasks: * Simultaneously remove a member from one group and move the member to a different group. * Set a primary group for the user<br><br> **Prerequisites:**  * Pro or higher account<br> **Scopes:** `group:write:admin`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Unique Identifier of the group. Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups) API.<br> To change a member's primary group, provide the groupId of the member's current primary group as the value of this field.<br> To remove a member from one group and move the member to another group, provide the groupId of the group from which the member is to be moved.
member_id = 'member_id_example' # str | Unique Identifier of the group member. Can be retrieved by calling the [List Group Members](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groupmembers) API.
body = swagger_client.Body38() # Body38 |  (optional)

try:
    # Update a Group Member
    api_response = api_instance.update_a_group_member(group_id, member_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_a_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Unique Identifier of the group. Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups) API.&lt;br&gt; To change a member&#x27;s primary group, provide the groupId of the member&#x27;s current primary group as the value of this field.&lt;br&gt; To remove a member from one group and move the member to another group, provide the groupId of the group from which the member is to be moved. | 
 **member_id** | **str**| Unique Identifier of the group member. Can be retrieved by calling the [List Group Members](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groupmembers) API. | 
 **body** | [**Body38**](Body38.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_settings**
> update_group_settings(group_id, body=body, option=option)

Update a Group's Settings

Update settings for a [group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).<p style=\"background-color:#FEEFB3; color:#9F6000\"><br>Note:</b> The `force_pmi_jbh_password` field under meeting settings is planned to be deprecated on September 22, 2019. This field will be replaced by another field that will provide the same functionality.</p> **Prerequisite**: Pro, Business, or Education account<br>  **Scopes**: `group:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | Id of the group.
body = NULL # object |  (optional)
option = 'option_example' # str |  (optional)

try:
    # Update a Group's Settings
    api_instance.update_group_settings(group_id, body=body, option=option)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group. | 
 **body** | [**object**](object.md)|  | [optional] 
 **option** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.RolesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role_members**](RolesApi.md#add_role_members) | **POST** /roles/{roleId}/members | Assign a Role to Members
[**create_role**](RolesApi.md#create_role) | **POST** /roles | Create a Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /roles/{roleId} | Delete a Role
[**get_role_information**](RolesApi.md#get_role_information) | **GET** /roles/{roleId} | Get Role Information
[**role_member_delete**](RolesApi.md#role_member_delete) | **DELETE** /roles/{roleId}/members/{memberId} | Unassign a Member&#x27;s Role
[**role_members**](RolesApi.md#role_members) | **GET** /roles/{roleId}/members | List Members in a Role
[**roles**](RolesApi.md#roles) | **GET** /roles | List Roles
[**update_role**](RolesApi.md#update_role) | **PATCH** /roles/{roleId} | Update Role Information

# **add_role_members**
> InlineResponse20115 add_role_members(body, role_id)

Assign a Role to Members

User [roles](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) can have a set of permissions that allows access only to the pages a user needs to view or edit. Use this API to [assign a role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control#h_748b6fd8-5057-4cf4-bbfd-787909c09db0) to members.  **Scopes:** `role:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:**<br> * A Pro or a higher plan.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body74() # Body74 | Role members
role_id = 'role_id_example' # str | The role ID

try:
    # Assign a Role to Members
    api_response = api_instance.add_role_members(body, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->add_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body74**](Body74.md)| Role members | 
 **role_id** | **str**| The role ID | 

### Return type

[**InlineResponse20115**](InlineResponse20115.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> object create_role(body=body)

Create a Role

Each Zoom user automatically has a role which can either be owner, administrator, or a member.   **Pre-requisite:**<br> * Pro or higher plan. * For setting the initial role, you must be the Account Owner.<br> * For subsequent role management, you must be the Account Owner or user with role management permissions.<br> **Scopes:** `role:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body72() # Body72 |  (optional)

try:
    # Create a Role
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_id)

Delete a Role

Each Zoom user automatically has a role which can either be owner, administrator, or a member. Account Owners and users with edit privileges for Role management can add customized roles with a list.  Use this API to delete a role.<br> **Pre-requisite:**<br> * A Pro or higher plan.<br> * For role management and updates, you must be the Account Owner or user with role management permissions.  **Scopes:** `role:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Role Id.

try:
    # Delete a Role
    api_instance.delete_role(role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Role Id. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_information**
> InlineResponse20071 get_role_information(role_id)

Get Role Information

Each Zoom user automatically has a role which can either be owner, administrator, or a member. Account Owners and users with edit privileges for Role management can add customized roles with a list of privileges.  Use this API to get information including specific privileges assigned to a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control).<br> **Pre-requisite:**<br> * A Pro or higher plan.<br> * For role management and updates, you must be the Account Owner or user with role management permissions.  **Scopes:** `role:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Role Id. 

try:
    # Get Role Information
    api_response = api_instance.get_role_information(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Role Id.  | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_member_delete**
> role_member_delete(role_id, member_id)

Unassign a Member's Role

User [roles](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) can have a set of permissions that allows access only to the pages a user needs to view or edit. Use this API to unassign a user's role.  **Scope:** `role:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * A Pro or a higher plan.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | The role ID
member_id = 'member_id_example' # str | Member's ID

try:
    # Unassign a Member's Role
    api_instance.role_member_delete(role_id, member_id)
except ApiException as e:
    print("Exception when calling RolesApi->role_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The role ID | 
 **member_id** | **str**| Member&#x27;s ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_members**
> RoleMembersList role_members(role_id)

List Members in a Role

User [roles](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) can have a set of permissions that allows access only to the pages a user needs to view or edit. Use this API to list all the members that are assigned a specific role.  **Scope:** `role:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>**Prerequisites:**<br> * A Pro or a higher plan.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | The role ID

try:
    # List Members in a Role
    api_response = api_instance.role_members(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The role ID | 

### Return type

[**RoleMembersList**](RoleMembersList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles**
> object roles()

List Roles

List [roles](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) on your account  **Scopes:** `role:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites** : *  Pro or higher plan.  *  For setting the initial role, you must be the Account Owner.  *  For subsequent role management, you must be the Account Owner or user with role management permissions.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))

try:
    # List Roles
    api_response = api_instance.roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> object update_role(role_id, body=body)

Update Role Information

Each Zoom user automatically has a [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) which can either be owner, administrator, or a member. Account Owners and users with edit privileges for Role management can add customized roles with a list.  Use this API to change the privileges, name and description of a specific role.<br> **Pre-requisite:**<br> * A Pro or higher plan.<br> * For role management and updates, you must be the Account Owner or user with role management permissions.<br>**Scopes:** `role:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role_id = 'role_id_example' # str | Role Id
body = swagger_client.Body133() # Body133 |  (optional)

try:
    # Update Role Information
    api_response = api_instance.update_role(role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Role Id | 
 **body** | [**Body133**](Body133.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


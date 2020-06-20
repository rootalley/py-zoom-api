# swagger_client.PhoneSharedLineGroupsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_shared_line_group**](PhoneSharedLineGroupsApi.md#add_members_to_shared_line_group) | **POST** /phone/shared_line_groups/{sharedLineGroupId}/members | Add Members to a Shared Line Group
[**assign_phone_numbers_slg**](PhoneSharedLineGroupsApi.md#assign_phone_numbers_slg) | **POST** /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers | Assign Phone Numbers
[**delete_a_member_slg**](PhoneSharedLineGroupsApi.md#delete_a_member_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/members/{memberId} | Unassign a Member From a Shared Line Group
[**delete_a_phone_number_slg**](PhoneSharedLineGroupsApi.md#delete_a_phone_number_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers/{phoneNumberId} | Unassign a Phone Number
[**delete_a_shared_line_group**](PhoneSharedLineGroupsApi.md#delete_a_shared_line_group) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId} | Delete a Shared Line Group
[**delete_members_of_slg**](PhoneSharedLineGroupsApi.md#delete_members_of_slg) | **DELETE** /phone/shared_line_groups/{sharedLineGroupId}/members | Unassign Members of a Shared Line Group
[**get_a_shared_line_group**](PhoneSharedLineGroupsApi.md#get_a_shared_line_group) | **GET** /phone/shared_line_groups/{sharedLineGroupId} | Get a Shared Line Group
[**update_a_shared_line_group**](PhoneSharedLineGroupsApi.md#update_a_shared_line_group) | **PATCH** /phone/shared_line_groups/{sharedLineGroupId} | Update a Shared Line Group

# **add_members_to_shared_line_group**
> object add_members_to_shared_line_group(shared_line_group_id, body=body)

Add Members to a Shared Line Group

A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common area phones. This gives members of the shared line group access to the group's direct phone number and voicemail. Use this API to [add members](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups#h_7cb42370-48f6-4a8f-84f4-c6eee4d9f0ca) to a Shared Line Group. Note that a member can only be added to one shared line group.   **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique Identifier of the shared line group.
body = swagger_client.Body186() # Body186 |  (optional)

try:
    # Add Members to a Shared Line Group
    api_response = api_instance.add_members_to_shared_line_group(shared_line_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->add_members_to_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique Identifier of the shared line group. | 
 **body** | [**Body186**](Body186.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_slg**
> assign_phone_numbers_slg(shared_line_group_id, body=body)

Assign Phone Numbers

Use this API to assign phone numbers to a shared line groups. These direct phone numbers will be shared among members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups). **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique Identifier of the Shared Line Group.
body = swagger_client.Body188() # Body188 |  (optional)

try:
    # Assign Phone Numbers
    api_instance.assign_phone_numbers_slg(shared_line_group_id, body=body)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->assign_phone_numbers_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique Identifier of the Shared Line Group. | 
 **body** | [**Body188**](Body188.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_member_slg**
> delete_a_member_slg(shared_line_group_id, member_id)

Unassign a Member From a Shared Line Group

Members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) have access to the group's phone number and voicemail. Use this API to unassign **a specific member** from a Shared Line Group. **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique Identifier of the shared line group from which you would like to remove a member.
member_id = 'member_id_example' # str | Unique identifier of the member who is to be removed.

try:
    # Unassign a Member From a Shared Line Group
    api_instance.delete_a_member_slg(shared_line_group_id, member_id)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->delete_a_member_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique Identifier of the shared line group from which you would like to remove a member. | 
 **member_id** | **str**| Unique identifier of the member who is to be removed. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_phone_number_slg**
> delete_a_phone_number_slg(shared_line_group_id, phone_number_id)

Unassign a Phone Number

Use this API to unassign a specific phone number that was assigned to the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792-Setting-up-shared-line-groups). **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique identifier of the shared line group from which you would like to unassign a phone number.
phone_number_id = 'phone_number_id_example' # str | Unique identifier of the phone number which is to be unassigned. This can be retrieved from Get a Shared Line Group API.

try:
    # Unassign a Phone Number
    api_instance.delete_a_phone_number_slg(shared_line_group_id, phone_number_id)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->delete_a_phone_number_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique identifier of the shared line group from which you would like to unassign a phone number. | 
 **phone_number_id** | **str**| Unique identifier of the phone number which is to be unassigned. This can be retrieved from Get a Shared Line Group API. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_shared_line_group**
> object delete_a_shared_line_group(shared_line_group_id)

Delete a Shared Line Group

A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common area phones. Use this API to delete a Shared Line Group.  **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique Identifier of the shared line group that you would like to delete.

try:
    # Delete a Shared Line Group
    api_response = api_instance.delete_a_shared_line_group(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->delete_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique Identifier of the shared line group that you would like to delete. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_of_slg**
> object delete_members_of_slg(shared_line_group_id)

Unassign Members of a Shared Line Group

Members of the [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) have access to the group's phone number and voicemail. Use this API to unassign **all** the existing members from a Shared Line Group. **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * A valid Shared Line Group * Account owner or admin privileges  **Scopes:** `phone:write:admin`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique identifier of the Shared Line Group that you would like to delete.

try:
    # Unassign Members of a Shared Line Group
    api_response = api_instance.delete_members_of_slg(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->delete_members_of_slg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique identifier of the Shared Line Group that you would like to delete. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_shared_line_group**
> InlineResponse20099 get_a_shared_line_group(shared_line_group_id)

Get a Shared Line Group

A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common area phones. This gives members of the shared line group access to the group's direct phone number and voicemail. Use this API to list all the Shared Line Groups.  **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:read:admin` or `phone:write:admin`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique Identifier of the Shared Line Group.

try:
    # Get a Shared Line Group
    api_response = api_instance.get_a_shared_line_group(shared_line_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->get_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique Identifier of the Shared Line Group. | 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_shared_line_group**
> object update_a_shared_line_group(shared_line_group_id, body=body)

Update a Shared Line Group

A [shared line group](https://support.zoom.us/hc/en-us/articles/360038850792) allows Zoom Phone admins to share a phone number and extension with a group of phone users or common area phones. This gives members of the shared line group access to the group's direct phone number and voicemail. Use this API to update information of a Shared Line Group.  **Prerequisties:** <br> * Pro or higher account with Zoom Phone license. * Account owner or admin privileges   **Scopes:** `phone:write:admin`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneSharedLineGroupsApi(swagger_client.ApiClient(configuration))
shared_line_group_id = 'shared_line_group_id_example' # str | Unique identifier of the shared line group that is to be updated.
body = swagger_client.Body184() # Body184 |  (optional)

try:
    # Update a Shared Line Group
    api_response = api_instance.update_a_shared_line_group(shared_line_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSharedLineGroupsApi->update_a_shared_line_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_line_group_id** | **str**| Unique identifier of the shared line group that is to be updated. | 
 **body** | [**Body184**](Body184.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


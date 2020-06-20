# swagger_client.RoomsLocationApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_azr_location**](RoomsLocationApi.md#add_azr_location) | **POST** /rooms/locations | Add a Location
[**change_parent_location**](RoomsLocationApi.md#change_parent_location) | **PUT** /rooms/locations/{locationId}/location | Change the Assigned Parent Location
[**get_zr_location_profile**](RoomsLocationApi.md#get_zr_location_profile) | **GET** /rooms/locations/{locationId} | Get Zoom Room Location Profile 
[**get_zr_location_settings**](RoomsLocationApi.md#get_zr_location_settings) | **GET** /rooms/locations/{locationId}/settings | Get Location Settings 
[**get_zr_location_structure**](RoomsLocationApi.md#get_zr_location_structure) | **GET** /rooms/locations/structure | Get Zoom Room Location Structure
[**list_zr_locations**](RoomsLocationApi.md#list_zr_locations) | **GET** /rooms/locations | List Zoom Room Locations
[**update_zoom_rooms_location_structure**](RoomsLocationApi.md#update_zoom_rooms_location_structure) | **PATCH** /rooms/locations/structure | Update Zoom Rooms Location Structure
[**update_zr_location_profile**](RoomsLocationApi.md#update_zr_location_profile) | **PATCH** /rooms/locations/{locationId} | Update Zoom Room Location Profile
[**update_zr_location_settings**](RoomsLocationApi.md#update_zr_location_settings) | **PATCH** /rooms/locations/{locationId}/settings | Update Location Settings

# **add_azr_location**
> InlineResponse20077 add_azr_location(body=body)

Add a Location

Add a location to the [location hierarchial structure(s)](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) of Zoom Rooms in an account.  **Prerequisites:** * Account owner or admin permissions. * Zoom Rooms Version 4.0 or higher<br><br> **Scopes:** `room:write:admin`<br>      **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body141() # Body141 |  (optional)

try:
    # Add a Location
    api_response = api_instance.add_azr_location(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->add_azr_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body141**](Body141.md)|  | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_parent_location**
> object change_parent_location(location_id, body=body)

Change the Assigned Parent Location

An account owner of a Zoom account can establish a [Zoom Rooms Location Hierarchy](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) to better organize Zoom Rooms spread accross various location. The location can be structured in a hierarchy with Country being the top-level location, followed by city, campus, building, and floor. The location in the lower level in the hierarchy is considered as a child of the location that is a level above in the hierarchy. Use this API to change the parent location of a child location. <br><br> For instance, if the location hierarchy is structured in a way where there are two campuses (Campus 1, and Campus 2) in a City and Campus 1 consists of a building named Building 1 with a floor where Zoom Rooms are located, and you would like to rearrange the structure so that Building 1 along with its child locations (floor and Zoom Rooms) are relocated directly under Campus 2 instead of Campus 1, you must provide the location ID of Building 1 in the path parameter of this request and the location ID of Campus 2 as the value of `parent_location_id` in the  request body.<br><br> **Prerequisite:**<br> * Account owner or admin permission * Zoom Rooms version 4.0 or higher<br> **Scopes:** `room:write:admin`<br><br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | 
body = swagger_client.Body159() # Body159 |  (optional)

try:
    # Change the Assigned Parent Location
    api_response = api_instance.change_parent_location(location_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->change_parent_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 
 **body** | [**Body159**](Body159.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zr_location_profile**
> InlineResponse20078 get_zr_location_profile(location_id)

Get Zoom Room Location Profile 

Each location type of the [Zoom Rooms location hierarchy](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) has a profile page that includes information such as name of the location, address, support email, etc. Use this API to retrieve information about a specific Zoom Rooms location type such as information about the city where the Zoom Rooms is located.  **Prerequisite:**<br> * Account owner or admin permission * Zoom Rooms version 4.0 or higher<br> **Scopes:** `room:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response).

try:
    # Get Zoom Room Location Profile 
    api_response = api_instance.get_zr_location_profile(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->get_zr_location_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response). | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zr_location_settings**
> object get_zr_location_settings(setting_type, location_id)

Get Location Settings 

Get information on meeting or alert settings applied to Zoom Rooms located in a specific location. By default, only **Meeting Settings** are returned. To view only **Alert Settings**, specify `alert` as the value of the `setting_type` query parameter.<br><br> **Prerequisites:**<br> * Zoom Room licenses * Owner or Admin privileges on the Zoom Account.<br> **Scopes:** `room:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
setting_type = 'meeting' # str | The type of setting that you would like to retrieve.<br> `alert`: Alert Settings applied on the Zoom Rooms Account.<br> `meeting`: Meeting settings of the Zoom Rooms Account. (default to meeting)
location_id = 'location_id_example' # str | Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response).

try:
    # Get Location Settings 
    api_response = api_instance.get_zr_location_settings(setting_type, location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->get_zr_location_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| The type of setting that you would like to retrieve.&lt;br&gt; &#x60;alert&#x60;: Alert Settings applied on the Zoom Rooms Account.&lt;br&gt; &#x60;meeting&#x60;: Meeting settings of the Zoom Rooms Account. | [default to meeting]
 **location_id** | **str**| Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response). | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zr_location_structure**
> InlineResponse20079 get_zr_location_structure()

Get Zoom Room Location Structure

Get the [location hierarchial structure(s)](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) applied on the Zoom Rooms in an account.<br><br> **Prerequisites:**<br> * Zoom Rooms version 4.0 or higher * Account owner or admin permissions<br> **Scopes:** `room:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))

try:
    # Get Zoom Room Location Structure
    api_response = api_instance.get_zr_location_structure()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->get_zr_location_structure: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zr_locations**
> InlineResponse20076 list_zr_locations(parent_location_id=parent_location_id, type=type, page_size=page_size, next_page_token=next_page_token)

List Zoom Room Locations

A Zoom account owner or a Zoom Room administrator can establish a [location hierarchy](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) to help manage Zoom Rooms that are spread among a variety of locations. Use this API to list the different location types used for Zoom Rooms in an account.<br><br> **Prerequisites:** * Account owner or admin permissions. * Zoom Rooms Version 4.0 or higher<br><br> **Scopes:** `room:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
parent_location_id = 'parent_location_id_example' # str | A unique identifier for the parent location. For instance, if a Zoom Room is located in Floor 1 of Building A, the location of Building A will be the parent location of Floor 1. Use this parameter to filter the response by a specific location hierarchy level. (optional)
type = 'type_example' # str | Use this field to filter the response by the type of location. The value can be one of the following: `country`, `states`, `city`, `campus`, `building`, `floor`.  (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Zoom Room Locations
    api_response = api_instance.list_zr_locations(parent_location_id=parent_location_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->list_zr_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_location_id** | **str**| A unique identifier for the parent location. For instance, if a Zoom Room is located in Floor 1 of Building A, the location of Building A will be the parent location of Floor 1. Use this parameter to filter the response by a specific location hierarchy level. | [optional] 
 **type** | **str**| Use this field to filter the response by the type of location. The value can be one of the following: &#x60;country&#x60;, &#x60;states&#x60;, &#x60;city&#x60;, &#x60;campus&#x60;, &#x60;building&#x60;, &#x60;floor&#x60;.  | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zoom_rooms_location_structure**
> object update_zoom_rooms_location_structure(body=body)

Update Zoom Rooms Location Structure

Update the [location hierarchial structure(s)](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) applied on the Zoom Rooms in an account.<br><br> **Prerequisites:**<br> * Zoom Rooms version 4.0 or higher * Account owner or admin permissions<br> **Scopes:** `room:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body145() # Body145 |  (optional)

try:
    # Update Zoom Rooms Location Structure
    api_response = api_instance.update_zoom_rooms_location_structure(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->update_zoom_rooms_location_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body145**](Body145.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zr_location_profile**
> object update_zr_location_profile(location_id, body=body)

Update Zoom Room Location Profile

Each location type of the [Zoom Rooms location hierarchy](https://support.zoom.us/hc/en-us/articles/115000342983-Zoom-Rooms-Location-Hierarchy) has a profile page that includes information such as name of the location, address, support email, etc. Use this API to update information about a specific Zoom Rooms location type such as information about the city where the Zoom Rooms is located.  **Prerequisite:**<br> * Account owner or admin permission * Zoom Rooms version 4.0 or higher<br> **Scopes:** `room:write:admin`<br>      **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | Unique Identifier of the location. This can be retrieved from the [List Zoom Room Locations](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) API.
body = swagger_client.Body143() # Body143 |  (optional)

try:
    # Update Zoom Room Location Profile
    api_response = api_instance.update_zr_location_profile(location_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->update_zr_location_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Unique Identifier of the location. This can be retrieved from the [List Zoom Room Locations](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) API. | 
 **body** | [**Body143**](Body143.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zr_location_settings**
> object update_zr_location_settings(setting_type, location_id, body=body)

Update Location Settings

Update information on either meeting or alert settings applied to Zoom Rooms located in a specific location. To update **Alert Settings**, specify `alert` as the value of the `setting_type` query parameter. Similarly, to update **Meeting Settings**, specify `meeting` as the value of the `setting_type` query parameter.<br><br> **Prerequisites:**<br> * Zoom Room licenses * Owner or Admin privileges on the Zoom Account.<br> **Scopes:** `room:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.RoomsLocationApi(swagger_client.ApiClient(configuration))
setting_type = 'meeting' # str | The type of setting that you would like to update.<br> `alert`: Alert Settings applied on the Zoom Rooms Account.<br> `meeting`: Meeting settings of the Zoom Rooms Account. (default to meeting)
location_id = 'location_id_example' # str | Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response).
body = NULL # object |  (optional)

try:
    # Update Location Settings
    api_response = api_instance.update_zr_location_settings(setting_type, location_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoomsLocationApi->update_zr_location_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_type** | **str**| The type of setting that you would like to update.&lt;br&gt; &#x60;alert&#x60;: Alert Settings applied on the Zoom Rooms Account.&lt;br&gt; &#x60;meeting&#x60;: Meeting settings of the Zoom Rooms Account. | [default to meeting]
 **location_id** | **str**| Unique identifier of the location type. This can be retrieved using the [List Zoom Room Location API](https://marketplace.zoom.us/docs/api-reference/zoom-api/rooms-location/listzrlocations) (Id property in the response). | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


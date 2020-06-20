# swagger_client.PhoneDevicesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_phone_device**](PhoneDevicesApi.md#add_phone_device) | **POST** /phone/devices | Add a Device
[**delete_a_device**](PhoneDevicesApi.md#delete_a_device) | **DELETE** /phone/devices/{deviceId} | Delete a Device
[**get_a_device**](PhoneDevicesApi.md#get_a_device) | **GET** /phone/devices/{deviceId} | Get Device Details
[**list_phone_devices**](PhoneDevicesApi.md#list_phone_devices) | **GET** /phone/devices | List Devices
[**update_a_device**](PhoneDevicesApi.md#update_a_device) | **PATCH** /phone/devices/{deviceId} | Update a Device

# **add_phone_device**
> object add_phone_device(body=body)

Add a Device

By default, all Zoom Phone users can make and receive calls using the Zoom desktop and mobile applications. Additionally, if a desk phone is required, use this API to [add a desk phone and assign it](https://support.zoom.us/hc/en-us/articles/360021119092#h_5ca07504-68a8-4c3d-ad0e-c1d3594436da) to a user.  **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body153() # Body153 |  (optional)

try:
    # Add a Device
    api_response = api_instance.add_phone_device(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->add_phone_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body153**](Body153.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_device**
> object delete_a_device(device_id)

Delete a Device

Remove a [desk phone device](https://support.zoom.us/hc/en-us/articles/360021119092) from the Zoom Phone System Management.<br><br> **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions * Device must not have been assigned to a user.<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique Identifier of the device.

try:
    # Delete a Device
    api_response = api_instance.delete_a_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->delete_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique Identifier of the device. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_device**
> InlineResponse20089 get_a_device(device_id)

Get Device Details

Get detailed information about a specific [desk phone device](https://support.zoom.us/hc/en-us/articles/360021119092).<br><br> **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique Identifier of the device.

try:
    # Get Device Details
    api_response = api_instance.get_a_device(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->get_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique Identifier of the device. | 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_devices**
> InlineResponse20088 list_phone_devices(type, next_page_token=next_page_token, page_size=page_size)

List Devices

List all the [desk phone devices](https://support.zoom.us/hc/en-us/articles/360021119092) that are configured with Zoom Phone on an account. To view devices that have not yet been assigned to a user, set the value of the `type` query parameter as `unassigned` and to view devices that have been assigned, set the value as `assigned`.<br><br> **Scopes:** `phone:read:admin`  <br> **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | State of the device. The value should be either `assigned` to list devices that have been assigned to user(s) or `unassigned` to list devices that have not yet been assigned to any user in the Zoom account.
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)

try:
    # List Devices
    api_response = api_instance.list_phone_devices(type, next_page_token=next_page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->list_phone_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| State of the device. The value should be either &#x60;assigned&#x60; to list devices that have been assigned to user(s) or &#x60;unassigned&#x60; to list devices that have not yet been assigned to any user in the Zoom account. | 
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_device**
> object update_a_device(device_id, body=body)

Update a Device

Update information of a [desk phone device](https://support.zoom.us/hc/en-us/articles/360021119092).<br><br> **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneDevicesApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Unique Identifier of the Device.
body = swagger_client.Body155() # Body155 |  (optional)

try:
    # Update a Device
    api_response = api_instance.update_a_device(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneDevicesApi->update_a_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Unique Identifier of the Device. | 
 **body** | [**Body155**](Body155.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.CommonAreaPhonesApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_common_area_phone**](CommonAreaPhonesApi.md#add_common_area_phone) | **POST** /phone/common_area_phones | Add a Common Area Phone
[**delete_common_area_phone**](CommonAreaPhonesApi.md#delete_common_area_phone) | **DELETE** /phone/common_area_phones/{commonAreaPhoneId} | Delete a Common Area Phone
[**get_a_common_area_phone**](CommonAreaPhonesApi.md#get_a_common_area_phone) | **GET** /phone/common_area_phones/{commonAreaPhoneId} | Get Common Area Phone Details
[**list_common_area_phones**](CommonAreaPhonesApi.md#list_common_area_phones) | **GET** /phone/common_area_phones | List Common Area Phones
[**update_common_area_phone**](CommonAreaPhonesApi.md#update_common_area_phone) | **PATCH** /phone/common_area_phones/{commonAreaPhoneId} | Update Common Area Phone

# **add_common_area_phone**
> InlineResponse20124 add_common_area_phone(body=body)

Add a Common Area Phone

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.<br> Use this API to [add a common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones#h_2d0da347-c35a-4993-9771-e21aaa568deb).<br><br> **Prerequisites:**<br> * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br> **Scope:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body177() # Body177 |  (optional)

try:
    # Add a Common Area Phone
    api_response = api_instance.add_common_area_phone(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->add_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body177**](Body177.md)|  | [optional] 

### Return type

[**InlineResponse20124**](InlineResponse20124.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_common_area_phone**
> object delete_common_area_phone(common_area_phone_id)

Delete a Common Area Phone

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.<br> Use this API to remove the [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) from Zoom Phone System in an account.<br><br>**Prerequisites:**<br> * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | Unique Identifier of the common area phone.

try:
    # Delete a Common Area Phone
    api_response = api_instance.delete_common_area_phone(common_area_phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->delete_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| Unique Identifier of the common area phone. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_common_area_phone**
> InlineResponse20096 get_a_common_area_phone(common_area_phone_id)

Get Common Area Phone Details

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.<br> Use this API to get details on a specific [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) in an account.<br><br>**Prerequisites:**<br> * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br> **Scopes:** `phone:read:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | Unique Identifier of the Common Area Phone. This can be retrieved from List Common Area Phones API.

try:
    # Get Common Area Phone Details
    api_response = api_instance.get_a_common_area_phone(common_area_phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->get_a_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**| Unique Identifier of the Common Area Phone. This can be retrieved from List Common Area Phones API. | 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_common_area_phones**
> InlineResponse20095 list_common_area_phones(page_size=page_size, next_page_token=next_page_token)

List Common Area Phones

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.<br> Use this API to [list all common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) in an account.<br><br>**Prerequisites:**<br> * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br><br> **Scope:** `phone:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The total number of records returned from a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Common Area Phones
    api_response = api_instance.list_common_area_phones(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->list_common_area_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The total number of records returned from a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_area_phone**
> object update_common_area_phone(common_area_phone_id, body=body)

Update Common Area Phone

A common area phone can be provisioned by a Zoom account owner or a Zoom admin so that anyone in an organization can use it. For example, if your office has shared desks that don't belong to a specific employees, you could add a common area phone so that any person can use it.<br> Use this API to update details on a specific [common area phone](https://support.zoom.us/hc/en-us/articles/360028516231-Managing-Common-Area-Phones) in an account.<br><br>**Prerequisites:**<br> * Pro or a higher account with Zoom Phone license. * Account owner or admin permissions. * [Supported device](https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Voice-Supported-Devices)<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CommonAreaPhonesApi(swagger_client.ApiClient(configuration))
common_area_phone_id = 'common_area_phone_id_example' # str | 
body = swagger_client.Body178() # Body178 |  (optional)

try:
    # Update Common Area Phone
    api_response = api_instance.update_common_area_phone(common_area_phone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonAreaPhonesApi->update_common_area_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_area_phone_id** | **str**|  | 
 **body** | [**Body178**](Body178.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


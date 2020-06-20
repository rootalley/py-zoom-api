# swagger_client.SIPPhoneApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sip_phone**](SIPPhoneApi.md#create_sip_phone) | **POST** /sip_phones | Create SIP Phone
[**delete_sip_phone**](SIPPhoneApi.md#delete_sip_phone) | **DELETE** /sip_phones/{phoneId} | Delete SIP Phone
[**list_sip_phones**](SIPPhoneApi.md#list_sip_phones) | **GET** /sip_phones | List SIP Phones
[**update_sip_phone**](SIPPhoneApi.md#update_sip_phone) | **PATCH** /sip_phones/{phoneId} | Update SIP Phone

# **create_sip_phone**
> create_sip_phone(body=body)

Create SIP Phone

Zoom’s Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to enable a user to use SIP phone.<br><br> **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.<br> **Scope:** `sip_phone:write:admin` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.SIPPhoneApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Create SIP Phone
    api_instance.create_sip_phone(body=body)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->create_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_phone**
> delete_sip_phone(phone_id)

Delete SIP Phone

Zoom’s Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to delete a specific SIP phone on a Zoom account.<br><br> **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * User must enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.<br> **Scope:** `sip_phone:read:admin` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.SIPPhoneApi(swagger_client.ApiClient(configuration))
phone_id = 'phone_id_example' # str | Unique Identifier of the SIP Phone. It can be retrieved from the List SIP Phones API.

try:
    # Delete SIP Phone
    api_instance.delete_sip_phone(phone_id)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->delete_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**| Unique Identifier of the SIP Phone. It can be retrieved from the List SIP Phones API. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_phones**
> InlineResponse2001 list_sip_phones(page_number=page_number, search_key=search_key, page_size=page_size)

List SIP Phones

Zoom’s Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to list SIP phones on an account.<br><br> **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * User must enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.<br> **Scope:** `sip_phone:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> 

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
api_instance = swagger_client.SIPPhoneApi(swagger_client.ApiClient(configuration))
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)
search_key = 'search_key_example' # str | User name or email address of a user. If this parameter is provided, only the SIP phone system integration enabled for that specific user will be returned. Otherwise, all SIP phones on an account will be returned. (optional)
page_size = 56 # int | The number of records returned within a single API call. (optional)

try:
    # List SIP Phones
    api_response = api_instance.list_sip_phones(page_number=page_number, search_key=search_key, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->list_sip_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]
 **search_key** | **str**| User name or email address of a user. If this parameter is provided, only the SIP phone system integration enabled for that specific user will be returned. Otherwise, all SIP phones on an account will be returned. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_phone**
> update_sip_phone(phone_id, body=body)

Update SIP Phone

Zoom’s Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to update information of a specific SIP Phone on a Zoom account.<br><br> **Prerequisites**: * Currently only supported on Cisco and Avaya PBX systems.  * The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.<br> **Scope:** `sip_phone:write:admin` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.SIPPhoneApi(swagger_client.ApiClient(configuration))
phone_id = 'phone_id_example' # str | Unique Identifier of the SIP Phone. This can be retrieved from the List SIP Phones API.
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # Update SIP Phone
    api_instance.update_sip_phone(phone_id, body=body)
except ApiException as e:
    print("Exception when calling SIPPhoneApi->update_sip_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **str**| Unique Identifier of the SIP Phone. This can be retrieved from the List SIP Phones API. | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.PhoneAutoReceptionistsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_auto_receptionist**](PhoneAutoReceptionistsApi.md#add_auto_receptionist) | **POST** /phone/auto_receptionists | Add an Auto Receptionist
[**assign_phone_numbers_auto_receptionist**](PhoneAutoReceptionistsApi.md#assign_phone_numbers_auto_receptionist) | **POST** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers | Assign Phone Numbers
[**unassign_a_phone_num_auto_receptionist**](PhoneAutoReceptionistsApi.md#unassign_a_phone_num_auto_receptionist) | **DELETE** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers/{phoneNumberId} | Unassign a Phone Number
[**unassign_all_phone_nums_auto_receptionist**](PhoneAutoReceptionistsApi.md#unassign_all_phone_nums_auto_receptionist) | **DELETE** /phone/auto_receptionists/{autoReceptionistId}/phone_numbers | Unassign all Phone Numbers
[**update_auto_receptionist**](PhoneAutoReceptionistsApi.md#update_auto_receptionist) | **PATCH** /phone/auto_receptionists/{autoReceptionistId} | Update Auto Receptionist Details 

# **add_auto_receptionist**
> InlineResponse20126 add_auto_receptionist(body=body)

Add an Auto Receptionist

Auto receptionists answer calls with a personalized recording and routes calls to a phone user, call queue, common area phone, voicemail or an IVR system. Use this API to add an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-) to a Zoom Phone.<br>  **Prerequisites:**<br> * Pro or higher account with Zoom Phone license.<br> **Scopes:** `phone:write:admin` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneAutoReceptionistsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body190() # Body190 |  (optional)

try:
    # Add an Auto Receptionist
    api_response = api_instance.add_auto_receptionist(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneAutoReceptionistsApi->add_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body190**](Body190.md)|  | [optional] 

### Return type

[**InlineResponse20126**](InlineResponse20126.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_phone_numbers_auto_receptionist**
> object assign_phone_numbers_auto_receptionist(auto_receptionist_id, body=body)

Assign Phone Numbers

Assign available phone numbers to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-). The available numbers can be retrieved using the List Phone Numbers API with `type` query parameter set to \"unassigned\".  **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneAutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | Unique Identifier of the Auto Receptionist. It can be retrieved from the [List Sites API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-site/listphonesites).
body = swagger_client.Body175() # Body175 |  (optional)

try:
    # Assign Phone Numbers
    api_response = api_instance.assign_phone_numbers_auto_receptionist(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneAutoReceptionistsApi->assign_phone_numbers_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| Unique Identifier of the Auto Receptionist. It can be retrieved from the [List Sites API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-site/listphonesites). | 
 **body** | [**Body175**](Body175.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_a_phone_num_auto_receptionist**
> object unassign_a_phone_num_auto_receptionist(auto_receptionist_id, phone_number_id)

Unassign a Phone Number

Unassign a specific phone number that was previously assigned to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).   **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneAutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | Unique identifier of the auto receptionist. This can be retrieved from the List Phone Sites API.
phone_number_id = 'phone_number_id_example' # str | Unique Identifier of the phone number or provide the actual phone number in e164 format (example: +19995550123).

try:
    # Unassign a Phone Number
    api_response = api_instance.unassign_a_phone_num_auto_receptionist(auto_receptionist_id, phone_number_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneAutoReceptionistsApi->unassign_a_phone_num_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| Unique identifier of the auto receptionist. This can be retrieved from the List Phone Sites API. | 
 **phone_number_id** | **str**| Unique Identifier of the phone number or provide the actual phone number in e164 format (example: +19995550123). | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_all_phone_nums_auto_receptionist**
> object unassign_all_phone_nums_auto_receptionist(auto_receptionist_id)

Unassign all Phone Numbers

Unassign all phone numbers that were previously assigned to an [auto receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-).   **Prerequisites:** * Pro or higher account plan with Zoom Phone License * Account owner or admin permissions<br> **Scopes:** `phone:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.PhoneAutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | 

try:
    # Unassign all Phone Numbers
    api_response = api_instance.unassign_all_phone_nums_auto_receptionist(auto_receptionist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneAutoReceptionistsApi->unassign_all_phone_nums_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_receptionist**
> object update_auto_receptionist(auto_receptionist_id, body=body)

Update Auto Receptionist Details 

An auto receptionist answers calls with a personalized recording and routes calls to a phone user, call queue, common area phone, or voicemail. An auto receptionist can also be set up so that it routes calls to an interactive voice response (IVR) system to allow callers to select the routing options.<br> Use this API to [change information](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Interactive-Voice-Response-IVR-#h_1d5ffc56-6ba3-4ce5-9d86-4a1a1ee743f3) such as display name and extension number assigned to the main auto receptionist.<br><br> **Prerequisites:**<br> * Pro or higher account with Zoom Phone license.<br> **Scopes:** `phone:write:admin` <br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.PhoneAutoReceptionistsApi(swagger_client.ApiClient(configuration))
auto_receptionist_id = 'auto_receptionist_id_example' # str | Unique Identifier of the Auto Receptionist. It can be retrieved from the [List Sites API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-site/listphonesites).
body = swagger_client.Body173() # Body173 |  (optional)

try:
    # Update Auto Receptionist Details 
    api_response = api_instance.update_auto_receptionist(auto_receptionist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneAutoReceptionistsApi->update_auto_receptionist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_receptionist_id** | **str**| Unique Identifier of the Auto Receptionist. It can be retrieved from the [List Sites API](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-site/listphonesites). | 
 **body** | [**Body173**](Body173.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


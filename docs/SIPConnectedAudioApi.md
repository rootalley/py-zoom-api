# swagger_client.SIPConnectedAudioApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_sip_config**](SIPConnectedAudioApi.md#assign_sip_config) | **PATCH** /accounts/{accountId}/sip_trunk/settings | Assign SIP Trunk Configuration
[**assign_sip_trunk_numbers**](SIPConnectedAudioApi.md#assign_sip_trunk_numbers) | **POST** /accounts/{accountId}/sip_trunk/numbers | Assign Numbers
[**delete_all_sip_numbers**](SIPConnectedAudioApi.md#delete_all_sip_numbers) | **DELETE** /accounts/{accountId}/sip_trunk/numbers | Delete All Numbers
[**list_sip_trunk_numbers**](SIPConnectedAudioApi.md#list_sip_trunk_numbers) | **GET** /sip_trunk/numbers | List SIP Trunk Numbers

# **assign_sip_config**
> object assign_sip_config(account_id, body=body)

Assign SIP Trunk Configuration

With SIP-connected audio, Zoom establishes a SIP trunk (a network connection specifically designed to make and deliver phone calls) over a direct and private connection between the customer’s network and the Zoom cloud. Meeting participants that dial into a meeting or have the meeting call them, and are On-Net from the perspective of the customers' IP telephony network, will be connected over this trunk rather than over the PSTN. <br><br> Using this API, a Master Account owner can copy the SIP Connected Audio configurations applied on the Master Account and enable those configurations on a Sub Account. The owner can also disable the configuration in the Sub Account where it was previously enabled.  **Prerequisites:**<br> * Pro or a higher account with SIP Connected Audio plan enabled. * Master Account Owner<br> **Scopes:** `sip_trunk:master`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.SIPConnectedAudioApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = swagger_client.Body149() # Body149 |  (optional)

try:
    # Assign SIP Trunk Configuration
    api_response = api_instance.assign_sip_config(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPConnectedAudioApi->assign_sip_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**Body149**](Body149.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_sip_trunk_numbers**
> object assign_sip_trunk_numbers(account_id, body=body)

Assign Numbers

With SIP-connected audio, Zoom establishes a SIP trunk (a network connection specifically designed to make and deliver phone calls) over a direct and private connection between the customer’s network and the Zoom cloud. Meeting participants that dial into a meeting or have the meeting call them, and are On-Net from the perspective of the customers' IP telephony network, will be connected over this trunk rather than over the PSTN. <br><br>Use this API to assign internal numbers to a Sub Account.  **Prerequisites:**<br> * Pro or a higher account with SIP Connected Audio plan enabled. * The account must be a Master Account<br> **Scopes:** `sip_trunk:master`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.SIPConnectedAudioApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique Identifier of the Sub Account.
body = swagger_client.Body151() # Body151 |  (optional)

try:
    # Assign Numbers
    api_response = api_instance.assign_sip_trunk_numbers(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPConnectedAudioApi->assign_sip_trunk_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique Identifier of the Sub Account. | 
 **body** | [**Body151**](Body151.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_sip_numbers**
> object delete_all_sip_numbers(account_id)

Delete All Numbers

With SIP-connected audio, Zoom establishes a SIP trunk (a network connection specifically designed to make and deliver phone calls) over a direct and private connection between the customer’s network and the Zoom cloud. Meeting participants that dial into a meeting or have the meeting call them, and are On-Net from the perspective of the customers' IP telephony network, will be connected over this trunk rather than over the PSTN. <br><br>Use this API to delete all internal numbers assigned to a Sub Account. **Prerequisites:**<br>  * Pro or a higher account with SIP Connected Audio plan enabled. * The account must be a Master Account<br> **Scopes:** `sip_trunk:master`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.SIPConnectedAudioApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account ID of the Sub Account from which the numbers are to be deleted. This can be retrieved from [List Sub Accounts](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/account) API.

try:
    # Delete All Numbers
    api_response = api_instance.delete_all_sip_numbers(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPConnectedAudioApi->delete_all_sip_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID of the Sub Account from which the numbers are to be deleted. This can be retrieved from [List Sub Accounts](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/account) API. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_trunk_numbers**
> InlineResponse20082 list_sip_trunk_numbers()

List SIP Trunk Numbers

With SIP-connected audio, Zoom establishes a SIP trunk (a network connection specifically designed to make and deliver phone calls) over a direct and private connection between the customer’s network and the Zoom cloud. Meeting participants that dial into a meeting or have the meeting call them, and are On-Net from the perspective of the customers' IP telephony network, will be connected over this trunk rather than over the PSTN. <br><br>Use this API to list all the internal numbers that are configured for SIP Connected Audio in a Zoom Account.  **Prerequisites:**<br> * Pro or a higher account with SIP Connected Audio plan enabled. * The account must be a Master Account<br> **Scopes:** `sip_trunk:master`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.SIPConnectedAudioApi(swagger_client.ApiClient(configuration))

try:
    # List SIP Trunk Numbers
    api_response = api_instance.list_sip_trunk_numbers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SIPConnectedAudioApi->list_sip_trunk_numbers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.PACApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_pa_cs**](PACApi.md#user_pa_cs) | **GET** /users/{userId}/pac | List a User&#x27;s PAC Accounts

# **user_pa_cs**
> InlineResponse20049 user_pa_cs(user_id)

List a User's PAC Accounts

[Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC) allows Pro or higher account holders to host meetings through PSTN (phone dial-in) only.<br>Use this API to list a user's PAC accounts.<br><br> **Scopes:** `user:read:admin` `user:read`<br> <br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * A Pro or higher plan with [Premium Audio Conferencing](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) add-on. * Personal Audio Conference must be enabled in the user's profile.

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
api_instance = swagger_client.PACApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # List a User's PAC Accounts
    api_response = api_instance.user_pa_cs(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PACApi->user_pa_cs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.TSPApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tsp**](TSPApi.md#tsp) | **GET** /tsp | Get Account&#x27;s TSP Information
[**tsp_update**](TSPApi.md#tsp_update) | **PATCH** /tsp | Update account&#x27;s TSP information
[**tsp_url_update**](TSPApi.md#tsp_url_update) | **PATCH** /users/{userId}/tsp/settings | Set Global Dial-in URL for a TSP User
[**user_ts_ps**](TSPApi.md#user_ts_ps) | **GET** /users/{userId}/tsp | List User&#x27;s TSP accounts
[**user_tsp**](TSPApi.md#user_tsp) | **GET** /users/{userId}/tsp/{tspId} | Get a User&#x27;s TSP Account
[**user_tsp_create**](TSPApi.md#user_tsp_create) | **POST** /users/{userId}/tsp | Add a User&#x27;s TSP Account
[**user_tsp_delete**](TSPApi.md#user_tsp_delete) | **DELETE** /users/{userId}/tsp/{tspId} | Delete a User&#x27;s TSP Account
[**user_tsp_update**](TSPApi.md#user_tsp_update) | **PATCH** /users/{userId}/tsp/{tspId} | Update a TSP Account

# **tsp**
> InlineResponse20045 tsp()

Get Account's TSP Information

Get information on Telephony Service Provider on an account level.<br><br> **Scopes:** `tsp:read:admin` <br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  **Prerequisites:**<br> * A Pro or a higher plan.

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))

try:
    # Get Account's TSP Information
    api_response = api_instance.tsp()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->tsp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tsp_update**
> tsp_update(body)

Update account's TSP information

Update information of the Telephony Service Provider set up on an account.<br> **Prerequisites**:<br> TSP account option should be enabled.<br> **Scopes:** `tsp:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body76() # Body76 | TSP Account

try:
    # Update account's TSP information
    api_instance.tsp_update(body)
except ApiException as e:
    print("Exception when calling TSPApi->tsp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body76**](Body76.md)| TSP Account | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tsp_url_update**
> tsp_url_update(user_id, body=body)

Set Global Dial-in URL for a TSP User

A global dial-in page can provide a list of global access numbers using which audio conferencing can be conducted. By calling this API, you can set the url for the global dial-in page of a user whose Zoom account has TSP and special TSP with third-party audio conferencing options enabled. <p></p> **Scopes:**`tsp:write:admin` `tsp:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The userId or email address of the user.
body = swagger_client.TSPGlobalDialInURLSetting() # TSPGlobalDialInURLSetting | Global dial-in URL of the user. (optional)

try:
    # Set Global Dial-in URL for a TSP User
    api_instance.tsp_url_update(user_id, body=body)
except ApiException as e:
    print("Exception when calling TSPApi->tsp_url_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The userId or email address of the user. | 
 **body** | [**TSPGlobalDialInURLSetting**](TSPGlobalDialInURLSetting.md)| Global dial-in URL of the user. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_ts_ps**
> InlineResponse20050 user_ts_ps(user_id)

List User's TSP accounts

A user can have a maximum of two TSP accounts. Use this API to list all TSP accounts of a user.<br><br> **Scopes:** `tsp:read:admin` `tsp:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # List User's TSP accounts
    api_response = api_instance.user_ts_ps(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_ts_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp**
> TSPAccount user_tsp(user_id, tsp_id)

Get a User's TSP Account

Each user can have a maximum of two TSP accounts. Use this API to retrieve details of a specific TSP account enabled for a specific user.<br><br> **Scopes:** `tsp:read:admin` `tsp:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
tsp_id = 'tsp_id_example' # str | TSP account ID.

try:
    # Get a User's TSP Account
    api_response = api_instance.user_tsp(user_id, tsp_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **tsp_id** | **str**| TSP account ID. | 

### Return type

[**TSPAccount**](TSPAccount.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_create**
> TSPAccountsList2 user_tsp_create(body, user_id)

Add a User's TSP Account

Add a user's TSP account.<br><br> **Scopes:** `tsp:write:admin` `tsp:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
body = swagger_client.TSPAccountsList() # TSPAccountsList | TSP account.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Add a User's TSP Account
    api_response = api_instance.user_tsp_create(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TSPAccountsList**](TSPAccountsList.md)| TSP account. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**TSPAccountsList2**](TSPAccountsList2.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_delete**
> user_tsp_delete(user_id, tsp_id)

Delete a User's TSP Account

Delete a user's TSP account.<br><br> **Scopes:** `tsp:write:admin` `tsp:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
tsp_id = 'tsp_id_example' # str | TSP account ID.

try:
    # Delete a User's TSP Account
    api_instance.user_tsp_delete(user_id, tsp_id)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **tsp_id** | **str**| TSP account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tsp_update**
> user_tsp_update(body, user_id, tsp_id)

Update a TSP Account

Update a user's TSP account.<br><br> **Scopes:** `tsp:write:admin` `tsp:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.TSPApi(swagger_client.ApiClient(configuration))
body = swagger_client.TSPAccount1() # TSPAccount1 | TSP account.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
tsp_id = 'tsp_id_example' # str | TSP account ID.

try:
    # Update a TSP Account
    api_instance.user_tsp_update(body, user_id, tsp_id)
except ApiException as e:
    print("Exception when calling TSPApi->user_tsp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TSPAccount1**](TSPAccount1.md)| TSP account. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **tsp_id** | **str**| TSP account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.AccountsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account**](AccountsApi.md#account) | **GET** /accounts/{accountId} | Get a Sub Account
[**account_create**](AccountsApi.md#account_create) | **POST** /accounts | Create a Sub Account
[**account_disassociate**](AccountsApi.md#account_disassociate) | **DELETE** /accounts/{accountId} | Disassociate a Sub Account
[**account_managed_domain**](AccountsApi.md#account_managed_domain) | **GET** /accounts/{accountId}/managed_domains | Get Managed Domains
[**account_options_update**](AccountsApi.md#account_options_update) | **PATCH** /accounts/{accountId}/options | Update Options
[**account_settings**](AccountsApi.md#account_settings) | **GET** /accounts/{accountId}/settings | Get Settings
[**account_settings_update**](AccountsApi.md#account_settings_update) | **PATCH** /accounts/{accountId}/settings | Update Settings
[**account_trusted_domain**](AccountsApi.md#account_trusted_domain) | **GET** /accounts/{accountId}/trusted_domains | Get Trusted Domains
[**accounts**](AccountsApi.md#accounts) | **GET** /accounts | List Sub Accounts
[**get_account_lock_settings**](AccountsApi.md#get_account_lock_settings) | **GET** /accounts/{accountId}/lock_settings | Get Locked Settings
[**update_account_lock_settings**](AccountsApi.md#update_account_lock_settings) | **PATCH** /accounts/{accountId}/lock_settings | Update Locked Settings
[**update_account_owner**](AccountsApi.md#update_account_owner) | **PUT** /accounts/{accountId}/owner | Update the Account Owner

# **account**
> InlineResponse20012 account(account_id)

Get a Sub Account

Get a Sub Account under the Master Account. Your account must be a Master Account in order to retrieve Sub Accounts. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [ISV team](https://zoom.us/plan/api) for more details.<br><br> **Prerequisites:** * Pro or a higher paid account with Master Account option enabled. <br> **Scope**: `account:write:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>     

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.

try:
    # Get a Sub Account
    api_response = api_instance.account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_create**
> InlineResponse2015 account_create(body)

Create a Sub Account

Create a Sub Account under the Master Account. <aside>Your account must be a Master Account in order to create Sub Accounts. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details. Please note that the created account user will receive a confirmation email.</aside><br><br> **Prerequisites:**<br> * Pro or a higher paid account with Master Account option enabled. <br> **Scope**: `account:write:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>    

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body20() # Body20 | Account.

try:
    # Create a Sub Account
    api_response = api_instance.account_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body20**](Body20.md)| Account. | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_disassociate**
> account_disassociate(account_id)

Disassociate a Sub Account

Disassociate a Sub Account from the Master Account. This will leave the Sub Account intact but it will no longer be associated with the master account.<br>  <aside>Your account must be a Master Account in order to disassociate Sub Accounts. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside> <br>  **Prerequisites:** * Pro or a higher paid account with Master Account option enabled. <br> **Scope**: `account:write:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>    

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.

try:
    # Disassociate a Sub Account
    api_instance.account_disassociate(account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->account_disassociate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_managed_domain**
> InlineResponse20013 account_managed_domain(account_id)

Get Managed Domains

Get a Sub Account's [managed domains](https://support.zoom.us/hc/en-us/articles/203395207-What-is-Managed-Domain-).<br><br>  **Note:** This API can be used by Zoom Accounts that are on a Pro or a higher plan as well accounts that have Master and Sub Accounts options enabled. <br><br> To get managed domains of the Master Account, provide `me` as the value for accountId in the path parameter. Provide the Sub Account's Account ID as the value of accountId path parameter to get managed domains of the Sub Account.<br><br> **Prerequisites:**<br> * Pro or a higher paid account with Master Account option enabled. <br> **Scope:** `account:read:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>    

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \"me\" as the value of this field. <br> To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field.

try:
    # Get Managed Domains
    api_response = api_instance.account_managed_domain(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_managed_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \&quot;me\&quot; as the value of this field. &lt;br&gt; To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field. | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_options_update**
> account_options_update(body, account_id)

Update Options

Update a Sub Account's options under the Master Account.<br> <aside>Your account must be a Master Account in order to update the options for Sub Accounts. Zoom only assigns this privilege to trusted partners. </aside>  **Prerequisites:** * Pro or a higher paid account with Master Account option enabled. <br> **Scope**: `account:write:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>    

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body22() # Body22 | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Update Options
    api_instance.account_options_update(body, account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->account_options_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body22**](Body22.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings**
> object account_settings(account_id, option=option)

Get Settings

Get the settings of an account.<br> To get the settings of a ISV enabled Master Account, use `me` as the value for the `accountId` path parameter.<br><br>  **Prerequisites**:  * The Account must be a paid account.<br> **Scopes**: `account:read:admin` <br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.
option = 'option_example' # str | `meeting_authentication`: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.<br>`recording_authentication`: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. (optional)

try:
    # Get Settings
    api_response = api_instance.account_settings(account_id, option=option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 
 **option** | **str**| &#x60;meeting_authentication&#x60;: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.&lt;br&gt;&#x60;recording_authentication&#x60;: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings_update**
> account_settings_update(body, account_id, option=option)

Update Settings

Update the settings of a Sub Account that is under a Master Account.<br> To update the settings of the Master Account, use `me` as the value of the `accountId` path parameter.<br><br> **Prerequisites**:  * The Sub Account must be a paid account.<br> **Scopes**: `account:write:admin` <br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object | 
account_id = 'account_id_example' # str | The account ID.
option = 'option_example' # str |  (optional)

try:
    # Update Settings
    api_instance.account_settings_update(body, account_id, option=option)
except ApiException as e:
    print("Exception when calling AccountsApi->account_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **account_id** | **str**| The account ID. | 
 **option** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_trusted_domain**
> object account_trusted_domain(account_id)

Get Trusted Domains

Get trusted domains of a Sub Account. To get the trusted domains of a Master Account, use `me` as the value for the `accountId` path parameter.  **Prerequisites:**<br> * The Sub Account must be a paid account.<br> **Scope:** `account:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.

try:
    # Get Trusted Domains
    api_response = api_instance.account_trusted_domain(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_trusted_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts**
> AccountList accounts(page_size=page_size, page_number=page_number)

List Sub Accounts

List all the Sub Accounts under the Master Account.<br><br> Only Master Accounts can create and have Sub Accounts. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [ISV team](https://zoom.us/plan/api) for more details. <br> <br>**Prerequisites:**<br> * Pro or a higher paid account with Master Account option enabled. <br> **Scope**: `account:read:admin` <br>**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Sub Accounts
    api_response = api_instance.accounts(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**AccountList**](AccountList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_lock_settings**
> InlineResponse20070 get_account_lock_settings(account_id)

Get Locked Settings

[Account Locked Settings](https://support.zoom.us/hc/en-us/articles/115005269866) allow you turn settings on or off for all users in your account. No user except the account admin or account owner can change these settings. With lock settings, you force the settings on for all users. Use this API to retrieve an account's locked settings.   **Note:** This API can be used by Zoom Accounts that are on a Pro or a higher plan as well accounts that have Master and Sub Accounts options enabled. <br><br> **Prerequisites:** * Pro or a higher paid account. <br> **Scope**: `account:read:admin`. <br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>      **Scope:** account:read:admin

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \"me\" as the value of this field. <br> To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field.

try:
    # Get Locked Settings
    api_response = api_instance.get_account_lock_settings(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_lock_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \&quot;me\&quot; as the value of this field. &lt;br&gt; To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field. | 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_lock_settings**
> object update_account_lock_settings(account_id, body=body)

Update Locked Settings

[Account Locked Settings](https://support.zoom.us/hc/en-us/articles/115005269866) allow you turn settings on or off for all users in your account. No user except the account admin or account owner can change these settings. With lock settings, you force the settings on for all users. Use this API to update an account's locked settings.  **Note:** This API can be used by Zoom Accounts that are on a Pro or a higher plan as well accounts that have Master and Sub Accounts options enabled.<br><br> **Prerequisites:**<br> * Pro or a higher paid account. <br> **Scope:** `account:write:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>    

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \"me\" as the value of this field. <br> To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field.
body = swagger_client.Body131() # Body131 |  (optional)

try:
    # Update Locked Settings
    api_response = api_instance.update_account_lock_settings(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account_lock_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique Identifier of the account. To retrieve locked settings of the Master account or a regular account, provide \&quot;me\&quot; as the value of this field. &lt;br&gt; To retrieve locked settings of a Sub Account, provide the Account ID of the Sub Account in this field. | 
 **body** | [**Body131**](Body131.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_owner**
> object update_account_owner(account_id, body=body)

Update the Account Owner

The current account owner can [change the owner of an account](https://support.zoom.us/hc/en-us/articles/115005686983-Change-Account-Owner) to another user on the same account.<br> Use this API to change the owner of a Sub Account.  <aside>Your account must be a Master Account in order to use this API to update the account owner of a Sub Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the <a href=\"https://zoom.us/plan/api\">ISV team</a> for more details. Please note that the created account user will receive a confirmation email.</aside><br>   **Prerequisites**: <br> * Account owner or admin permissions of an account. * Pro or a higher plan with Master Account option enabled.<br> **Scopes:**  `account:write:admin` or `account:master`<br>**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>   <br> 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Account Id of the account.
body = swagger_client.Body135() # Body135 |  (optional)

try:
    # Update the Account Owner
    api_response = api_instance.update_account_owner(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id of the account. | 
 **body** | [**Body135**](Body135.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


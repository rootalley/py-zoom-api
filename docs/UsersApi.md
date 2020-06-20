# swagger_client.UsersApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**switch_user_account**](UsersApi.md#switch_user_account) | **PUT** /accounts/{accountId}/users/{userId}/account | Switch a User&#x27;s Account
[**user**](UsersApi.md#user) | **GET** /users/{userId} | Get a User
[**user_assistant_create**](UsersApi.md#user_assistant_create) | **POST** /users/{userId}/assistants | Add Assistants
[**user_assistant_delete**](UsersApi.md#user_assistant_delete) | **DELETE** /users/{userId}/assistants/{assistantId} | Delete a User Assistant
[**user_assistants**](UsersApi.md#user_assistants) | **GET** /users/{userId}/assistants | List User Assistants
[**user_assistants_delete**](UsersApi.md#user_assistants_delete) | **DELETE** /users/{userId}/assistants | Delete User Assistants
[**user_create**](UsersApi.md#user_create) | **POST** /users | Create Users
[**user_delete**](UsersApi.md#user_delete) | **DELETE** /users/{userId} | Delete User
[**user_email**](UsersApi.md#user_email) | **GET** /users/email | Check a User Email
[**user_email_update**](UsersApi.md#user_email_update) | **PUT** /users/{userId}/email | Update a User&#x27;s Email
[**user_password**](UsersApi.md#user_password) | **PUT** /users/{userId}/password | Update a User&#x27;s Password
[**user_permission**](UsersApi.md#user_permission) | **GET** /users/{userId}/permissions | Get User Permissions
[**user_picture**](UsersApi.md#user_picture) | **POST** /users/{userId}/picture | Upload a User&#x27;s Profile Picture
[**user_scheduler_delete**](UsersApi.md#user_scheduler_delete) | **DELETE** /users/{userId}/schedulers/{schedulerId} | Delete a Scheduler
[**user_schedulers**](UsersApi.md#user_schedulers) | **GET** /users/{userId}/schedulers | List User Schedulers
[**user_schedulers_delete**](UsersApi.md#user_schedulers_delete) | **DELETE** /users/{userId}/schedulers | Delete User Schedulers
[**user_settings**](UsersApi.md#user_settings) | **GET** /users/{userId}/settings | Get User Settings
[**user_settings_update**](UsersApi.md#user_settings_update) | **PATCH** /users/{userId}/settings | Update User Settings
[**user_sso_token_delete**](UsersApi.md#user_sso_token_delete) | **DELETE** /users/{userId}/token | Revoke a User&#x27;s SSO Token
[**user_status**](UsersApi.md#user_status) | **PUT** /users/{userId}/status | Update User Status
[**user_token**](UsersApi.md#user_token) | **GET** /users/{userId}/token | Get a User Token
[**user_update**](UsersApi.md#user_update) | **PATCH** /users/{userId} | Update User
[**user_vanity_name**](UsersApi.md#user_vanity_name) | **GET** /users/vanity_name | Check a User&#x27;s PM Room Name
[**users**](UsersApi.md#users) | **GET** /users | List Users

# **switch_user_account**
> object switch_user_account(user_id, account_id, body=body)

Switch a User's Account

Disassociate a user from one Account and move the user to another Account under the same Master Account.   With this API, a user under a Master Account or a Sub Account can be moved to another Sub Account within the same Master Account. To move a user from a Master Account to a Sub Account, use `me` as the value for `accountId`. In this scenario, \"me\" refers to the Account ID of the Master Account.   To move a user from one Sub Account to another Sub Account, provide the Sub Account's Account ID as the value for `accountId`.   **Prerequisites**: * The account should have Pro or a higher plan with Master Account option enabled. * The user whose account needs to be switched should not be an admin or an owner of that account. * The user should not have the same [managed domain](https://support.zoom.us/hc/en-us/articles/203395207-What-is-Managed-Domain-) as the account owner.  **Scope:** `user:master`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
account_id = 'account_id_example' # str | 
body = swagger_client.Body137() # Body137 |  (optional)

try:
    # Switch a User's Account
    api_response = api_instance.switch_user_account(user_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->switch_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**Body137**](Body137.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> InlineResponse20047 user(user_id, login_type=login_type)

Get a User

A Zoom account can have one or more users. Use this API to view information of a specific user on a Zoom account.<br><br> **Scopes:** `user:read:admin` `user:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>If a user's status is pending, only `id` and `created_at` fields will be returned. The value of `created_at` will be the time at which the API call was made until the user activates their account.</p>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
login_type = 'login_type_example' # str | `0` - Facebook.<br>`1` - Google.<br>`99` - API.<br>`100` - Zoom.<br>`101` - SSO. (optional)

try:
    # Get a User
    api_response = api_instance.user(user_id, login_type=login_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **login_type** | **str**| &#x60;0&#x60; - Facebook.&lt;br&gt;&#x60;1&#x60; - Google.&lt;br&gt;&#x60;99&#x60; - API.&lt;br&gt;&#x60;100&#x60; - Zoom.&lt;br&gt;&#x60;101&#x60; - SSO. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistant_create**
> InlineResponse20117 user_assistant_create(body, user_id)

Add Assistants

Assistants are the users to whom the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user as well as manage and act as an alternative host for all meetings if the admin has enabled [Co-host option](https://zoom.us/account/setting) on the account.<br>Use this API to assign assistants to a user. <br> In the request body, provide either the User ID or the email address of the user.<br><br> **Prerequisite**:  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.<br> **Scopes**: `user:write:admin` `user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAssistantsList1() # UserAssistantsList1 | User assistant.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Add Assistants
    api_response = api_instance.user_assistant_create(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAssistantsList1**](UserAssistantsList1.md)| User assistant. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20117**](InlineResponse20117.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistant_delete**
> user_assistant_delete(user_id, assistant_id)

Delete a User Assistant

Delete a specific assistant of a user. Assistants are the users to whom the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user as well as manage and act as an alternative host for all meetings if the admin has enabled [Co-host option](https://zoom.us/account/setting) on the account.<br><br> **Prerequisites**:  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.<br> **Scopes**: `user:write:admin` `user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
assistant_id = 'assistant_id_example' # str | Assistant ID.

try:
    # Delete a User Assistant
    api_instance.user_assistant_delete(user_id, assistant_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistant_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **assistant_id** | **str**| Assistant ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistants**
> UserAssistantsList user_assistants(user_id)

List User Assistants

List a user's assistants.  Assistants are the users to whom the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user as well as manage and act as an alternative host for all meetings if the admin has enabled [Co-host option](https://zoom.us/account/setting) on the account.<br><br> **Prerequisites**: <br> * Current user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.<br> **Scopes**: `user:read:admin` `user:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # List User Assistants
    api_response = api_instance.user_assistants(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**UserAssistantsList**](UserAssistantsList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_assistants_delete**
> user_assistants_delete(user_id)

Delete User Assistants

Delete all assistants of the current user.<br> Assistants are the users to whom the current user has assigned [scheduling privilege](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-Privilege). These assistants can schedule meeting on behalf of the current user as well as manage and act as an alternative host for all meetings if the admin has enabled [Co-host option](https://zoom.us/account/setting) on the account.<br> **Prerequisite**:  * The user as well as the assistant must have Licensed or an On-prem license. * Assistants must be under the current user's account.<br> **Scopes**: `user:write:admin` `user:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Delete User Assistants
    api_instance.user_assistants_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_assistants_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> InlineResponse20116 user_create(body)

Create Users

A Zoom account can have one or more users. Use this API to add a new user to your account.<br><br> **Prerequisites:**<br> * Pro or higher plan<br><br> **Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body78() # Body78 | User

try:
    # Create Users
    api_response = api_instance.user_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body78**](Body78.md)| User | 

### Return type

[**InlineResponse20116**](InlineResponse20116.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(user_id, action=action, transfer_email=transfer_email, transfer_meeting=transfer_meeting, transfer_webinar=transfer_webinar, transfer_recording=transfer_recording)

Delete User

Deleting a user permanently removes them and their data from Zoom. They will be able to create a new Zoom account with the same email address if they have access to it. An account owner or an account admin can transfer meetings, webinars and cloud recordings to another Zoom user before deleting, but if not transferred, they will be permanently deleted.<br><br>  By default, this API disassociates (unlinks) a user from the associated account. The disassociation will give them their own basic, free Zoom account. It will not be associated with your account, and they will be able to purchase their own licenses. You can transfer the user's data (meetings, webinars and cloud recordings) to another user before disassociation.<br> To permanently delete a user, specify \"delete\" as the value of the `action` query parameter. **Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
action = 'disassociate' # str | Delete action options:<br>`disassociate` - Disassociate a user.<br>`delete`-  Permanently delete a user.<br>Note: To delete pending user in the account, use `disassociate` (optional) (default to disassociate)
transfer_email = 'transfer_email_example' # str | Transfer email. (optional)
transfer_meeting = true # bool | Transfer meeting. (optional)
transfer_webinar = true # bool | Transfer webinar. (optional)
transfer_recording = true # bool | Transfer recording. (optional)

try:
    # Delete User
    api_instance.user_delete(user_id, action=action, transfer_email=transfer_email, transfer_meeting=transfer_meeting, transfer_webinar=transfer_webinar, transfer_recording=transfer_recording)
except ApiException as e:
    print("Exception when calling UsersApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **action** | **str**| Delete action options:&lt;br&gt;&#x60;disassociate&#x60; - Disassociate a user.&lt;br&gt;&#x60;delete&#x60;-  Permanently delete a user.&lt;br&gt;Note: To delete pending user in the account, use &#x60;disassociate&#x60; | [optional] [default to disassociate]
 **transfer_email** | **str**| Transfer email. | [optional] 
 **transfer_meeting** | **bool**| Transfer meeting. | [optional] 
 **transfer_webinar** | **bool**| Transfer webinar. | [optional] 
 **transfer_recording** | **bool**| Transfer recording. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_email**
> InlineResponse20052 user_email(email)

Check a User Email

Verify if a user's email is registered with Zoom.<br><br> <p style=\"background-color:#ffffcc; color:#01579b; padding:8px\"> <b>Note: </b>Starting November 17, 2019, the behavior of this API will change so that you will be able to successfully check to see if a user is a registered Zoom user only if the user is within your account. If you provide an email address of a user who is not in your account, the value of \"existed_email\" parameter will be \"false\" irrespective of whether or not the user is registered with Zoom. </p>  **Scopes:** `user:read:admin` `user:read`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
email = 'email_example' # str | The email address to be verified.

try:
    # Check a User Email
    api_response = api_instance.user_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address to be verified. | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_email_update**
> user_email_update(body, user_id)

Update a User's Email

Change a user's [email address](https://support.zoom.us/hc/en-us/articles/201362563-How-Do-I-Change-the-Email-on-My-Account-) on a Zoom account that has managed domain set up.<br>If the Zoom Account in which the user belongs, has multiple [managed domains](https://support.zoom.us/hc/en-us/articles/203395207-What-is-Managed-Domain-), the email to be updated must match one of the managed domains.<br> **Scopes:** `user:write:admin` `user:write`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> >  Note: A user's email address can only be changed for a maximum of 3 times in a day(24 hours). **Prerequisite:**<br> * Managed domain must be enabled in the account. * The new email address should not already exist in Zoom.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body87() # Body87 | User email.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Update a User's Email
    api_instance.user_email_update(body, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_email_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body87**](Body87.md)| User email. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_password**
> user_password(body, user_id)

Update a User's Password

Update the [password](https://support.zoom.us/hc/en-us/articles/206344385-Change-a-User-s-Password) of a user using which the user can login to Zoom.<br> After this request is processed successfully, an email notification will be sent to the user stating that the password was changed.<br> **Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` **Prerequisites:**<br> * Owner or admin of the Zoom account.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body85() # Body85 | User password.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Update a User's Password
    api_instance.user_password(body, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body85**](Body85.md)| User password. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_permission**
> InlineResponse20048 user_permission(user_id)

Get User Permissions

Users can be assigned a set of permissions that allows them to access only the pages/information that a user needs to view or edit.<br>  Use this API to get permissions that have been granted to the user.<br><br> **Scopes:** `user:read:admin` `user:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Get User Permissions
    api_response = api_instance.user_permission(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_picture**
> user_picture(pic_file, user_id)

Upload a User's Profile Picture

Upload a user's profile picture.<br><br>  Provide `multipart/form-data` as the value of the `content-type` header for this request.   **Scopes:** `user:write:admin` `user:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
pic_file = 'pic_file_example' # str | 
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Upload a User's Profile Picture
    api_instance.user_picture(pic_file, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pic_file** | **str**|  | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_scheduler_delete**
> user_scheduler_delete(user_id, scheduler_id)

Delete a Scheduler

Delete a Scheduler.  Schedulers are users on whose behalf the current user (assistant) can schedule meetings for. By calling this API, the current user will no longer be a scheduling assistant of this scheduler.   **Prerequisite**: Current user must be under the same account as the scheduler.<br> **Scopes**: `user:write:admin` `user:write`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
scheduler_id = 'scheduler_id_example' # str | Scheduler's ID.

try:
    # Delete a Scheduler
    api_instance.user_scheduler_delete(user_id, scheduler_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_scheduler_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **scheduler_id** | **str**| Scheduler&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_schedulers**
> UserSchedulersList user_schedulers(user_id)

List User Schedulers

List all the schedulers of a user. Schedulers in this context are the users for whom the current user can schedule meetings for.  For instance, if the current user (i.e., the user whose userId was passed in the path parameter of this API call) is user A, the response of this API will contain a list of user(s), for whom user A can schedule and manage meetings. User A is the assistant of these users and thus has scheduling privilege for these user(s).   **Prerequisites**: * Current user must be under the same account as the scheduler.<br> **Scopes**: `user:read:admin` `user:read`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # List User Schedulers
    api_response = api_instance.user_schedulers(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**UserSchedulersList**](UserSchedulersList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_schedulers_delete**
> user_schedulers_delete(user_id)

Delete User Schedulers

Delete all of a user's schedulers. Schedulers are users on whose behalf the current user (assistant) can schedule meetings for. By calling this API, the current user will no longer be a scheduling assistant of any user.   **Prerequisite**: Current user (assistant) must be under the same account as the scheduler.<br> **Scopes**: `user:write:admin` `user:write`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Delete User Schedulers
    api_instance.user_schedulers_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_schedulers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings**
> object user_settings(user_id, login_type=login_type, option=option)

Get User Settings

Retrieve a user's settings.<br><br> **Scopes:** `user:read:admin` `user:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
login_type = 'login_type_example' # str | `0` - Facebook.<br>`1` - Google.<br>`99` - API.<br>`100` - Zoom.<br>`101` - SSO. (optional)
option = 'option_example' # str | `meeting_authentication`: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.<br>`recording_authentication`: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. (optional)

try:
    # Get User Settings
    api_response = api_instance.user_settings(user_id, login_type=login_type, option=option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **login_type** | **str**| &#x60;0&#x60; - Facebook.&lt;br&gt;&#x60;1&#x60; - Google.&lt;br&gt;&#x60;99&#x60; - API.&lt;br&gt;&#x60;100&#x60; - Zoom.&lt;br&gt;&#x60;101&#x60; - SSO. | [optional] 
 **option** | **str**| &#x60;meeting_authentication&#x60;: Use this query parameter to view [meeting authentication configuration](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) applied on the account.&lt;br&gt;&#x60;recording_authentication&#x60;: Use this query parameter to view [recording authentication configuration](https://support.zoom.us/hc/en-us/articles/360037756671-Authentication-Profiles-for-Cloud-Recordings) applied on the account. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_update**
> user_settings_update(body, user_id, option=option)

Update User Settings

Update a user's settings.<br><br> **Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = NULL # object | User Settings
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
option = 'option_example' # str |  (optional)

try:
    # Update User Settings
    api_instance.user_settings_update(body, user_id, option=option)
except ApiException as e:
    print("Exception when calling UsersApi->user_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| User Settings | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **option** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_sso_token_delete**
> user_sso_token_delete(user_id)

Revoke a User's SSO Token

Revoke a user's SSO token.<br><br> After calling this API, the SSO user will be logged out of their current Zoom session.<br> **Scopes:** `user:write:admin` `user:write`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Revoke a User's SSO Token
    api_instance.user_sso_token_delete(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_sso_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_status**
> user_status(body, user_id)

Update User Status

An account owner or admins can deactivate as well as activate a user in a Zoom account. Deactivating a user will remove all licenses associated with a user. It will prevent the deactivated user from logging into their Zoom account. A deactivated user can be reactivated. Reactivating a user grants the user access to login to their Zoom account.<br> Use this API to either [deactivate](https://support.zoom.us/hc/en-us/articles/115005269946-Remove-User-from-your-Account#h_6a9bc1c3-d739-4945-b1f2-00b3b88fb5cc) an active user or to [reactivate](https://support.zoom.us/hc/en-us/articles/115005269946-Remove-User-from-your-Account#h_16319724-d120-4be6-af5d-31582d134ea0) a deactivated user .<br><br>**Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body83() # Body83 | User status.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Update User Status
    api_instance.user_status(body, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body83**](Body83.md)| User status. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token**
> InlineResponse20051 user_token(user_id, type=type, ttl=ttl)

Get a User Token

Retrieve a user's token.<br><br> This token is used for starting meetings with the Client SDK.<br> **Scopes:** `user:read:admin` `user:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` If a user signed into Zoom using Google or Facebook, a null value will be returned for the token. To get the token with this API, ask the user to sign into Zoom using their email and password instead.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
type = 'type_example' # str | User token types:<br>`token` - Used for starting meetings with the client SDK. This token expires in 14 days and a new token will be returned after the expiry.<br>`zak` - Used for generating the start meeting URL. The token expiration time is two hours. For API users, the expiration time is 90 days. (optional)
ttl = 56 # int | Use this field in conjunction with the `type` field where the value of `type` field is `zak`. The value of this field denotes the expiry time of the `zak` token in seconds. For example, if you would like the zak token to be expired after one hour of the token generation, the value of this field should be `3600`. (optional)

try:
    # Get a User Token
    api_response = api_instance.user_token(user_id, type=type, ttl=ttl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **type** | **str**| User token types:&lt;br&gt;&#x60;token&#x60; - Used for starting meetings with the client SDK. This token expires in 14 days and a new token will be returned after the expiry.&lt;br&gt;&#x60;zak&#x60; - Used for generating the start meeting URL. The token expiration time is two hours. For API users, the expiration time is 90 days. | [optional] 
 **ttl** | **int**| Use this field in conjunction with the &#x60;type&#x60; field where the value of &#x60;type&#x60; field is &#x60;zak&#x60;. The value of this field denotes the expiry time of the &#x60;zak&#x60; token in seconds. For example, if you would like the zak token to be expired after one hour of the token generation, the value of this field should be &#x60;3600&#x60;. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> user_update(body, user_id, login_type=login_type)

Update User

Update information on a user's Zoom [profile](https://support.zoom.us/hc/en-us/articles/201363203-My-Profile).<br><br> **Scopes:** `user:write:admin` `user:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body80() # Body80 | User
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
login_type = 'login_type_example' # str | `0` - Facebook.<br>`1` - Google.<br>`99` - API.<br>`100` - Zoom.<br>`101` - SSO. (optional)

try:
    # Update User
    api_instance.user_update(body, user_id, login_type=login_type)
except ApiException as e:
    print("Exception when calling UsersApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body80**](Body80.md)| User | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **login_type** | **str**| &#x60;0&#x60; - Facebook.&lt;br&gt;&#x60;1&#x60; - Google.&lt;br&gt;&#x60;99&#x60; - API.&lt;br&gt;&#x60;100&#x60; - Zoom.&lt;br&gt;&#x60;101&#x60; - SSO. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_vanity_name**
> InlineResponse20053 user_vanity_name(vanity_name)

Check a User's PM Room Name

A personal meeting room is a virtual meeting room that can be permanently assigned to a user. Use this API to check if a personal meeting room with the given name exists or not.<br><br> **Scopes:** `user:read:admin` `user:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
vanity_name = 'vanity_name_example' # str | Personal meeting room name.

try:
    # Check a User's PM Room Name
    api_response = api_instance.user_vanity_name(vanity_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_vanity_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanity_name** | **str**| Personal meeting room name. | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users**
> InlineResponse20046 users(status=status, page_size=page_size, page_number=page_number, role_id=role_id)

List Users

A Zoom account can have one or more users. Use this API to list users on your account.<br><br> **Scopes:** `user:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
status = 'active' # str | User statuses:<br>`active` - Users with an active status.<br>`inactive` - Users with an inactive status.<br>`pending` - Users with a pending status. (optional) (default to active)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)
role_id = 'role_id_example' # str | Unique identifier for the role. Provide this parameter if you would like to filter the response by a specific role. You can retrieve Role IDs from [List Roles](https://marketplace.zoom.us/docs/api-reference/zoom-api/roles/roles) API.  (optional)

try:
    # List Users
    api_response = api_instance.users(status=status, page_size=page_size, page_number=page_number, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| User statuses:&lt;br&gt;&#x60;active&#x60; - Users with an active status.&lt;br&gt;&#x60;inactive&#x60; - Users with an inactive status.&lt;br&gt;&#x60;pending&#x60; - Users with a pending status. | [optional] [default to active]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]
 **role_id** | **str**| Unique identifier for the role. Provide this parameter if you would like to filter the response by a specific role. You can retrieve Role IDs from [List Roles](https://marketplace.zoom.us/docs/api-reference/zoom-api/roles/roles) API.  | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


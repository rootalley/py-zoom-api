# swagger_client.WebinarsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tracking_sources**](WebinarsApi.md#get_tracking_sources) | **GET** /webinars/{webinarId}/tracking_sources | Get Webinar Tracking Sources
[**list_past_webinar_files**](WebinarsApi.md#list_past_webinar_files) | **GET** /past_webinars/{webinarId}/files | List Past Webinar Files
[**list_past_webinar_poll_results**](WebinarsApi.md#list_past_webinar_poll_results) | **GET** /past_webinars/{webinarId}/polls | List Past Webinar Poll Results
[**list_past_webinar_qa**](WebinarsApi.md#list_past_webinar_qa) | **GET** /past_webinars/{webinarId}/qa | List Q&amp;A of Past Webinar
[**past_webinars**](WebinarsApi.md#past_webinars) | **GET** /past_webinars/{webinarId}/instances | List Past Webinar Instances
[**webinar**](WebinarsApi.md#webinar) | **GET** /webinars/{webinarId} | Get a Webinar
[**webinar_absentees**](WebinarsApi.md#webinar_absentees) | **GET** /past_webinars/{WebinarUUID}/absentees | Get Webinar Absentees
[**webinar_create**](WebinarsApi.md#webinar_create) | **POST** /users/{userId}/webinars | Create a Webinar
[**webinar_delete**](WebinarsApi.md#webinar_delete) | **DELETE** /webinars/{webinarId} | Delete a Webinar
[**webinar_panelist_create**](WebinarsApi.md#webinar_panelist_create) | **POST** /webinars/{webinarId}/panelists | Add Panelists
[**webinar_panelist_delete**](WebinarsApi.md#webinar_panelist_delete) | **DELETE** /webinars/{webinarId}/panelists/{panelistId} | Remove a Panelist
[**webinar_panelists**](WebinarsApi.md#webinar_panelists) | **GET** /webinars/{webinarId}/panelists | List Panelists
[**webinar_panelists_delete**](WebinarsApi.md#webinar_panelists_delete) | **DELETE** /webinars/{webinarId}/panelists | Remove Panelists
[**webinar_poll_create**](WebinarsApi.md#webinar_poll_create) | **POST** /webinars/{webinarId}/polls | Create a Webinar&#x27;s Poll
[**webinar_poll_delete**](WebinarsApi.md#webinar_poll_delete) | **DELETE** /webinars/{webinarId}/polls/{pollId} | Delete a Webinar Poll
[**webinar_poll_get**](WebinarsApi.md#webinar_poll_get) | **GET** /webinars/{webinarId}/polls/{pollId} | Get a Webinar Poll
[**webinar_poll_update**](WebinarsApi.md#webinar_poll_update) | **PUT** /webinars/{webinarId}/polls/{pollId} | Update a Webinar Poll
[**webinar_polls**](WebinarsApi.md#webinar_polls) | **GET** /webinars/{webinarId}/polls | List a Webinar&#x27;s Polls 
[**webinar_registrant_create**](WebinarsApi.md#webinar_registrant_create) | **POST** /webinars/{webinarId}/registrants | Add a Webinar Registrant
[**webinar_registrant_get**](WebinarsApi.md#webinar_registrant_get) | **GET** /webinars/{webinarId}/registrants/{registrantId} | Get a Webinar Registrant
[**webinar_registrant_question_update**](WebinarsApi.md#webinar_registrant_question_update) | **PATCH** /webinars/{webinarId}/registrants/questions | Update Registration Questions
[**webinar_registrant_status**](WebinarsApi.md#webinar_registrant_status) | **PUT** /webinars/{webinarId}/registrants/status | Update Webinar Registrant Status
[**webinar_registrants**](WebinarsApi.md#webinar_registrants) | **GET** /webinars/{webinarId}/registrants | List Webinar Registrants
[**webinar_registrants_questions_get**](WebinarsApi.md#webinar_registrants_questions_get) | **GET** /webinars/{webinarId}/registrants/questions | List Registration Questions
[**webinar_status**](WebinarsApi.md#webinar_status) | **PUT** /webinars/{webinarId}/status | Update Webinar Status
[**webinar_update**](WebinarsApi.md#webinar_update) | **PATCH** /webinars/{webinarId} | Update a Webinar
[**webinars**](WebinarsApi.md#webinars) | **GET** /users/{userId}/webinars | List Webinars

# **get_tracking_sources**
> InlineResponse20074 get_tracking_sources(webinar_id)

Get Webinar Tracking Sources

[Webinar Registration Tracking Sources](https://support.zoom.us/hc/en-us/articles/360000315683-Webinar-Registration-Source-Tracking) allow you to see where your registrants are coming from if you share the webinar registration page in multiple platforms. You can then use the source tracking to see the number of registrants generated from each platform.<br> Use this API to list information on all the tracking sources of a Webinar.<br> **Scopes:** `webinar:read:admin`, `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites**:<br> * [Webinar license](https://zoom.us/webinar). * Registration must be required for the Webinar. 

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Get Webinar Tracking Sources
    api_response = api_instance.get_tracking_sources(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->get_tracking_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_webinar_files**
> InlineResponse20084 list_past_webinar_files(webinar_id)

List Past Webinar Files

List files sent via in-meeting chat during a meeting. The in-meeting files are deleted after 24 hours of the meeting completion time.  <br><br> **Scope:** `webinar:read`, `webinar:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | 

try:
    # List Past Webinar Files
    api_response = api_instance.list_past_webinar_files(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_past_webinar_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**|  | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_webinar_poll_results**
> InlineResponse20085 list_past_webinar_poll_results(webinar_id)

List Past Webinar Poll Results

The polling feature for webinar allows you to create single choice or multiple choice polling questions for your webinars. Use this API to retrieve the results for Webinar Polls of a specific Webinar.  **Prerequisites:**<br> * [Webinar license](https://zoom.us/webinar)<br> **Scopes**: `webinar:read:admin`, `webinar:read`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The Webinar ID or Webinar UUID. If the webinar ID is passed, it will take the last webinar instance.

try:
    # List Past Webinar Poll Results
    api_response = api_instance.list_past_webinar_poll_results(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_past_webinar_poll_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The Webinar ID or Webinar UUID. If the webinar ID is passed, it will take the last webinar instance. | 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_webinar_qa**
> InlineResponse20086 list_past_webinar_qa(webinar_id)

List Q&A of Past Webinar

The [Question & Answer (Q&A)](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) feature for Webinars allows attendees to ask questions during the Webinar and for the panelists, co-hosts and host to answer their questions.<br> Use this API to list Q&A of a specific Webinar.  **Prerequisites:**<br> * [Webinar license](https://zoom.us/webinar)<br> **Scopes**: `webinar:read:admin`, `webinar:read`<br>  <br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The Webinar ID or Webinar UUID. If the webinar ID is passed, it will take the last webinar instance.

try:
    # List Q&A of Past Webinar
    api_response = api_instance.list_past_webinar_qa(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->list_past_webinar_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The Webinar ID or Webinar UUID. If the webinar ID is passed, it will take the last webinar instance. | 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_webinars**
> object past_webinars(webinar_id)

List Past Webinar Instances

List past webinar instances.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # List Past Webinar Instances
    api_response = api_instance.past_webinars(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->past_webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar**
> InlineResponse20054 webinar(webinar_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)

Get a Webinar

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees.<br>Use this API to get details of a scheduled webinar.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>**Prerequisites:** * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_id = 'occurrence_id_example' # str | Unique Identifier that identifies an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences. When you create a recurring Webinar using [Create a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarcreate), you can retrieve the Occurrence ID from the response of the API call. (optional)
show_previous_occurrences = true # bool | Set the value of this field to `true` if you would like to view Webinar details of all previous occurrences of a recurring Webinar. (optional)

try:
    # Get a Webinar
    api_response = api_instance.webinar(webinar_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_id** | **str**| Unique Identifier that identifies an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences. When you create a recurring Webinar using [Create a Webinar API](https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarcreate), you can retrieve the Occurrence ID from the response of the API call. | [optional] 
 **show_previous_occurrences** | **bool**| Set the value of this field to &#x60;true&#x60; if you would like to view Webinar details of all previous occurrences of a recurring Webinar. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_absentees**
> RegistrationList webinar_absentees(webinar_uuid, occurrence_id=occurrence_id, page_size=page_size, next_page_token=next_page_token)

Get Webinar Absentees

List absentees of a webinar.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_uuid = 'webinar_uuid_example' # str | The Webinar UUID. Each Webinar instance will generate its own Webinar UUID (i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). Please double encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Webinar Absentees
    api_response = api_instance.webinar_absentees(webinar_uuid, occurrence_id=occurrence_id, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_absentees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_uuid** | **str**| The Webinar UUID. Each Webinar instance will generate its own Webinar UUID (i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). Please double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27; in it. | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**RegistrationList**](RegistrationList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_create**
> InlineResponse20118 webinar_create(body, user_id)

Create a Webinar

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees.<br>Use this API to schedule a Webinar for a user (host).<br><br>  **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body89() # Body89 | 
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Create a Webinar
    api_response = api_instance.webinar_create(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body89**](Body89.md)|  | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20118**](InlineResponse20118.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_delete**
> webinar_delete(webinar_id, occurrence_id=occurrence_id)

Delete a Webinar

Delete a Webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)

try:
    # Delete a Webinar
    api_instance.webinar_delete(webinar_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelist_create**
> webinar_panelist_create(body, webinar_id)

Add Panelists

Panelists in a Webinar can view and send video, screen share, annotate, etc and do much more compared to attendees in a webinar.<br>Use this API to [add panelists](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_7550d59e-23f5-4703-9e22-e76bded1ed70) to a scheduled webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>   **Prerequisites:** * Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).<br> 

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body95() # Body95 | 
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Add Panelists
    api_instance.webinar_panelist_create(body, webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelist_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body95**](Body95.md)|  | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelist_delete**
> webinar_panelist_delete(webinar_id, panelist_id)

Remove a Panelist

[Remove](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_de31f237-a91c-4fb2-912b-ecfba8ec5ffb) a single panelist from a webinar.<br> You can retrieve the `panelistId` by calling **List Panelists API**.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>   **Prerequisites:**<br> * Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).<br> 

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
panelist_id = 56 # int | The panelist ID or panelist email.

try:
    # Remove a Panelist
    api_instance.webinar_panelist_delete(webinar_id, panelist_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelist_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **panelist_id** | **int**| The panelist ID or panelist email. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelists**
> InlineResponse20055 webinar_panelists(webinar_id)

List Panelists

Panelists in a Webinar can view and send video, screen share, annotate, etc and do much more compared to attendees in a Webinar.   Use this API to list all the panelists of a Webinar.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:**<br> * Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).<br> 

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # List Panelists
    api_response = api_instance.webinar_panelists(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_panelists_delete**
> webinar_panelists_delete(webinar_id)

Remove Panelists

Remove all the panelists from a Webinar.<br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).<br> 

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Remove Panelists
    api_instance.webinar_panelists_delete(webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_panelists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_create**
> InlineResponse20121 webinar_poll_create(body, webinar_id)

Create a Webinar's Poll

Create a [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) for a webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body101() # Body101 | Webinar poll object
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Create a Webinar's Poll
    api_response = api_instance.webinar_poll_create(body, webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body101**](Body101.md)| Webinar poll object | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

[**InlineResponse20121**](InlineResponse20121.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_delete**
> webinar_poll_delete(webinar_id, poll_id)

Delete a Webinar Poll

Delete a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Delete a Webinar Poll
    api_instance.webinar_poll_delete(webinar_id, poll_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_get**
> InlineResponse20121 webinar_poll_get(webinar_id, poll_id)

Get a Webinar Poll

Get a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) details.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Get a Webinar Poll
    api_response = api_instance.webinar_poll_get(webinar_id, poll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **poll_id** | **str**| The poll ID | 

### Return type

[**InlineResponse20121**](InlineResponse20121.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_poll_update**
> webinar_poll_update(body, webinar_id, poll_id)

Update a Webinar Poll

Update a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body103() # Body103 | Webinar Poll
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Update a Webinar Poll
    api_instance.webinar_poll_update(body, webinar_id, poll_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_poll_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body103**](Body103.md)| Webinar Poll | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_polls**
> object webinar_polls(webinar_id)

List a Webinar's Polls 

List all the [polls](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) of a Webinar.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # List a Webinar's Polls 
    api_response = api_instance.webinar_polls(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_create**
> InlineResponse20120 webinar_registrant_create(body, webinar_id, occurrence_ids=occurrence_ids)

Add a Webinar Registrant

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [Webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the Webinar.<br>Use this API to create and submit the registration of a user for a webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body97() # Body97 | 
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_ids = 'occurrence_ids_example' # str | Occurrence ID. Get this value from the webinar get API. Multiple values separated by a comma. (optional)

try:
    # Add a Webinar Registrant
    api_response = api_instance.webinar_registrant_create(body, webinar_id, occurrence_ids=occurrence_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body97**](Body97.md)|  | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_ids** | **str**| Occurrence ID. Get this value from the webinar get API. Multiple values separated by a comma. | [optional] 

### Return type

[**InlineResponse20120**](InlineResponse20120.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_get**
> WebianrRegistrant webinar_registrant_get(webinar_id, registrant_id, occurrence_id=occurrence_id)

Get a Webinar Registrant

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [Webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the Webinar.<br>Use this API to get details on a specific user who has registered for the Webinar.<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * The account must have a Webinar plan.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
registrant_id = 'registrant_id_example' # str | The registrant ID.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)

try:
    # Get a Webinar Registrant
    api_response = api_instance.webinar_registrant_get(webinar_id, registrant_id, occurrence_id=occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **registrant_id** | **str**| The registrant ID. | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 

### Return type

[**WebianrRegistrant**](WebianrRegistrant.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_question_update**
> webinar_registrant_question_update(body, webinar_id)

Update Registration Questions

Scheduling a [Webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the Webinar.<br>Use this API to update registration questions and fields of a scheduled Webinar that are to be answered by users while registering for a Webinar.<br><br> **Prerequisites:**<br>   * Pro or higher plan with a Webinar Add-on. * Registration option for Webinar should be set as required to use this API.  **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body105() # Body105 | Webinar Registrant Questions
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Update Registration Questions
    api_instance.webinar_registrant_question_update(body, webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body105**](Body105.md)| Webinar Registrant Questions | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrant_status**
> webinar_registrant_status(body, webinar_id, occurrence_id=occurrence_id)

Update Webinar Registrant Status

Update a webinar registrant's status. Using this API, you can specify whether you want to approve a registration, deny a registration or cancel a previously approved registration.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body99() # Body99 | 
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)

try:
    # Update Webinar Registrant Status
    api_instance.webinar_registrant_status(body, webinar_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body99**](Body99.md)|  | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrants**
> RegistrationList webinar_registrants(webinar_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number)

List Webinar Registrants

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [Webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the Webinar.<br> Use this API to list all the users that have registered for a webinar.<br><br> **Prerequisites:** * Pro or higher plan with a Webinar Add-on.<br> **Scopes:** `webinar:read:admin` `webinar:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)
status = 'approved' # str | The registrant status:<br>`pending` - Registrant's status is pending.<br>`approved` - Registrant's status is approved.<br>`denied` - Registrant's status is denied. (optional) (default to approved)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Webinar Registrants
    api_response = api_instance.webinar_registrants(webinar_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 
 **status** | **str**| The registrant status:&lt;br&gt;&#x60;pending&#x60; - Registrant&#x27;s status is pending.&lt;br&gt;&#x60;approved&#x60; - Registrant&#x27;s status is approved.&lt;br&gt;&#x60;denied&#x60; - Registrant&#x27;s status is denied. | [optional] [default to approved]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**RegistrationList**](RegistrationList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_registrants_questions_get**
> InlineResponse20056 webinar_registrants_questions_get(webinar_id)

List Registration Questions

Scheduling a [Webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the Webinar.<br>Use this API to list registration questions and fields that are to be answered by users while registering for a Webinar.<br> **Prerequisites:**<br>   * Pro or higher plan with a Webinar Add-on. **Scopes:** `webinar:read:admin` `webinar:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br>  

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # List Registration Questions
    api_response = api_instance.webinar_registrants_questions_get(webinar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_status**
> webinar_status(body, webinar_id)

Update Webinar Status

Update a webinar's status. Use this API to end an ongoing webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * The account must hold a valid [Webinar plan](https://zoom.us/webinar).

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body93() # Body93 | 
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 

try:
    # Update Webinar Status
    api_instance.webinar_status(body, webinar_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body93**](Body93.md)|  | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinar_update**
> webinar_update(body, webinar_id, occurrence_id=occurrence_id)

Update a Webinar

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees.<br> Use this API to make updates to a scheduled Webinar.<br><br> **Scopes:** `webinar:write:admin` `webinar:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:**<br> * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body91() # Body91 | Webinar.
webinar_id = 789 # int | The webinar ID in \"**long**\" format(represented as int64 data type in JSON). 
occurrence_id = 'occurrence_id_example' # str | Webinar occurrence id. Support change of agenda, start_time, duration, settings: {host_video, panelist_video, hd_video, watermark, auto_recording} (optional)

try:
    # Update a Webinar
    api_instance.webinar_update(body, webinar_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinar_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body91**](Body91.md)| Webinar. | 
 **webinar_id** | **int**| The webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON).  | 
 **occurrence_id** | **str**| Webinar occurrence id. Support change of agenda, start_time, duration, settings: {host_video, panelist_video, hd_video, watermark, auto_recording} | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webinars**
> UserList webinars(user_id, page_size=page_size, page_number=page_number)

List Webinars

Zoom users with a [Webinar Plan](https://zoom.us/webinar) have access to creating and managing Webinars. Webinar allows a host to broadcast a Zoom meeting to up to 10,000 attendees.<br> Use this API to list all the webinars that are scheduled by or on-behalf a user (Webinar host).<br><br> **Scopes:** `webinar:read:admin` `webinar:read`<br> <br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` **Prerequisites:** * Pro or higher plan with a Webinar Add-on.

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
api_instance = swagger_client.WebinarsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Webinars
    api_response = api_instance.webinars(user_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebinarsApi->webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**UserList**](UserList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


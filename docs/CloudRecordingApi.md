# swagger_client.CloudRecordingApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_cloud_recording**](CloudRecordingApi.md#get_account_cloud_recording) | **GET** /accounts/{accountId}/recordings | List Recordings of an Account
[**meeting_recording_registrant_create**](CloudRecordingApi.md#meeting_recording_registrant_create) | **POST** /meetings/{meetingId}/recordings/registrants | Create a Recording Registrant
[**meeting_recording_registrant_status**](CloudRecordingApi.md#meeting_recording_registrant_status) | **PUT** /meetings/{meetingId}/recordings/registrants/status | Update Recording Registrant&#x27;s Status
[**meeting_recording_registrants**](CloudRecordingApi.md#meeting_recording_registrants) | **GET** /meetings/{meetingId}/recordings/registrants | List Recording Registrants
[**recording_delete**](CloudRecordingApi.md#recording_delete) | **DELETE** /meetings/{meetingId}/recordings | Delete Meeting Recordings
[**recording_delete_one**](CloudRecordingApi.md#recording_delete_one) | **DELETE** /meetings/{meetingId}/recordings/{recordingId} | Delete a Meeting Recording File
[**recording_get**](CloudRecordingApi.md#recording_get) | **GET** /meetings/{meetingId}/recordings | Get Meeting Recordings
[**recording_registrant_question_update**](CloudRecordingApi.md#recording_registrant_question_update) | **PATCH** /meetings/{meetingId}/recordings/registrants/questions | Update Registration Questions
[**recording_registrants_questions_get**](CloudRecordingApi.md#recording_registrants_questions_get) | **GET** /meetings/{meetingId}/recordings/registrants/questions | Get Registration Questions
[**recording_setting_update**](CloudRecordingApi.md#recording_setting_update) | **GET** /meetings/{meetingId}/recordings/settings | Get Meeting Recording Settings
[**recording_settings_update**](CloudRecordingApi.md#recording_settings_update) | **PATCH** /meetings/{meetingId}/recordings/settings | Update Meeting Recording Settings
[**recording_status_update**](CloudRecordingApi.md#recording_status_update) | **PUT** /meetings/{meetingId}/recordings/status | Recover Meeting Recordings
[**recording_status_update_one**](CloudRecordingApi.md#recording_status_update_one) | **PUT** /meetings/{meetingId}/recordings/{recordingId}/status | Recover a Single Recording
[**recordings_list**](CloudRecordingApi.md#recordings_list) | **GET** /users/{userId}/recordings | List All Recordings

# **get_account_cloud_recording**
> InlineResponse20073 get_account_cloud_recording(account_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)

List Recordings of an Account

List [Cloud Recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) available on an Account.  > To access a password protected cloud recording, add an \"access_token\" parameter to the download URL and provide [JWT](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-jwt-app) as the value of the \"access_token\". <br> **Prerequisites**:<br> * A Pro or a higher paid plan with Cloud Recording option enabled.<br> **Scopes**: `recording:read:admin` or `account:read:admin`  If the scope `recording:read:admin` is used, the Account ID of the Account must be provided in the `accountId` path parameter to list recordings that belong to the Account. This scope only works for Sub Accounts.   To list recordings of a Master Account, the scope must be `account:read:admin` and the value of `accountId` should be `me`.<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique identifier of the account.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | The start date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | The end date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. (optional)

try:
    # List Recordings of an Account
    api_response = api_instance.get_account_cloud_recording(account_id, page_size=page_size, next_page_token=next_page_token, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->get_account_cloud_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique identifier of the account. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **_from** | **datetime**| The start date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. | [optional] 
 **to** | **datetime**| The end date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrant_create**
> InlineResponse20113 meeting_recording_registrant_create(body, meeting_id)

Create a Recording Registrant

Cloud Recordings of past Zoom Meetings can be made [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings). Users should be [registered](https://marketplace.zoom.us/docs/api-reference/zoom-api/cloud-recording/meetingrecordingregistrantcreate) to view these recordings.  Use this API to register a user to gain access to **On-demand Cloud Recordings** of a past meeting.<br> **Scopes:** `recording:write:admin`, `recording:write`.<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body66() # Body66 | 
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Create a Recording Registrant
    api_response = api_instance.meeting_recording_registrant_create(body, meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body66**](Body66.md)|  | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

[**InlineResponse20113**](InlineResponse20113.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrant_status**
> meeting_recording_registrant_status(body, meeting_id)

Update Recording Registrant's Status

A registrant can either be approved or denied from viewing the [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) recording.  Use this API to update a registrant's status.  **Scopes:** `recording:write:admin`, `recording:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body68() # Body68 | 
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Update Recording Registrant's Status
    api_instance.meeting_recording_registrant_status(body, meeting_id)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body68**](Body68.md)|  | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_recording_registrants**
> RegistrationList1 meeting_recording_registrants(meeting_id, status=status, page_size=page_size, page_number=page_number)

List Recording Registrants

Cloud Recordings of past Zoom Meetings can be made [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings). Users should be [registered](https://marketplace.zoom.us/docs/api-reference/zoom-api/cloud-recording/meetingrecordingregistrantcreate) to view these recordings.  Use this API to list registrants of **On-demand Cloud Recordings** of a past meeting.<br> **Scopes:** `recording:read:admin`, `recording:read`.<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
status = 'approved' # str | The registrant status:<br>`pending` - Registrant's status is pending.<br>`approved` - Registrant's status is approved.<br>`denied` - Registrant's status is denied. (optional) (default to approved)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Recording Registrants
    api_response = api_instance.meeting_recording_registrants(meeting_id, status=status, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->meeting_recording_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **status** | **str**| The registrant status:&lt;br&gt;&#x60;pending&#x60; - Registrant&#x27;s status is pending.&lt;br&gt;&#x60;approved&#x60; - Registrant&#x27;s status is approved.&lt;br&gt;&#x60;denied&#x60; - Registrant&#x27;s status is denied. | [optional] [default to approved]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**RegistrationList1**](RegistrationList1.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_delete**
> recording_delete(meeting_id, action=action)

Delete Meeting Recordings

Delete all recording files of a meeting.<br><br>  **Scopes:** `recording:write:admin` `recording:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites**: * Cloud Recording should be enabled on the user's account.<br> 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 
action = 'trash' # str | The recording delete actions:<br>`trash` - Move recording to trash.<br>`delete` - Delete recording permanently. (optional) (default to trash)

try:
    # Delete Meeting Recordings
    api_instance.recording_delete(meeting_id, action=action)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 
 **action** | **str**| The recording delete actions:&lt;br&gt;&#x60;trash&#x60; - Move recording to trash.&lt;br&gt;&#x60;delete&#x60; - Delete recording permanently. | [optional] [default to trash]

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_delete_one**
> recording_delete_one(meeting_id, recording_id, action=action)

Delete a Meeting Recording File

Delete a sprecific recording file from a meeting.<br><br> **Scopes**: `recording:write:admin` `recording:write`<br>  <br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 
recording_id = 'recording_id_example' # str | The recording ID.
action = 'trash' # str | The recording delete actions:<br>`trash` - Move recording to trash.<br>`delete` - Delete recording permanently. (optional) (default to trash)

try:
    # Delete a Meeting Recording File
    api_instance.recording_delete_one(meeting_id, recording_id, action=action)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_delete_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 
 **recording_id** | **str**| The recording ID. | 
 **action** | **str**| The recording delete actions:&lt;br&gt;&#x60;trash&#x60; - Move recording to trash.&lt;br&gt;&#x60;delete&#x60; - Delete recording permanently. | [optional] [default to trash]

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_get**
> object recording_get(meeting_id)

Get Meeting Recordings

Get all the [recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording#h_7420acb5-1897-4061-87b4-5b76e99c03b4) from a meeting.<br><br> The recording files can be downloaded via the `download_url` property listed in the response.  > To access a password protected cloud recording, add an \"access_token\" parameter to the download URL and provide [JWT](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-jwt-app) as the value of the \"access_token\". <br>  **Scopes:** `recording:read:admin` `recording:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Get Meeting Recordings
    api_response = api_instance.recording_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_registrant_question_update**
> recording_registrant_question_update(body, meeting_id)

Update Registration Questions

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.  Use this API to update registration questions that are to be answered by users while registering to view a recording.<br> **Scopes:** `recording:write:admin`, `recording:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body70() # Body70 | Recording Registrant Questions
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Update Registration Questions
    api_instance.recording_registrant_question_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body70**](Body70.md)| Recording Registrant Questions | 
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_registrants_questions_get**
> RecordingRegistrantQuestions recording_registrants_questions_get(meeting_id)

Get Registration Questions

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.  Use this API to retrieve a list of questions that are displayed for users to complete when registering to view the recording of a specific meeting.<br> **Scopes:** `recording:read:admin`, `recording:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Get Registration Questions
    api_response = api_instance.recording_registrants_questions_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

[**RecordingRegistrantQuestions**](RecordingRegistrantQuestions.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_setting_update**
> RecordingSettings recording_setting_update(meeting_id)

Get Meeting Recording Settings

Retrieve settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording).<br><br> **Scopes**: `recording:read:admin` `recording:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` <br>

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Get Meeting Recording Settings
    api_response = api_instance.recording_setting_update(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_setting_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

[**RecordingSettings**](RecordingSettings.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_settings_update**
> recording_settings_update(body, meeting_id)

Update Meeting Recording Settings

Update settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording)<br><br> **Scopes**: `recording:write:admin` `recording:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` <br>

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.RecordingSettings1() # RecordingSettings1 | Meeting recording Settings
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Update Meeting Recording Settings
    api_instance.recording_settings_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordingSettings1**](RecordingSettings1.md)| Meeting recording Settings | 
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_status_update**
> recording_status_update(body, meeting_id)

Recover Meeting Recordings

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover all deleted [Cloud Recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) of a specific meeting.<br><br> **Scopes**: `recording:write:admin` `recording:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites**:<br> * A Pro user with Cloud Recording enabled.

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body62() # Body62 | 
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 

try:
    # Recover Meeting Recordings
    api_instance.recording_status_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body62**](Body62.md)|  | 
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recording_status_update_one**
> recording_status_update_one(body, meeting_id, recording_id)

Recover a Single Recording

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover a single recording file from the meeting.<br> **Scopes:** `recording:write:admin` `recording:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> 

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body64() # Body64 | 
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \"/\" or contains \"//\" (example: \"/ajXp112QmuoKj4854875==\"), you must **double encode** the UUID before making an API request. 
recording_id = 'recording_id_example' # str | The recording ID.

try:
    # Recover a Single Recording
    api_instance.recording_status_update_one(body, meeting_id, recording_id)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recording_status_update_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body64**](Body64.md)|  | 
 **meeting_id** | **str**| The meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance. If a UUID starts with \&quot;/\&quot; or contains \&quot;//\&quot; (example: \&quot;/ajXp112QmuoKj4854875&#x3D;&#x3D;\&quot;), you must **double encode** the UUID before making an API request.  | 
 **recording_id** | **str**| The recording ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recordings_list**
> RecordingList recordings_list(user_id, page_size=page_size, next_page_token=next_page_token, mc=mc, trash=trash, _from=_from, to=to, trash_type=trash_type)

List All Recordings

When a user records a meeting by choosing the **Record to the Cloud** option, the video, audio, and chat text are recorded in the Zoom cloud.   Use this API to list all [Cloud recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) of a user.<br> > To access a user's password protected cloud recording, add an \"access_token\" parameter to the download URL and provide either the [JWT](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-jwt-app) or the user's OAuth access token as the value of the \"access_token\" parameter.  <br>  **Scopes:** `recording:read:admin` `recording:read`  <br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:**  * Pro or a higher plan. * Cloud Recording must be enabled on the user's account.

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
api_instance = swagger_client.CloudRecordingApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)
mc = 'false' # str | Query Metadata of Recording if an On-Premise Meeting Connector was used for the meeting. (optional) (default to false)
trash = false # bool | Query trash. `true`: List recordings from trash.<br> `false`: Do not list recordings from the trash.<br> The default value is `false`. If you set it to `true`, you can use the `trash_type` property to indicate the type of Cloud recording that you need to retrieve.  (optional) (default to false)
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. (Within 6 month range)  **Note**: The \"trash\" files cannot be filtered by date range and thus, the \"from\" and \"to\" fields should not be used for trash files. (optional)
to = '2013-10-20' # date | End date in 'yyyy-mm-dd' format. (Within 6 month range) (optional)
trash_type = 'meeting_recordings' # str | The type of Cloud recording that you would like to retrieve from the trash. The value can be one of the following:<br>     `meeting_recordings`: List all meeting recordings from the trash.<br>     `recording_file`: List all individual recording files from the trash.  (optional) (default to meeting_recordings)

try:
    # List All Recordings
    api_response = api_instance.recordings_list(user_id, page_size=page_size, next_page_token=next_page_token, mc=mc, trash=trash, _from=_from, to=to, trash_type=trash_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudRecordingApi->recordings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
 **mc** | **str**| Query Metadata of Recording if an On-Premise Meeting Connector was used for the meeting. | [optional] [default to false]
 **trash** | **bool**| Query trash. &#x60;true&#x60;: List recordings from trash.&lt;br&gt; &#x60;false&#x60;: Do not list recordings from the trash.&lt;br&gt; The default value is &#x60;false&#x60;. If you set it to &#x60;true&#x60;, you can use the &#x60;trash_type&#x60; property to indicate the type of Cloud recording that you need to retrieve.  | [optional] [default to false]
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. (Within 6 month range)  **Note**: The \&quot;trash\&quot; files cannot be filtered by date range and thus, the \&quot;from\&quot; and \&quot;to\&quot; fields should not be used for trash files. | [optional] 
 **to** | **date**| End date in &#x27;yyyy-mm-dd&#x27; format. (Within 6 month range) | [optional] 
 **trash_type** | **str**| The type of Cloud recording that you would like to retrieve from the trash. The value can be one of the following:&lt;br&gt;     &#x60;meeting_recordings&#x60;: List all meeting recordings from the trash.&lt;br&gt;     &#x60;recording_file&#x60;: List all individual recording files from the trash.  | [optional] [default to meeting_recordings]

### Return type

[**RecordingList**](RecordingList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


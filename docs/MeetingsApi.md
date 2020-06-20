# swagger_client.MeetingsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_past_meeting_files**](MeetingsApi.md#list_past_meeting_files) | **GET** /past_meetings/{meetingId}/files | List Past Meeting Files
[**list_past_meeting_polls**](MeetingsApi.md#list_past_meeting_polls) | **GET** /past_meetings/{meetingId}/polls | List Past Meeting&#x27;s Poll Results
[**meeting**](MeetingsApi.md#meeting) | **GET** /meetings/{meetingId} | Get a Meeting
[**meeting_create**](MeetingsApi.md#meeting_create) | **POST** /users/{userId}/meetings | Create a Meeting
[**meeting_delete**](MeetingsApi.md#meeting_delete) | **DELETE** /meetings/{meetingId} | Delete a Meeting
[**meeting_invitation**](MeetingsApi.md#meeting_invitation) | **GET** /meetings/{meetingId}/invitation | Get Meeting Invitation
[**meeting_live_stream_status_update**](MeetingsApi.md#meeting_live_stream_status_update) | **PATCH** /meetings/{meetingId}/livestream/status | Update Live Stream Status
[**meeting_live_stream_update**](MeetingsApi.md#meeting_live_stream_update) | **PATCH** /meetings/{meetingId}/livestream | Update Live Stream
[**meeting_poll_create**](MeetingsApi.md#meeting_poll_create) | **POST** /meetings/{meetingId}/polls | Create a Meeting Poll
[**meeting_poll_delete**](MeetingsApi.md#meeting_poll_delete) | **DELETE** /meetings/{meetingId}/polls/{pollId} | Delete a Meeting Poll
[**meeting_poll_get**](MeetingsApi.md#meeting_poll_get) | **GET** /meetings/{meetingId}/polls/{pollId} | Get a Meeting Poll
[**meeting_poll_update**](MeetingsApi.md#meeting_poll_update) | **PUT** /meetings/{meetingId}/polls/{pollId} | Update a Meeting Poll
[**meeting_polls**](MeetingsApi.md#meeting_polls) | **GET** /meetings/{meetingId}/polls | List Meeting Polls
[**meeting_registrant_create**](MeetingsApi.md#meeting_registrant_create) | **POST** /meetings/{meetingId}/registrants | Add Meeting Registrant
[**meeting_registrant_question_update**](MeetingsApi.md#meeting_registrant_question_update) | **PATCH** /meetings/{meetingId}/registrants/questions | Update Registration Questions
[**meeting_registrant_status**](MeetingsApi.md#meeting_registrant_status) | **PUT** /meetings/{meetingId}/registrants/status | Update Meeting Registrant Status
[**meeting_registrants**](MeetingsApi.md#meeting_registrants) | **GET** /meetings/{meetingId}/registrants | List Meeting Registrants
[**meeting_registrants_questions_get**](MeetingsApi.md#meeting_registrants_questions_get) | **GET** /meetings/{meetingId}/registrants/questions | List Registration Questions 
[**meeting_status**](MeetingsApi.md#meeting_status) | **PUT** /meetings/{meetingId}/status | Update Meeting Status
[**meeting_update**](MeetingsApi.md#meeting_update) | **PATCH** /meetings/{meetingId} | Update a Meeting
[**meetings**](MeetingsApi.md#meetings) | **GET** /users/{userId}/meetings | List Meetings
[**past_meeting_details**](MeetingsApi.md#past_meeting_details) | **GET** /past_meetings/{meetingUUID} | Get Past Meeting Details
[**past_meeting_participants**](MeetingsApi.md#past_meeting_participants) | **GET** /past_meetings/{meetingUUID}/participants | Get Past Meeting Participants
[**past_meetings**](MeetingsApi.md#past_meetings) | **GET** /past_meetings/{meetingId}/instances | List Ended Meeting Instances

# **list_past_meeting_files**
> InlineResponse20084 list_past_meeting_files(meeting_id)

List Past Meeting Files

List files sent via in-meeting chat during a meeting. The in-meeting files are deleted after 24 hours of the meeting completion time.  <br><br> **Scope:** `meeting:read`, `meeting:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # List Past Meeting Files
    api_response = api_instance.list_past_meeting_files(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->list_past_meeting_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_past_meeting_polls**
> InlineResponse20083 list_past_meeting_polls(meeting_id)

List Past Meeting's Poll Results

[Polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) allow the meeting host to survey attendees. Use this API to list poll results of a meeting.<br><br>  **Scopes**: `meeting:read:admin`, `meeting:read`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` <br> **Prerequisites**:<br> * Host user type must be **Pro**. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If   meeting ID is provided, it will take the last meeting instance.

try:
    # List Past Meeting's Poll Results
    api_response = api_instance.list_past_meeting_polls(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->list_past_meeting_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If   meeting ID is provided, it will take the last meeting instance. | 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting**
> InlineResponse20022 meeting(meeting_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)

Get a Meeting

Retrieve the details of a meeting.<br><br> **Scopes:** `meeting:read:admin` `meeting:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_id = 'occurrence_id_example' # str | Meeting Occurrence ID. Provide this field to view meeting details of a particular occurrence of the [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings). (optional)
show_previous_occurrences = true # bool | Set the value of this field to `true` if you would like to view meeting details of all previous occurrences of a [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings).  (optional)

try:
    # Get a Meeting
    api_response = api_instance.meeting(meeting_id, occurrence_id=occurrence_id, show_previous_occurrences=show_previous_occurrences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **occurrence_id** | **str**| Meeting Occurrence ID. Provide this field to view meeting details of a particular occurrence of the [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings). | [optional] 
 **show_previous_occurrences** | **bool**| Set the value of this field to &#x60;true&#x60; if you would like to view meeting details of all previous occurrences of a [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings).  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_create**
> InlineResponse20110 meeting_create(body, user_id)

Create a Meeting

[Create a meeting](https://support.zoom.us/hc/en-us/articles/201362413-Scheduling-meetings) for a user. <br>This API has a daily rate limit of 100 requests per day. Therefore, only 100 **Create a Meeting** API requests are permitted within a 24 hour window for a user.<br>  <aside>The <code>start_url</code> of a meeting is a URL using which a host or an alternative host can start a meeting. The expiration time for the <code>start_url</code> field is two hours for all regular users.    For users created using the <code>custCreate</code> option via the [Create Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usercreate) API, the expiration time of the <code>start_url</code> field is 90 days.   For security reasons, the recommended way to retrieve the updated value for the <code>start_url</code> field programmatically (after expiry) is by calling the [Retrieve a Meeting API](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meeting) and referring to the value of the <code>start_url</code> field in the response.</aside><br><br> Scopes: `meeting:write:admin` `meeting:write`    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body46() # Body46 | Meeting object.
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.

try:
    # Create a Meeting
    api_response = api_instance.meeting_create(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body46**](Body46.md)| Meeting object. | 
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 

### Return type

[**InlineResponse20110**](InlineResponse20110.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_delete**
> meeting_delete(meeting_id, occurrence_id=occurrence_id, schedule_for_reminder=schedule_for_reminder)

Delete a Meeting

Delete a meeting.<br><br> **Scopes:** `meeting:write:admin` `meeting:write`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)
schedule_for_reminder = true # bool | `true`: Notify host and alternative host about the meeting cancellation via email. `false`: Do not send any email notification. (optional)

try:
    # Delete a Meeting
    api_instance.meeting_delete(meeting_id, occurrence_id=occurrence_id, schedule_for_reminder=schedule_for_reminder)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 
 **schedule_for_reminder** | **bool**| &#x60;true&#x60;: Notify host and alternative host about the meeting cancellation via email. &#x60;false&#x60;: Do not send any email notification. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_invitation**
> MeetingInvitation meeting_invitation(meeting_id)

Get Meeting Invitation

Retrieve the meeting invite note that was sent for a specific meeting.<br><br> **Scopes:** `meeting:read:admin` `meeting:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Get Meeting Invitation
    api_response = api_instance.meeting_invitation(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

[**MeetingInvitation**](MeetingInvitation.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_live_stream_status_update**
> meeting_live_stream_status_update(body, meeting_id)

Update Live Stream Status

Zoom allows users to [live stream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Use this API to update the status of a meeting's live stream.<br><br> **Prerequisites:**<br> * Meeting host must have a Pro license.<br> **Scopes:** `meeting:write:admin` `meeting:write`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body115() # Body115 | Meeting
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Update Live Stream Status
    api_instance.meeting_live_stream_status_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_live_stream_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body115**](Body115.md)| Meeting | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_live_stream_update**
> meeting_live_stream_update(body, meeting_id)

Update Live Stream

Zoom allows users to [live stream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Use this API to update a meeting's live stream information.<br><br> **Prerequisites:**<br> * Meeting host must have a Pro license.<br> **Scopes:** `meeting:write:admin` `meeting:write`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body113() # Body113 | Meeting
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Update Live Stream
    api_instance.meeting_live_stream_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_live_stream_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body113**](Body113.md)| Meeting | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_create**
> InlineResponse20112 meeting_poll_create(body, meeting_id)

Create a Meeting Poll

Polls allow the meeting host to survey attendees. Use this API to create a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) for a meeting.<br><br>  **Scopes**: `meeting:write:admin` `meeting:write`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites**:<br> * Host user type must be **Pro**. * Polling feature should be enabled in the host's account. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body56() # Body56 | Meeting poll object
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Create a Meeting Poll
    api_response = api_instance.meeting_poll_create(body, meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body56**](Body56.md)| Meeting poll object | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

[**InlineResponse20112**](InlineResponse20112.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_delete**
> meeting_poll_delete(meeting_id, poll_id)

Delete a Meeting Poll

Polls allow the meeting host to survey attendees. Use this API to delete a meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).<br> **Scopes**: `meeting:write:admin` `meeting:write`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` <br> **Prerequisites**:<br> * Host user type must be **Pro**. * Polling feature should be enabled in the host's account. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Delete a Meeting Poll
    api_instance.meeting_poll_delete(meeting_id, poll_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_get**
> InlineResponse20112 meeting_poll_get(meeting_id, poll_id)

Get a Meeting Poll

Polls allow the meeting host to survey attendees. Use this API to get information about a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).<br><br> **Scopes**: `meeting:read:admin` `meeting:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Get a Meeting Poll
    api_response = api_instance.meeting_poll_get(meeting_id, poll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **poll_id** | **str**| The poll ID | 

### Return type

[**InlineResponse20112**](InlineResponse20112.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_poll_update**
> meeting_poll_update(body, meeting_id, poll_id)

Update a Meeting Poll

Polls allow the meeting host to survey attendees. Use this API to update information of a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings)<br><br> **Scopes**: `meeting:write:admin` `meeting:write`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`   

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body58() # Body58 | Meeting Poll
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
poll_id = 'poll_id_example' # str | The poll ID

try:
    # Update a Meeting Poll
    api_instance.meeting_poll_update(body, meeting_id, poll_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_poll_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body58**](Body58.md)| Meeting Poll | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **poll_id** | **str**| The poll ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_polls**
> object meeting_polls(meeting_id)

List Meeting Polls

Polls allow the meeting host to survey attendees. Use this API to list [polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) of a meeting.<br><br>  **Scopes**: `meeting:read:admin` `meeting:read`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites**:<br> * Host user type must be **Pro**. * Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # List Meeting Polls
    api_response = api_instance.meeting_polls(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_create**
> InlineResponse20111 meeting_registrant_create(body, meeting_id, occurrence_ids=occurrence_ids)

Add Meeting Registrant

Register a participant for a meeting.<br><br> **Scopes:** `meeting:write:admin` `meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body52() # Body52 | 
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_ids = 'occurrence_ids_example' # str | Occurrence IDs. You can find these with the meeting get API. Multiple values separated by comma. (optional)

try:
    # Add Meeting Registrant
    api_response = api_instance.meeting_registrant_create(body, meeting_id, occurrence_ids=occurrence_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body52**](Body52.md)|  | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **occurrence_ids** | **str**| Occurrence IDs. You can find these with the meeting get API. Multiple values separated by comma. | [optional] 

### Return type

[**InlineResponse20111**](InlineResponse20111.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_question_update**
> meeting_registrant_question_update(body, meeting_id)

Update Registration Questions

Update registration questions that will be displayed to users while [registering for a meeeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).<br><br> **Scopes:** `meeting:write`, `meeting:write:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`    

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body60() # Body60 | Meeting Registrant Questions
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Update Registration Questions
    api_instance.meeting_registrant_question_update(body, meeting_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_question_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body60**](Body60.md)| Meeting Registrant Questions | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrant_status**
> meeting_registrant_status(body, meeting_id, occurrence_id=occurrence_id)

Update Meeting Registrant Status

Update a meeting registrant's status by either approving, cancelling or denying a registrant from joining the meeting.<br><br> **Scopes:** `meeting:write:admin` `meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body54() # Body54 | 
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)

try:
    # Update Meeting Registrant Status
    api_instance.meeting_registrant_status(body, meeting_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrant_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body54**](Body54.md)|  | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **occurrence_id** | **str**| The meeting occurrence ID. | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_registrants**
> RegistrationList meeting_registrants(meeting_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number)

List Meeting Registrants

A host or a user with admin permission can require [registration for a Zoom meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings). Use this API to list users that have registered for a meeting.<br><br> **Scopes**: `meeting:read:admin` `meeting:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_id = 'occurrence_id_example' # str | The meeting occurrence ID. (optional)
status = 'approved' # str | The registrant status:<br>`pending` - Registrant's status is pending.<br>`approved` - Registrant's status is approved.<br>`denied` - Registrant's status is denied. (optional) (default to approved)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Meeting Registrants
    api_response = api_instance.meeting_registrants(meeting_id, occurrence_id=occurrence_id, status=status, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
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

# **meeting_registrants_questions_get**
> InlineResponse20025 meeting_registrants_questions_get(meeting_id)

List Registration Questions 

List registration questions that will be displayed to users while [registering for a meeeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).<br>  **Scopes:** `meeting:read`, `meeting:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # List Registration Questions 
    api_response = api_instance.meeting_registrants_questions_get(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_registrants_questions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_status**
> meeting_status(body, meeting_id)

Update Meeting Status

End a meeting by updating its status.<br><br> **Scopes:** `meeting:write:admin` `meeting:write`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body50() # Body50 | 
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # Update Meeting Status
    api_instance.meeting_status(body, meeting_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body50**](Body50.md)|  | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meeting_update**
> meeting_update(body, meeting_id, occurrence_id=occurrence_id)

Update a Meeting

Update the details of a meeting.<br>This API has a rate limit of 100 requests per day. Therefore, a meeting can only be updated for a maximum of 100 times within a 24 hour window.<br> **Scopes:** `meeting:write:admin` `meeting:write`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body48() # Body48 | Meeting
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.
occurrence_id = 'occurrence_id_example' # str | Meeting occurrence id. Support change of agenda, start_time, duration, settings: {host_video, participant_video, join_before_host, mute_upon_entry, waiting_room, watermark, auto_recording} (optional)

try:
    # Update a Meeting
    api_instance.meeting_update(body, meeting_id, occurrence_id=occurrence_id)
except ApiException as e:
    print("Exception when calling MeetingsApi->meeting_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body48**](Body48.md)| Meeting | 
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 
 **occurrence_id** | **str**| Meeting occurrence id. Support change of agenda, start_time, duration, settings: {host_video, participant_video, join_before_host, mute_upon_entry, waiting_room, watermark, auto_recording} | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meetings**
> GroupList meetings(user_id, type=type, page_size=page_size, page_number=page_number)

List Meetings

List all the meetings that were scheduled for a user (meeting host).<br><br> **Scopes:** `meeting:read:admin` `meeting:read`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user ID or email address of the user. For user-level apps, pass `me` as the value for userId.
type = 'live' # str | The meeting types: <br>`scheduled` - This includes all valid past meetings (unexpired), live meetings and upcoming scheduled meetings. It is equivalent to the combined list of \"Previous Meetings\" and \"Upcoming Meetings\" displayed in the user's [Meetings page](https://zoom.us/meeting) on the Zoom Web Portal.<br>`live` - All the ongoing meetings.<br>`upcoming` - All upcoming meetings including live meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Meetings
    api_response = api_instance.meetings(user_id, type=type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID or email address of the user. For user-level apps, pass &#x60;me&#x60; as the value for userId. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;scheduled&#x60; - This includes all valid past meetings (unexpired), live meetings and upcoming scheduled meetings. It is equivalent to the combined list of \&quot;Previous Meetings\&quot; and \&quot;Upcoming Meetings\&quot; displayed in the user&#x27;s [Meetings page](https://zoom.us/meeting) on the Zoom Web Portal.&lt;br&gt;&#x60;live&#x60; - All the ongoing meetings.&lt;br&gt;&#x60;upcoming&#x60; - All upcoming meetings including live meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**GroupList**](GroupList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meeting_details**
> InlineResponse20023 past_meeting_details(meeting_uuid)

Get Past Meeting Details

Get details on a past meeting. <br><br> **Scopes:** `meeting:read:admin` `meeting:read`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light` > **Note**: Please double encode your UUID when using this API if the UUID begins with a '/'or contains '//' in it.

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_uuid = 'meeting_uuid_example' # str | The meeting UUID. Each meeting instance will generate its own Meeting UUID (i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for other API calls if the UUID begins with a '/'or contains '//' in it.

try:
    # Get Past Meeting Details
    api_response = api_instance.past_meeting_details(meeting_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meeting_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_uuid** | **str**| The meeting UUID. Each meeting instance will generate its own Meeting UUID (i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for other API calls if the UUID begins with a &#x27;/&#x27;or contains &#x27;//&#x27; in it. | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meeting_participants**
> InlineResponse20024 past_meeting_participants(meeting_uuid, page_size=page_size, next_page_token=next_page_token)

Get Past Meeting Participants

Retrieve information on participants from a past meeting. <br><br> **Scopes:** `meeting:read:admin` `meeting:read`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` **Prerequisites:**<br> * Paid account on a Pro or higher plan.  <br> <br>  **Note**: Please double encode your UUID when using this API if the UUID begins with a '/'or contains '//' in it. 

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_uuid = 'meeting_uuid_example' # str | The meeting UUID. Each meeting instance will generate its own Meeting UUID (i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for other API calls if the UUID begins with a '/'or contains '//' in it.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Past Meeting Participants
    api_response = api_instance.past_meeting_participants(meeting_uuid, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meeting_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_uuid** | **str**| The meeting UUID. Each meeting instance will generate its own Meeting UUID (i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for other API calls if the UUID begins with a &#x27;/&#x27;or contains &#x27;//&#x27; in it. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_meetings**
> object past_meetings(meeting_id)

List Ended Meeting Instances

Get a list of ended meeting instances<br><br> **Scopes:** `meeting:read:admin` `meeting:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.MeetingsApi(swagger_client.ApiClient(configuration))
meeting_id = 789 # int | The meeting ID in **long** format. The data type of this field is \"long\"(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits.

try:
    # List Ended Meeting Instances
    api_response = api_instance.past_meetings(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->past_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**| The meeting ID in **long** format. The data type of this field is \&quot;long\&quot;(represented as int64 in JSON).  While storing it in your database, store it as a **long** data type and **not as an integer**, as the Meeting IDs can be longer than 10 digits. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


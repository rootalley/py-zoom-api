# swagger_client.DashboardsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_client_feedback**](DashboardsApi.md#dashboard_client_feedback) | **GET** /metrics/client/feedback | List Zoom Meetings Client Feedbacks
[**dashboard_client_feedback_detail**](DashboardsApi.md#dashboard_client_feedback_detail) | **GET** /metrics/client/feedback/{feedbackId} | Get Zoom Meetings Client Feedback
[**dashboard_crc**](DashboardsApi.md#dashboard_crc) | **GET** /metrics/crc | Get CRC Port Usage
[**dashboard_im**](DashboardsApi.md#dashboard_im) | **GET** /metrics/im | Get IM Metrics
[**dashboard_issue_detail_zoom_room**](DashboardsApi.md#dashboard_issue_detail_zoom_room) | **GET** /metrics/issues/zoomrooms/{zoomroomId} | Get Issues of Zoom Rooms 
[**dashboard_issue_zoom_room**](DashboardsApi.md#dashboard_issue_zoom_room) | **GET** /metrics/issues/zoomrooms | Get Top 25 Zoom Rooms with Issues
[**dashboard_meeting_detail**](DashboardsApi.md#dashboard_meeting_detail) | **GET** /metrics/meetings/{meetingId} | Get Meeting Details
[**dashboard_meeting_participant_qos**](DashboardsApi.md#dashboard_meeting_participant_qos) | **GET** /metrics/meetings/{meetingId}/participants/{participantId}/qos | Get Meeting Participant QOS
[**dashboard_meeting_participant_share**](DashboardsApi.md#dashboard_meeting_participant_share) | **GET** /metrics/meetings/{meetingId}/participants/sharing | Get Sharing/Recording Details of Meeting Participants
[**dashboard_meeting_participants**](DashboardsApi.md#dashboard_meeting_participants) | **GET** /metrics/meetings/{meetingId}/participants | List Meeting Participants
[**dashboard_meeting_participants_qos**](DashboardsApi.md#dashboard_meeting_participants_qos) | **GET** /metrics/meetings/{meetingId}/participants/qos | List Meeting Participants QOS
[**dashboard_meetings**](DashboardsApi.md#dashboard_meetings) | **GET** /metrics/meetings | List Meetings
[**dashboard_webinar_detail**](DashboardsApi.md#dashboard_webinar_detail) | **GET** /metrics/webinars/{webinarId} | Get Webinar Details
[**dashboard_webinar_participant_qos**](DashboardsApi.md#dashboard_webinar_participant_qos) | **GET** /metrics/webinars/{webinarId}/participants/{participantId}/qos | Get Webinar Participant QOS
[**dashboard_webinar_participant_share**](DashboardsApi.md#dashboard_webinar_participant_share) | **GET** /metrics/webinars/{webinarId}/participants/sharing | Get Sharing/Recording Details of Webinar Participants
[**dashboard_webinar_participants**](DashboardsApi.md#dashboard_webinar_participants) | **GET** /metrics/webinars/{webinarId}/participants | Get Webinar Participants
[**dashboard_webinar_participants_qos**](DashboardsApi.md#dashboard_webinar_participants_qos) | **GET** /metrics/webinars/{webinarId}/participants/qos | List Webinar Participant QOS
[**dashboard_webinars**](DashboardsApi.md#dashboard_webinars) | **GET** /metrics/webinars | List Webinars
[**dashboard_zoom_room**](DashboardsApi.md#dashboard_zoom_room) | **GET** /metrics/zoomrooms/{zoomroomId} | Get Zoom Rooms Details
[**dashboard_zoom_room_issue**](DashboardsApi.md#dashboard_zoom_room_issue) | **GET** /metrics/zoomrooms/issues | Get Top 25 issues of Zoom Rooms
[**dashboard_zoom_rooms**](DashboardsApi.md#dashboard_zoom_rooms) | **GET** /metrics/zoomrooms | List Zoom Rooms
[**list_meeting_satisfaction**](DashboardsApi.md#list_meeting_satisfaction) | **GET** /metrics/client/satisfaction | List Client Meeting Satisfaction 

# **dashboard_client_feedback**
> InlineResponse20032 dashboard_client_feedback(_from, to)

List Zoom Meetings Client Feedbacks

Retrieve survey results from [Zoom meetings client feedback](https://support.zoom.us/hc/en-us/articles/115005855266-End-of-Meeting-Feedback-Survey#h_e30d552b-6d8e-4e0a-a588-9ca8180c4dbf). <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  **Prerequisites:** * Business or higher account * [Feedback to Zoom](https://support.zoom.us/hc/en-us/articles/115005838023) enabled.  **Scope:** `account:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # List Zoom Meetings Client Feedbacks
    api_response = api_instance.dashboard_client_feedback(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_client_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_client_feedback_detail**
> InlineResponse20059 dashboard_client_feedback_detail(feedback_id, _from=_from, to=to, page_size=page_size, next_page_token=next_page_token)

Get Zoom Meetings Client Feedback

Retrieve detailed information on a [Zoom meetings client feedback](https://support.zoom.us/hc/en-us/articles/115005855266-End-of-Meeting-Feedback-Survey#h_e30d552b-6d8e-4e0a-a588-9ca8180c4dbf). <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  **Prerequisites:** * Business or higher account * [Feedback to Zoom](https://support.zoom.us/hc/en-us/articles/115005838023) enabled.  **Scope:** `dashboard_home:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  `

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
feedback_id = 'feedback_id_example' # str | Feedback Detail Id
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)
page_size = 30 # int |  (optional) (default to 30)
next_page_token = 'next_page_token_example' # str |  (optional)

try:
    # Get Zoom Meetings Client Feedback
    api_response = api_instance.dashboard_client_feedback_detail(feedback_id, _from=_from, to=to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_client_feedback_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**| Feedback Detail Id | 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 30]
 **next_page_token** | **str**|  | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_crc**
> object dashboard_crc(_from, to)

Get CRC Port Usage

A Cloud Room Connector allows H.323/SIP endpoints to connect to a Zoom meeting.   Use this API to get the hour by hour CRC Port usage for a specified period of time. <aside class='notice'>We will provide the report for a maximum of one month. For example, if \"from\" is set to \"2017-08-05\" and \"to\" is set to \"2017-10-10\", we will adjust \"from\" to \"2017-09-10\".</aside><br><br> **Prerequisites:**<br> * Business, Education or API Plan. * Room Connector must be enabled on the account.<br><br> **Scopes:** `dashboard_crc:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy` 

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get CRC Port Usage
    api_response = api_instance.dashboard_crc(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_crc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_im**
> InlineResponse20031 dashboard_im(_from, to, page_size=page_size, next_page_token=next_page_token)

Get IM Metrics

Get [metrics](https://support.zoom.us/hc/en-us/articles/204654719-Dashboard#h_cc7e9749-1c70-4afb-a9a2-9680654821e4) on how users are utilizing the Zoom Chat Client.<br><br> <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months. **Scope:** `dashboard_im:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`<br> **Prerequisites:**<br> * Business or a higher plan.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get IM Metrics
    api_response = api_instance.dashboard_im(_from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_im: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_issue_detail_zoom_room**
> InlineResponse20033 dashboard_issue_detail_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)

Get Issues of Zoom Rooms 

Get information about the issues that occured on the Top 25 **Zoom Rooms with issues** in an acount. <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  **Scope:** `dashboard_home:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** <br> * Business or a higher plan. * Zoom Room must be enabled in the account.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
zoomroom_id = 'zoomroom_id_example' # str | The Zoom room ID.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Issues of Zoom Rooms 
    api_response = api_instance.dashboard_issue_detail_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_issue_detail_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoomroom_id** | **str**| The Zoom room ID. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_issue_zoom_room**
> object dashboard_issue_zoom_room(_from, to)

Get Top 25 Zoom Rooms with Issues

Get information on top 25 Zoom Rooms with issues in a month. The month specified with the \"from\" and \"to\" range should fall within the last six months.<br> **Scope:** `dashboard_home:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:**<br> * Business or a higher plan. * Zoom Room must be enabled in the account.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get Top 25 Zoom Rooms with Issues
    api_response = api_instance.dashboard_issue_zoom_room(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_issue_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_detail**
> MeetingMetrics dashboard_meeting_detail(meeting_id, type=type)

Get Meeting Details

Get details on live or past meetings. This overview will show if features such as audio, video, screen sharing, and recording were being used in the meeting. You can also see the license types of each user on your account.<br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  <br> **Scopes:** `dashboard_meetings:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** <br> * Business or a higher plan.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance.
type = 'live' # str | The meeting types: <br>`past` - Past meetings.<br>`pastOne` - Past one user meetings.<br>`live` - Live meetings. (optional) (default to live)

try:
    # Get Meeting Details
    api_response = api_instance.dashboard_meeting_detail(meeting_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;past&#x60; - Past meetings.&lt;br&gt;&#x60;pastOne&#x60; - Past one user meetings.&lt;br&gt;&#x60;live&#x60; - Live meetings. | [optional] [default to live]

### Return type

[**MeetingMetrics**](MeetingMetrics.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participant_qos**
> ParticipantQOS dashboard_meeting_participant_qos(meeting_id, participant_id, type=type)

Get Meeting Participant QOS

Retrieve the quality of service for participants from live or past meetings. This data indicates the connection quality for sending/receiving video, audio, and shared content. If nothing is being sent or received at that time, no information will be shown in the fields. <br><br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance.
participant_id = 'participant_id_example' # str | Participant ID.
type = 'live' # str | The meeting types: <br>`past` - Past meetings.<br>`live` - Live Meetings. (optional) (default to live)

try:
    # Get Meeting Participant QOS
    api_response = api_instance.dashboard_meeting_participant_qos(meeting_id, participant_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participant_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance. | 
 **participant_id** | **str**| Participant ID. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;past&#x60; - Past meetings.&lt;br&gt;&#x60;live&#x60; - Live Meetings. | [optional] [default to live]

### Return type

[**ParticipantQOS**](ParticipantQOS.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participant_share**
> InlineResponse20028 dashboard_meeting_participant_share(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get Sharing/Recording Details of Meeting Participants

Retrieve the sharing and recording details of participants from live or past meetings.<br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** <br> * Business or a higher plan.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance.
type = 'live' # str | The meeting types: <br>`past` - Past meetings.<br>`live` - Live Meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Sharing/Recording Details of Meeting Participants
    api_response = api_instance.dashboard_meeting_participant_share(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participant_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;past&#x60; - Past meetings.&lt;br&gt;&#x60;live&#x60; - Live Meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participants**
> InlineResponse20027 dashboard_meeting_participants(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)

List Meeting Participants

Get a list of participants from live or past meetings.<br><br> If you do not provide the `type` query parameter, the default value will be set to `live` and thus, you will only see metrics for participants in a live meeting, if any meeting is currently being conducted. To view metrics on past meeting participants, provide the appropriate value for `type`. <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.  **Scopes:** `dashboard_meetings:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** Business or a higher plan.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance.
type = 'live' # str | The meeting types: <br>`past` - Past meetings.<br>`pastOne` - Past one user meetings.<br>`live` - Live meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Meeting Participants
    api_response = api_instance.dashboard_meeting_participants(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;past&#x60; - Past meetings.&lt;br&gt;&#x60;pastOne&#x60; - Past one user meetings.&lt;br&gt;&#x60;live&#x60; - Live meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meeting_participants_qos**
> ParticipantQOSList dashboard_meeting_participants_qos(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)

List Meeting Participants QOS

Get a list of meeting participants from live or past meetings along with the quality of service they recieve during the meeting such as connection quality for sending/receiving video, audio, and shared content.<br>If you do not provide the `type` query parameter, the default value will be set to `live` and thus, you will only see metrics for participants in a live meeting, if any meeting is currently being conducted. To view metrics on past meeting participants, provide the appropriate value for `type`.<br> <br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.<br><br> **Scopes:** `dashboard_meetings:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** <br> * Business or a higher plan.

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance.
type = 'live' # str | The meeting types: <br>`past` - Past meetings.<br>`live` - Live Meetings. (optional) (default to live)
page_size = 1 # int | The number of items returned per page. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Meeting Participants QOS
    api_response = api_instance.dashboard_meeting_participants_qos(meeting_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meeting_participants_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| The meeting ID or meeting UUID. If given the meeting ID it will take the last meeting instance. | 
 **type** | **str**| The meeting types: &lt;br&gt;&#x60;past&#x60; - Past meetings.&lt;br&gt;&#x60;live&#x60; - Live Meetings. | [optional] [default to live]
 **page_size** | **int**| The number of items returned per page. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**ParticipantQOSList**](ParticipantQOSList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_meetings**
> InlineResponse20026 dashboard_meetings(_from, to, type=type, page_size=page_size, next_page_token=next_page_token)

List Meetings

List total live or past meetings that occurred during a specified period of time. This overview will show if features such as audio, video, screen sharing, and recording were being used in the meeting. You can also see the license types of each user on your account.<br> You can specify a monthly date range for the dashboard data using the `from` and `to` query parameters. The month should fall within the last six months.<br> **Scopes:** `dashboard_meetings:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`<br><br> **Prerequisites:** <br> * Business or a higher plan.<br><br>

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = 'live' # str | Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:<br> <br>`past` - Meeting that already occurred in the specified date range.<br>`pastOne` - Past meetings that were attended by only one user. <br>`live` - Live meetings.<br><br>  If you do not provide this field, the default value will be `live` and thus, the API will only query responses for live meetings. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Meetings
    api_response = api_instance.dashboard_meetings(_from, to, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| Specify a value to get the response for the corresponding meeting type. The value of this field can be one of the following:&lt;br&gt; &lt;br&gt;&#x60;past&#x60; - Meeting that already occurred in the specified date range.&lt;br&gt;&#x60;pastOne&#x60; - Past meetings that were attended by only one user. &lt;br&gt;&#x60;live&#x60; - Live meetings.&lt;br&gt;&lt;br&gt;  If you do not provide this field, the default value will be &#x60;live&#x60; and thus, the API will only query responses for live meetings. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_detail**
> WebinarMetrics dashboard_webinar_detail(webinar_id, type=type)

Get Webinar Details

Retrieve details from live or past webinars.<br><br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:**<br> * Business, Education or API Plan with Webinar add-on.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance.
type = 'live' # str | The webinar type. (optional) (default to live)

try:
    # Get Webinar Details
    api_response = api_instance.dashboard_webinar_detail(webinar_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance. | 
 **type** | **str**| The webinar type. | [optional] [default to live]

### Return type

[**WebinarMetrics**](WebinarMetrics.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participant_qos**
> ParticipantQOS dashboard_webinar_participant_qos(webinar_id, participant_id, type=type)

Get Webinar Participant QOS

Retrieve details on the quality of service that participants from live or past webinars recieved.<br>This data indicates the connection quality for sending/receiving video, audio, and shared content. If nothing is being sent or received at that time, no information will be shown in the fields.<br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy` <br> **Prerequisites:** <br> * Business, Education or API Plan with Zoom Rooms set up. 

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance.
participant_id = 'participant_id_example' # str | Participant ID.
type = 'live' # str | The webinar type. (optional) (default to live)

try:
    # Get Webinar Participant QOS
    api_response = api_instance.dashboard_webinar_participant_qos(webinar_id, participant_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participant_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance. | 
 **participant_id** | **str**| Participant ID. | 
 **type** | **str**| The webinar type. | [optional] [default to live]

### Return type

[**ParticipantQOS**](ParticipantQOS.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participant_share**
> InlineResponse20028 dashboard_webinar_participant_share(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get Sharing/Recording Details of Webinar Participants

Retrieve the sharing and recording details of participants from live or past webinars. <br><br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy` <br> **Prerequisites:**<br> * Business, Education or API Plan with Webinar add-on.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance.
type = 'live' # str | The webinar type. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Sharing/Recording Details of Webinar Participants
    api_response = api_instance.dashboard_webinar_participant_share(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participant_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance. | 
 **type** | **str**| The webinar type. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceed the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participants**
> InlineResponse20030 dashboard_webinar_participants(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

Get Webinar Participants

Retrieve details on participants from live or past webinars.<br><br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:**<br> * Business, Education or API Plan with Webinar add-on.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance.
type = 'live' # str | The webinar type. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Webinar Participants
    api_response = api_instance.dashboard_webinar_participants(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance. | 
 **type** | **str**| The webinar type. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinar_participants_qos**
> ParticipantQOSList dashboard_webinar_participants_qos(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)

List Webinar Participant QOS

Retrieve a list of participants from live or past webinars and the quality of service they received.<br>This data indicates the connection quality for sending/receiving video, audio, and shared content. If nothing is being sent or received at that time, no information will be shown in the fields.<br> **Scopes:** `dashboard:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:** * Business, Education or API Plan with Webinar add-on.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
webinar_id = 'webinar_id_example' # str | The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance.
type = 'live' # str | The webinar type. (optional) (default to live)
page_size = 1 # int | The number of items returned per page. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Webinar Participant QOS
    api_response = api_instance.dashboard_webinar_participants_qos(webinar_id, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinar_participants_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webinar_id** | **str**| The webinar ID or webinar UUID. If given the webinar ID it will take the last webinar instance. | 
 **type** | **str**| The webinar type. | [optional] [default to live]
 **page_size** | **int**| The number of items returned per page. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**ParticipantQOSList**](ParticipantQOSList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_webinars**
> InlineResponse20029 dashboard_webinars(_from, to, type=type, page_size=page_size, next_page_token=next_page_token)

List Webinars

List all the live or past webinars from a specified period of time. <br><br> **Scopes:** `dashboard:read:admin`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`<br> **Prerequisites:**<br> * Business, Education or API Plan with Webinar add-on.   

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
type = 'live' # str | The webinar type. (optional) (default to live)
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Webinars
    api_response = api_instance.dashboard_webinars(_from, to, type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_webinars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **type** | **str**| The webinar type. | [optional] [default to live]
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_room**
> object dashboard_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)

Get Zoom Rooms Details

The Zoom Rooms dashboard metrics lets you know the type of configuration a Zoom room has and details on the meetings held in that room.   Use this API to retrieve information on a specific room.<br><br> **Scopes:** `dashboard_zr:read:admin`<br> <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`**Prerequisites:**<br> * Business, Education or API Plan with Zoom Rooms set up. 

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
zoomroom_id = 'zoomroom_id_example' # str | The Zoom room ID.
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Get Zoom Rooms Details
    api_response = api_instance.dashboard_zoom_room(zoomroom_id, _from, to, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zoomroom_id** | **str**| The Zoom room ID. | 
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_room_issue**
> object dashboard_zoom_room_issue(_from, to)

Get Top 25 issues of Zoom Rooms

Get Top 25 issues of Zoom Rooms.<br> **Scopes:** `dashboard_zr:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>  **Prerequisites:**<br> * Business, Education or API Plan with Zoom Rooms set up.  

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | Start date in 'yyyy-mm-dd' format. The date range defined by the \"from\" and \"to\" parameters should only be one month as the report includes only one month worth of data at once.
to = '2013-10-20' # date | End date.

try:
    # Get Top 25 issues of Zoom Rooms
    api_response = api_instance.dashboard_zoom_room_issue(_from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_room_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| Start date in &#x27;yyyy-mm-dd&#x27; format. The date range defined by the \&quot;from\&quot; and \&quot;to\&quot; parameters should only be one month as the report includes only one month worth of data at once. | 
 **to** | **date**| End date. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_zoom_rooms**
> ZoomRoomList dashboard_zoom_rooms(page_size=page_size, page_number=page_number)

List Zoom Rooms

List information on all Zoom Rooms in an account.<br><br> **Scopes:** `dashboard_zr:read:admin`   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Resource-intensive`<br>  **Prerequisites:**<br> * Business, Education or API Plan with Zoom Rooms set up.   

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
page_number = 1 # int | The current page number of returned records. (optional) (default to 1)

try:
    # List Zoom Rooms
    api_response = api_instance.dashboard_zoom_rooms(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->dashboard_zoom_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **page_number** | **int**| The current page number of returned records. | [optional] [default to 1]

### Return type

[**ZoomRoomList**](ZoomRoomList.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_meeting_satisfaction**
> InlineResponse20087 list_meeting_satisfaction(_from=_from, to=to)

List Client Meeting Satisfaction 

If the [End of Meeting Feedback Survey](https://support.zoom.us/hc/en-us/articles/115005855266) option is enabled, attendees will be prompted with a survey window where they can tap either the **Thumbs Up** or **Thumbs Down** button that indicates their Zoom meeting experience. With this API, you can get information on the attendees' meeting satisfaction. Specify a monthly date range for the query using the from and to query parameters. The month should fall within the last six months.  To get information on the survey results with negative experiences (indicated by **Thumbs Down**), use the [Get Zoom Meetings Client Feedback API](https://marketplace.zoom.us/docs/api-reference/zoom-api/dashboards/dashboardclientfeedbackdetail).<br> **Scopes:** `dashboard:read:admin`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

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
api_instance = swagger_client.DashboardsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20' # date | The start date for the query in “yyyy-mm-dd” format.  (optional)
to = '2013-10-20' # date | The end date for the query in “yyyy-mm-dd” format.  (optional)

try:
    # List Client Meeting Satisfaction 
    api_response = api_instance.list_meeting_satisfaction(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->list_meeting_satisfaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **date**| The start date for the query in “yyyy-mm-dd” format.  | [optional] 
 **to** | **date**| The end date for the query in “yyyy-mm-dd” format.  | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


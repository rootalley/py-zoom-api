# MeetingInfoGet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Meeting topic. | [optional] 
**type** | **int** | Meeting Types:&lt;br&gt;&#x60;1&#x60; - Instant meeting.&lt;br&gt;&#x60;2&#x60; - Scheduled meeting.&lt;br&gt;&#x60;3&#x60; - Recurring meeting with no fixed time.&lt;br&gt;&#x60;4&#x60; - PMI Meeting&lt;br&gt; &#x60;8&#x60; - Recurring meeting with a fixed time. | [optional] 
**status** | **str** | Meeting status | [optional] 
**start_time** | **datetime** | Meeting start time in GMT/UTC. Start time will not be returned if the meeting is an **instant** meeting.   | [optional] 
**duration** | **int** | Meeting duration. | [optional] 
**timezone** | **str** | Timezone to format the meeting start time on the . | [optional] 
**created_at** | **datetime** | Time of creation.  | [optional] 
**agenda** | **str** | Agenda. | [optional] 
**start_url** | **str** | &lt;br&gt;&lt;aside&gt;The &lt;code&gt;start_url&lt;/code&gt; of a Meeting is a URL using which a host or an alternative host can start the Meeting.   The expiration time for the &lt;code&gt;start_url&lt;/code&gt; field listed in the response of [Create a Meeting API](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate) is two hours for all regular users.    For users created using the &lt;code&gt;custCreate&lt;/code&gt; option via the [Create Users](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usercreate) API, the expiration time of the &lt;code&gt;start_url&lt;/code&gt; field is 90 days.   For security reasons, to retrieve the updated value for the &lt;code&gt;start_url&lt;/code&gt; field programmatically (after the expiry time), you must call the [Retrieve a Meeting API](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meeting) and refer to the value of the &lt;code&gt;start_url&lt;/code&gt; field in the response.&lt;/aside&gt;&lt;br&gt;This URL should only be used by the host of the meeting and **should not be shared with anyone other than the host** of the meeting as anyone with this URL will be able to login to the Zoom Client as the host of the meeting. | [optional] 
**join_url** | **str** | URL for participants to join the meeting. This URL should only be shared with users that you would like to invite for the meeting. | [optional] 
**password** | **str** | Meeting password. | [optional] 
**h323_password** | **str** | H.323/SIP room system password. | [optional] 
**encrypted_password** | **str** | Encrypted password for third party endpoints (H323/SIP). | [optional] 
**pmi** | **int** | Personal Meeting Id. Only used for scheduled meetings and recurring meetings with no fixed time. | [optional] 
**tracking_fields** | [**list[MeetingTrackingFields]**](MeetingTrackingFields.md) | Tracking fields | [optional] 
**occurrences** | [**list[MeetingInfoOccurrences]**](MeetingInfoOccurrences.md) | Array of occurrence objects. | [optional] 
**settings** | [**MeetingSettings**](MeetingSettings.md) |  | [optional] 
**recurrence** | [**UsersuserIdmeetingsRecurrence**](UsersuserIdmeetingsRecurrence.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


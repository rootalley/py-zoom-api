# Session

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Meeting topic. | [optional] 
**type** | **int** | Meeting Type:&lt;br&gt;&#x60;1&#x60; - Instant meeting.&lt;br&gt;&#x60;2&#x60; - Scheduled meeting.&lt;br&gt;&#x60;3&#x60; - Recurring meeting with no fixed time.&lt;br&gt;&#x60;8&#x60; - Recurring meeting with fixed time. | [optional] 
**start_time** | **datetime** | Meeting start time. When using a format like \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;\&quot;, always use GMT time. When using a format like \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss\&quot;, you should use local time and specify the time zone. This is only used for scheduled meetings and recurring meetings with a fixed time. | [optional] 
**duration** | **int** | Meeting duration (minutes). Used for scheduled meetings only. | [optional] 
**timezone** | **str** | Time zone to format start_time. For example, \&quot;America/Los_Angeles\&quot;. For scheduled meetings only. Please reference our [time zone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) list for supported time zones and their formats. | [optional] 
**password** | **str** | Password to join the meeting. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters. | [optional] 
**agenda** | **str** | Meeting description. | [optional] 
**tracking_fields** | [**list[MeetingTrackingFields]**](MeetingTrackingFields.md) | Tracking fields | [optional] 
**recurrence** | [**UsersuserIdmeetingsRecurrence**](UsersuserIdmeetingsRecurrence.md) |  | [optional] 
**settings** | [**MeetingSettings**](MeetingSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


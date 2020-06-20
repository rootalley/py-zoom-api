# SessionUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Meeting topic. | [optional] 
**type** | **int** | Meeting Types:&lt;br&gt;&#x60;1&#x60; - Instant meeting.&lt;br&gt;&#x60;2&#x60; - Scheduled meeting.&lt;br&gt;&#x60;3&#x60; - Recurring meeting with no fixed time.&lt;br&gt;&#x60;8&#x60; - Recurring meeting with a fixed time. | [optional] 
**start_time** | **datetime** | Meeting start time. When using a format like \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;\&quot;, always use GMT time. When using a format like \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss\&quot;, you should use local time and  specify the time zone. Only used for scheduled meetings and recurring meetings with a fixed time. | [optional] 
**duration** | **int** | Meeting duration (minutes). Used for scheduled meetings only. | [optional] 
**timezone** | **str** | Time zone to format start_time. For example, \&quot;America/Los_Angeles\&quot;. For scheduled meetings only. Please reference our [time zone](#timezones) list for supported time zones and their formats. | [optional] 
**password** | **str** | Password to join the meeting. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *] and can have a maximum of 10 characters.  **Note:** If the account owner or the admin has configured [minimum password requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the password value provided here must meet those requirements. &lt;br&gt;&lt;br&gt;If the requirements are enabled, you can view those requirements by calling either the [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings) or the  [Get Account Settings](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) API.  | [optional] 
**agenda** | **str** | Meeting description. | [optional] 
**tracking_fields** | [**list[MeetingTrackingFields]**](MeetingTrackingFields.md) | Tracking fields | [optional] 
**recurrence** | [**UsersuserIdmeetingsRecurrence**](UsersuserIdmeetingsRecurrence.md) |  | [optional] 
**settings** | **AllOfSessionUpdateSettings** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


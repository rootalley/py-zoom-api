# Body47

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Meeting topic. | [optional] 
**type** | **int** | Meeting Type:&lt;br&gt;&#x60;1&#x60; - Instant meeting.&lt;br&gt;&#x60;2&#x60; - Scheduled meeting.&lt;br&gt;&#x60;3&#x60; - Recurring meeting with no fixed time.&lt;br&gt;&#x60;8&#x60; - Recurring meeting with fixed time. | [optional] 
**start_time** | **datetime** | Meeting start time. We support two formats for &#x60;start_time&#x60; - local time and GMT.&lt;br&gt;   To set time as GMT the format should be &#x60;yyyy-MM-dd&#x60;T&#x60;HH:mm:ssZ&#x60;. Example: \&quot;2020-03-31T12:02:00Z\&quot;  To set time using a specific timezone, use &#x60;yyyy-MM-dd&#x60;T&#x60;HH:mm:ss&#x60; format and specify the timezone [ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) in the &#x60;timezone&#x60; field OR leave it blank and the timezone set on your Zoom account will be used. You can also set the time as UTC as the timezone field.  The &#x60;start_time&#x60; should only be used for scheduled and / or recurring webinars with fixed time. | [optional] 
**duration** | **int** | Meeting duration (minutes). Used for scheduled meetings only. | [optional] 
**schedule_for** | **str** | If you would like to schedule this meeting for someone else in your account, provide the Zoom user id or email address of the user here. | [optional] 
**timezone** | **str** | Time zone to format start_time. For example, \&quot;America/Los_Angeles\&quot;. For scheduled meetings only. Please reference our [time zone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) list for supported time zones and their formats. | [optional] 
**password** | **str** | Password to join the meeting. By default, password may only contain the following characters: [a-z A-Z 0-9 @ - _ *] and can have a maximum of 10 characters.  **Note:** If the account owner or the admin has configured [minimum password requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the password value provided here must meet those requirements. &lt;br&gt;&lt;br&gt;If the requirements are enabled, you can view those requirements by calling either the [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings) or the [Get Account Settings](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) API.  | [optional] 
**agenda** | **str** | Meeting description. | [optional] 
**tracking_fields** | [**list[UsersuserIdmeetingsTrackingFields]**](UsersuserIdmeetingsTrackingFields.md) | Tracking fields | [optional] 
**recurrence** | [**UsersuserIdmeetingsRecurrence**](UsersuserIdmeetingsRecurrence.md) |  | [optional] 
**settings** | [**UsersuserIdmeetingsSettings**](UsersuserIdmeetingsSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


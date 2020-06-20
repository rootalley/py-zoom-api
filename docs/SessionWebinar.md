# SessionWebinar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Webinar topic. | [optional] 
**type** | **int** | Webinar Types:&lt;br&gt;&#x60;5&#x60; - Webinar.&lt;br&gt;&#x60;6&#x60; - Recurring webinar with no fixed time.&lt;br&gt;&#x60;9&#x60; - Recurring webinar with a fixed time. | [optional] 
**start_time** | **datetime** | Webinar start time. We support two formats for &#x60;start_time&#x60; - local time and GMT.&lt;br&gt;   To set time as GMT the format should be &#x60;yyyy-MM-dd&#x60;T&#x60;HH:mm:ssZ&#x60;.  To set time using a specific timezone, use &#x60;yyyy-MM-dd&#x60;T&#x60;HH:mm:ss&#x60; format and specify the timezone [ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) in the &#x60;timezone&#x60; field OR leave it blank and the timezone set on your Zoom account will be used. You can also set the time as UTC as the timezone field.  The &#x60;start_time&#x60; should only be used for scheduled and / or recurring webinars with fixed time. | [optional] 
**duration** | **int** | Webinar duration (minutes). Used for scheduled webinars only. | [optional] 
**timezone** | **str** | Time zone to format start_time. For example, \&quot;America/Los_Angeles\&quot;. For scheduled meetings only. Please reference our [time zone](#timezones) list for supported time zones and their formats. | [optional] 
**password** | **str** | Webinar password. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters. | [optional] 
**agenda** | **str** | Webinar description. | [optional] 
**tracking_fields** | [**list[MeetingTrackingFields]**](MeetingTrackingFields.md) | Tracking fields | [optional] 
**recurrence** | [**RecurrenceWebinar**](RecurrenceWebinar.md) |  | [optional] 
**settings** | [**SessionWebinarSettings**](SessionWebinarSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


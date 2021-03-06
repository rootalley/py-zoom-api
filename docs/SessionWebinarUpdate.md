# SessionWebinarUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Webinar topic. | [optional] 
**type** | **int** | Webinar Types:&lt;br&gt;&#x60;5&#x60; - webinar.&lt;br&gt;&#x60;6&#x60; - Recurring webinar with no fixed time.&lt;br&gt;&#x60;9&#x60; - Recurring webinar with a fixed time. | [optional] 
**start_time** | **datetime** | Webinar start time, in the format \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss&#x27;Z&#x27;.\&quot; Should be in GMT time. In the format \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.\&quot; This should be in local time and the timezone should be specified. Only used for scheduled webinars and recurring webinars with a fixed time. | [optional] 
**duration** | **int** | Webinar duration (minutes). Used for scheduled webinar only. | [optional] 
**timezone** | **str** | Time zone to format start_time. For example, \&quot;America/Los_Angeles\&quot;. For scheduled meetings only. Please reference our [time zone](#timezones) list for supported time zones and their formats. | [optional] 
**password** | **str** | Webinar password. By default, password may only contain the following characters: [a-z A-Z 0-9 @ - _ * !] and can have a maximum of 10 characters.  **Note:** If the account owner or the admin has configured [minimum password requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the password value provided here must meet those requirements. &lt;br&gt;&lt;br&gt;If the requirements are enabled, you can view those requirements by calling either the [Get User Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings) or the  [Get Account Settings](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) API.   If \&quot;**Require a password when scheduling new meetings**\&quot; setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the password field will be autogenerated for the Webinar in the response even if it is not provided in the API request. &lt;br&gt;&lt;br&gt;         | [optional] 
**agenda** | **str** | Webinar description. | [optional] 
**tracking_fields** | [**list[MeetingTrackingFields]**](MeetingTrackingFields.md) | Tracking fields | [optional] 
**recurrence** | [**UsersuserIdmeetingsRecurrence**](UsersuserIdmeetingsRecurrence.md) |  | [optional] 
**settings** | **AllOfSessionWebinarUpdateSettings** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


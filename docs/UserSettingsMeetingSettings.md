# UserSettingsMeetingSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_video** | **bool** | Start meetings with host video on. | [optional] 
**participants_video** | **bool** | Start meetings with participants video on. | [optional] 
**audio_type** | **str** | Determine how participants can join the audio portion of the meeting:&lt;br&gt;&#x60;both&#x60; - Telephony and VoIP.&lt;br&gt;&#x60;telephony&#x60; - Audio PSTN telephony only.&lt;br&gt;&#x60;voip&#x60; - VoIP only.&lt;br&gt;&#x60;thirdParty&#x60; - Third party audio conference. | [optional] [default to 'voip']
**join_before_host** | **bool** | Join the meeting before host arrives. | [optional] 
**force_pmi_jbh_password** | **bool** | Require a password for personal meetings if attendees can join before host. | [optional] 
**pstn_password_protected** | **bool** | Generate and require password for participants joining by phone. | [optional] 
**use_pmi_for_scheduled_meetings** | **bool** | Use Personal Meeting ID (PMI) when scheduling a meeting  | [optional] 
**use_pmi_for_instant_meetings** | **bool** | Use Personal Meeting ID (PMI) when starting an instant meeting  | [optional] 
**require_password_for_scheduling_new_meetings** | **bool** | Require a password when scheduling new meetings.This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.  | [optional] 
**require_password_for_scheduled_meetings** | **bool** | Require a password for meetings which have already been scheduled  | [optional] 
**default_password_for_scheduled_meetings** | **str** | Password for already scheduled meetings  | [optional] 
**require_password_for_instant_meetings** | **bool** | Require a password for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.  | [optional] 
**require_password_for_pmi_meetings** | **str** | Require a password for Personal Meeting ID (PMI). This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts.  | [optional] 
**pmi_password** | **str** | PMI password  | [optional] 
**embed_password_in_join_link** | **bool** | If the value is set to &#x60;true&#x60;, the meeting password will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the password.   | [optional] 
**meeting_password_requirement** | [**AccountSettingsScheduleMeetingMeetingPasswordRequirement**](AccountSettingsScheduleMeetingMeetingPasswordRequirement.md) |  | [optional] 
**personal_meeting** | **bool** | Personal Meeting Setting.&lt;br&gt;&lt;br&gt; &#x60;true&#x60;: Indicates that the **\&quot;Enable Personal Meeting ID\&quot;** setting is turned on. Users can choose to use personal meeting ID for their meetings. &lt;br&gt;&lt;br&gt; &#x60;false&#x60;: Indicates that the **\&quot;Enable Personal Meeting ID\&quot;** setting is [turned off](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a). If this setting is disabled, meetings that were scheduled with PMI will be invalid. Scheduled meetings will need to be manually updated. For Zoom Phone only:If a user has been assigned a desk phone, **\&quot;Elevate to Zoom Meeting\&quot;** on desk phone will be disabled.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


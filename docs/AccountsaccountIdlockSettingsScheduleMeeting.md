# AccountsaccountIdlockSettingsScheduleMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_video** | **bool** | Start meetings with host video on. | [optional] 
**participant_video** | **bool** | Start meetings with participant video on. | [optional] 
**audio_type** | **bool** | Determine how participants can join the audio portion of the meeting. | [optional] 
**join_before_host** | **bool** | Allow participants to join the meeting before the host arrives | [optional] 
**enforce_login** | **bool** | Participants must always sign in before joining the scheduled meeting. | [optional] 
**enforce_login_with_domains** | **bool** |  | [optional] 
**enforce_login_domains** | **str** |  | [optional] 
**not_store_meeting_topic** | **bool** |  | [optional] 
**require_password_for_scheduling_new_meetings** | **bool** | This setting applies for regular meetings that do not use PMI. If enabled, a password will be generated while a host schedules a new meeting and participants will be required to enter the password before they can join the meeting. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**require_password_for_instant_meetings** | **bool** | Require password for instant meetings. If you use PMI for your instant meetings, this option will be disabled. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**require_password_for_pmi_meetings** | **bool** | Require participants to enter password for PMI meetings. This setting is always enabled for free accounts and Pro accounts with a single host and cannot be modified for these accounts. | [optional] 
**meeting_authentication** | **bool** |  | [optional] 
**embed_password_in_join_link** | **bool** | If the value is set to &#x60;true&#x60;, the meeting password will be encrypted and included in the join meeting link to allow participants to join with just one click without having to enter the password.   | [optional] 
**personal_meeting** | **bool** | Turn the lock setting on or off for the **Enable Personal Meeting ID** setting for an entire account.&lt;br&gt;&lt;br&gt; &#x60;true&#x60;: Turn the **\&quot;Enable Personal Meeting ID\&quot;** setting **on** for all users in the account. Users can choose to use personal meeting ID for their meetings. &lt;br&gt;&lt;br&gt; &#x60;false&#x60;: Turn **off** the **\&quot;Enable Personal Meeting ID\&quot;** setting. **If this setting is [disabled](https://support.zoom.us/hc/en-us/articles/201362843-Personal-meeting-ID-PMI-and-personal-link?flash_digest&#x3D;eb7ac62d8c7fb4daf285916e3e15d87537806133#h_aa0335c8-3b06-41bc-bc1f-a8b84ef17f2a), meetings that were scheduled with PMI by the users in the account will be invalid. Users will have to update previously scheduled PMI meetings.**&lt;br&gt;&lt;br&gt; For Zoom Phone only: If a user has been assigned a desk phone, **\&quot;Elevate to Zoom Meeting\&quot;** on desk phone will be disabled.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


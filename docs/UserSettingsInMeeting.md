# UserSettingsInMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e2e_encryption** | **bool** | Zoom requires encryption for all data between the Zoom cloud, Zoom client, and Zoom Room. Require encryption for 3rd party endpoints (H323/SIP). | [optional] 
**chat** | **bool** | Enable chat during meeting for all participants. | [optional] [default to False]
**private_chat** | **bool** | Enable 1:1 private chat between participants during meetings. | [optional] [default to False]
**auto_saving_chat** | **bool** | Auto save all in-meeting chats. | [optional] [default to False]
**entry_exit_chime** | **str** | Play sound when participants join or leave:&lt;br&gt;&#x60;host&#x60; - When host joins or leaves.&lt;br&gt;&#x60;all&#x60; - When any participant joins or leaves.&lt;br&gt;&#x60;none&#x60; - No join or leave sound. | [optional] [default to 'all']
**record_play_voice** | **bool** | Record and play their own voice. | [optional] 
**feedback** | **bool** | Enable option to send feedback to Zoom at the end of the meeting. | [optional] [default to False]
**co_host** | **bool** | Allow the host to add co-hosts. | [optional] [default to False]
**polling** | **bool** | Add polls to the meeting controls. | [optional] [default to False]
**attendee_on_hold** | **bool** | Allow host to put attendee on hold. | [optional] [default to False]
**annotation** | **bool** | Allow participants to use annotation tools. | [optional] [default to False]
**remote_control** | **bool** | Enable remote control during screensharing. | [optional] [default to False]
**non_verbal_feedback** | **bool** | Enable non-verbal feedback through screens. | [optional] [default to False]
**breakout_room** | **bool** | Allow host to split meeting participants into separate breakout rooms. | [optional] [default to False]
**remote_support** | **bool** | Allow host to provide 1:1 remote support to a participant. | [optional] [default to False]
**closed_caption** | **bool** | Enable closed captions. | [optional] [default to False]
**group_hd** | **bool** | Enable group HD video. | [optional] [default to False]
**virtual_background** | **bool** | Enable virtual background. | [optional] [default to False]
**far_end_camera_control** | **bool** | Allow another user to take control of the camera. | [optional] [default to False]
**share_dual_camera** | **bool** | Share dual camera (deprecated). | [optional] [default to False]
**waiting_room** | **bool** | Enable Waiting room - if enabled, attendees can only join after host approves. | [optional] [default to False]
**allow_live_streaming** | **bool** | Allow live streaming. | [optional] 
**workplace_by_facebook** | **bool** | Allow livestreaming by host through Workplace by Facebook. | [optional] 
**custom_live_streaming_service** | **bool** | Allow custom live streaming. | [optional] 
**custom_service_instructions** | **str** | Custom service instructions. | [optional] 
**show_meeting_control_toolbar** | **bool** | Always show meeting controls during a meeting. | [optional] 
**custom_data_center_regions** | **bool** | If set to &#x60;true&#x60;, you can [select data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) to use for hosting your real-time meeting and webinar traffic. These regions can be provided in the &#x60;data_center_regions&#x60; field. If set to &#x60;false&#x60;, the regions cannot be customized and the default regions will be used. | [optional] 
**data_center_regions** | **list[str]** | If you have set the value of &#x60;custom_data_center_regions&#x60; to &#x60;true&#x60;, specify the data center regions that you would like to opt in to (country codes from among: [\&quot;EU\&quot;, \&quot;HK\&quot;, \&quot;AU\&quot;, \&quot;IN\&quot;, \&quot;LA\&quot;, \&quot;TY\&quot;, \&quot;CN\&quot;, \&quot;US\&quot;, \&quot;CA\&quot;]).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


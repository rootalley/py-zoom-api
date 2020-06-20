# InlineResponse20070InMeeting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e2e_encryption** | **bool** | Require that all meetings are encrypted using AES. | [optional] 
**chat** | **bool** | Allow meeting participants to send chat message visible to all participants. | [optional] 
**private_chat** | **bool** | Allow meeting participants to send a private 1:1 message to another participant. | [optional] 
**auto_saving_chat** | **bool** | Automatically save all in-meeting chats. | [optional] 
**entry_exit_chime** | **str** | Play sound when participants join or leave. | [optional] 
**feedback** | **bool** | Enable users to provide feedback to Zoom at the end of the meeting. | [optional] 
**post_meeting_feedback** | **bool** | Display end-of-meeting experience feedback survey. | [optional] 
**co_host** | **bool** | Allow the host to add co-hosts. Co-hosts have the same in-meeting controls as the host. | [optional] 
**polling** | **bool** | Add &#x27;Polls&#x27; to the meeting controls. This allows the host to survey the attendees. | [optional] 
**attendee_on_hold** | **bool** | Allow hosts to temporarily remove an attendee from the meeting. | [optional] 
**show_meeting_control_toolbar** | **bool** | Always show meeting controls during a meeting. | [optional] 
**allow_show_zoom_windows** | **bool** | Show Zoom windows during screen share. | [optional] 
**annotation** | **bool** | Allow participants to use annotation tools to add information to shared screens. | [optional] 
**whiteboard** | **bool** | Allow participants to share a whiteboard that includes annotation tools. | [optional] 
**remote_control** | **bool** | During screen sharing, allow the person who is sharing to let others control the shared content. | [optional] 
**webinar_question_answer** | **bool** | Allow attendees to ask questions for the host and panelists to answer in the webinar. | [optional] 
**anonymous_question_answer** | **bool** |  | [optional] 
**breakout_room** | **bool** | Allow host to split meeting participants into separate, smaller rooms. | [optional] 
**closed_caption** | **bool** | Allow host to type closed captions or assign a participant/third party device to add closed captions. | [optional] 
**far_end_camera_control** | **bool** | Allow another user to take control of the camera during a meeting. | [optional] 
**group_hd** | **bool** | Enable higher quality video for host and participants. This will require more bandwidth. | [optional] 
**virtual_background** | **bool** | Enable virtual background. | [optional] 
**alert_guest_join** | **bool** | Allow participants who belong to your account to see that a guest (someone who does not belong to your account) is participating in the meeting/webinar. | [optional] 
**auto_answer** | **bool** | Enable users to see and add contacts to &#x27;auto-answer group&#x27; in the contact list on chat. Any call from members of this group will be automatically answered. | [optional] 
**sending_default_email_invites** | **bool** | Allow users to invite participants by email only by default. | [optional] 
**use_html_format_email** | **bool** | Allow  HTML formatting instead of plain text for meeting invitations scheduled with the Outlook plugin. | [optional] 
**dscp_marking** | **bool** | Enable DSCP marking for signaling and media packets. (Default is 56 for audio, 40 for video, and 40 for signaling.)  | [optional] 
**stereo_audio** | **bool** | Allow users to select stereo audio during a meeting. | [optional] 
**original_audio** | **bool** | Allow users to select original sound during a meeting. | [optional] 
**screen_sharing** | **bool** | Allow host and participants to share their screen or content during meetings. | [optional] 
**custom_data_center_regions** | **bool** | Displays whether or not custom [data center regions](https://support.zoom.us/hc/en-us/articles/360042411451-Selecting-data-center-regions-for-hosted-meetings-and-webinars) have been selected for meetings/webinars hosted by the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


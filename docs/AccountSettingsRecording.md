# AccountSettingsRecording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_recording** | **bool** | Allow hosts and participants to record the meeting using a local file. | [optional] 
**cloud_recording** | **bool** | Allow hosts to record and save the meeting in the cloud. | [optional] 
**record_speaker_view** | **bool** | Record the active speaker with a shared screen. | [optional] 
**record_gallery_view** | **bool** | Record the gallery view with a shared screen. | [optional] 
**record_audio_file** | **bool** | Record an audio only file. | [optional] 
**save_chat_text** | **bool** | Save the chat text from the meeting. | [optional] 
**show_timestamp** | **bool** | Add a timestamp to the recording. | [optional] 
**recording_audio_transcript** | **bool** | Automatically transcribe the audio of the meeting or webinar to the cloud. | [optional] 
**auto_recording** | **str** | Automatic recording:&lt;br&gt;&#x60;local&#x60; - Record on local.&lt;br&gt;&#x60;cloud&#x60; -  Record on cloud.&lt;br&gt;&#x60;none&#x60; - Disabled. | [optional] 
**cloud_recording_download** | **bool** | Cloud recording downloads. | [optional] 
**cloud_recording_download_host** | **bool** | Only the host can download cloud recordings. | [optional] 
**account_user_access_recording** | **bool** | Cloud recordings are only accessible to account members. People outside of your organization cannot open links that provide access to cloud recordings. | [optional] 
**auto_delete_cmr** | **bool** | Allow Zoom to permanantly delete recordings automatically after a specified number of days. | [optional] 
**auto_delete_cmr_days** | **int** | When &#x60;auto_delete_cmr&#x60; function is &#x27;true&#x27; this value will set the number of days before the auto deletion of cloud recordings. | [optional] 
**recording_password_requirement** | [**AccountSettingsRecordingRecordingPasswordRequirement**](AccountSettingsRecordingRecordingPasswordRequirement.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


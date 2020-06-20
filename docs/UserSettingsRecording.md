# UserSettingsRecording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_recording** | **bool** | Local recording. | [optional] 
**cloud_recording** | **bool** | Cloud recording. | [optional] [default to False]
**record_speaker_view** | **bool** | Record the active speaker view. | [optional] [default to False]
**record_gallery_view** | **bool** | Record the gallery view. | [optional] [default to False]
**record_audio_file** | **bool** | Record an audio only file. | [optional] [default to False]
**save_chat_text** | **bool** | Save chat text from the meeting. | [optional] [default to False]
**show_timestamp** | **bool** | Show timestamp on video. | [optional] [default to False]
**recording_audio_transcript** | **bool** | Audio transcript. | [optional] 
**auto_recording** | **str** | Automatic recording:&lt;br&gt;&#x60;local&#x60; - Record on local.&lt;br&gt;&#x60;cloud&#x60; - Record on cloud.&lt;br&gt;&#x60;none&#x60; - Disabled. | [optional] [default to 'local']
**host_pause_stop_recording** | **bool** | Host can pause/stop the auto recording in the cloud. | [optional] [default to False]
**auto_delete_cmr** | **bool** | Auto delete cloud recordings. | [optional] [default to False]
**auto_delete_cmr_days** | **int** | A specified number of days of auto delete cloud recordings. | [optional] 
**recording_password_requirement** | [**AccountSettingsRecordingRecordingPasswordRequirement**](AccountSettingsRecordingRecordingPasswordRequirement.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


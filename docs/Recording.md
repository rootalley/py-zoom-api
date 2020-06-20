# Recording

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The recording file ID. Included in the response of general query. | [optional] 
**meeting_id** | **str** | The meeting ID.  | [optional] 
**recording_start** | **str** | The recording start time. | [optional] 
**recording_end** | **str** | The recording end time. Response in general query. | [optional] 
**file_type** | **str** | The recording file type. The value of this field could be one of the following:&lt;br&gt; &#x60;MP4&#x60;: Video file of the recording.&lt;br&gt;&#x60;M4A&#x60; Audio-only file of the recording.&lt;br&gt;&#x60;TIMELINE&#x60;: Timestamp file of the recording. To get a timeline file, the \&quot;Add a timestamp to the recording\&quot; setting must be enabled in the [recording settings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-recording#h_3f14c3a4-d16b-4a3c-bbe5-ef7d24500048). The time will display in the host&#x27;s timezone, set on their Zoom profile. &lt;br&gt; &#x60;TRANSCRIPT&#x60;: Transcription file of the recording.&lt;br&gt; &#x60;CHAT&#x60;: A TXT file containing in-meeting chat messages that were sent during the meeting.&lt;br&gt;&#x60;CC&#x60;: File containing closed captions of the recording.&lt;br&gt;&lt;br&gt; A recording file object with file type of either &#x60;CC&#x60; or &#x60;TIMELINE&#x60; **does not have** the following properties:&lt;br&gt;  &#x60;id&#x60;, &#x60;status&#x60;, &#x60;file_size&#x60;, &#x60;recording_type&#x60;, and &#x60;play_url&#x60;. | [optional] 
**file_size** | **float** | The recording file size. | [optional] 
**play_url** | **str** | The URL using which a recording file can be played. | [optional] 
**download_url** | **str** | The URL using which the recording file can be downloaded. **To access a private or password protected cloud recording of a user in your account, you can use a [Zoom JWT App Type](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-jwt-app). Use the generated JWT token as the value of the &#x60;access_token&#x60; query parameter and include this query parameter at the end of the URL as shown in the example.**   &lt;br&gt; Example: &#x60;https://api.zoom.us/recording/download/{{ Download Path }}?access_token&#x3D;{{ JWT Token }}&#x60;  **Similarly, if the user has installed your OAuth app that contains recording scope(s), you can also use the user&#x27;s [OAuth access token](https://marketplace.zoom.us/docs/guides/auth/oauth) to download the Cloud Recording.**&lt;br&gt;  Example: &#x60;https://api.zoom.us/recording/download/{{ Download Path }}?access_token&#x3D;{{ OAuth Access Token }}&#x60;   | [optional] 
**status** | **str** | The recording status. | [optional] 
**deleted_time** | **str** | The time at which recording was deleted. Returned in the response only for trash query. | [optional] 
**recording_type** | **str** | The recording type. The value of this field can be one of the following:&lt;br&gt;&#x60;shared_screen_with_speaker_view(CC)&#x60;&lt;br&gt;&#x60;shared_screen_with_speaker_view&#x60;&lt;br&gt;&#x60;shared_screen_with_gallery_view&#x60;&lt;br&gt;&#x60;speaker_view&#x60;&lt;br&gt;&#x60;gallery_view&#x60;&lt;br&gt;&#x60;shared_screen&#x60;&lt;br&gt;&#x60;audio_only&#x60;&lt;br&gt;&#x60;audio_transcript&#x60;&lt;br&gt;&#x60;chat_file&#x60;&lt;br&gt;&#x60;TIMELINE&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


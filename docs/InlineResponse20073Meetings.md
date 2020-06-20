# InlineResponse20073Meetings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Universally Unique Identifier of a meeting instance. Each meeting instance will have its own meeting UUID. | [optional] 
**id** | **str** | Meeting ID - Unique Identifier for a meeting, also known as Meeting Number. | [optional] 
**host_id** | **str** | User ID of the user who is set as the host of the meeting. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**start_time** | **datetime** | The date and time at which the meeting started. | [optional] 
**duration** | **int** | The scheduled duration of the meeting. | [optional] 
**total_size** | **int** | The total size of the meeting in bytes. | [optional] 
**recording_count** | **int** | The total number of recordings retrieved from the account. | [optional] 
**recording_files** | [**list[InlineResponse20073RecordingFiles]**](InlineResponse20073RecordingFiles.md) | Recording files object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


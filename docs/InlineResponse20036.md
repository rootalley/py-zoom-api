# InlineResponse20036

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27; in it. | [optional] 
**id** | **int** | [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in \&quot;**long**\&quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**type** | **int** | Meeting type. | [optional] 
**topic** | **str** | Meeting topic. | [optional] 
**user_name** | **str** | User display name. | [optional] 
**user_email** | **str** | User email. | [optional] 
**start_time** | **datetime** | Meeting start time. | [optional] 
**end_time** | **datetime** | Meeting end time. | [optional] 
**duration** | **int** | Meeting duration. | [optional] 
**total_minutes** | **int** | Number of meeting minutes. This represents the total amount of meeting minutes attended by each participant including the host, for meetings hosted by the user. For instance if there were one host(named A) and one participant(named B) in a meeting, the value of total_minutes would be calculated as below:  **total_minutes** &#x3D; Total Meeting Attendance Minutes of A + Total Meeting Attendance Minutes of B | [optional] 
**participants_count** | **int** | Number of meeting participants. | [optional] 
**tracking_fields** | [**list[InlineResponse20036TrackingFields]**](InlineResponse20036TrackingFields.md) | Tracking fields. | [optional] 
**dept** | **str** | Department of the host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


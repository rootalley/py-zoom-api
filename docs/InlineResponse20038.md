# InlineResponse20038

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in \&quot;**long**\&quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**uuid** | **str** | Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). Please double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27; in it. | [optional] 
**start_time** | **datetime** | Meeting start time. | [optional] 
**questions** | [**list[InlineResponse20038Questions]**](InlineResponse20038Questions.md) | Array of meeting question objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


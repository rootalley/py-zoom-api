# InlineResponse20111

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in \&quot;**long**\&quot; format(represented as int64 data type in JSON), also known as the meeting number. | [optional] 
**join_url** | **str** | Unique URL for this registrant to join the meeting. This URL should only be shared with the registrant for whom the API request was made. If the meeting was [created](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate) with manual approval type (&#x60;approval_type&#x60;: 1), the join URL will not be returned in the response. | [optional] 
**registrant_id** | **str** | Unique identifier of the registrant. | [optional] 
**start_time** | **str** | The start time for the meeting. | [optional] 
**topic** | **str** | Topic of the meeting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# InlineResponse20042

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Webinar ID in \&quot;**long**\&quot; format(represented as int64 data type in JSON), also known as the webinar number. | [optional] 
**uuid** | **str** | Webinar UUID. Each Webinar instance will generate its own UUID(i.e., after a Webinar ends, a new UUID will be generated for the next instance of the Webinar). Please double encode your UUID when using it for API calls if the UUID begins with a &#x27;/&#x27; or contains &#x27;//&#x27; in it. | [optional] 
**start_time** | **datetime** | Webinar start time. | [optional] 
**questions** | [**list[InlineResponse20042Questions]**](InlineResponse20042Questions.md) | Array of webinar question objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


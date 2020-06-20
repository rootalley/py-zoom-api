# InlineResponse20073

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **datetime** | The start date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. | [optional] 
**to** | **datetime** | The end date for the monthly range for which you would like to retrieve recordings. The maximum range can be a month. The month should fall within the past six months period from the date of query. | [optional] 
**page_size** | **str** | The number of records returned within a single API call. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**meetings** | [**list[InlineResponse20073Meetings]**](InlineResponse20073Meetings.md) | Meetings Object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


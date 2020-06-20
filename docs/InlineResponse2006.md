# InlineResponse2006

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **date** | The date provided in the query parameter. If a date is not provided, the default value is the **current date**. | [optional] 
**page_size** | **int** | The number of records returned with a single API call. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.  | [optional] 
**messages** | [**list[InlineResponse2006Messages]**](InlineResponse2006Messages.md) | List of message(s). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


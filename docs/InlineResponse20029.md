# InlineResponse20029

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **date** | Start date for this report in &#x27;yyyy-mm-dd&#x27; format. | [optional] 
**next_page_token** | **str** | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 
**page_count** | **int** | The number of pages returned for the request made. | [optional] 
**page_size** | **int** | The number of records returned within a single API call. | [optional] 
**to** | **date** | End date for this report in &#x27;yyyy-mm-dd&#x27; format. | [optional] 
**total_records** | **int** | The number of all records available across pages. | [optional] 
**webinars** | [**list[WebinarMetrics1]**](WebinarMetrics1.md) | Array of webinar objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


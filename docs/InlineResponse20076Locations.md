# InlineResponse20076Locations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the location. | [optional] 
**name** | **str** | Name of the location. | [optional] 
**parent_location_id** | **str** | ID (Unique Identifier) of the parent location. For instance, if a Zoom Room is located in Floor 1 of Building A, the location of Building A will be the parent location of Floor 1 and the parent_location_id of Floor 1 will be the ID of Building A.&lt;br&gt; The value of parent_location_id of the top-level location (country) is the Account ID of the Zoom account. | [optional] 
**type** | **str** | The type of location. The value can be one of the following: &#x60;country&#x60;, &#x60;states&#x60;, &#x60;city&#x60;, &#x60;campus&#x60;, &#x60;building&#x60;, &#x60;floor&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


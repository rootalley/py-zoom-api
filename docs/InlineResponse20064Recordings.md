# InlineResponse20064Recordings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of recording | [optional] 
**caller_number** | **str** | Number of caller | [optional] 
**caller_number_type** | **str** | Type of caller&#x27;s number. 1 - internal | 2 - external | [optional] 
**caller_name** | **str** | Contact name of caller | [optional] 
**callee_number** | **str** | Number of callee | [optional] 
**callee_number_type** | **str** | Type of callee&#x27;s number. 1 - internal | 2 - external | [optional] 
**callee_name** | **str** | Contact name of callee | [optional] 
**direction** | **str** | Direction of the call. \&quot;inbound\&quot; | \&quot;outbound\&quot; | [optional] 
**duration** | **str** | Duration of the call | [optional] 
**download_url** | **str** | Download url for the recording. For security purposes, you must provide an OAuth access token in the auth header to download the recording file using this url. &lt;br&gt;  Example request:&lt;br&gt; &#x60;&#x60;&#x60; curl --request GET \\   --url {download_url} \\   --header &#x27;authorization: Bearer {access_token} \\   --header &#x27;content-type: application/json&#x27; &#x60;&#x60;&#x60;  | [optional] 
**date_time** | **str** | Date and time at which the record is received | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


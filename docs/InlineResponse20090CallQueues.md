# InlineResponse20090CallQueues

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the Call Queue. | [optional] 
**name** | **str** | Name of the Call Queue. | [optional] 
**extension_number** | **int** | Extension number assigned to the queue. | [optional] 
**phone_numbers** | [**list[InlineResponse20090PhoneNumbers]**](InlineResponse20090PhoneNumbers.md) | Phone number(s) assigned to the call queue. | [optional] 
**status** | **str** | Status of the Call Queue.&lt;br&gt;&#x60;active&#x60;: Call queue is enabled and active.&lt;br&gt;&#x60;inactive&#x60;: Call queue is inactive. Inactive call queues cannot be called but will retain its settings and appear in the [Call Queues](https://zoom.us/pbx/page/telephone/groups#/groups) page. | [optional] 
**site** | [**InlineResponse20090Site**](InlineResponse20090Site.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# InlineResponse20095CommonAreaPhones

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the common area phone. | [optional] 
**display_name** | **str** | Display name of the common area phone. | [optional] 
**device_type** | **str** | Type of device (manufacturer name + model name). Refer to the table here for a list of [supported devices](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice). | [optional] 
**mac_address** | **str** |  Mac address or serial number. | [optional] 
**calling_plans** | [**list[InlineResponse20095CallingPlans]**](InlineResponse20095CallingPlans.md) |  | [optional] 
**phone_numbers** | [**list[InlineResponse20095PhoneNumbers]**](InlineResponse20095PhoneNumbers.md) |  | [optional] 
**status** | **str** | Status of the common area phone. It can be either &#x60;online&#x60; or &#x60;offline&#x60;. | [optional] 
**site** | [**InlineResponse20095Site**](InlineResponse20095Site.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


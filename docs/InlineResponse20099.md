# InlineResponse20099

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the Shared Line Group. | [optional] 
**display_name** | **str** | Display Name of the Shared Line Group. | [optional] 
**extension_number** | **int** | Extension number assigned to the Shared Line Group. | [optional] 
**phone_numbers** | [**list[InlineResponse20099PhoneNumbers]**](InlineResponse20099PhoneNumbers.md) | Object representing information about phone number(s) assigned to the group. | [optional] 
**primary_number** | **str** | If you have multiple direct phone numbers assigned to the shared line group, this is the primary number selected for desk phones. The primary number shares the same line as the extension number. This means if a caller is routed to the shared line group through an auto receptionist, the line associated with the primary number will be used. | [optional] 
**site** | [**InlineResponse20099Site**](InlineResponse20099Site.md) |  | [optional] 
**members** | [**InlineResponse20099Members**](InlineResponse20099Members.md) |  | [optional] 
**timezone** | **str** | Timezone used for the Business Hours. | [optional] 
**status** | **str** | Status of the Shared Line Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


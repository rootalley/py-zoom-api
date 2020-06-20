# InlineResponse20094Users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the user (userId). | [optional] 
**phone_user_id** | **str** | Zoom Phone Identifier of the user. | [optional] 
**name** | **str** | Name of the user. | [optional] 
**email** | **str** | Email address of the user. | [optional] 
**site** | [**InlineResponse20094Site**](InlineResponse20094Site.md) |  | [optional] 
**extension_number** | **int** | Extension number assigned to the user&#x27;s Zoom phone number. | [optional] 
**status** | **str** | Displays the status of the user&#x27;s Zoom Phone license. The value can be either of the following:&lt;br&gt; &#x60;activate&#x60;: Active Zoom phone user.&lt;br&gt; &#x60;deactivate&#x60;: User with Zoom phone license disabled. This type of user can&#x27;t make or receive calls. | [optional] 
**calling_plans** | [**list[InlineResponse20094CallingPlans]**](InlineResponse20094CallingPlans.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


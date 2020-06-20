# InlineResponse2005Contacts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID of the contact. | [optional] 
**email** | **str** | Email address of the contact. | [optional] 
**first_name** | **str** | First name of the contact. | [optional] 
**last_name** | **str** | Last name of the contact. | [optional] 
**presence_status** | **str** | Presence status of the contact in Zoom Client. The value of this field can be one of the following: &#x60;Do_Not_Disturb&#x60;&lt;br&gt; &#x60;away&#x60;&lt;br&gt; &#x60;Available&#x60;&lt;br&gt; &#x60;Offline&#x60; | [optional] 
**phone_number** | **str** | Phone number of the user. | [optional] 
**sip_phone_number** | **str** | SIP Phone number of the user. Returned only if user has SIP phone enabled. | [optional] 
**direct_numbers** | **list[str]** | Direct Number(s) of a user who has Zoom Phone license assigned. | [optional] 
**extension_number** | **str** | Extension Number of a user who has Zoom Phone license assigned. | [optional] 
**im_group_id** | **str** | Unique Identifier of the [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) in which the user has been added. An IM Directory group is not the same as a channel. IM Directory allows administrators to assign users in their account to groups that display within the Contacts list on Zoom clients.  | [optional] 
**im_group_name** | **str** | Name of the [IM directory group](https://support.zoom.us/hc/en-us/articles/203749815-IM-Management) in which the user has been added. An IM Directory group is not the same as a channel. IM Directory allows administrators to assign users in their account to groups that display within the Contacts list on Zoom clients.  | [optional] 
**dept** | **str** | Department of the contact as provided in the user&#x27;s Zoom profile. | [optional] 
**job_title** | **str** | Department of the user as provided in the user&#x27;s Zoom profile. | [optional] 
**location** | **str** | Location of the user as provided in the user&#x27;s Zoom profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


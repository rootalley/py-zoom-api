# Body161

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Required only if [multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) have been enabled. This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/zoom-api/phone-site/listphonesites) API. | 
**name** | **str** | Name of the Call Queue. | 
**extension_number** | **int** | Phone extension number for the site.&lt;br&gt;  If a site code has been [assigned](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_79ca9c8f-c97b-4486-aa59-d0d9d31a525b) to the site, provide the short extension number instead of the original extension number.. | [optional] 
**description** | **str** | Description for the Call Queue. | [optional] 
**members** | [**PhonecallQueuesMembers**](PhonecallQueuesMembers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


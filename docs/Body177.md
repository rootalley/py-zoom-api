# Body177

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from List Sites API. | [optional] 
**display_name** | **str** | Display name of the Common area phone. | 
**description** | **str** | Description for the common area phone. | [optional] 
**extension_number** | **int** | Extension number assigned to the common area phone. If site code is enabled, provide the short extension number instead. | 
**mac_address** | **str** | Mac Address (serial number) of the common area desk phone. These examples show the formats supported: &#x60;64-16-7f-37-90-92&#x60; or &#x60;64167f379092&#x60; | 
**type** | **str** | Phone device manufacturer name. Refer to the \&quot;Manufacturer Name\&quot; field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table. | 
**model** | **str** | Device Model name. Refer to the \&quot;Model Name\&quot; field in [this](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice) table. | [optional] 
**time_zone** | **str** | [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area phone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


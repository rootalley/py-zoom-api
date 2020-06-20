# InlineResponse20027Participants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Universally unique identifier of the Participant. It is the same as the User ID of the participant if the participant joins the meeting by logging into Zoom. If the participant joins the meeting without logging in, the value of this field will be blank. | [optional] 
**user_id** | **str** | Participant ID | [optional] 
**user_name** | **str** | Participant display name. | [optional] 
**device** | **str** | The type of device using which the participant joined the meeting. | [optional] 
**ip_address** | **str** | Participant&#x27;s IP address. | [optional] 
**location** | **str** | Participant&#x27;s location. | [optional] 
**network_type** | **str** | Participant&#x27;s network type. | [optional] 
**microphone** | **str** | The type of Microphone that participant used during the meeting. | [optional] 
**speaker** | **str** | The type of speaker participant used during the meeting. | [optional] 
**camera** | **str** | The type of camera used by participant during the meeting. | [optional] 
**data_center** | **str** | Data Center where participant&#x27;s meeting data is stored. | [optional] 
**connection_type** | **str** | Participant connection type. | [optional] 
**join_time** | **datetime** | The time at which participant joined the meeting. | [optional] 
**leave_time** | **datetime** | The time at which participant left the meeting. | [optional] 
**share_application** | **bool** | Indicates whether or not a user selected to share an iPhone/iPad app during the screenshare.  | [optional] 
**share_desktop** | **bool** | Indicates whether or not a user selected to share their desktop during the screenshare.  | [optional] 
**share_whiteboard** | **bool** | Indicates whether or not a user selected to share their whiteboard during the screenshare.  | [optional] 
**recording** | **bool** | Indicates whether or not recording was used during the meeting. | [optional] 
**pc_name** | **str** | Name of Participant&#x27;s PC. | [optional] 
**domain** | **str** | Participant&#x27;s PC domain. | [optional] 
**mac_addr** | **str** | Participant&#x27;s MAC address. | [optional] 
**harddisk_id** | **str** | Participant&#x27;s hard disk ID. | [optional] 
**version** | **str** | Participant&#x27;s Zoom Client version. | [optional] 
**in_room_participants** | **int** | The number of participants who joined via Zoom Room. | [optional] 
**leave_reason** | **str** | Possible reasons for why participant left the meeting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


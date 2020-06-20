# Body38

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify the type of action to be performed:&lt;br&gt;&lt;br&gt; &#x60;move&#x60;: Simultaneously remove a member from one group and move the member to a different group.&lt;br&gt; &#x60;set_primary&#x60;: Set a primary group for the user.  | 
**target_group_id** | **str** | Can be retrieved by calling [GET /groups](https://marketplace.zoom.us/docs/api-reference/zoom-api/groups/groups) API.&lt;br&gt;  To move a user, use this field to specify the groupId of the group where the member is to be moved.&lt;br&gt;  To set a primary group for the user, provide the groupId of the group which is going to be the primary group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


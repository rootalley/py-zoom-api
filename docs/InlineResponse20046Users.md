# InlineResponse20046Users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID. | [optional] 
**first_name** | **str** | User&#x27;s first name. | [optional] 
**last_name** | **str** | User&#x27;s last name. | [optional] 
**email** | **str** | User&#x27;s email address. | [default to 'john.doe@gmail.com']
**type** | **int** | User&#x27;s plan type.&lt;br&gt; &#x60;1&#x60; - Basic.&lt;br&gt; &#x60;2&#x60; - Licensed.&lt;br&gt; &#x60;3&#x60; - On-prem.  | 
**status** | **str** | User&#x27;s status | [optional] 
**pmi** | **int** | Personal meeting ID of the user. | [optional] 
**timezone** | **str** | The time zone of the user. | [optional] 
**dept** | **str** | Department, if provided by the user. | [optional] 
**created_at** | **datetime** | The time when user&#x27;s account was created. | [optional] 
**last_login_time** | **datetime** | User&#x27;s last login time. There is a three-days buffer period for this field. For example, if user first logged in on 2020-01-01 and then logged out and logged in on 2020-01-02, the value of this field will still reflect the login time of 2020-01-01. However, if the user logs in on 2020-01-04, the value of this field will reflect the corresponding login time since it exceeds the three-day buffer period. | [optional] 
**last_client_version** | **str** | The last client version that user used to login. | [optional] 
**group_ids** | **list[str]** | IDs of groups where the user is a member. | [optional] 
**im_group_ids** | **list[str]** | IDs of IM directory groups where the user is a member. | [optional] 
**verified** | **int** | Display whether the user&#x27;s email address for the Zoom account is verified or not. &lt;br&gt; &#x60;1&#x60; - Verified user email.&lt;br&gt; &#x60;0&#x60; - User&#x27;s email not verified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


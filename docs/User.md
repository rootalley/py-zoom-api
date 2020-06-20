# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | User&#x27;s first name. | [optional] 
**last_name** | **str** | User&#x27;s last name. | [optional] 
**email** | **str** | User&#x27;s email address. | [default to 'john.doe@email.com']
**type** | **int** | User&#x27;s plan type:&lt;br&gt;&#x60;1&#x60; - Basic.&lt;br&gt;&#x60;2&#x60; - Licensed.&lt;br&gt;&#x60;3&#x60; - On-prem. | 
**role_name** | **str** | User&#x27;s [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) name. | [optional] 
**pmi** | **int** | Personal meeting ID. | [optional] 
**use_pmi** | **bool** | Use Personal Meeting ID for instant meetings. | [optional] [default to False]
**timezone** | **str** | The time zone of the user. | [optional] 
**dept** | **str** | Department. | [optional] 
**created_at** | **datetime** | User create time. | [optional] 
**last_login_time** | **datetime** | User last login time. | [optional] 
**last_client_version** | **str** | User last login client version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


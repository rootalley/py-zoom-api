# InlineResponse20047

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | User&#x27;s account ID. | [optional] 
**cms_user_id** | **str** | CMS ID of user, only enabled for Kaltura integration. | [optional] 
**company** | **str** | User&#x27;s company. | [optional] 
**created_at** | **datetime** | User create time. | [optional] 
**dept** | **str** | Department. | [optional] 
**email** | **str** | User&#x27;s email address. | [default to 'john.doe@email.com']
**first_name** | **str** | User&#x27;s first name. | [optional] 
**group_ids** | **list[str]** | IDs of the web groups user belongs to.  | [optional] 
**host_key** | **str** | User&#x27;s host key. | [optional] 
**id** | **str** | User ID. | [optional] 
**im_group_ids** | **list[str]** | IM IDs of the groups user belongs to. | [optional] 
**jid** | **str** |  | [optional] 
**job_title** | **str** | User&#x27;s job title. | [optional] 
**language** | **str** | Default language for the Zoom Web Portal. | [optional] 
**last_client_version** | **str** | User last login client version. | [optional] 
**last_login_time** | **datetime** | User last login time. | [optional] 
**last_name** | **str** | User&#x27;s last name. | [optional] 
**location** | **str** | User&#x27;s location. | [optional] 
**personal_meeting_url** | **str** | User&#x27;s personal meeting url. | [optional] 
**phone_country** | **str** | User&#x27;s country for Company Phone Number. | [optional] 
**phone_number** | **str** | User&#x27;s phone number. | [optional] 
**pic_url** | **str** | The URL for user&#x27;s profile picture. | [optional] 
**pmi** | **int** | Personal meeting ID. | [optional] 
**role_name** | **str** | User&#x27;s [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) name. | [optional] 
**status** | **str** | Status of user&#x27;s account. | [optional] 
**timezone** | **str** | The time zone of the user. | [optional] 
**type** | **int** | User&#x27;s plan type:&lt;br&gt;&#x60;1&#x60; - Basic.&lt;br&gt;&#x60;2&#x60; - Licensed.&lt;br&gt;&#x60;3&#x60; - On-prem. | 
**use_pmi** | **bool** | Displays &#x60;true&#x60; if user has enabled PMI for instant meetinsgs, &#x60;false&#x60; otherwise. | [optional] [default to False]
**vanity_url** | **str** | Personal meeting room URL, if the user has one. | [optional] 
**verified** | **int** | Displays whether user is verified or not. &lt;br&gt; &#x60;1&#x60; - Account verified.&lt;br&gt; &#x60;0&#x60; - Account not verified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


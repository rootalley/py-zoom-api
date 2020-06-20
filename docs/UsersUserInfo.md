# UsersUserInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address. | 
**type** | **int** | User type:&lt;br&gt;&#x60;1&#x60; - Basic.&lt;br&gt;&#x60;2&#x60; - Licensed.&lt;br&gt;&#x60;3&#x60; - On-prem. | 
**first_name** | **str** | User&#x27;s first name: cannot contain more than 5 Chinese words. | [optional] 
**last_name** | **str** | User&#x27;s last name: cannot contain more than 5 Chinese words. | [optional] 
**password** | **str** | User password. Only used for the \&quot;autoCreate\&quot; function. The password has to have a minimum of 8 characters and maximum of 32 characters. By default (basic requirement), password must have at least one letter (a, b, c..), at least one number (1, 2, 3...) and include both uppercase and lowercase letters. It should not contain only one identical character repeatedly (&#x27;11111111&#x27; or &#x27;aaaaaaaa&#x27;) and it cannot contain consecutive characters (&#x27;12345678&#x27; or &#x27;abcdefgh&#x27;).  **Note:** If the account owner or admin has enabled [enhanced password requirements](https://support.zoom.us/hc/en-us/articles/360034675592-Advanced-security-settings#h_fa9186e4-6818-4f7a-915c-2e25c19f0acd), the value provided in this field must meet those requirements. These requirements can be retrieved by calling the [Get Account Settings API](https://marketplace.zoom.us/docs/api-reference/zoom-api/accounts/accountsettings) and referring to the &#x60;password_requirement&#x60; field present in the &#x60;security&#x60; object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


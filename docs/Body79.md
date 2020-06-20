# Body79

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify how to create the new user: &lt;br&gt;&#x60;create&#x60; - User will get an email sent from Zoom. There is a confirmation link in this email. The user will then need to use the link to activate their Zoom account. The user can then set or change their password.&lt;br&gt;&#x60;autoCreate&#x60; - This action is provided for the enterprise customer who has a managed domain. This feature is disabled by default because of the security risk involved in creating a user who does not belong to your domain.&lt;br&gt;&#x60;custCreate&#x60; - Users created via this option do not have passwords and will not have the ability to log into the Zoom Web Portal or the Zoom Client. These users can still host and join meetings using the &#x60;start_url&#x60; and &#x60;join_url&#x60; respectively. To use this option, you must contact the ISV Platform Sales team at isv@zoom.us.&lt;br&gt;&#x60;ssoCreate&#x60; - This action is provided for the enabled “Pre-provisioning SSO User” option. A user created in this way has no password. If not a basic user, a personal vanity URL using the user name (no domain) of the provisioning email will be generated. If the user name or PMI is invalid or occupied, it will use a random number or random personal vanity URL. | 
**user_info** | [**UsersUserInfo**](UsersUserInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


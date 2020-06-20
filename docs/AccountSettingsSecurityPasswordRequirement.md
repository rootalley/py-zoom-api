# AccountSettingsSecurityPasswordRequirement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_password_length** | **int** | Specify a minimum length for the password. The password length can be from a minimum of 9 characters, up to 14 characters. If you provide &#x60;0&#x60; as the value of this field, this field will be disabled and not be used and the basic password length requirement (minimum of 8 characters) will be applied for the requirement. | [optional] 
**have_special_character** | **bool** | If the value of this field is set to &#x60;true&#x60;, the password must have at least one special character(!, @, #...). | [optional] 
**consecutive_characters_length** | **int** |  Specify the max length of consecutive characters(abcde...) that can be used in a password. If you set the value of this field to &#x60;0&#x60;, no restriction will be applied on consecutive characters.   If you would like to set this restriction, you can specify a number between 4 and 8 that define the maximum allowed length for consecutive characters in a password.  The max allowed length will be &#x60;n-1&#x60; where &#x60;n&#x60; refers to the value you provide for this field.  For instance, if you provide &#x60;4&#x60; as the value, there can only be a maximum of &#x60;3&#x60; consecutive characters in a password(example: abc1x@8fdh). | [optional] 
**weak_enhance_detection** | **bool** | If the value of this field is set to &#x60;true&#x60;, user passwords will have to pass detection through a weak password dictionary in case hackers use simple passwords to sign in to your users’ accounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


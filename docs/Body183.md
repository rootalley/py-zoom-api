# Body183

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | **str** | Specify the match type for the blocked list. The values can be one of the following:&lt;br&gt;&lt;br&gt; &#x60;phoneNumber&#x60;: Choose this option (Phone Number Match) if you want to block a specific phone number. Then, in the &#x60;phone_number&#x60; field, provide the phone number along with the country code.&lt;br&gt;&lt;br&gt; &#x60;prefix&#x60;: Choose this option (Prefix Match) if you want to block all numbers with a specific country code and area code. Next, in the &#x60;phone_number&#x60; field, enter a country code as part of the prefix. For example, entering 1907 blocks numbers with country code 1 and area code 907. | [optional] 
**phone_number** | **str** | The phone number to be blocked if you passed \&quot;phoneNumber\&quot; as the value for the &#x60;match_type&#x60; field. If you passed \&quot;prefix\&quot; as the value for the &#x60;match_type&#x60; field, provide the prefix of the phone number here including the country code. For example, entering 1905 blocks numbers with country code 1 and area code 905.  | [optional] 
**block_type** | **str** | State whether you want the block type to be inbound or outbound.&lt;br&gt; &#x60;inbound&#x60;: Pass this value to prevent the blocked number or prefix from calling in to phone users.&lt;br&gt; &#x60;outbound&#x60;: Pass this value to prevent phone users from calling the blocked number or prefix. | [optional] 
**status** | **str** | Enable or disable the blocking. One of the following values are allowed:&lt;br&gt; &#x60;active&#x60;: Keep the blocking active.&lt;br&gt; &#x60;inactive&#x60;: Disable the blocking. | [optional] 
**comment** | **str** | Provide a comment to help you identify the blocked number or prefix. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# InlineResponse20045

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tsp_provider** | **str** | Telephony Service Provider. | [optional] 
**enable** | **bool** | Enable Telephony Service Provider for account users. | [optional] 
**dial_in_numbers** | [**list[InlineResponse20045DialInNumbers]**](InlineResponse20045DialInNumbers.md) |  | [optional] 
**tsp_enabled** | **bool** | Enable TSP feature for account. This has to be enabled to use any other tsp settings/features. | [optional] 
**master_account_setting_extended** | **bool** | For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account. | [optional] 
**modify_credential_forbidden** | **bool** | Control restriction on account users being able to modify their TSP credentials. | [optional] 
**dial_in_number_unrestricted** | **bool** | Control restriction on account users adding a TSP number outside of account&#x27;s dial in numbers. | [optional] 
**tsp_bridge** | **str** | Telephony bridge zone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


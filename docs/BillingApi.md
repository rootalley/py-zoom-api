# swagger_client.BillingApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_billing**](BillingApi.md#account_billing) | **GET** /accounts/{accountId}/billing | Get Billing Information
[**account_billing_update**](BillingApi.md#account_billing_update) | **PATCH** /accounts/{accountId}/billing | Update Billing Information
[**account_plan_addon_cancel**](BillingApi.md#account_plan_addon_cancel) | **PATCH** /accounts/{accountId}/plans/addons/status | Cancel  Additional Plans
[**account_plan_addon_create**](BillingApi.md#account_plan_addon_create) | **POST** /accounts/{accountId}/plans/addons | Add an Additional Plan
[**account_plan_addon_update**](BillingApi.md#account_plan_addon_update) | **PUT** /accounts/{accountId}/plans/addons | Update an Additional Plan
[**account_plan_base_delete**](BillingApi.md#account_plan_base_delete) | **PATCH** /accounts/{accountId}/plans/base/status | Cancel Base Plan
[**account_plan_base_update**](BillingApi.md#account_plan_base_update) | **PUT** /accounts/{accountId}/plans/base | Update a Base Plan
[**account_plan_create**](BillingApi.md#account_plan_create) | **POST** /accounts/{accountId}/plans | Subscribe to Plans
[**account_plans**](BillingApi.md#account_plans) | **GET** /accounts/{accountId}/plans | Get Plan Information
[**get_plan_usage**](BillingApi.md#get_plan_usage) | **GET** /accounts/{accountId}/plans/usage | Get Plan Usage

# **account_billing**
> InlineResponse20014 account_billing(account_id)

Get Billing Information

Get [billing information](https://support.zoom.us/hc/en-us/articles/201363263-About-Billing) of a Sub Account under a Master Account.<br>Only Master Accounts can use this API. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.<br>  **Prerequisites:** * Pro or a higher paid account with Master Account option enabled. <br> **Scope**:`billing:master`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.

try:
    # Get Billing Information
    api_response = api_instance.account_billing(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->account_billing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_billing_update**
> account_billing_update(body, account_id)

Update Billing Information

Update [billing information](https://support.zoom.us/hc/en-us/articles/201363263-About-Billing) for a Sub Account under a Master account. <aside>This API can only be used to update Billing information of Pro or higher Sub Accounts whose billing charges are paid by their Master account. Only Master Accounts can use this API. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br>  **Prerequisites:** * Pro or a higher paid account with Master Account option enabled. <br> **Scope**:`billing:master`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body24() # Body24 | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Update Billing Information
    api_instance.account_billing_update(body, account_id)
except ApiException as e:
    print("Exception when calling BillingApi->account_billing_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body24**](Body24.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_addon_cancel**
> account_plan_addon_cancel(account_id, body=body)

Cancel  Additional Plans

[Cancel additional plan](https://support.zoom.us/hc/en-us/articles/203634215-How-Do-I-Cancel-My-Subscription-) of a Sub Account. The cancellation does not provide refund for the current subscription. The service remains active for the current session. <aside> Only a Master Account can use this API to cancel the addon plans for a Sub Account whose billing charges are paid by the Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the <a href=\"https://zoom.us/plan/api\">ISV team</a> for more details.</aside><br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>  **Prerequisites:**<br> * Pro or a higher plan with Master Account option enabled. * The Sub Account must be a paid account.<br> **Scope:** `billing:master`<br>  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = swagger_client.Body127() # Body127 |  (optional)

try:
    # Cancel  Additional Plans
    api_instance.account_plan_addon_cancel(account_id, body=body)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_addon_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**Body127**](Body127.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_addon_create**
> account_plan_addon_create(body, account_id)

Add an Additional Plan

Add an additional plan for a Sub Account. <br> <aside> Only a Master Account can use this API to subscribe addon plans for a Sub Account whose billing charges are paid by the Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br> <br>**Prerequisites:**<br> * Pro or a higher plan with Master Account enabled. * The Sub Account must be a paid account. The billing charges for the Sub Account must be paid by the Master Account.<br> **Scopes**: `billing:master`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
body = NULL # object | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Add an Additional Plan
    api_instance.account_plan_addon_create(body, account_id)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_addon_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_addon_update**
> account_plan_addon_update(body, account_id)

Update an Additional Plan

Update an additional plan for a sub account.<br><br> <aside> Only a Master Account can use this API to update the addon plans for a Sub Account whose billing charges are paid by the Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br> <br>**Prerequisites:**<br> * Pro or a higher plan with Master Account enabled. * The Sub Account must be a paid account. The billing charges for the Sub Account must be paid by the Master Account.<br> **Scopes**: `billing:master`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br>    

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body30() # Body30 | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Update an Additional Plan
    api_instance.account_plan_addon_update(body, account_id)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_addon_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body30**](Body30.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_base_delete**
> account_plan_base_delete(account_id, body=body)

Cancel Base Plan

[Cancel a base plan](https://support.zoom.us/hc/en-us/articles/203634215-How-Do-I-Cancel-My-Subscription-) for a sub account. <aside> <aside> Only a Master Account can use this API to cancel the base plan of a Sub Account whose billing charges are paid by the Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br></aside><br><br>  **Scopes**: `billing:master`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:**<br> * The Sub Account must have a Pro or a higher plan.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = swagger_client.Body125() # Body125 |  (optional)

try:
    # Cancel Base Plan
    api_instance.account_plan_base_delete(account_id, body=body)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_base_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**Body125**](Body125.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_base_update**
> account_plan_base_update(body, account_id)

Update a Base Plan

Update a base plan of a Sub Account. <aside> <aside> Only a Master Account can use this API to update the base plan of a Sub Account whose billing charges are paid by the Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br></aside> **Scopes:** `billing:master`<br><br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`<br> **Prerequisites:**<br> * The Sub Account must have a Pro or a higher plan.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body28() # Body28 | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Update a Base Plan
    api_instance.account_plan_base_update(body, account_id)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_base_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body28**](Body28.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plan_create**
> account_plan_create(body, account_id)

Subscribe to Plans

Subscribe plans for a Sub Account under a Master Account. <aside> The plans can only be subscribed for an existing free Sub Account and the subscriptions charge for these plans should be paid by a Master Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br> **Scopes**: `billing:master`<br>  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body26() # Body26 | 
account_id = 'account_id_example' # str | The account ID.

try:
    # Subscribe to Plans
    api_instance.account_plan_create(body, account_id)
except ApiException as e:
    print("Exception when calling BillingApi->account_plan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body26**](Body26.md)|  | 
 **account_id** | **str**| The account ID. | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_plans**
> InlineResponse20015 account_plans(account_id)

Get Plan Information

Get plan information for a Sub Account under the Master account.  <aside> This API can only be used by a Master Account that pays for the billing charges of the associated Pro or a higher Sub Account. Zoom only assigns this privilege to trusted partners and only approved partners can use this API. Contact the [**ISV team**](https://zoom.us/plan/api) for more details.</aside><br><br> **Scopes:** `billing:master`<br> **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br>    

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The account ID.

try:
    # Get Plan Information
    api_response = api_instance.account_plans(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->account_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account ID. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_usage**
> InlineResponse20072 get_plan_usage(account_id)

Get Plan Usage

Get information on usage of [plans](https://marketplace.zoom.us/docs/api-reference/other-references/plans) of a Sub Account or a Master Account. To get plan usage for Master Account, provide the keyword \"me\" as the value of the `accountId` path parameter. To get plan usage of Sub Accounts, provide the actual account Id of the Sub Account as the value of the `accountId` path parameter.   **Prerequisite**:<br> Account type: Master Account on a paid Pro, Business or Enterprise plan.<br> **Scope:** `billing:master`<br>  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BillingApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    # Get Plan Usage
    api_response = api_instance.get_plan_usage(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_plan_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


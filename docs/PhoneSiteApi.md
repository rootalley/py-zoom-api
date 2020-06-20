# swagger_client.PhoneSiteApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone_site**](PhoneSiteApi.md#create_phone_site) | **POST** /phone/sites | Create a Phone Site
[**delete_phone_site**](PhoneSiteApi.md#delete_phone_site) | **DELETE** /phone/sites/{siteId} | Delete a Phone Site
[**get_a_site**](PhoneSiteApi.md#get_a_site) | **GET** /phone/sites/{siteId} | Get Phone Site Details
[**list_phone_sites**](PhoneSiteApi.md#list_phone_sites) | **GET** /phone/sites | List Phone Sites
[**update_site_details**](PhoneSiteApi.md#update_site_details) | **PATCH** /phone/sites/{siteId} | Update Phone Site Details

# **create_phone_site**
> InlineResponse204 create_phone_site(body=body)

Create a Phone Site

Sites allow you to organize Zoom Phone users in your organization. Use this API to create a [Site](https://support.zoom.us/hc/en-us/articles/360020809672).<br> **Prerequisites:**<br> * Multiple Sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15). * Pro or a higher account with Zoom Phone enabled. **Scope:** `phone:write:admin`<br>     **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneSiteApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body6() # Body6 |  (optional)

try:
    # Create a Phone Site
    api_response = api_instance.create_phone_site(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSiteApi->create_phone_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phone_site**
> object delete_phone_site(site_id, transfer_site_id)

Delete a Phone Site

Sites allow you to organize Zoom Phone users in your organization. Use this API to delete a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672) in a Zoom account. To delete a site, in the query parameter, you must provide the Site ID of another site where the assets of current site (users, numbers and phones) can be transferred to.  You cannot use this API to delete the main site.  **Prerequisites:** <br> * Account must have a Pro or a higher plan with Zoom Phone license.  * [Multiple Sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) must be enabled.<br> **Scope:** `phone:write:admin` <br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneSiteApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique Identifier of the Site.
transfer_site_id = 'transfer_site_id_example' # str | The Site ID of another site where the assets of the current site (users, numbers and phones) can be transferred to.

try:
    # Delete a Phone Site
    api_response = api_instance.delete_phone_site(site_id, transfer_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSiteApi->delete_phone_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique Identifier of the Site. | 
 **transfer_site_id** | **str**| The Site ID of another site where the assets of the current site (users, numbers and phones) can be transferred to. | 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_site**
> InlineResponse2004 get_a_site(site_id)

Get Phone Site Details

Sites allow you to organize Zoom Phone users in your organization. Use this API to get information about a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672).   **Prerequisites:** <br> * Account must have a Pro or a higher plan with Zoom Phone license. * Multiple Sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15).<br> **Scope:** `phone:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneSiteApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique Identifier of the Site.

try:
    # Get Phone Site Details
    api_response = api_instance.get_a_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSiteApi->get_a_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique Identifier of the Site. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_phone_sites**
> InlineResponse2003 list_phone_sites(page_size=page_size, next_page_token=next_page_token)

List Phone Sites

Sites allow you to organize Zoom Phone users in your organization. Use this API to list all the [sites](https://support.zoom.us/hc/en-us/articles/360020809672) that have been created for an account.<br> **Prerequisites:**<br> * Multiple Sites must be [enabled](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15). * Pro or a higher account with Zoom Phone enabled.  **Scope:** `phone:read:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.PhoneSiteApi(swagger_client.ApiClient(configuration))
page_size = 30 # int | The number of records returned within a single API call. (optional) (default to 30)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List Phone Sites
    api_response = api_instance.list_phone_sites(page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSiteApi->list_phone_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records returned within a single API call. | [optional] [default to 30]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_details**
> object update_site_details(site_id, body=body)

Update Phone Site Details

Sites allow you to organize Zoom Phone users in your organization. Use this API to update information about a specific [site](https://support.zoom.us/hc/en-us/articles/360020809672).   **Prerequisites:** <br> * Account must have a Pro or a higher plan with Zoom Phone license. * **Scope:** `phone:write:admin`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  

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
api_instance = swagger_client.PhoneSiteApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Unique Identifier of the Site.
body = swagger_client.Body8() # Body8 |  (optional)

try:
    # Update Phone Site Details
    api_response = api_instance.update_site_details(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneSiteApi->update_site_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Unique Identifier of the Site. | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


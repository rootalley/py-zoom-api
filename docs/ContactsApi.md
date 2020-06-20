# swagger_client.ContactsApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_contact**](ContactsApi.md#get_user_contact) | **GET** /chat/users/me/contacts/{contactId} | Get User&#x27;s Contact Details
[**get_user_contacts**](ContactsApi.md#get_user_contacts) | **GET** /chat/users/me/contacts | List User&#x27;s Contacts
[**search_company_contacts**](ContactsApi.md#search_company_contacts) | **GET** /contacts | Search Company Contacts

# **get_user_contact**
> InlineResponse2009 get_user_contact(contact_id, query_presence_status=query_presence_status)

Get User's Contact Details

A user under an organization’s Zoom account has internal users listed under Company Contacts in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts). Call this API to get information on a specific contact of the Zoom user.  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b>This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope**: `chat_contact:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
contact_id = 'contact_id_example' # str | The user's contact Id or email address. The contact can be either a company contact or an external contact.
query_presence_status = true # bool | The presence status of the contact.  Include this query parameter with a value of `true` to get the presence status of the contact in the response. (optional)

try:
    # Get User's Contact Details
    api_response = api_instance.get_user_contact(contact_id, query_presence_status=query_presence_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_user_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| The user&#x27;s contact Id or email address. The contact can be either a company contact or an external contact. | 
 **query_presence_status** | **bool**| The presence status of the contact.  Include this query parameter with a value of &#x60;true&#x60; to get the presence status of the contact in the response. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_contacts**
> InlineResponse2008 get_user_contacts(type=type, page_size=page_size, next_page_token=next_page_token)

List User's Contacts

A user under an organization’s Zoom account has internal users listed under Company Contacts in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts). Call this API to list all the contacts of a Zoom user. Zoom contacts are categorized into \"company contacts\" and \"external contacts\". You must specify the contact type in the `type` query parameter. If you do not specify, by default, the type will be set as company contact.  <p style=\"background-color:#e1f5fe; color:#01579b; padding:8px\"> <b>Note: </b> This API only supports <b>user-managed</b> <a href=\"https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app\">OAuth app</a>.</p><br>  **Scope**: `chat_contact:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
type = 'company' # str | The type of contact. The value can be one of the following: `company`: Contacts from the user's organization. `external`: External contacts.  (optional) (default to company)
page_size = 10 # int | The number of records returned with a single API call. (optional) (default to 10)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # List User's Contacts
    api_response = api_instance.get_user_contacts(type=type, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_user_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of contact. The value can be one of the following: &#x60;company&#x60;: Contacts from the user&#x27;s organization. &#x60;external&#x60;: External contacts.  | [optional] [default to company]
 **page_size** | **int**| The number of records returned with a single API call. | [optional] [default to 10]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_company_contacts**
> InlineResponse2005 search_company_contacts(search_key, query_presence_status=query_presence_status, page_size=page_size, next_page_token=next_page_token)

Search Company Contacts

A user under an organization's Zoom account has internal users listed under Company Contacts in the Zoom Client. Use this API to search users that are in the company contacts of a Zoom account. Using the `search_key` query parameter, provide either first name, last name or the email address of the user that you would like to search for. Optionally, set `query_presence_status` to `true` in order to include the presence status of a contact. <br><br>  **Scopes:** `contact:read:admin`, `contact:read`<br>   **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium` 

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
api_instance = swagger_client.ContactsApi(swagger_client.ApiClient(configuration))
search_key = 'search_key_example' # str | Provide the keyword - either first name, last name or email of the contact whom you have to search for.
query_presence_status = 'query_presence_status_example' # str | Set `query_presence_status` to `true` in order to include the presence status of a contact in the response. (optional)
page_size = 1 # int | The number of records to be returned with a single API call. (optional) (default to 1)
next_page_token = 'next_page_token_example' # str | The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. (optional)

try:
    # Search Company Contacts
    api_response = api_instance.search_company_contacts(search_key, query_presence_status=query_presence_status, page_size=page_size, next_page_token=next_page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->search_company_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**| Provide the keyword - either first name, last name or email of the contact whom you have to search for. | 
 **query_presence_status** | **str**| Set &#x60;query_presence_status&#x60; to &#x60;true&#x60; in order to include the presence status of a contact in the response. | [optional] 
 **page_size** | **int**| The number of records to be returned with a single API call. | [optional] [default to 1]
 **next_page_token** | **str**| The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


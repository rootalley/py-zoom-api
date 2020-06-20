# swagger_client.TrackingFieldApi

All URIs are relative to *https://api.zoom.us/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trackingfield_create**](TrackingFieldApi.md#trackingfield_create) | **POST** /tracking_fields | Create a Tracking Field
[**trackingfield_delete**](TrackingFieldApi.md#trackingfield_delete) | **DELETE** /tracking_fields/{fieldId} | Delete a Tracking Field
[**trackingfield_get**](TrackingFieldApi.md#trackingfield_get) | **GET** /tracking_fields/{fieldId} | Get a Tracking Field
[**trackingfield_list**](TrackingFieldApi.md#trackingfield_list) | **GET** /tracking_fields | List Tracking Fields
[**trackingfield_update**](TrackingFieldApi.md#trackingfield_update) | **PATCH** /tracking_fields/{fieldId} | Update a Tracking Field

# **trackingfield_create**
> InlineResponse2018 trackingfield_create(body)

Create a Tracking Field

[Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to create a new tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackingField() # TrackingField | Tracking Field

try:
    # Create a Tracking Field
    api_response = api_instance.trackingfield_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingField**](TrackingField.md)| Tracking Field | 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_delete**
> trackingfield_delete(field_id)

Delete a Tracking Field

[Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to delete a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
field_id = 'field_id_example' # str | The Tracking Field ID

try:
    # Delete a Tracking Field
    api_instance.trackingfield_delete(field_id)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| The Tracking Field ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_get**
> InlineResponse2018 trackingfield_get(field_id)

Get a Tracking Field

[Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br><br> When scheduling a meeting, the tracking field will be included in the meeting options.<br>Use this API to get information on a tracking field.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan 

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
field_id = 'field_id_example' # str | The Tracking Field ID

try:
    # Get a Tracking Field
    api_response = api_instance.trackingfield_get(field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **str**| The Tracking Field ID | 

### Return type

[**InlineResponse2018**](InlineResponse2018.md)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_list**
> object trackingfield_list()

List Tracking Fields

[Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to list all the tracking fields on your Zoom account.<br><br> **Scopes:** `trackingfield:read:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`<br> **Prerequisites:** * Business, Education, API or higher plan

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))

try:
    # List Tracking Fields
    api_response = api_instance.trackingfield_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trackingfield_update**
> trackingfield_update(body, field_id)

Update a Tracking Field

[Tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) allow you to analyze usage by various fields within an organization.<br> Use this API to update a tracking field.<br><br> **Scope:** `trackingfield:write:admin`<br>    **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`<br> **Prerequisites:** * Business, Education, API or higher plan

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
api_instance = swagger_client.TrackingFieldApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackingField2() # TrackingField2 | 
field_id = 'field_id_example' # str | The Tracking Field ID

try:
    # Update a Tracking Field
    api_instance.trackingfield_update(body, field_id)
except ApiException as e:
    print("Exception when calling TrackingFieldApi->trackingfield_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackingField2**](TrackingField2.md)|  | 
 **field_id** | **str**| The Tracking Field ID | 

### Return type

void (empty response body)

### Authorization

[OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# client.ApplicationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_create_post**](ApplicationApi.md#application_create_post) | **POST** /application/create | 15_999
[**application_delete_delete**](ApplicationApi.md#application_delete_delete) | **DELETE** /application/delete | 15_997
[**application_list_get**](ApplicationApi.md#application_list_get) | **GET** /application/list | 15_996
[**application_update_put**](ApplicationApi.md#application_update_put) | **PUT** /application/update | 15_998

# **application_create_post**
> CreateApplicationResponse application_create_post(body=body)

15_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 15_999_101 | ApplicationNameAlreadyExist | Application name already exists. |  | 15_999_102 | UnknownExceptionWhenValidateApplicationNameUniqueness | Unknown exception when validating application name uniqueness. |  | 15_999_103 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |  | 15_999_104 | UserNotFound | User not found. |  | 15_999_105 | UnknownExceptionWhenCreateOrganization |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApi(client.ApiClient(configuration))
body = client.ApplicationCreateBody() # ApplicationCreateBody |  (optional)

try:
    # 15_999
    api_response = api_instance.application_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationCreateBody**](ApplicationCreateBody.md)|  | [optional] 

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_delete_delete**
> DeleteApplicationResponse application_delete_delete(id=id)

15_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 15_997_101 | ApplicationNotFound | Application not found. |  | 15_997_102 | UnknownExceptionWhenFetchApplicationExistence | Unknown exception when fetching application existence. |  | 15_997_103 | UnknownExceptionWhenDeleteApplication | Unknown exception when deleting application. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # 15_997
    api_response = api_instance.application_delete_delete(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | [optional] 

### Return type

[**DeleteApplicationResponse**](DeleteApplicationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_list_get**
> UserApplicationListResponse application_list_get(page=page, per_page=per_page)

15_996

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 15_996_101 | UnknownExceptionWhenTryingFetchApplications | Unknown exception when trying to fetch applications. |  | 15_996_102 | UserNotFound | User not found. |  | 15_996_103 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApi(client.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try:
    # 15_996
    api_response = api_instance.application_list_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**UserApplicationListResponse**](UserApplicationListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_update_put**
> UpdateApplicationResponse application_update_put(body=body)

15_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 15_998_101 | ApplicationNotFound | Application not found. |  | 15_998_102 | UnknownExceptionWhenFetchApplication | Unknown exception when fetching application. |  | 15_998_103 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApi(client.ApiClient(configuration))
body = client.ApplicationUpdateBody() # ApplicationUpdateBody |  (optional)

try:
    # 15_998
    api_response = api_instance.application_update_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->application_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationUpdateBody**](ApplicationUpdateBody.md)|  | [optional] 

### Return type

[**UpdateApplicationResponse**](UpdateApplicationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


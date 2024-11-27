# client.ApplicationApiKeyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_apikey_generate_post**](ApplicationApiKeyApi.md#application_apikey_generate_post) | **POST** /application-apikey/generate | 16_999
[**application_apikey_get_by_application_id_get**](ApplicationApiKeyApi.md#application_apikey_get_by_application_id_get) | **GET** /application-apikey/get-by-application-id | 16_995
[**application_apikey_revoke_delete**](ApplicationApiKeyApi.md#application_apikey_revoke_delete) | **DELETE** /application-apikey/revoke | 16_998

# **application_apikey_generate_post**
> CreateApplicationApiKeyResponse application_apikey_generate_post(body=body)

16_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 16_999_101 | ApplicationNotFound | Application not found. |  | 16_999_102 | UnknownExceptionWhenCheckApplicationExistence | Unknown exception when checking if application exists. |  | 16_999_103 | UnknownExceptionWhenGenerateApplicationApiKey | Unknown exception when generating application API key. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApiKeyApi(client.ApiClient(configuration))
body = client.ApplicationapikeyGenerateBody() # ApplicationapikeyGenerateBody |  (optional)

try:
    # 16_999
    api_response = api_instance.application_apikey_generate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApiKeyApi->application_apikey_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationapikeyGenerateBody**](ApplicationapikeyGenerateBody.md)|  | [optional] 

### Return type

[**CreateApplicationApiKeyResponse**](CreateApplicationApiKeyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_apikey_get_by_application_id_get**
> ApplicationApiKeyByApplicationIdResponse application_apikey_get_by_application_id_get(application_id=application_id)

16_995

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 16_995_101 | ApplicationApiKeyNotFound | Application API key not found. |  | 16_995_102 | UnknownExceptionWhenTryingFetchApplications | Unknown exception when trying to fetch applications. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApiKeyApi(client.ApiClient(configuration))
application_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # 16_995
    api_response = api_instance.application_apikey_get_by_application_id_get(application_id=application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApiKeyApi->application_apikey_get_by_application_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)|  | [optional] 

### Return type

[**ApplicationApiKeyByApplicationIdResponse**](ApplicationApiKeyByApplicationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_apikey_revoke_delete**
> RevokeApplicationApiKeyResponse application_apikey_revoke_delete(id=id)

16_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 16_998_101 | ApplicationApiKeyNotFound | Application API key not found. |  | 16_998_102 | UnknownExceptionWhenCheckApplicationExistence | Unknown exception when checking if application exists. |  | 16_998_103 | UnknownExceptionWhenGenerateApplicationApiKey | Unknown exception when generating application API key. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationApiKeyApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # 16_998
    api_response = api_instance.application_apikey_revoke_delete(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApiKeyApi->application_apikey_revoke_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | [optional] 

### Return type

[**RevokeApplicationApiKeyResponse**](RevokeApplicationApiKeyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


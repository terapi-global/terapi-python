# client.ApplicationIntegrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_integration_add_integration_to_application_post**](ApplicationIntegrationApi.md#application_integration_add_integration_to_application_post) | **POST** /application-integration/add-integration-to-application | 18_999
[**application_integration_application_integration_list_by_application_id_get**](ApplicationIntegrationApi.md#application_integration_application_integration_list_by_application_id_get) | **GET** /application-integration/application-integration-list-by-application-id | 18_997

# **application_integration_add_integration_to_application_post**
> AddIntegrationToApplicationResponse application_integration_add_integration_to_application_post(body=body)

18_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 18_999_101 | ApplicationNotFound | Application not found. |  | 18_999_102 | UnknownExceptionWhenCheckApplicationExistence | Unknown exception when checking if application exists. |  | 18_999_103 | IntegrationNotFound | Integration not found. |  | 18_999_104 | UnknownExceptionWhenCheckIntegrationExistence | Unknown exception when checking if integration exists. |  | 18_999_105 | UnknownExceptionWhenAddIntegrationToApplication | Unknown exception when adding integration to application. |  | 18_999_106 | IntegrationAlreadyAddedToTheApplication | You already map this integration to your application. |  | 18_999_107 | UnknownExceptionWhenCheckApplicationIntegrationUniqueness |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationIntegrationApi(client.ApiClient(configuration))
body = client.ApplicationintegrationAddintegrationtoapplicationBody() # ApplicationintegrationAddintegrationtoapplicationBody |  (optional)

try:
    # 18_999
    api_response = api_instance.application_integration_add_integration_to_application_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIntegrationApi->application_integration_add_integration_to_application_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationintegrationAddintegrationtoapplicationBody**](ApplicationintegrationAddintegrationtoapplicationBody.md)|  | [optional] 

### Return type

[**AddIntegrationToApplicationResponse**](AddIntegrationToApplicationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_integration_application_integration_list_by_application_id_get**
> ApplicationIntegrationListByApplicationIdResponse application_integration_application_integration_list_by_application_id_get(application_id=application_id, page=page, per_page=per_page)

18_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 18_998 | UnknownExceptionWhenTryingFetchApplicationIntegrations |  |  | 18_999 | ApplicationNotFound |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApplicationIntegrationApi(client.ApiClient(configuration))
application_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try:
    # 18_997
    api_response = api_instance.application_integration_application_integration_list_by_application_id_get(application_id=application_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIntegrationApi->application_integration_application_integration_list_by_application_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ApplicationIntegrationListByApplicationIdResponse**](ApplicationIntegrationListByApplicationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


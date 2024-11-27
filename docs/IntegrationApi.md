# client.IntegrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_get_get**](IntegrationApi.md#integration_get_get) | **GET** /integration/get | 17_997
[**integration_list_get**](IntegrationApi.md#integration_list_get) | **GET** /integration/list | 17_999

# **integration_get_get**
> GetOneIntegrationResponse integration_get_get(id=id)

17_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 17_997_101 | UnknownExceptionWhenTryingFetchOneIntegration |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.IntegrationApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # 17_997
    api_response = api_instance.integration_get_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integration_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | [optional] 

### Return type

[**GetOneIntegrationResponse**](GetOneIntegrationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_list_get**
> IntegrationListResponse integration_list_get(page=page, per_page=per_page, search_keyword=search_keyword, category_id=category_id)

17_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 17_999_101 | UnknownExceptionWhenTryingFetchIntegrations | Unknown exception when trying to fetch integrations. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.IntegrationApi(client.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
search_keyword = 'search_keyword_example' # str |  (optional)
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # 17_999
    api_response = api_instance.integration_list_get(page=page, per_page=per_page, search_keyword=search_keyword, category_id=category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integration_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **search_keyword** | **str**|  | [optional] 
 **category_id** | [**str**](.md)|  | [optional] 

### Return type

[**IntegrationListResponse**](IntegrationListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


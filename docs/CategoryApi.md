# client.CategoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**category_list_get**](CategoryApi.md#category_list_get) | **GET** /category/list | 19_999

# **category_list_get**
> CategoryListResponse category_list_get(page=page, per_page=per_page)

19_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 19_999_101 | UnknownExceptionWhenTryingFetchCategories | Unknown exception when fetching category. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.CategoryApi(client.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try:
    # 19_999
    api_response = api_instance.category_list_get(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->category_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CategoryListResponse**](CategoryListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


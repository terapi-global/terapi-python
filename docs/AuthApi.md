# client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_authenticate_post**](AuthApi.md#auth_authenticate_post) | **POST** /auth/authenticate | 23_999
[**auth_refresh_post**](AuthApi.md#auth_refresh_post) | **POST** /auth/refresh | 23_998

# **auth_authenticate_post**
> GetAuthenticationTokenResponse auth_authenticate_post(secret_key=secret_key)

23_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 23_999_101 | UnknownExceptionWhenTryingFetchApplicationApiKey |  |  | 23_999_102 | FailedToFindApplicationApiKey |  |  | 23_999_103 | UnknownExceptionWhenTryingToGetUserAuthenticationToken |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.AuthApi(client.ApiClient(configuration))
secret_key = 'secret_key_example' # str |  (optional)

try:
    # 23_999
    api_response = api_instance.auth_authenticate_post(secret_key=secret_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_authenticate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_key** | **str**|  | [optional] 

### Return type

[**GetAuthenticationTokenResponse**](GetAuthenticationTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh_post**
> RefreshAuthenticationTokenResponse auth_refresh_post(refresh_token=refresh_token)

23_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 23_998_101 | UnknownExceptionWhenTryingToRefreshUserAuthenticationToken |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.AuthApi(client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str |  (optional)

try:
    # 23_998
    api_response = api_instance.auth_refresh_post(refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | [optional] 

### Return type

[**RefreshAuthenticationTokenResponse**](RefreshAuthenticationTokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


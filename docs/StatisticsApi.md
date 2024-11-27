# client.StatisticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_user_profile_get**](StatisticsApi.md#statistics_user_profile_get) | **GET** /statistics/user-profile | 14_997

# **statistics_user_profile_get**
> UserProfileStatisticsResponse statistics_user_profile_get()

14_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 14_997_101 | UserNotFound | User not found. |  | 14_997_102 | UserDoesNotHaveActiveSubscription | User does not have an active subscription. |  | 14_997_103 | UnknownExceptionWhenFetchUserProfileStatistics | Unknown exception when fetching user profile statistics. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.StatisticsApi(client.ApiClient(configuration))

try:
    # 14_997
    api_response = api_instance.statistics_user_profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_user_profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfileStatisticsResponse**](UserProfileStatisticsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


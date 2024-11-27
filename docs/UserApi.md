# client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create_or_get_user_profile_post**](UserApi.md#user_create_or_get_user_profile_post) | **POST** /user/create-or-get-user-profile | 14_998

# **user_create_or_get_user_profile_post**
> CreateUserProfileResponse user_create_or_get_user_profile_post()

14_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 14_998_101 | UnknownExceptionWhenFetchJwtUserProfile | Unknown exception when fetching JWT user profile. |  | 14_998_102 | UnknownExceptionWhenCreateUserProfile | Unknown exception when creating user profile. |  | 14_998_103 | IncorrectDataInUserJwtPayload | Incorrect data in user JWT payload. |  | 14_998_104 | UnknownExceptionWhenSubscribeUserToFreePlan | Unknown exception when subscribing user to free plan. |  | 14_998_105 | UserAlreadyExistInDataStorage | Logged user not found in data storage. |  | 14_998_106 | UnknownExceptionWhenCheckUserExistence | Unknown exception when fetching logged user profile. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.UserApi(client.ApiClient(configuration))

try:
    # 14_998
    api_response = api_instance.user_create_or_get_user_profile_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_create_or_get_user_profile_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateUserProfileResponse**](CreateUserProfileResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


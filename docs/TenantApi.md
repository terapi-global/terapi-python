# client.TenantApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_decline_tenant_id_get**](TenantApi.md#tenant_decline_tenant_id_get) | **GET** /tenant/decline-tenant/{id} | 20_996
[**tenant_invite_tenant_by_application_integration_id_post**](TenantApi.md#tenant_invite_tenant_by_application_integration_id_post) | **POST** /tenant/invite-tenant-by-application-integration-id | 20_998
[**tenant_invite_tenant_post**](TenantApi.md#tenant_invite_tenant_post) | **POST** /tenant/invite-tenant | 20_998
[**tenant_update_tenant_connection_post**](TenantApi.md#tenant_update_tenant_connection_post) | **POST** /tenant/update-tenant-connection | 20_997
[**tenant_user_tenant_list_get**](TenantApi.md#tenant_user_tenant_list_get) | **GET** /tenant/user-tenant-list | 20_999

# **tenant_decline_tenant_id_get**
> DeclineTenantInvitationResponse tenant_decline_tenant_id_get(id)

20_996

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 20_996_101 | TenantNotFound | Tenant Not Found |  | 20_996_102 | UnknownExceptionWhileFetchingTenant | Unknown exception when checking tenant existence. |  | 20_996_103 | UnknownExceptionWhileDecliningTenant | Unknown exception when declining tenant. |  | 20_996_104 | TenantIsNotInInvitedStatus |  |  | 20_996_105 | UnknownExceptionWhileCheckingIfTenantIsInCorrectStatus |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.TenantApi(client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # 20_996
    api_response = api_instance.tenant_decline_tenant_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenant_decline_tenant_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**DeclineTenantInvitationResponse**](DeclineTenantInvitationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_invite_tenant_by_application_integration_id_post**
> InviteTenantByApplicationIntegrationIdResponse tenant_invite_tenant_by_application_integration_id_post(body=body)

20_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 20_998_101 | ApplicationIntegrationNotFound | Application integration not found. |  | 20_998_102 | UnknownExceptionWhenCheckApplicationExistence | Unknown exception when checking application existence. |  | 20_998_103 | UnknownExceptionWhenCreateTenant | Unknown exception when createing tenant. |  | 20_998_104 | UnknownExceptionWhenSendingEmailToInvitedEmailAddress | Unknown exception when sending email to invited email address. |  | 20_998_105 | UserNotFound | User not found. |  | 20_998_106 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |  | 20_998_107 | UnknownExceptionWhenCreateUserTenant | Unknown exception when creating user tenant. |  | 20_998_108 | UnknownExceptionWhenCreatingEmailContent | Unknown exception when creating email content. |  | 20_998_109 | UnknownExceptionWhenCreatingEmailAcceptInvitationUrl |  |  | 20_998_110 | UnknownExceptionWhenAddingTenantInKeycloak |  |  | 20_998_111 | UnknownExceptionWhenAddingTenantInOrganization |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.TenantApi(client.ApiClient(configuration))
body = client.TenantInvitetenantbyapplicationintegrationidBody() # TenantInvitetenantbyapplicationintegrationidBody |  (optional)

try:
    # 20_998
    api_response = api_instance.tenant_invite_tenant_by_application_integration_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenant_invite_tenant_by_application_integration_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantInvitetenantbyapplicationintegrationidBody**](TenantInvitetenantbyapplicationintegrationidBody.md)|  | [optional] 

### Return type

[**InviteTenantByApplicationIntegrationIdResponse**](InviteTenantByApplicationIntegrationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_invite_tenant_post**
> InviteTenantResponse tenant_invite_tenant_post(body=body)

20_998

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 20_998_101 | ApplicationIntegrationNotFound | Application integration not found. |  | 20_998_102 | UnknownExceptionWhenCheckApplicationExistence | Unknown exception when checking application existence. |  | 20_998_103 | UnknownExceptionWhenCreateTenant | Unknown exception when createing tenant. |  | 20_998_104 | UnknownExceptionWhenSendingEmailToInvitedEmailAddress | Unknown exception when sending email to invited email address. |  | 20_998_105 | UserNotFound | User not found. |  | 20_998_106 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |  | 20_998_107 | UnknownExceptionWhenCreateUserTenant | Unknown exception when creating user tenant. |  | 20_998_108 | UnknownExceptionWhenCreatingEmailContent | Unknown exception when creating email content. |  | 20_998_109 | UnknownExceptionWhenCreatingEmailAcceptInvitationUrl |  |  | 20_998_110 | UnknownExceptionWhenAddingTenantInKeycloak |  |  | 20_998_111 | UnknownExceptionWhenAddingTenantInOrganization |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.TenantApi(client.ApiClient(configuration))
body = client.TenantInvitetenantBody() # TenantInvitetenantBody |  (optional)

try:
    # 20_998
    api_response = api_instance.tenant_invite_tenant_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenant_invite_tenant_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantInvitetenantBody**](TenantInvitetenantBody.md)|  | [optional] 

### Return type

[**InviteTenantResponse**](InviteTenantResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_update_tenant_connection_post**
> UpdateTenantConnectionResponse tenant_update_tenant_connection_post(body=body)

20_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 20_997_101 | TenantNotFound | Tenant not found. |  | 20_997_102 | UnknownExceptionWhenCheckTenantExistence | Unknown exception when checking tenant existence. |  | 20_997_103 | UnknownExceptionWhenUpdateTenantConnection | Unknown exception when updating tenant connection. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.TenantApi(client.ApiClient(configuration))
body = client.TenantUpdatetenantconnectionBody() # TenantUpdatetenantconnectionBody |  (optional)

try:
    # 20_997
    api_response = api_instance.tenant_update_tenant_connection_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenant_update_tenant_connection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantUpdatetenantconnectionBody**](TenantUpdatetenantconnectionBody.md)|  | [optional] 

### Return type

[**UpdateTenantConnectionResponse**](UpdateTenantConnectionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_user_tenant_list_get**
> UserTenantListResponse tenant_user_tenant_list_get(invitation_status=invitation_status, page=page, per_page=per_page)

20_999

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 20_999_101 | UnknownExceptionWhenTryingFetchTenants | Unknown exception when trying to fetch tenants. |  | 20_999_102 | UserNotFound | User not found. |  | 20_999_103 | UnknownExceptionWhenInsertApplication | Unknown exception when inserting application. |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.TenantApi(client.ApiClient(configuration))
invitation_status = client.InvitationStatus1() # InvitationStatus1 |   0 = Invited  1 = Accepted  2 = Declined (optional)
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try:
    # 20_999
    api_response = api_instance.tenant_user_tenant_list_get(invitation_status=invitation_status, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->tenant_user_tenant_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_status** | [**InvitationStatus1**](.md)|   0 &#x3D; Invited  1 &#x3D; Accepted  2 &#x3D; Declined | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**UserTenantListResponse**](UserTenantListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


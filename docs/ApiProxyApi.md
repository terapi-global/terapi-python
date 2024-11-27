# client.ApiProxyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_proxy_endpoint_delete**](ApiProxyApi.md#api_proxy_endpoint_delete) | **DELETE** /api-proxy/{endpoint} | 21_997
[**api_proxy_endpoint_get**](ApiProxyApi.md#api_proxy_endpoint_get) | **GET** /api-proxy/{endpoint} | 21_997
[**api_proxy_endpoint_patch**](ApiProxyApi.md#api_proxy_endpoint_patch) | **PATCH** /api-proxy/{endpoint} | 21_997
[**api_proxy_endpoint_post**](ApiProxyApi.md#api_proxy_endpoint_post) | **POST** /api-proxy/{endpoint} | 21_997
[**api_proxy_endpoint_put**](ApiProxyApi.md#api_proxy_endpoint_put) | **PUT** /api-proxy/{endpoint} | 21_997
[**api_proxy_oauth2_challenge_get**](ApiProxyApi.md#api_proxy_oauth2_challenge_get) | **GET** /api-proxy/oauth2/challenge | 
[**api_proxy_unified_contacts_external_id_get**](ApiProxyApi.md#api_proxy_unified_contacts_external_id_get) | **GET** /api-proxy/unified/contacts/{externalId} | 
[**api_proxy_unified_contacts_get**](ApiProxyApi.md#api_proxy_unified_contacts_get) | **GET** /api-proxy/unified/contacts | 

# **api_proxy_endpoint_delete**
> CallActionResponse api_proxy_endpoint_delete(x_tenant_id, integration_name, endpoint, body=body)

21_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 21_997_101 | TenantNotFound |  |  | 21_997_102 | IntegrationNotFound |  |  | 21_997_103 | UnknownExceptionWhenCallingThirdPartyApi |  |  | 21_997_104 | UnknownExceptionWhenCallAction |  |  | 21_997_105 | IntegrationIsNotEnabled |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
x_tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
integration_name = 'integration_name_example' # str | 
endpoint = 'endpoint_example' # str | 
body = client.ApiproxyEndpointBody6() # ApiproxyEndpointBody6 |  (optional)

try:
    # 21_997
    api_response = api_instance.api_proxy_endpoint_delete(x_tenant_id, integration_name, endpoint, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_endpoint_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | [**str**](.md)|  | 
 **integration_name** | **str**|  | 
 **endpoint** | **str**|  | 
 **body** | [**ApiproxyEndpointBody6**](ApiproxyEndpointBody6.md)|  | [optional] 

### Return type

[**CallActionResponse**](CallActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_endpoint_get**
> CallActionResponse api_proxy_endpoint_get(integration_name, endpoint, x_tenant_id)

21_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 21_997_101 | TenantNotFound |  |  | 21_997_102 | IntegrationNotFound |  |  | 21_997_103 | UnknownExceptionWhenCallingThirdPartyApi |  |  | 21_997_104 | UnknownExceptionWhenCallAction |  |  | 21_997_105 | IntegrationIsNotEnabled |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
integration_name = 'integration_name_example' # str | 
endpoint = 'endpoint_example' # str | 
x_tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # 21_997
    api_response = api_instance.api_proxy_endpoint_get(integration_name, endpoint, x_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_endpoint_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_name** | **str**|  | 
 **endpoint** | **str**|  | 
 **x_tenant_id** | [**str**](.md)|  | 

### Return type

[**CallActionResponse**](CallActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_endpoint_patch**
> CallActionResponse api_proxy_endpoint_patch(x_tenant_id, integration_name, endpoint, body=body)

21_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 21_997_101 | TenantNotFound |  |  | 21_997_102 | IntegrationNotFound |  |  | 21_997_103 | UnknownExceptionWhenCallingThirdPartyApi |  |  | 21_997_104 | UnknownExceptionWhenCallAction |  |  | 21_997_105 | IntegrationIsNotEnabled |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
x_tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
integration_name = 'integration_name_example' # str | 
endpoint = 'endpoint_example' # str | 
body = client.ApiproxyEndpointBody9() # ApiproxyEndpointBody9 |  (optional)

try:
    # 21_997
    api_response = api_instance.api_proxy_endpoint_patch(x_tenant_id, integration_name, endpoint, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_endpoint_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | [**str**](.md)|  | 
 **integration_name** | **str**|  | 
 **endpoint** | **str**|  | 
 **body** | [**ApiproxyEndpointBody9**](ApiproxyEndpointBody9.md)|  | [optional] 

### Return type

[**CallActionResponse**](CallActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_endpoint_post**
> CallActionResponse api_proxy_endpoint_post(x_tenant_id, integration_name, endpoint, body=body)

21_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 21_997_101 | TenantNotFound |  |  | 21_997_102 | IntegrationNotFound |  |  | 21_997_103 | UnknownExceptionWhenCallingThirdPartyApi |  |  | 21_997_104 | UnknownExceptionWhenCallAction |  |  | 21_997_105 | IntegrationIsNotEnabled |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
x_tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
integration_name = 'integration_name_example' # str | 
endpoint = 'endpoint_example' # str | 
body = client.ApiproxyEndpointBody3() # ApiproxyEndpointBody3 |  (optional)

try:
    # 21_997
    api_response = api_instance.api_proxy_endpoint_post(x_tenant_id, integration_name, endpoint, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_endpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | [**str**](.md)|  | 
 **integration_name** | **str**|  | 
 **endpoint** | **str**|  | 
 **body** | [**ApiproxyEndpointBody3**](ApiproxyEndpointBody3.md)|  | [optional] 

### Return type

[**CallActionResponse**](CallActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_endpoint_put**
> CallActionResponse api_proxy_endpoint_put(x_tenant_id, integration_name, endpoint, body=body)

21_997

### Error Codes  | Code | Name | Message |  | :--- | :--- | :--- |  | 21_997_101 | TenantNotFound |  |  | 21_997_102 | IntegrationNotFound |  |  | 21_997_103 | UnknownExceptionWhenCallingThirdPartyApi |  |  | 21_997_104 | UnknownExceptionWhenCallAction |  |  | 21_997_105 | IntegrationIsNotEnabled |  |

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
x_tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
integration_name = 'integration_name_example' # str | 
endpoint = 'endpoint_example' # str | 
body = client.ApiproxyEndpointBody() # ApiproxyEndpointBody |  (optional)

try:
    # 21_997
    api_response = api_instance.api_proxy_endpoint_put(x_tenant_id, integration_name, endpoint, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_endpoint_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | [**str**](.md)|  | 
 **integration_name** | **str**|  | 
 **endpoint** | **str**|  | 
 **body** | [**ApiproxyEndpointBody**](ApiproxyEndpointBody.md)|  | [optional] 

### Return type

[**CallActionResponse**](CallActionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_oauth2_challenge_get**
> OAuth2ChallengeDtoResponse api_proxy_oauth2_challenge_get(tenant_id=tenant_id)



### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
tenant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    api_response = api_instance.api_proxy_oauth2_challenge_get(tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_oauth2_challenge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**str**](.md)|  | [optional] 

### Return type

[**OAuth2ChallengeDtoResponse**](OAuth2ChallengeDtoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_unified_contacts_external_id_get**
> UnifiedContactResponse api_proxy_unified_contacts_external_id_get(external_id)



### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))
external_id = 'external_id_example' # str | 

try:
    api_response = api_instance.api_proxy_unified_contacts_external_id_get(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_unified_contacts_external_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

[**UnifiedContactResponse**](UnifiedContactResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_proxy_unified_contacts_get**
> UnifiedContactsListResponse api_proxy_unified_contacts_get()



### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = client.ApiProxyApi(client.ApiClient(configuration))

try:
    api_response = api_instance.api_proxy_unified_contacts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiProxyApi->api_proxy_unified_contacts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnifiedContactsListResponse**](UnifiedContactsListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# priceloop_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_table**](DefaultApi.md#delete_table) | **DELETE** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_table**](DefaultApi.md#get_table) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_table_data**](DefaultApi.md#get_table_data) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table}/data | 
[**get_table_upload_csv_url**](DefaultApi.md#get_table_upload_csv_url) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table}/upload-csv-url | 
[**get_workspace**](DefaultApi.md#get_workspace) | **GET** /api/v1.0/workspaces/{workspace} | 
[**list_workspaces**](DefaultApi.md#list_workspaces) | **GET** /api/v1.0/workspaces | 


# **delete_table**
> delete_table(workspace, table)



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    table = "table_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_table(workspace, table)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **table** | **str**|  |

### Return type

void (empty response body)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> ApiTable get_table(workspace, table)



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from priceloop_api.model.api_table import ApiTable
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    table = "table_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_table(workspace, table)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **table** | **str**|  |

### Return type

[**ApiTable**](ApiTable.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_data**
> TableData get_table_data(workspace, table, limit, offset)



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from priceloop_api.model.table_data import TableData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    table = "table_example" # str | 
    limit = 0 # int | 
    offset = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_table_data(workspace, table, limit, offset)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **table** | **str**|  |
 **limit** | **int**|  |
 **offset** | **int**|  |

### Return type

[**TableData**](TableData.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value for: query parameter limit, Invalid value for: query parameter offset |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_upload_csv_url**
> str get_table_upload_csv_url(workspace, table)



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    table = "table_example" # str | 
    mode = "new" # str |  (optional) if omitted the server will use the default value of "new"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_table_upload_csv_url(workspace, table)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_upload_csv_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_table_upload_csv_url(workspace, table, mode=mode)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_upload_csv_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **table** | **str**|  |
 **mode** | **str**|  | [optional] if omitted the server will use the default value of "new"

### Return type

**str**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> ApiWorkspace get_workspace(workspace)



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from priceloop_api.model.api_workspace import ApiWorkspace
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_workspace(workspace)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |

### Return type

[**ApiWorkspace**](ApiWorkspace.md)

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> [str] list_workspaces()



### Example

* Bearer Authentication (httpAuth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = priceloop_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_workspaces()
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->list_workspaces: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

[httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


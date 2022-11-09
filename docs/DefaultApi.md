# priceloop_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_function**](DefaultApi.md#create_external_function) | **POST** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**delete_external_function**](DefaultApi.md#delete_external_function) | **DELETE** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**delete_table**](DefaultApi.md#delete_table) | **DELETE** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_external_functions**](DefaultApi.md#get_external_functions) | **GET** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**get_table**](DefaultApi.md#get_table) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_table_data**](DefaultApi.md#get_table_data) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table}/data | 
[**get_table_upload_csv_url**](DefaultApi.md#get_table_upload_csv_url) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table}/upload-csv-url | 
[**get_workspace**](DefaultApi.md#get_workspace) | **GET** /api/v1.0/workspaces/{workspace} | 
[**hello**](DefaultApi.md#hello) | **GET** /api/v1.0/hello | 
[**hello_auth**](DefaultApi.md#hello_auth) | **GET** /api/v1.0/hello-auth | 
[**list_workspaces**](DefaultApi.md#list_workspaces) | **GET** /api/v1.0/workspaces | 
[**update_external_function**](DefaultApi.md#update_external_function) | **PUT** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 


# **create_external_function**
> str create_external_function(workspace, function, runtime, return_type)



Create a new external function, specifying the function name, runtime, return type and the paremeter types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    function = "function_example" # str | 
    runtime = "python" # str | 
    return_type = "number" # str | 
    param_type = [
        "paramType_example",
    ] # [str] | Specify parameter types. Expected: number,string,boolean,date (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_external_function(workspace, function, runtime, return_type)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->create_external_function: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_external_function(workspace, function, runtime, return_type, param_type=param_type)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->create_external_function: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **function** | **str**|  |
 **runtime** | **str**|  |
 **return_type** | **str**|  |
 **param_type** | **[str]**| Specify parameter types. Expected: number,string,boolean,date | [optional]

### Return type

**str**

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value for: query parameter runtime, Invalid value for: query parameter returnType, Invalid value for: query parameter paramType |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_function**
> delete_external_function(workspace, function)



Delete an existing external function.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    function = "function_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_external_function(workspace, function)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_external_function: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **function** | **str**|  |

### Return type

void (empty response body)

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> delete_table(workspace, table)



Delete your table.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_functions**
> ApiExternalFunction get_external_functions(workspace, function)



Get details about your existing external function.

### Example

* OAuth Authentication (oauth2Auth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from priceloop_api.model.api_external_function import ApiExternalFunction
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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    function = "function_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_external_functions(workspace, function)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_external_functions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **function** | **str**|  |

### Return type

[**ApiExternalFunction**](ApiExternalFunction.md)

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> ApiTable get_table(workspace, table)



Get the metadata of your table.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[oauth2Auth](../README.md#oauth2Auth)

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
> ApiTableData get_table_data(workspace, table, limit, offset)



Get the data of your table.

### Example

* OAuth Authentication (oauth2Auth):

```python
import time
import priceloop_api
from priceloop_api.api import default_api
from priceloop_api.model.api_table_data import ApiTableData
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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[**ApiTableData**](ApiTableData.md)

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

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



Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value for: query parameter mode |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> ApiWorkspace get_workspace(workspace)



Get all details about your workspace.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hello**
> str hello()



### Example


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


# Enter a context with an instance of the API client
with priceloop_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.hello()
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->hello: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hello_auth**
> str hello_auth()



### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.hello_auth()
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->hello_auth: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> [str] list_workspaces()



List all your existing workspaces.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

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

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_function**
> str update_external_function(workspace, function)



Create the code of an existing external function. This API endpoint returns a url, to which you can upload your function code. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):

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

# Configure OAuth2 access token for authorization: oauth2Auth
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    function = "function_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_external_function(workspace, function)
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->update_external_function: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**|  |
 **function** | **str**|  |

### Return type

**str**

### Authorization

[oauth2Auth](../README.md#oauth2Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


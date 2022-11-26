<a name="__pageTop"></a>
# priceloop_api.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_column**](#add_data_column) | **post** /api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column} | 
[**create_external_function**](#create_external_function) | **post** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**delete_external_function**](#delete_external_function) | **delete** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**delete_table**](#delete_table) | **delete** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_external_functions**](#get_external_functions) | **get** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 
[**get_table**](#get_table) | **get** /api/v1.0/workspaces/{workspace}/tables/{table} | 
[**get_table_data**](#get_table_data) | **get** /api/v1.0/workspaces/{workspace}/tables/{table}/data | 
[**get_table_upload_csv_url**](#get_table_upload_csv_url) | **get** /api/v1.0/workspaces/{workspace}/tables/{table}/upload-csv-url | 
[**get_workspace**](#get_workspace) | **get** /api/v1.0/workspaces/{workspace} | 
[**hello**](#hello) | **get** /api/v1.0/hello | 
[**hello_auth**](#hello_auth) | **get** /api/v1.0/hello-auth | 
[**list_workspaces**](#list_workspaces) | **get** /api/v1.0/workspaces | 
[**update_column_position**](#update_column_position) | **put** /api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column} | 
[**update_external_function**](#update_external_function) | **put** /api/v1.0/workspaces/{workspace}/external-functions/{function} | 

# **add_data_column**
<a name="add_data_column"></a>
> ApiColumn add_data_column(workspacetablecolumn)



Add a column to a table.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
from priceloop_api.model.api_column import ApiColumn
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
        'column': "column_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.add_data_column(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->add_data_column: %s\n" % e)

    # example passing only optional values
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
        'column': "column_example",
    }
    query_params = {
        'type': "string",
    }
    try:
        api_response = api_instance.add_data_column(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->add_data_column: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["string", "number", "boolean", "date", "json", ] if omitted the server will use the default value of "string"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 
column | ColumnSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ColumnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_data_column.ApiResponseFor200) | 
400 | [ApiResponseFor400](#add_data_column.ApiResponseFor400) | Invalid value for: query parameter type
default | [ApiResponseForDefault](#add_data_column.ApiResponseForDefault) | 

#### add_data_column.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiColumn**](../../models/ApiColumn.md) |  | 


#### add_data_column.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### add_data_column.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_external_function**
<a name="create_external_function"></a>
> str create_external_function(workspacefunctionruntimereturn_type)



Create a new external function, specifying the function name, runtime, return type and the paremeter types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'function': "function_example",
    }
    query_params = {
        'runtime': "python",
        'returnType': "number",
    }
    try:
        api_response = api_instance.create_external_function(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->create_external_function: %s\n" % e)

    # example passing only optional values
    path_params = {
        'workspace': "workspace_example",
        'function': "function_example",
    }
    query_params = {
        'runtime': "python",
        'returnType': "number",
        'paramType': [
        "paramType_example"
    ],
    }
    try:
        api_response = api_instance.create_external_function(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->create_external_function: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
runtime | RuntimeSchema | | 
returnType | ReturnTypeSchema | | 
paramType | ParamTypeSchema | | optional


# RuntimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["python", "python_numpy", "python_pandas", "nodejs", "go", ] 

# ReturnTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["number", "string", "boolean", "date", ] 

# ParamTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
function | FunctionSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_external_function.ApiResponseFor200) | 
400 | [ApiResponseFor400](#create_external_function.ApiResponseFor400) | Invalid value for: query parameter runtime, Invalid value for: query parameter returnType, Invalid value for: query parameter paramType
default | [ApiResponseForDefault](#create_external_function.ApiResponseForDefault) | 

#### create_external_function.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### create_external_function.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### create_external_function.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_external_function**
<a name="delete_external_function"></a>
> delete_external_function(workspacefunction)



Delete an existing external function.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'function': "function_example",
    }
    try:
        api_response = api_instance.delete_external_function(
            path_params=path_params,
        )
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_external_function: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
function | FunctionSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_external_function.ApiResponseFor200) | 
default | [ApiResponseForDefault](#delete_external_function.ApiResponseForDefault) | 

#### delete_external_function.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_external_function.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_table**
<a name="delete_table"></a>
> delete_table(workspacetable)



Delete your table.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
    }
    try:
        api_response = api_instance.delete_table(
            path_params=path_params,
        )
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->delete_table: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_table.ApiResponseFor200) | 
default | [ApiResponseForDefault](#delete_table.ApiResponseForDefault) | 

#### delete_table.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_table.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_external_functions**
<a name="get_external_functions"></a>
> ApiExternalFunction get_external_functions(workspacefunction)



Get details about your existing external function.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'function': "function_example",
    }
    try:
        api_response = api_instance.get_external_functions(
            path_params=path_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_external_functions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
function | FunctionSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_external_functions.ApiResponseFor200) | 
default | [ApiResponseForDefault](#get_external_functions.ApiResponseForDefault) | 

#### get_external_functions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiExternalFunction**](../../models/ApiExternalFunction.md) |  | 


#### get_external_functions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_table**
<a name="get_table"></a>
> ApiTable get_table(workspacetable)



Get the metadata of your table.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
    }
    try:
        api_response = api_instance.get_table(
            path_params=path_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_table.ApiResponseFor200) | 
default | [ApiResponseForDefault](#get_table.ApiResponseForDefault) | 

#### get_table.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiTable**](../../models/ApiTable.md) |  | 


#### get_table.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_table_data**
<a name="get_table_data"></a>
> ApiTableData get_table_data(workspacetablelimitoffset)



Get the data of your table.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
    }
    query_params = {
        'limit': 0,
        'offset': 0,
    }
    try:
        api_response = api_instance.get_table_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | 
offset | OffsetSchema | | 


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_table_data.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_table_data.ApiResponseFor400) | Invalid value for: query parameter limit, Invalid value for: query parameter offset
default | [ApiResponseForDefault](#get_table_data.ApiResponseForDefault) | 

#### get_table_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiTableData**](../../models/ApiTableData.md) |  | 


#### get_table_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### get_table_data.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_table_upload_csv_url**
<a name="get_table_upload_csv_url"></a>
> str get_table_upload_csv_url(workspacetable)



Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_table_upload_csv_url(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_upload_csv_url: %s\n" % e)

    # example passing only optional values
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
    }
    query_params = {
        'mode': "new",
    }
    try:
        api_response = api_instance.get_table_upload_csv_url(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_table_upload_csv_url: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
mode | ModeSchema | | optional


# ModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["new", "delete_and_recreate", "replace_data", "append_data", ] if omitted the server will use the default value of "new"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_table_upload_csv_url.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get_table_upload_csv_url.ApiResponseFor400) | Invalid value for: query parameter mode
default | [ApiResponseForDefault](#get_table_upload_csv_url.ApiResponseForDefault) | 

#### get_table_upload_csv_url.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### get_table_upload_csv_url.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### get_table_upload_csv_url.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_workspace**
<a name="get_workspace"></a>
> ApiWorkspace get_workspace(workspace)



Get all details about your workspace.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
    }
    try:
        api_response = api_instance.get_workspace(
            path_params=path_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->get_workspace: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_workspace.ApiResponseFor200) | 
default | [ApiResponseForDefault](#get_workspace.ApiResponseForDefault) | 

#### get_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiWorkspace**](../../models/ApiWorkspace.md) |  | 


#### get_workspace.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **hello**
<a name="hello"></a>
> str hello()



### Example

```python
import priceloop_api
from priceloop_api.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = priceloop_api.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with priceloop_api.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#hello.ApiResponseFor200) | 
default | [ApiResponseForDefault](#hello.ApiResponseForDefault) | 

#### hello.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### hello.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **hello_auth**
<a name="hello_auth"></a>
> str hello_auth()



### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#hello_auth.ApiResponseFor200) | 
default | [ApiResponseForDefault](#hello_auth.ApiResponseForDefault) | 

#### hello_auth.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### hello_auth.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_workspaces**
<a name="list_workspaces"></a>
> [str] list_workspaces()



List all your existing workspaces.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_workspaces.ApiResponseFor200) | 
default | [ApiResponseForDefault](#list_workspaces.ApiResponseForDefault) | 

#### list_workspaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### list_workspaces.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_column_position**
<a name="update_column_position"></a>
> update_column_position(workspacetablecolumnposition)



Change column position in a table.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'table': "table_example",
        'column': "column_example",
    }
    query_params = {
        'position': 1,
    }
    try:
        api_response = api_instance.update_column_position(
            path_params=path_params,
            query_params=query_params,
        )
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->update_column_position: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
position | PositionSchema | | 


# PositionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
table | TableSchema | | 
column | ColumnSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ColumnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_column_position.ApiResponseFor200) | 
400 | [ApiResponseFor400](#update_column_position.ApiResponseFor400) | Invalid value for: query parameter position
default | [ApiResponseForDefault](#update_column_position.ApiResponseForDefault) | 

#### update_column_position.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_column_position.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### update_column_position.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_external_function**
<a name="update_external_function"></a>
> str update_external_function(workspacefunction)



Create the code of an existing external function. This API endpoint returns a url, to which you can upload your function code. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

### Example

* OAuth Authentication (oauth2Auth):
```python
import priceloop_api
from priceloop_api.apis.tags import default_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'workspace': "workspace_example",
        'function': "function_example",
    }
    try:
        api_response = api_instance.update_external_function(
            path_params=path_params,
        )
        pprint(api_response)
    except priceloop_api.ApiException as e:
        print("Exception when calling DefaultApi->update_external_function: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workspace | WorkspaceSchema | | 
function | FunctionSchema | | 

# WorkspaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_external_function.ApiResponseFor200) | 
default | [ApiResponseForDefault](#update_external_function.ApiResponseForDefault) | 

#### update_external_function.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### update_external_function.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[oauth2Auth](../../../README.md#oauth2Auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


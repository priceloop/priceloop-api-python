# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/priceloop/priceloop-api-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/priceloop/priceloop-api-python.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import default_api
from openapi_client.model.api_table import ApiTable
from openapi_client.model.api_workspace import ApiWorkspace
from openapi_client.model.table_data import TableData
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: httpAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    workspace = "workspace_example" # str | 
    table = "table_example" # str | 

    try:
        api_response = api_instance.get_table(workspace, table)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_table: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_table**](docs/DefaultApi.md#get_table) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table} | 
*DefaultApi* | [**get_table_data**](docs/DefaultApi.md#get_table_data) | **GET** /api/v1.0/workspaces/{workspace}/tables/{table}/data | 
*DefaultApi* | [**get_workspace**](docs/DefaultApi.md#get_workspace) | **GET** /api/v1.0/workspaces/{workspace} | 
*DefaultApi* | [**list_workspaces**](docs/DefaultApi.md#list_workspaces) | **GET** /api/v1.0/workspaces | 


## Documentation For Models

 - [ApiColumn](docs/ApiColumn.md)
 - [ApiTable](docs/ApiTable.md)
 - [ApiWorkspace](docs/ApiWorkspace.md)
 - [TableData](docs/TableData.md)


## Documentation For Authorization


## httpAuth

- **Type**: Bearer authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```


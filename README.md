# priceloop-api

Connect to your Priceloop Data through our API.

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

Install
```sh
pip install git+https://github.com/priceloop/priceloop-api-python.git@v0.1.0
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/priceloop/priceloop-api-python.git@v0.1.0`)

Then import the package:
```python
import priceloop_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import priceloop_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from priceloop_api import ApiClient
from priceloop_api.api.default_api import DefaultApi
from priceloop_api.util import DefaultConfiguration


configuration = DefaultConfiguration.with_user_credentials('username', 'password')

with ApiClient(configuration) as api_client:
    api_instance = DefaultApi(api_client)

    workspaces = api_instance.list_workspaces()
    print(workspaces)

    workspace = api_instance.get_workspace(workspaces[0])
    print(workspace)

    table = api_instance.get_table(workspace.name, workspace.tables[0].name)
```

## Documentation

Api Endpoint and Online-Docs: https://api.alpha.priceloop.ai

[Api Docs](docs/DefaultApi.md)

## OpenAPI

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

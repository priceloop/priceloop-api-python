# priceloop-api-python
A client library for accessing Priceloop API

## Install
```
pip install priceloop-api
```

## Usage
First, create a `PriceloopClient`:

```python
from priceloop_api.priceloop.auth import PriceloopClient

client = PriceloopClient.with_credentials("username", "password")
```

read and write to nocode:

```python
import pandas as pd
from priceloop_api.priceloop.data import to_nocode, read_nocode

# write to nocode
data = [["Alex", 10], ["Bob", 12], ["Clarke", 13]]
df = pd.DataFrame(data, columns=["Name", "Age"])
to_nocode(df, "table_name", client)

# read from nocode
new_df = read_nocode("table_name", client, limit=limit, offset=offset)
```

call your endpoint, example:

```python
from priceloop_api.api.default import list_workspaces, get_workspace

workspaces = list_workspaces.sync(client=client)
workspace = get_workspace.sync(workspaces[0], client=client)
```
add columns to existing table:

```python
from priceloop_api.api.default import add_data_column, add_formula_column
from priceloop_api.models import AddDataColumnType

add_data_column.sync(workspace.name, "table_name", "column_name", type=AddDataColumnType.STRING, client=client)
add_formula_column.sync(workspace.name, "table_name", "column_name", "expression", client=client)
```


Things to know:
1. Every path/method combo becomes has four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    2. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    3. `asyncio`: Like `sync` but async instead of blocking
    4. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

2. All path/query params, and bodies become method arguments.
3. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
4. Any endpoint which did not have a tag will be in `priceloop_api.api.default`

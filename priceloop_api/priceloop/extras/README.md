# Platform Table Operations README
This README provides examples and explanations for the functions in the platform_table_operations.py module. These functions are designed to interact with tables on a platform using an authenticated client.

```
from priceloop_api.priceloop.extras.helpers import get_priceloop_client

client = get_priceloop_client(username, password, env="prod")
```

Function List
1. `is_table_on_platform`
   
Description:
Checks if a table exists on the platform.

Example:
```
from priceloop_api.priceloop.extras import TableUtils

workspace_name = "my_workspace"
table_name = "example_table"

if TableUtils.is_table_on_platform(workspace_name, table_name, client):
    print(f"The table {table_name} exists in the workspace {workspace_name}.")
else:
    print(f"The table {table_name} does not exist in the workspace {workspace_name}.")

```

2. `initialize_table`

Description:
Initializes a table with the given name and columns on the platform.

```
from priceloop_api.priceloop.extras import TableUtils, Column

workspace_name = "my_workspace"
table_name = "example_table"
columns = [Column(name="column1", data_type="string"), Column(name="column2", data_type="int")]


if TableUtils.initialize_table(workspace_name, table_name, columns, client):
    print(f"The table {table_name} has been successfully initialized in the workspace {workspace_name}.")
else:
    print(f"Failed to initialize the table {table_name} in the workspace {workspace_name}.")
```

3. `delete_table` & `truncate_table`
   
Description:
Deletes a table from the platform.

Example:
```
from platform_table_operations import TableUtils

workspace_name = "my_workspace"
table_name = "example_table"

if truncate(workspace_name, table_name, client):
    print(f"The table {table_name} has been successfully truncated in the workspace {workspace_name}.")
else:
    print(f"Failed to truncate the table {table_name} in the workspace {workspace_name}.")


if TableUtils.delete_table(workspace_name, table_name, client):
    print(f"The table {table_name} has been successfully deleted from the workspace {workspace_name}.")
else:
    print(f"Failed to delete the table {table_name} from the workspace)
```

4. `read_table`

Description:
Reads data from a table on the platform and returns it as a DataFrame.

Example:
```
from platform_table_operations import TableUtils

workspace_name = "my_workspace"
table_name = "example_table"
client = AuthenticatedClient("your_api_key")

# Reading all columns
data_frame = TableUtils.read_table(workspace_name, table_name, client)

# Reading specific subset of columns
selected_columns = ["column1", "column2"]
data_frame_selected = TableUtils.read_table(workspace_name, table_name, client, columns=selected_columns)


print(data_frame)
print(data_frame_selected)
```

5. `import_data`
   Description:
    use priceloop import API to Create/Update table.

```
from platform_table_operations import TableUtils

workspace_name = "my_workspace"
table_name = "example_table"

if TableUtils.import_data(workspace_name, table_name, dataframe, client):
    print(f"Data has been imported successfully to {workspace_name}.{table_name} .")
else:
    print("Failed to import data")
```

6. `patch_table`
   Description: this method can be used do multiple operations on an existing tables.
   1. Append rows to the Table:
    ```
    from platform_table_operations import TableUtils, PatchMode
    workspace_name = "my_workspace"
    table_name = "example_table"
    table_df = pd.DataFrame({"column1": ["value1", "value2"]})

    TableUtils.patch_table(workspace_name, table_name, table_df, client, mode= PatchMode.Append)
    ```

   2. Delete rows
   ```
    from platform_table_operations import TableUtils, PatchMode
    
    workspace_name = "my_workspace"
    table_name = "example_table"
    table_df = pd.DataFrame({"column1": ["value1", "value2"]})

    TableUtils.patch_table(workspace_name, table_name, table_df, client, mode= PatchMode.Delete)
   ```
   3. Insert rows with checking for key identifier
   ```
    from platform_table_operations import TableUtils, PatchMode
    
    workspace_name = "my_workspace"
    table_name = "example_table"
    table_df = pd.DataFrame({"column1": ["value1", "value2"], "column2": [1, 2]})
    mode = PatchMode.InsertOnConflictFail
    match_on_columns = ["column1"]
    data_columns = ["column2"]

    if TableUtils.patch_table(workspace_name, table_name, table_df, client, mode, match_on_columns=match_on_columns, data_columns=data_columns):
        print(f"Data successfully inserted with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")
    else:
        print(f"Failed to insert data with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")

   ```

   3. Insert rows without checking for key identifier (might end up with duplications)
   ```
    from platform_table_operations import TableUtils, PatchMode
    
    workspace_name = "my_workspace"
    table_name = "example_table"
    table_df = pd.DataFrame({"column1": ["value1", "value2"], "column2": [1, 2]})
    mode = PatchMode.InsertOnConflictIgnore
    match_on_columns = ["column1"]
    data_columns = ["column2"]

    if TableUtils.patch_table(workspace_name, table_name, table_df, client, mode, match_on_columns=match_on_columns, data_columns=data_columns):
        print(f"Data successfully inserted with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")
    else:
        print(f"Failed to insert data with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")

   ```

   3. Insert rows with checking for key identifier and updating already existing rows (Upsert)
   ```
    from platform_table_operations import TableUtils, PatchMode
    
    workspace_name = "my_workspace"
    table_name = "example_table"
    table_df = pd.DataFrame({"column1": ["value1", "value2"], "column2": [1, 2]})
    mode = PatchMode.InsertOnConflictUpdate
    match_on_columns = ["column1"]
    data_columns = ["column2"]

    if TableUtils.patch_table(workspace_name, table_name, table_df, client, mode, match_on_columns=match_on_columns, data_columns=data_columns):
        print(f"Data successfully inserted with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")
    else:
        print(f"Failed to insert data with fail conflict resolution to the table {table_name} in workspace {workspace_name}.")

   ```
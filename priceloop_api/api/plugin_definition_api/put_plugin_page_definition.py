from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.view_page_config import ViewPageConfig
from ...types import Response


def _get_kwargs(
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: ViewPageConfig,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/plugin-definition/{plugin}/pages".format(client.base_url, plugin=plugin)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: ViewPageConfig,
) -> Response[Any]:
    r"""Create or update a plugin page

     # Create custom plugin pages

    Plugins can define their own pages consisting of a template.
    This is an html template where you can layout customizable priceloop-blocks.

    ## Template

    Create your own page with a HTML-template (see template documentation: https://eta.js.org/).

    We expose a global variable `app` in our templates to render reusable components and to access
    necessary data.

    ### API

    ```
    type WorkspaceName = String

    type ViewPagePath = String

    type Action = { storeInState: String?, sendEvent: Any?, gotoLink: String? }

    type UIBlock = String(<html>...</html>)

    type TableName = String

    type ColumnName = String

    type FilterOp = String(Eq | Ne | Lt | Lte | Gt | Gte | Is | IsNot | Contains | NotContains | IsEmpty
    | IsNotEmpty)

    type TableQueryCondition = { column: ColumnName, op: FilterOp, value: String? }

    type SortingOrder = String(Ascending | Descending)

    type TableQueryOrdering = { column: ColumnName, order: SortingOrder }

    type ColumnAggregate = String(avg | max | min | sum | bool_and | bool_or | string_agg(,))

    type TableQueryAggregate = { column: ColumnName, agg: ColumnAggregate }

    type TableQuery = {
        from: TableName,
        limit: Int?,
        offset: Int?,
        select: ColumnName[]?,
        where: TableQueryCondition[]?,
        orderBy: TableQueryOrdering[]?,
        groupBy: ColumnName[]?,
        aggregates: TableQueryAggregate[]?
    }

    type TableOptions = { showDecoration: Boolean? }

    type ChartType = String(Apex Chart Type: line | area | bar | pie | donut | radialBar | scatter |
    bubble | heatmap | candlestick | boxPlot | radar | polarArea | rangeBar | rangeArea | treemap (see:
    https://apexcharts.com/docs/chart-types/#))

    type ChartXAxis = {
        column: ColumnName,
        labelColumn: ColumnName?,
        colorColumn: ColumnName?,
        unit: String?
    }

    type ChartYAxis = {
        column: ColumnName,
        partitionColumn: ColumnName?,
        label: String?,
        color: String?,
        unit: String?
    }

    type ChartAnnotation = {
        start: String,
        end: String,
        label: String,
        color: String?
    }

    type ChartOptions = { xAnnotations: ChartAnnotation[]?, yAnnotations: ChartAnnotation[]?,
    additionalApexOptions: Object? }

    type TableRow = { values: String?[], byName: (column: ColumnName) => String? }

    type TableData = { rows: TableRow[] }

    type App = {
        workspaceName: WorkspaceName,
        state: Object,
        workspaceLink: (pagePath: ViewPagePath) => String,
        button: (text: String, action: Action) => UIBlock,
        selectionBox: (placeholder: String, options: String[], action: Action) => UIBlock,
        selectionTableBox: (placeholder: String, options: String[][], headers: String[], action: Action) =>
    UIBlock,
        tableSheet: (query: TableQuery, options: TableOptions?) => UIBlock,
        chart: (query: TableQuery, chartType: ChartType, x: ChartXAxis, y: ChartYAxis[], options:
    ChartOptions?) => UIBlock,
        chartCustom: (apexOptions: Object) => UIBlock,
        load: async (query: TableQuery) => TableData,
        loadOnce: async (query: TableQuery) => TableData
    }

    app: App
    ```

    ### Usage

    Inside a template, you can write javascript inside of `<%...%>`.
    A `String` or any primitive value is rendered like this: `<%= app.workspaceName %>`.
    A `UIBlock` contains html and has to be rendered like this: `<%~ app.tableSheet(query) %>`.
    It is possible to use `await` for `async` functions.

    ### Example

    ```
    <b>Hi <%= app.workspaceName %></b>

    <% let myQuery = { select: [ \"my-category\", \"my-value\" ], from: \"my-table\" } %>

    <div class=\"flex flex-row\">
      <iframe class=\"h-full w-full\" src=\"https://example.com\"></iframe>
      <%~ app.chart(myQuery, \"bar\", { column: \"my-category\" }, [ { column: \"my-value\" } ]) %>
    </div>

    <%~ app.tableSheet(myQuery) %>
    ```

    Args:
        plugin (str):
        json_body (ViewPageConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plugin=plugin,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: ViewPageConfig,
) -> Response[Any]:
    r"""Create or update a plugin page

     # Create custom plugin pages

    Plugins can define their own pages consisting of a template.
    This is an html template where you can layout customizable priceloop-blocks.

    ## Template

    Create your own page with a HTML-template (see template documentation: https://eta.js.org/).

    We expose a global variable `app` in our templates to render reusable components and to access
    necessary data.

    ### API

    ```
    type WorkspaceName = String

    type ViewPagePath = String

    type Action = { storeInState: String?, sendEvent: Any?, gotoLink: String? }

    type UIBlock = String(<html>...</html>)

    type TableName = String

    type ColumnName = String

    type FilterOp = String(Eq | Ne | Lt | Lte | Gt | Gte | Is | IsNot | Contains | NotContains | IsEmpty
    | IsNotEmpty)

    type TableQueryCondition = { column: ColumnName, op: FilterOp, value: String? }

    type SortingOrder = String(Ascending | Descending)

    type TableQueryOrdering = { column: ColumnName, order: SortingOrder }

    type ColumnAggregate = String(avg | max | min | sum | bool_and | bool_or | string_agg(,))

    type TableQueryAggregate = { column: ColumnName, agg: ColumnAggregate }

    type TableQuery = {
        from: TableName,
        limit: Int?,
        offset: Int?,
        select: ColumnName[]?,
        where: TableQueryCondition[]?,
        orderBy: TableQueryOrdering[]?,
        groupBy: ColumnName[]?,
        aggregates: TableQueryAggregate[]?
    }

    type TableOptions = { showDecoration: Boolean? }

    type ChartType = String(Apex Chart Type: line | area | bar | pie | donut | radialBar | scatter |
    bubble | heatmap | candlestick | boxPlot | radar | polarArea | rangeBar | rangeArea | treemap (see:
    https://apexcharts.com/docs/chart-types/#))

    type ChartXAxis = {
        column: ColumnName,
        labelColumn: ColumnName?,
        colorColumn: ColumnName?,
        unit: String?
    }

    type ChartYAxis = {
        column: ColumnName,
        partitionColumn: ColumnName?,
        label: String?,
        color: String?,
        unit: String?
    }

    type ChartAnnotation = {
        start: String,
        end: String,
        label: String,
        color: String?
    }

    type ChartOptions = { xAnnotations: ChartAnnotation[]?, yAnnotations: ChartAnnotation[]?,
    additionalApexOptions: Object? }

    type TableRow = { values: String?[], byName: (column: ColumnName) => String? }

    type TableData = { rows: TableRow[] }

    type App = {
        workspaceName: WorkspaceName,
        state: Object,
        workspaceLink: (pagePath: ViewPagePath) => String,
        button: (text: String, action: Action) => UIBlock,
        selectionBox: (placeholder: String, options: String[], action: Action) => UIBlock,
        selectionTableBox: (placeholder: String, options: String[][], headers: String[], action: Action) =>
    UIBlock,
        tableSheet: (query: TableQuery, options: TableOptions?) => UIBlock,
        chart: (query: TableQuery, chartType: ChartType, x: ChartXAxis, y: ChartYAxis[], options:
    ChartOptions?) => UIBlock,
        chartCustom: (apexOptions: Object) => UIBlock,
        load: async (query: TableQuery) => TableData,
        loadOnce: async (query: TableQuery) => TableData
    }

    app: App
    ```

    ### Usage

    Inside a template, you can write javascript inside of `<%...%>`.
    A `String` or any primitive value is rendered like this: `<%= app.workspaceName %>`.
    A `UIBlock` contains html and has to be rendered like this: `<%~ app.tableSheet(query) %>`.
    It is possible to use `await` for `async` functions.

    ### Example

    ```
    <b>Hi <%= app.workspaceName %></b>

    <% let myQuery = { select: [ \"my-category\", \"my-value\" ], from: \"my-table\" } %>

    <div class=\"flex flex-row\">
      <iframe class=\"h-full w-full\" src=\"https://example.com\"></iframe>
      <%~ app.chart(myQuery, \"bar\", { column: \"my-category\" }, [ { column: \"my-value\" } ]) %>
    </div>

    <%~ app.tableSheet(myQuery) %>
    ```

    Args:
        plugin (str):
        json_body (ViewPageConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plugin=plugin,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)

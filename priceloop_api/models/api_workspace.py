from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_external_function import ApiExternalFunction
    from ..models.api_table import ApiTable


T = TypeVar("T", bound="ApiWorkspace")


@attr.s(auto_attribs=True)
class ApiWorkspace:
    """
    Attributes:
        name (str):
        external_functions (Union[Unset, List['ApiExternalFunction']]):
        tables (Union[Unset, List['ApiTable']]):
    """

    name: str
    external_functions: Union[Unset, List["ApiExternalFunction"]] = UNSET
    tables: Union[Unset, List["ApiTable"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        external_functions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.external_functions, Unset):
            external_functions = []
            for external_functions_item_data in self.external_functions:
                external_functions_item = external_functions_item_data.to_dict()

                external_functions.append(external_functions_item)

        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if external_functions is not UNSET:
            field_dict["externalFunctions"] = external_functions
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_external_function import ApiExternalFunction
        from ..models.api_table import ApiTable

        d = src_dict.copy()
        name = d.pop("name")

        external_functions = []
        _external_functions = d.pop("externalFunctions", UNSET)
        for external_functions_item_data in _external_functions or []:
            external_functions_item = ApiExternalFunction.from_dict(external_functions_item_data)

            external_functions.append(external_functions_item)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = ApiTable.from_dict(tables_item_data)

            tables.append(tables_item)

        api_workspace = cls(
            name=name,
            external_functions=external_functions,
            tables=tables,
        )

        api_workspace.additional_properties = d
        return api_workspace

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column_schema import ApiColumnSchema
    from ..models.api_table_attributes import ApiTableAttributes


T = TypeVar("T", bound="ApiTableSchema")


@attr.s(auto_attribs=True)
class ApiTableSchema:
    """
    Attributes:
        name (str):  Example: table-name.
        attributes (Union[Unset, ApiTableAttributes]):
        columns (Union[Unset, List['ApiColumnSchema']]):
    """

    name: str
    attributes: Union[Unset, "ApiTableAttributes"] = UNSET
    columns: Union[Unset, List["ApiColumnSchema"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_column_schema import ApiColumnSchema
        from ..models.api_table_attributes import ApiTableAttributes

        d = src_dict.copy()
        name = d.pop("name")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ApiTableAttributes]
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = ApiTableAttributes.from_dict(_attributes)

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = ApiColumnSchema.from_dict(columns_item_data)

            columns.append(columns_item)

        api_table_schema = cls(
            name=name,
            attributes=attributes,
            columns=columns,
        )

        api_table_schema.additional_properties = d
        return api_table_schema

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column import ApiColumn
    from ..models.api_table_attributes import ApiTableAttributes


T = TypeVar("T", bound="ApiTable")


@attr.s(auto_attribs=True)
class ApiTable:
    """
    Attributes:
        attributes (ApiTableAttributes):
        name (str):  Example: table-name.
        position (int):
        columns (Union[Unset, List['ApiColumn']]):
    """

    attributes: "ApiTableAttributes"
    name: str
    position: int
    columns: Union[Unset, List["ApiColumn"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes.to_dict()

        name = self.name
        position = self.position
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
                "attributes": attributes,
                "name": name,
                "position": position,
            }
        )
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_column import ApiColumn
        from ..models.api_table_attributes import ApiTableAttributes

        d = src_dict.copy()
        attributes = ApiTableAttributes.from_dict(d.pop("attributes"))

        name = d.pop("name")

        position = d.pop("position")

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = ApiColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        api_table = cls(
            attributes=attributes,
            name=name,
            position=position,
            columns=columns,
        )

        api_table.additional_properties = d
        return api_table

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

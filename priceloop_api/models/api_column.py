from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiColumn")


@attr.s(auto_attribs=True)
class ApiColumn:
    """
    Attributes:
        name (str):
        position (int):
        table_name (str):
        tpe (str):
    """

    name: str
    position: int
    table_name: str
    tpe: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        position = self.position
        table_name = self.table_name
        tpe = self.tpe

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
                "tableName": table_name,
                "tpe": tpe,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        position = d.pop("position")

        table_name = d.pop("tableName")

        tpe = d.pop("tpe")

        api_column = cls(
            name=name,
            position=position,
            table_name=table_name,
            tpe=tpe,
        )

        api_column.additional_properties = d
        return api_column

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

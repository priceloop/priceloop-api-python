from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column_attributes import ApiColumnAttributes


T = TypeVar("T", bound="ApiColumn")


@attr.s(auto_attribs=True)
class ApiColumn:
    """
    Attributes:
        attributes (ApiColumnAttributes):
        name (str):  Example: column-name.
        position (int):
        table_name (str):  Example: table-name.
        tpe (str):
        formula (Union[Unset, None, str]):  Example: 1 + 2.
    """

    attributes: "ApiColumnAttributes"
    name: str
    position: int
    table_name: str
    tpe: str
    formula: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes.to_dict()

        name = self.name
        position = self.position
        table_name = self.table_name
        tpe = self.tpe
        formula = self.formula

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "name": name,
                "position": position,
                "tableName": table_name,
                "tpe": tpe,
            }
        )
        if formula is not UNSET:
            field_dict["formula"] = formula

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_column_attributes import ApiColumnAttributes

        d = src_dict.copy()
        attributes = ApiColumnAttributes.from_dict(d.pop("attributes"))

        name = d.pop("name")

        position = d.pop("position")

        table_name = d.pop("tableName")

        tpe = d.pop("tpe")

        formula = d.pop("formula", UNSET)

        api_column = cls(
            attributes=attributes,
            name=name,
            position=position,
            table_name=table_name,
            tpe=tpe,
            formula=formula,
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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_attribute_schema import ColumnAttributeSchema


T = TypeVar("T", bound="ColumnSchema")


@attr.s(auto_attribs=True)
class ColumnSchema:
    """
    Attributes:
        name (str):
        tpe (str):
        attributes (Union[Unset, ColumnAttributeSchema]):
        formula (Union[Unset, str]):
    """

    name: str
    tpe: str
    attributes: Union[Unset, "ColumnAttributeSchema"] = UNSET
    formula: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        tpe = self.tpe
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        formula = self.formula

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "tpe": tpe,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if formula is not UNSET:
            field_dict["formula"] = formula

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_attribute_schema import ColumnAttributeSchema

        d = src_dict.copy()
        name = d.pop("name")

        tpe = d.pop("tpe")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ColumnAttributeSchema]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ColumnAttributeSchema.from_dict(_attributes)

        formula = d.pop("formula", UNSET)

        column_schema = cls(
            name=name,
            tpe=tpe,
            attributes=attributes,
            formula=formula,
        )

        column_schema.additional_properties = d
        return column_schema

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

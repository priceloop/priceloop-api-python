from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.explicit_expr_type import ExplicitExprType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column_attributes_update import ApiColumnAttributesUpdate


T = TypeVar("T", bound="ApiColumnSchema")


@attr.s(auto_attribs=True)
class ApiColumnSchema:
    """
    Attributes:
        name (str):  Example: column-name.
        tpe (ExplicitExprType):
        attributes (Union[Unset, ApiColumnAttributesUpdate]):
        formula (Union[Unset, None, str]):  Example: 1 + 2.
    """

    name: str
    tpe: ExplicitExprType
    attributes: Union[Unset, "ApiColumnAttributesUpdate"] = UNSET
    formula: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        tpe = self.tpe.value

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
        from ..models.api_column_attributes_update import ApiColumnAttributesUpdate

        d = src_dict.copy()
        name = d.pop("name")

        tpe = ExplicitExprType(d.pop("tpe"))

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ApiColumnAttributesUpdate]
        if isinstance(_attributes, Unset) or _attributes is None:
            attributes = UNSET
        else:
            attributes = ApiColumnAttributesUpdate.from_dict(_attributes)

        formula = d.pop("formula", UNSET)

        api_column_schema = cls(
            name=name,
            tpe=tpe,
            attributes=attributes,
            formula=formula,
        )

        api_column_schema.additional_properties = d
        return api_column_schema

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

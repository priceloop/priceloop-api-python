from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ape_data_typeform import ApeDataTypeform


T = TypeVar("T", bound="ApeData")


@attr.s(auto_attribs=True)
class ApeData:
    """
    Attributes:
        typeform (Union[Unset, ApeDataTypeform]):
    """

    typeform: Union[Unset, "ApeDataTypeform"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        typeform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.typeform, Unset):
            typeform = self.typeform.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if typeform is not UNSET:
            field_dict["typeform"] = typeform

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ape_data_typeform import ApeDataTypeform

        d = src_dict.copy()
        _typeform = d.pop("typeform", UNSET)
        typeform: Union[Unset, ApeDataTypeform]
        if isinstance(_typeform, Unset):
            typeform = UNSET
        else:
            typeform = ApeDataTypeform.from_dict(_typeform)

        ape_data = cls(
            typeform=typeform,
        )

        ape_data.additional_properties = d
        return ape_data

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

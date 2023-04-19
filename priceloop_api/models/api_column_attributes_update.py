from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiColumnAttributesUpdate:
    """
    Attributes:
        is_gui_locked (Union[Unset, bool]):
        is_hidden (Union[Unset, bool]):
    """

    is_gui_locked: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_gui_locked is not UNSET:
            field_dict["isGuiLocked"] = is_gui_locked
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_gui_locked = d.pop("isGuiLocked", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        api_column_attributes_update = cls(
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
        )

        api_column_attributes_update.additional_properties = d
        return api_column_attributes_update

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

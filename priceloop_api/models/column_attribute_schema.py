from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnAttributeSchema")


@attr.s(auto_attribs=True)
class ColumnAttributeSchema:
    """
    Attributes:
        is_gui_locked (Union[Unset, bool]):
        is_hidden (Union[Unset, bool]):
        position (Union[Unset, int]):
        width_px (Union[Unset, int]):
    """

    is_gui_locked: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    width_px: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        position = self.position
        width_px = self.width_px

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_gui_locked is not UNSET:
            field_dict["isGuiLocked"] = is_gui_locked
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if position is not UNSET:
            field_dict["position"] = position
        if width_px is not UNSET:
            field_dict["widthPx"] = width_px

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_gui_locked = d.pop("isGuiLocked", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        position = d.pop("position", UNSET)

        width_px = d.pop("widthPx", UNSET)

        column_attribute_schema = cls(
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            position=position,
            width_px=width_px,
        )

        column_attribute_schema.additional_properties = d
        return column_attribute_schema

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

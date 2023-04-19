from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiColumnAttributes")


@attr.s(auto_attribs=True)
class ApiColumnAttributes:
    """
    Attributes:
        is_gui_locked (bool):
        is_hidden (bool):
        description (Union[Unset, str]):
    """

    is_gui_locked: bool
    is_hidden: bool
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isGuiLocked": is_gui_locked,
                "isHidden": is_hidden,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_gui_locked = d.pop("isGuiLocked")

        is_hidden = d.pop("isHidden")

        description = d.pop("description", UNSET)

        api_column_attributes = cls(
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            description=description,
        )

        api_column_attributes.additional_properties = d
        return api_column_attributes

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

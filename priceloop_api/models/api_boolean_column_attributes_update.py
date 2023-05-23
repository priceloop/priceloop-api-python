from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.boolean_display_style import BooleanDisplayStyle
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBooleanColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiBooleanColumnAttributesUpdate:
    """
    Attributes:
        display_style (Union[Unset, BooleanDisplayStyle]):
    """

    display_style: Union[Unset, BooleanDisplayStyle] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_style: Union[Unset, str] = UNSET
        if not isinstance(self.display_style, Unset):
            display_style = self.display_style.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_style is not UNSET:
            field_dict["displayStyle"] = display_style

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _display_style = d.pop("displayStyle", UNSET)
        display_style: Union[Unset, BooleanDisplayStyle]
        if isinstance(_display_style, Unset) or _display_style is None:
            display_style = UNSET
        else:
            display_style = BooleanDisplayStyle(_display_style)

        api_boolean_column_attributes_update = cls(
            display_style=display_style,
        )

        api_boolean_column_attributes_update.additional_properties = d
        return api_boolean_column_attributes_update

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

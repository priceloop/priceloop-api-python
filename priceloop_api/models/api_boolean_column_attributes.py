from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.boolean_display_style import BooleanDisplayStyle

T = TypeVar("T", bound="ApiBooleanColumnAttributes")


@attr.s(auto_attribs=True)
class ApiBooleanColumnAttributes:
    """
    Attributes:
        display_style (BooleanDisplayStyle):
    """

    display_style: BooleanDisplayStyle
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_style = self.display_style.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayStyle": display_style,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_style = BooleanDisplayStyle(d.pop("displayStyle"))

        api_boolean_column_attributes = cls(
            display_style=display_style,
        )

        api_boolean_column_attributes.additional_properties = d
        return api_boolean_column_attributes

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

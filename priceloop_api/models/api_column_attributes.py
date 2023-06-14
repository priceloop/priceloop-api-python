from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_boolean_column_attributes import ApiBooleanColumnAttributes


T = TypeVar("T", bound="ApiColumnAttributes")


@attr.s(auto_attribs=True)
class ApiColumnAttributes:
    """
    Attributes:
        boolean_column_attributes (ApiBooleanColumnAttributes):
        is_gui_locked (bool):
        is_hidden (bool):
        description (Union[Unset, None, str]):
        background_color (Union[Unset, None, str]):
    """

    boolean_column_attributes: "ApiBooleanColumnAttributes"
    is_gui_locked: bool
    is_hidden: bool
    description: Union[Unset, None, str] = UNSET
    background_color: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boolean_column_attributes = self.boolean_column_attributes.to_dict()

        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        description = self.description
        background_color = self.background_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "booleanColumnAttributes": boolean_column_attributes,
                "isGuiLocked": is_gui_locked,
                "isHidden": is_hidden,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_boolean_column_attributes import ApiBooleanColumnAttributes

        d = src_dict.copy()
        boolean_column_attributes = ApiBooleanColumnAttributes.from_dict(d.pop("booleanColumnAttributes"))

        is_gui_locked = d.pop("isGuiLocked")
        is_hidden = d.pop("isHidden")
        description = d.pop("description", UNSET)
        background_color = d.pop("backgroundColor", UNSET)

        api_column_attributes = cls(
            boolean_column_attributes=boolean_column_attributes,
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            description=description,
            background_color=d.pop("backgroundColor", UNSET),
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

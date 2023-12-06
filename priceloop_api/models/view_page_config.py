from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewPageConfig")


@attr.s(auto_attribs=True)
class ViewPageConfig:
    """
    Attributes:
        display_name (str):
        path (str):
        view_template (str):
        abbreviation (Union[Unset, None, str]):
        emoji (Union[Unset, None, str]):
        icon_url (Union[Unset, None, str]):
    """

    display_name: str
    path: str
    view_template: str
    abbreviation: Union[Unset, None, str] = UNSET
    emoji: Union[Unset, None, str] = UNSET
    icon_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        path = self.path
        view_template = self.view_template
        abbreviation = self.abbreviation
        emoji = self.emoji
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "path": path,
                "viewTemplate": view_template,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        path = d.pop("path")

        view_template = d.pop("viewTemplate")

        abbreviation = d.pop("abbreviation", UNSET)

        emoji = d.pop("emoji", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        view_page_config = cls(
            display_name=display_name,
            path=path,
            view_template=view_template,
            abbreviation=abbreviation,
            emoji=emoji,
            icon_url=icon_url,
        )

        view_page_config.additional_properties = d
        return view_page_config

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

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewPageConfig")


@attr.s(auto_attribs=True)
class ViewPageConfig:
    """
    Attributes:
        display_name (str):
        icon_url (str):
        path (str):
        view_template (str):
    """

    display_name: str
    icon_url: str
    path: str
    view_template: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        icon_url = self.icon_url
        path = self.path
        view_template = self.view_template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "iconUrl": icon_url,
                "path": path,
                "viewTemplate": view_template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName")

        icon_url = d.pop("iconUrl")

        path = d.pop("path")

        view_template = d.pop("viewTemplate")

        view_page_config = cls(
            display_name=display_name,
            icon_url=icon_url,
            path=path,
            view_template=view_template,
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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_requirement import PluginRequirement
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginDefinition")


@attr.s(auto_attribs=True)
class PluginDefinition:
    """
    Attributes:
        description (str):
        display_name (str):
        icon_url (str):
        name (str):
        show_in_catalog (bool):
        requirements (Union[Unset, List[PluginRequirement]]):
    """

    description: str
    display_name: str
    icon_url: str
    name: str
    show_in_catalog: bool
    requirements: Union[Unset, List[PluginRequirement]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        display_name = self.display_name
        icon_url = self.icon_url
        name = self.name
        show_in_catalog = self.show_in_catalog
        requirements: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = []
            for requirements_item_data in self.requirements:
                requirements_item = requirements_item_data.value

                requirements.append(requirements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "displayName": display_name,
                "iconUrl": icon_url,
                "name": name,
                "showInCatalog": show_in_catalog,
            }
        )
        if requirements is not UNSET:
            field_dict["requirements"] = requirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        display_name = d.pop("displayName")

        icon_url = d.pop("iconUrl")

        name = d.pop("name")

        show_in_catalog = d.pop("showInCatalog")

        requirements = []
        _requirements = d.pop("requirements", UNSET)
        for requirements_item_data in _requirements or []:
            requirements_item = PluginRequirement(requirements_item_data)

            requirements.append(requirements_item)

        plugin_definition = cls(
            description=description,
            display_name=display_name,
            icon_url=icon_url,
            name=name,
            show_in_catalog=show_in_catalog,
            requirements=requirements,
        )

        plugin_definition.additional_properties = d
        return plugin_definition

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

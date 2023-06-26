from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_table_role_semantic import PluginTableRoleSemantic
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginTableRole")


@attr.s(auto_attribs=True)
class PluginTableRole:
    """
    Attributes:
        name (str):
        plugin_name (str):
        semantic (PluginTableRoleSemantic):
        description (Union[Unset, None, str]):
    """

    name: str
    plugin_name: str
    semantic: PluginTableRoleSemantic
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        plugin_name = self.plugin_name
        semantic = self.semantic.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "pluginName": plugin_name,
                "semantic": semantic,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        plugin_name = d.pop("pluginName")

        semantic = PluginTableRoleSemantic(d.pop("semantic"))

        description = d.pop("description", UNSET)

        plugin_table_role = cls(
            name=name,
            plugin_name=plugin_name,
            semantic=semantic,
            description=description,
        )

        plugin_table_role.additional_properties = d
        return plugin_table_role

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_table_role_semantic_type_0 import PluginTableRoleSemanticType0


T = TypeVar("T", bound="PluginTableRole")


@attr.s(auto_attribs=True)
class PluginTableRole:
    """
    Attributes:
        name (str):
        plugin_name (str):
        semantic ('PluginTableRoleSemanticType0'):
        description (Union[Unset, None, str]):
    """

    name: str
    plugin_name: str
    semantic: "PluginTableRoleSemanticType0"
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.plugin_table_role_semantic_type_0 import PluginTableRoleSemanticType0

        name = self.name
        plugin_name = self.plugin_name
        semantic: Dict[str, Any]

        if isinstance(self.semantic, PluginTableRoleSemanticType0):
            semantic = self.semantic.to_dict()

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
        from ..models.plugin_table_role_semantic_type_0 import PluginTableRoleSemanticType0

        d = src_dict.copy()
        name = d.pop("name")

        plugin_name = d.pop("pluginName")

        def _parse_semantic(data: object) -> "PluginTableRoleSemanticType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_table_role_semantic_type_0 = PluginTableRoleSemanticType0.from_dict(data)

            return componentsschemas_plugin_table_role_semantic_type_0

        semantic = _parse_semantic(d.pop("semantic"))

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_table_role_semantic_type_0 import PluginTableRoleSemanticType0


T = TypeVar("T", bound="ApiPluginTableRoleBody")


@attr.s(auto_attribs=True)
class ApiPluginTableRoleBody:
    """
    Attributes:
        semantic ('PluginTableRoleSemanticType0'):
        description (Union[Unset, None, str]):
    """

    semantic: "PluginTableRoleSemanticType0"
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.plugin_table_role_semantic_type_0 import PluginTableRoleSemanticType0

        semantic: Dict[str, Any]

        if isinstance(self.semantic, PluginTableRoleSemanticType0):
            semantic = self.semantic.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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

        def _parse_semantic(data: object) -> "PluginTableRoleSemanticType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_table_role_semantic_type_0 = PluginTableRoleSemanticType0.from_dict(data)

            return componentsschemas_plugin_table_role_semantic_type_0

        semantic = _parse_semantic(d.pop("semantic"))

        description = d.pop("description", UNSET)

        api_plugin_table_role_body = cls(
            semantic=semantic,
            description=description,
        )

        api_plugin_table_role_body.additional_properties = d
        return api_plugin_table_role_body

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

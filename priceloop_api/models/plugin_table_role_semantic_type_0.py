from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.publish_input import PublishInput


T = TypeVar("T", bound="PluginTableRoleSemanticType0")


@attr.s(auto_attribs=True)
class PluginTableRoleSemanticType0:
    """
    Attributes:
        publish_input (PublishInput):
    """

    publish_input: "PublishInput"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        publish_input = self.publish_input.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PublishInput": publish_input,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.publish_input import PublishInput

        d = src_dict.copy()
        publish_input = PublishInput.from_dict(d.pop("PublishInput"))

        plugin_table_role_semantic_type_0 = cls(
            publish_input=publish_input,
        )

        plugin_table_role_semantic_type_0.additional_properties = d
        return plugin_table_role_semantic_type_0

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

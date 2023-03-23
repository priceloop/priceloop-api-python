from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.plugin_1 import Plugin1


T = TypeVar("T", bound="WebhookEventSelectorType0")


@attr.s(auto_attribs=True)
class WebhookEventSelectorType0:
    """
    Attributes:
        plugin (Plugin1):
    """

    plugin: "Plugin1"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plugin = self.plugin.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Plugin": plugin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_1 import Plugin1

        d = src_dict.copy()
        plugin = Plugin1.from_dict(d.pop("Plugin"))

        webhook_event_selector_type_0 = cls(
            plugin=plugin,
        )

        webhook_event_selector_type_0.additional_properties = d
        return webhook_event_selector_type_0

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

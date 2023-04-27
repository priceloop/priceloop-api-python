from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.plugin_name import PluginName
from ..models.webhook_plugin_event import WebhookPluginEvent

T = TypeVar("T", bound="Plugin1")


@attr.s(auto_attribs=True)
class Plugin1:
    """
    Attributes:
        event (WebhookPluginEvent):
        plugin_name (PluginName):
    """

    event: WebhookPluginEvent
    plugin_name: PluginName
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event.value

        plugin_name = self.plugin_name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "pluginName": plugin_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = WebhookPluginEvent(d.pop("event"))

        plugin_name = PluginName(d.pop("pluginName"))

        plugin_1 = cls(
            event=event,
            plugin_name=plugin_name,
        )

        plugin_1.additional_properties = d
        return plugin_1

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

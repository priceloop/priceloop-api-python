from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_name import PluginName
from ..models.webhook_plugin_event import WebhookPluginEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="Plugin1")


@attr.s(auto_attribs=True)
class Plugin1:
    """
    Attributes:
        plugin_name (PluginName):
        events (Union[Unset, List[WebhookPluginEvent]]):
    """

    plugin_name: PluginName
    events: Union[Unset, List[WebhookPluginEvent]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plugin_name = self.plugin_name.value

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pluginName": plugin_name,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plugin_name = PluginName(d.pop("pluginName"))

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookPluginEvent(events_item_data)

            events.append(events_item)

        plugin_1 = cls(
            plugin_name=plugin_name,
            events=events,
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

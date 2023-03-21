from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.webhook_config import WebhookConfig
    from ..models.webhook_event_selector_type_0 import WebhookEventSelectorType0


T = TypeVar("T", bound="WebhookInfo")


@attr.s(auto_attribs=True)
class WebhookInfo:
    """
    Attributes:
        config (WebhookConfig):
        event_selector ('WebhookEventSelectorType0'):
        id (str):
    """

    config: "WebhookConfig"
    event_selector: "WebhookEventSelectorType0"
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.webhook_event_selector_type_0 import WebhookEventSelectorType0

        config = self.config.to_dict()

        event_selector: Dict[str, Any]

        if isinstance(self.event_selector, WebhookEventSelectorType0):
            event_selector = self.event_selector.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "eventSelector": event_selector,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_config import WebhookConfig
        from ..models.webhook_event_selector_type_0 import WebhookEventSelectorType0

        d = src_dict.copy()
        config = WebhookConfig.from_dict(d.pop("config"))

        def _parse_event_selector(data: object) -> "WebhookEventSelectorType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_webhook_event_selector_type_0 = WebhookEventSelectorType0.from_dict(data)

            return componentsschemas_webhook_event_selector_type_0

        event_selector = _parse_event_selector(d.pop("eventSelector"))

        id = d.pop("id")

        webhook_info = cls(
            config=config,
            event_selector=event_selector,
            id=id,
        )

        webhook_info.additional_properties = d
        return webhook_info

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.send_notification import SendNotification


T = TypeVar("T", bound="ApiActionType0")


@attr.s(auto_attribs=True)
class ApiActionType0:
    """
    Attributes:
        send_notification (SendNotification):
    """

    send_notification: "SendNotification"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_notification = self.send_notification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SendNotification": send_notification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.send_notification import SendNotification

        d = src_dict.copy()
        send_notification = SendNotification.from_dict(d.pop("SendNotification"))

        api_action_type_0 = cls(
            send_notification=send_notification,
        )

        api_action_type_0.additional_properties = d
        return api_action_type_0

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

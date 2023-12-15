from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiAutomation")


@attr.s(auto_attribs=True)
class ApiAutomation:
    """
    Attributes:
        action_name (str):  Example: action-name.
        trigger_name (str):  Example: trigger-name.
    """

    action_name: str
    trigger_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_name = self.action_name
        trigger_name = self.trigger_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionName": action_name,
                "triggerName": trigger_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action_name = d.pop("actionName")

        trigger_name = d.pop("triggerName")

        api_automation = cls(
            action_name=action_name,
            trigger_name=trigger_name,
        )

        api_automation.additional_properties = d
        return api_automation

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

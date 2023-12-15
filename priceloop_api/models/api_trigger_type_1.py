from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.schedule import Schedule


T = TypeVar("T", bound="ApiTriggerType1")


@attr.s(auto_attribs=True)
class ApiTriggerType1:
    """
    Attributes:
        schedule (Schedule):
    """

    schedule: "Schedule"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schedule import Schedule

        d = src_dict.copy()
        schedule = Schedule.from_dict(d.pop("Schedule"))

        api_trigger_type_1 = cls(
            schedule=schedule,
        )

        api_trigger_type_1.additional_properties = d
        return api_trigger_type_1

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

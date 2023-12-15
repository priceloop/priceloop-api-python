from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.record_updated import RecordUpdated


T = TypeVar("T", bound="ApiTriggerType0")


@attr.s(auto_attribs=True)
class ApiTriggerType0:
    """
    Attributes:
        record_updated (RecordUpdated):
    """

    record_updated: "RecordUpdated"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_updated = self.record_updated.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "RecordUpdated": record_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_updated import RecordUpdated

        d = src_dict.copy()
        record_updated = RecordUpdated.from_dict(d.pop("RecordUpdated"))

        api_trigger_type_0 = cls(
            record_updated=record_updated,
        )

        api_trigger_type_0.additional_properties = d
        return api_trigger_type_0

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

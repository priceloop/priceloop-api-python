from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Truncated")


@attr.s(auto_attribs=True)
class Truncated:
    """
    Attributes:
        decimal_points (int):
    """

    decimal_points: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        decimal_points = self.decimal_points

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decimalPoints": decimal_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        decimal_points = d.pop("decimalPoints")

        truncated = cls(
            decimal_points=decimal_points,
        )

        truncated.additional_properties = d
        return truncated

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

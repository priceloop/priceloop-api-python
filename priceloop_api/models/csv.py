from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CSV")


@attr.s(auto_attribs=True)
class CSV:
    """
    Attributes:
        delimiter (str):
    """

    delimiter: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delimiter = self.delimiter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delimiter": delimiter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delimiter = d.pop("delimiter")

        csv = cls(
            delimiter=delimiter,
        )

        csv.additional_properties = d
        return csv

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

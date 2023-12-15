from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.one_of import OneOf


T = TypeVar("T", bound="ApiWatchColumnsType1")


@attr.s(auto_attribs=True)
class ApiWatchColumnsType1:
    """
    Attributes:
        one_of (OneOf):
    """

    one_of: "OneOf"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        one_of = self.one_of.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OneOf": one_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.one_of import OneOf

        d = src_dict.copy()
        one_of = OneOf.from_dict(d.pop("OneOf"))

        api_watch_columns_type_1 = cls(
            one_of=one_of,
        )

        api_watch_columns_type_1.additional_properties = d
        return api_watch_columns_type_1

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

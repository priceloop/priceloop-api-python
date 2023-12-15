from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.all_ import All


T = TypeVar("T", bound="ApiWatchColumnsType0")


@attr.s(auto_attribs=True)
class ApiWatchColumnsType0:
    """
    Attributes:
        all_ (All):
    """

    all_: "All"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "All": all_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.all_ import All

        d = src_dict.copy()
        all_ = All.from_dict(d.pop("All"))

        api_watch_columns_type_0 = cls(
            all_=all_,
        )

        api_watch_columns_type_0.additional_properties = d
        return api_watch_columns_type_0

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

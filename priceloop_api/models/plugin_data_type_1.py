from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.empty import Empty


T = TypeVar("T", bound="PluginDataType1")


@attr.s(auto_attribs=True)
class PluginDataType1:
    """
    Attributes:
        empty (Empty):
    """

    empty: "Empty"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        empty = self.empty.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Empty": empty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.empty import Empty

        d = src_dict.copy()
        empty = Empty.from_dict(d.pop("Empty"))

        plugin_data_type_1 = cls(
            empty=empty,
        )

        plugin_data_type_1.additional_properties = d
        return plugin_data_type_1

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

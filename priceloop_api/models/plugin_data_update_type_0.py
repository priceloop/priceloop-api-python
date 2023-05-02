from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.ape_data_1 import ApeData1


T = TypeVar("T", bound="PluginDataUpdateType0")


@attr.s(auto_attribs=True)
class PluginDataUpdateType0:
    """
    Attributes:
        ape_data (ApeData1):
    """

    ape_data: "ApeData1"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ape_data = self.ape_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ApeData": ape_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ape_data_1 import ApeData1

        d = src_dict.copy()
        ape_data = ApeData1.from_dict(d.pop("ApeData"))

        plugin_data_update_type_0 = cls(
            ape_data=ape_data,
        )

        plugin_data_update_type_0.additional_properties = d
        return plugin_data_update_type_0

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

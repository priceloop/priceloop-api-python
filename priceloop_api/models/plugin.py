from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.plugin_data_type_0 import PluginDataType0
    from ..models.plugin_external_data import PluginExternalData


T = TypeVar("T", bound="Plugin")


@attr.s(auto_attribs=True)
class Plugin:
    """
    Attributes:
        data ('PluginDataType0'):
        external_data (PluginExternalData):
        name (str):
        status (str):
    """

    data: "PluginDataType0"
    external_data: "PluginExternalData"
    name: str
    status: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.plugin_data_type_0 import PluginDataType0

        data: Dict[str, Any]

        if isinstance(self.data, PluginDataType0):
            data = self.data.to_dict()

        external_data = self.external_data.to_dict()

        name = self.name
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "externalData": external_data,
                "name": name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_data_type_0 import PluginDataType0
        from ..models.plugin_external_data import PluginExternalData

        d = src_dict.copy()

        def _parse_data(data: object) -> "PluginDataType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_data_type_0 = PluginDataType0.from_dict(data)

            return componentsschemas_plugin_data_type_0

        data = _parse_data(d.pop("data"))

        external_data = PluginExternalData.from_dict(d.pop("externalData"))

        name = d.pop("name")

        status = d.pop("status")

        plugin = cls(
            data=data,
            external_data=external_data,
            name=name,
            status=status,
        )

        plugin.additional_properties = d
        return plugin

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

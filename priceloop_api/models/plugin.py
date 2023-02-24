from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.active import Active
    from ..models.ape import Ape
    from ..models.ape_data import ApeData
    from ..models.inactive import Inactive
    from ..models.plugin_external_data import PluginExternalData


T = TypeVar("T", bound="Plugin")


@attr.s(auto_attribs=True)
class Plugin:
    """
    Attributes:
        data (ApeData):
        external_data (PluginExternalData):
        name (Ape):
        status (Union['Active', 'Inactive']):
    """

    data: "ApeData"
    external_data: "PluginExternalData"
    name: "Ape"
    status: Union["Active", "Inactive"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.active import Active

        data = self.data.to_dict()

        external_data = self.external_data.to_dict()

        name = self.name.to_dict()

        status: Dict[str, Any]

        if isinstance(self.status, Active):
            status = self.status.to_dict()

        else:
            status = self.status.to_dict()

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
        from ..models.active import Active
        from ..models.ape import Ape
        from ..models.ape_data import ApeData
        from ..models.inactive import Inactive
        from ..models.plugin_external_data import PluginExternalData

        d = src_dict.copy()
        data = ApeData.from_dict(d.pop("data"))

        external_data = PluginExternalData.from_dict(d.pop("externalData"))

        name = Ape.from_dict(d.pop("name"))

        def _parse_status(data: object) -> Union["Active", "Inactive"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_status_type_0 = Active.from_dict(data)

                return componentsschemas_plugin_status_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_status_type_1 = Inactive.from_dict(data)

            return componentsschemas_plugin_status_type_1

        status = _parse_status(d.pop("status"))

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

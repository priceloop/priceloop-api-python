from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.config_type_0 import ConfigType0


T = TypeVar("T", bound="Action")


@attr.s(auto_attribs=True)
class Action:
    """
    Attributes:
        config ('ConfigType0'):
        name (str):  Example: action-name.
    """

    config: "ConfigType0"
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.config_type_0 import ConfigType0

        config: Dict[str, Any]

        if isinstance(self.config, ConfigType0):
            config = self.config.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_type_0 import ConfigType0

        d = src_dict.copy()

        def _parse_config(data: object) -> "ConfigType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_config_type_0 = ConfigType0.from_dict(data)

            return componentsschemas_config_type_0

        config = _parse_config(d.pop("config"))

        name = d.pop("name")

        action = cls(
            config=config,
            name=name,
        )

        action.additional_properties = d
        return action

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

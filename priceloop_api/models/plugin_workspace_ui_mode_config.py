from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PluginWorkspaceUIModeConfig")


@attr.s(auto_attribs=True)
class PluginWorkspaceUIModeConfig:
    """
    Attributes:
        enabled (bool):
        fullscreen (bool):
    """

    enabled: bool
    fullscreen: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        fullscreen = self.fullscreen

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "fullscreen": fullscreen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        fullscreen = d.pop("fullscreen")

        plugin_workspace_ui_mode_config = cls(
            enabled=enabled,
            fullscreen=fullscreen,
        )

        plugin_workspace_ui_mode_config.additional_properties = d
        return plugin_workspace_ui_mode_config

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

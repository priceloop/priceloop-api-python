from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_workspace_state import PluginWorkspaceState


T = TypeVar("T", bound="PluginWorkspaceList")


@attr.s(auto_attribs=True)
class PluginWorkspaceList:
    """
    Attributes:
        enabled_workspaces (Union[Unset, List['PluginWorkspaceState']]):
    """

    enabled_workspaces: Union[Unset, List["PluginWorkspaceState"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled_workspaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enabled_workspaces, Unset):
            enabled_workspaces = []
            for enabled_workspaces_item_data in self.enabled_workspaces:
                enabled_workspaces_item = enabled_workspaces_item_data.to_dict()

                enabled_workspaces.append(enabled_workspaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled_workspaces is not UNSET:
            field_dict["enabledWorkspaces"] = enabled_workspaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_workspace_state import PluginWorkspaceState

        d = src_dict.copy()
        enabled_workspaces = []
        _enabled_workspaces = d.pop("enabledWorkspaces", UNSET)
        for enabled_workspaces_item_data in _enabled_workspaces or []:
            enabled_workspaces_item = PluginWorkspaceState.from_dict(enabled_workspaces_item_data)

            enabled_workspaces.append(enabled_workspaces_item)

        plugin_workspace_list = cls(
            enabled_workspaces=enabled_workspaces,
        )

        plugin_workspace_list.additional_properties = d
        return plugin_workspace_list

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

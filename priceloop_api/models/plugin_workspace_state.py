from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.plugin import Plugin
    from ..models.workspace_integrations import WorkspaceIntegrations


T = TypeVar("T", bound="PluginWorkspaceState")


@attr.s(auto_attribs=True)
class PluginWorkspaceState:
    """
    Attributes:
        plugin (Plugin):
        workspace_integrations (WorkspaceIntegrations):
        workspace_name (str):  Example: workspace-name.
    """

    plugin: "Plugin"
    workspace_integrations: "WorkspaceIntegrations"
    workspace_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plugin = self.plugin.to_dict()

        workspace_integrations = self.workspace_integrations.to_dict()

        workspace_name = self.workspace_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin": plugin,
                "workspaceIntegrations": workspace_integrations,
                "workspaceName": workspace_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin import Plugin
        from ..models.workspace_integrations import WorkspaceIntegrations

        d = src_dict.copy()
        plugin = Plugin.from_dict(d.pop("plugin"))

        workspace_integrations = WorkspaceIntegrations.from_dict(d.pop("workspaceIntegrations"))

        workspace_name = d.pop("workspaceName")

        plugin_workspace_state = cls(
            plugin=plugin,
            workspace_integrations=workspace_integrations,
            workspace_name=workspace_name,
        )

        plugin_workspace_state.additional_properties = d
        return plugin_workspace_state

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

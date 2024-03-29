from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plugin_requirement import PluginRequirement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_workspace_ui_mode_config import PluginWorkspaceUIModeConfig


T = TypeVar("T", bound="PluginDefinition")


@attr.s(auto_attribs=True)
class PluginDefinition:
    """
    Attributes:
        description (str):
        display_name (str):
        name (str):
        show_in_catalog (bool):
        abbreviation (Union[Unset, None, str]):
        emoji (Union[Unset, None, str]):
        icon_url (Union[Unset, None, str]):
        inactive_description (Union[Unset, None, str]):
        installation_description (Union[Unset, None, str]):
        installation_typeform_id (Union[Unset, None, str]):
        requirements (Union[Unset, List[PluginRequirement]]):
        workspace_ui_mode_config (Union[Unset, None, PluginWorkspaceUIModeConfig]):
    """

    description: str
    display_name: str
    name: str
    show_in_catalog: bool
    abbreviation: Union[Unset, None, str] = UNSET
    emoji: Union[Unset, None, str] = UNSET
    icon_url: Union[Unset, None, str] = UNSET
    inactive_description: Union[Unset, None, str] = UNSET
    installation_description: Union[Unset, None, str] = UNSET
    installation_typeform_id: Union[Unset, None, str] = UNSET
    requirements: Union[Unset, List[PluginRequirement]] = UNSET
    workspace_ui_mode_config: Union[Unset, None, "PluginWorkspaceUIModeConfig"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        display_name = self.display_name
        name = self.name
        show_in_catalog = self.show_in_catalog
        abbreviation = self.abbreviation
        emoji = self.emoji
        icon_url = self.icon_url
        inactive_description = self.inactive_description
        installation_description = self.installation_description
        installation_typeform_id = self.installation_typeform_id
        requirements: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = []
            for requirements_item_data in self.requirements:
                requirements_item = requirements_item_data.value

                requirements.append(requirements_item)

        workspace_ui_mode_config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace_ui_mode_config, Unset):
            workspace_ui_mode_config = (
                self.workspace_ui_mode_config.to_dict() if self.workspace_ui_mode_config else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "displayName": display_name,
                "name": name,
                "showInCatalog": show_in_catalog,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if inactive_description is not UNSET:
            field_dict["inactiveDescription"] = inactive_description
        if installation_description is not UNSET:
            field_dict["installationDescription"] = installation_description
        if installation_typeform_id is not UNSET:
            field_dict["installationTypeformId"] = installation_typeform_id
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if workspace_ui_mode_config is not UNSET:
            field_dict["workspaceUIModeConfig"] = workspace_ui_mode_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plugin_workspace_ui_mode_config import PluginWorkspaceUIModeConfig

        d = src_dict.copy()
        description = d.pop("description")

        display_name = d.pop("displayName")

        name = d.pop("name")

        show_in_catalog = d.pop("showInCatalog")

        abbreviation = d.pop("abbreviation", UNSET)

        emoji = d.pop("emoji", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        inactive_description = d.pop("inactiveDescription", UNSET)

        installation_description = d.pop("installationDescription", UNSET)

        installation_typeform_id = d.pop("installationTypeformId", UNSET)

        requirements = []
        _requirements = d.pop("requirements", UNSET)
        for requirements_item_data in _requirements or []:
            requirements_item = PluginRequirement(requirements_item_data)

            requirements.append(requirements_item)

        _workspace_ui_mode_config = d.pop("workspaceUIModeConfig", UNSET)
        workspace_ui_mode_config: Union[Unset, None, PluginWorkspaceUIModeConfig]
        if _workspace_ui_mode_config is None:
            workspace_ui_mode_config = None
        elif isinstance(_workspace_ui_mode_config, Unset) or _workspace_ui_mode_config is None:
            workspace_ui_mode_config = UNSET
        else:
            workspace_ui_mode_config = PluginWorkspaceUIModeConfig.from_dict(_workspace_ui_mode_config)

        plugin_definition = cls(
            description=description,
            display_name=display_name,
            name=name,
            show_in_catalog=show_in_catalog,
            abbreviation=abbreviation,
            emoji=emoji,
            icon_url=icon_url,
            inactive_description=inactive_description,
            installation_description=installation_description,
            installation_typeform_id=installation_typeform_id,
            requirements=requirements,
            workspace_ui_mode_config=workspace_ui_mode_config,
        )

        plugin_definition.additional_properties = d
        return plugin_definition

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

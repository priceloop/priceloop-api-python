from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_action_type_0 import ApiActionType0
    from ..models.api_automation import ApiAutomation
    from ..models.api_trigger_type_0 import ApiTriggerType0
    from ..models.api_trigger_type_1 import ApiTriggerType1


T = TypeVar("T", bound="ApiWorkspaceAutomations")


@attr.s(auto_attribs=True)
class ApiWorkspaceAutomations:
    """
    Attributes:
        actions (Union[Unset, List['ApiActionType0']]):
        automations (Union[Unset, List['ApiAutomation']]):
        triggers (Union[Unset, List[Union['ApiTriggerType0', 'ApiTriggerType1']]]):
    """

    actions: Union[Unset, List["ApiActionType0"]] = UNSET
    automations: Union[Unset, List["ApiAutomation"]] = UNSET
    triggers: Union[Unset, List[Union["ApiTriggerType0", "ApiTriggerType1"]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_action_type_0 import ApiActionType0
        from ..models.api_trigger_type_0 import ApiTriggerType0

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item: Dict[str, Any]

                if isinstance(actions_item_data, ApiActionType0):
                    actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        automations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.automations, Unset):
            automations = []
            for automations_item_data in self.automations:
                automations_item = automations_item_data.to_dict()

                automations.append(automations_item)

        triggers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item: Dict[str, Any]

                if isinstance(triggers_item_data, ApiTriggerType0):
                    triggers_item = triggers_item_data.to_dict()

                else:
                    triggers_item = triggers_item_data.to_dict()

                triggers.append(triggers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if automations is not UNSET:
            field_dict["automations"] = automations
        if triggers is not UNSET:
            field_dict["triggers"] = triggers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_action_type_0 import ApiActionType0
        from ..models.api_automation import ApiAutomation
        from ..models.api_trigger_type_0 import ApiTriggerType0
        from ..models.api_trigger_type_1 import ApiTriggerType1

        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:

            def _parse_actions_item(data: object) -> "ApiActionType0":
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_action_type_0 = ApiActionType0.from_dict(data)

                return componentsschemas_api_action_type_0

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        automations = []
        _automations = d.pop("automations", UNSET)
        for automations_item_data in _automations or []:
            automations_item = ApiAutomation.from_dict(automations_item_data)

            automations.append(automations_item)

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:

            def _parse_triggers_item(data: object) -> Union["ApiTriggerType0", "ApiTriggerType1"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_trigger_type_0 = ApiTriggerType0.from_dict(data)

                    return componentsschemas_api_trigger_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_trigger_type_1 = ApiTriggerType1.from_dict(data)

                return componentsschemas_api_trigger_type_1

            triggers_item = _parse_triggers_item(triggers_item_data)

            triggers.append(triggers_item)

        api_workspace_automations = cls(
            actions=actions,
            automations=automations,
            triggers=triggers,
        )

        api_workspace_automations.additional_properties = d
        return api_workspace_automations

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

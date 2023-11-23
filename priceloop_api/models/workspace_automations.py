from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.map_type_vector_type import MapTypeVectorType
    from ..models.trigger_type_0 import TriggerType0
    from ..models.trigger_type_1 import TriggerType1


T = TypeVar("T", bound="WorkspaceAutomations")


@attr.s(auto_attribs=True)
class WorkspaceAutomations:
    """
    Attributes:
        automations (MapTypeVectorType):  Example: {'trigger-name': ['action-name']}.
        actions (Union[Unset, List['Action']]):
        triggers (Union[Unset, List[Union['TriggerType0', 'TriggerType1']]]):
    """

    automations: "MapTypeVectorType"
    actions: Union[Unset, List["Action"]] = UNSET
    triggers: Union[Unset, List[Union["TriggerType0", "TriggerType1"]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trigger_type_0 import TriggerType0

        automations = self.automations.to_dict()

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        triggers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item: Dict[str, Any]

                if isinstance(triggers_item_data, TriggerType0):
                    triggers_item = triggers_item_data.to_dict()

                else:
                    triggers_item = triggers_item_data.to_dict()

                triggers.append(triggers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automations": automations,
            }
        )
        if actions is not UNSET:
            field_dict["actions"] = actions
        if triggers is not UNSET:
            field_dict["triggers"] = triggers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action import Action
        from ..models.map_type_vector_type import MapTypeVectorType
        from ..models.trigger_type_0 import TriggerType0
        from ..models.trigger_type_1 import TriggerType1

        d = src_dict.copy()
        automations = MapTypeVectorType.from_dict(d.pop("automations"))

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = Action.from_dict(actions_item_data)

            actions.append(actions_item)

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:

            def _parse_triggers_item(data: object) -> Union["TriggerType0", "TriggerType1"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_trigger_type_0 = TriggerType0.from_dict(data)

                    return componentsschemas_trigger_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_trigger_type_1 = TriggerType1.from_dict(data)

                return componentsschemas_trigger_type_1

            triggers_item = _parse_triggers_item(triggers_item_data)

            triggers.append(triggers_item)

        workspace_automations = cls(
            automations=automations,
            actions=actions,
            triggers=triggers,
        )

        workspace_automations.additional_properties = d
        return workspace_automations

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

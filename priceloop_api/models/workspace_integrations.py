from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon import Amazon


T = TypeVar("T", bound="WorkspaceIntegrations")


@attr.s(auto_attribs=True)
class WorkspaceIntegrations:
    """
    Attributes:
        amazon (Union[Unset, Amazon]):
    """

    amazon: Union[Unset, "Amazon"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amazon, Unset):
            amazon = self.amazon.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon is not UNSET:
            field_dict["amazon"] = amazon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon import Amazon

        d = src_dict.copy()
        _amazon = d.pop("amazon", UNSET)
        amazon: Union[Unset, Amazon]
        if isinstance(_amazon, Unset) or _amazon is None:
            amazon = UNSET
        else:
            amazon = Amazon.from_dict(_amazon)

        workspace_integrations = cls(
            amazon=amazon,
        )

        workspace_integrations.additional_properties = d
        return workspace_integrations

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

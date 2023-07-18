from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confirmation_modal_description import ConfirmationModalDescription


T = TypeVar("T", bound="PublishInput")


@attr.s(auto_attribs=True)
class PublishInput:
    """
    Attributes:
        confirmation_modal (Union[Unset, ConfirmationModalDescription]):
    """

    confirmation_modal: Union[Unset, "ConfirmationModalDescription"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmation_modal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmation_modal, Unset):
            confirmation_modal = self.confirmation_modal.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmation_modal is not UNSET:
            field_dict["confirmationModal"] = confirmation_modal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confirmation_modal_description import ConfirmationModalDescription

        d = src_dict.copy()
        _confirmation_modal = d.pop("confirmationModal", UNSET)
        confirmation_modal: Union[Unset, ConfirmationModalDescription]
        if isinstance(_confirmation_modal, Unset) or _confirmation_modal is None:
            confirmation_modal = UNSET
        else:
            confirmation_modal = ConfirmationModalDescription.from_dict(_confirmation_modal)

        publish_input = cls(
            confirmation_modal=confirmation_modal,
        )

        publish_input.additional_properties = d
        return publish_input

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

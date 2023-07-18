from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmationModalDescription")


@attr.s(auto_attribs=True)
class ConfirmationModalDescription:
    """
    Attributes:
        cancel_label (Union[Unset, None, str]):
        confirmation_label (Union[Unset, None, str]):
        subtitle (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
    """

    cancel_label: Union[Unset, None, str] = UNSET
    confirmation_label: Union[Unset, None, str] = UNSET
    subtitle: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cancel_label = self.cancel_label
        confirmation_label = self.confirmation_label
        subtitle = self.subtitle
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_label is not UNSET:
            field_dict["cancelLabel"] = cancel_label
        if confirmation_label is not UNSET:
            field_dict["confirmationLabel"] = confirmation_label
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cancel_label = d.pop("cancelLabel", UNSET)

        confirmation_label = d.pop("confirmationLabel", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        title = d.pop("title", UNSET)

        confirmation_modal_description = cls(
            cancel_label=cancel_label,
            confirmation_label=confirmation_label,
            subtitle=subtitle,
            title=title,
        )

        confirmation_modal_description.additional_properties = d
        return confirmation_modal_description

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

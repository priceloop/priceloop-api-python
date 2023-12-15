from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTableAttributes")


@attr.s(auto_attribs=True)
class ApiTableAttributes:
    """
    Attributes:
        hidden (bool):
        prominent_import_your_data_button (bool):
        writable (bool):
        confirm_edits (Union[Unset, None, bool]):
        group_name (Union[Unset, None, str]):
        position (Union[Unset, None, int]):
    """

    hidden: bool
    prominent_import_your_data_button: bool
    writable: bool
    confirm_edits: Union[Unset, None, bool] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hidden = self.hidden
        prominent_import_your_data_button = self.prominent_import_your_data_button
        writable = self.writable
        confirm_edits = self.confirm_edits
        group_name = self.group_name
        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hidden": hidden,
                "prominentImportYourDataButton": prominent_import_your_data_button,
                "writable": writable,
            }
        )
        if confirm_edits is not UNSET:
            field_dict["confirmEdits"] = confirm_edits
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hidden = d.pop("hidden")

        prominent_import_your_data_button = d.pop("prominentImportYourDataButton")

        writable = d.pop("writable")

        confirm_edits = d.pop("confirmEdits", UNSET)

        group_name = d.pop("groupName", UNSET)

        position = d.pop("position", UNSET)

        api_table_attributes = cls(
            hidden=hidden,
            prominent_import_your_data_button=prominent_import_your_data_button,
            writable=writable,
            confirm_edits=confirm_edits,
            group_name=group_name,
            position=position,
        )

        api_table_attributes.additional_properties = d
        return api_table_attributes

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

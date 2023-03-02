from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Amazon")


@attr.s(auto_attribs=True)
class Amazon:
    """
    Attributes:
        refresh_token (str):
        selling_partner_id (Union[Unset, str]):
    """

    refresh_token: str
    selling_partner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh_token = self.refresh_token
        selling_partner_id = self.selling_partner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refreshToken": refresh_token,
            }
        )
        if selling_partner_id is not UNSET:
            field_dict["sellingPartnerId"] = selling_partner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh_token = d.pop("refreshToken")

        selling_partner_id = d.pop("sellingPartnerId", UNSET)

        amazon = cls(
            refresh_token=refresh_token,
            selling_partner_id=selling_partner_id,
        )

        amazon.additional_properties = d
        return amazon

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

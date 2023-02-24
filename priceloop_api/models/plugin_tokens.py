from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginTokens")


@attr.s(auto_attribs=True)
class PluginTokens:
    """
    Attributes:
        amazon_seller_refresh_token (Union[Unset, str]):
    """

    amazon_seller_refresh_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_seller_refresh_token = self.amazon_seller_refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_seller_refresh_token is not UNSET:
            field_dict["amazonSellerRefreshToken"] = amazon_seller_refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amazon_seller_refresh_token = d.pop("amazonSellerRefreshToken", UNSET)

        plugin_tokens = cls(
            amazon_seller_refresh_token=amazon_seller_refresh_token,
        )

        plugin_tokens.additional_properties = d
        return plugin_tokens

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

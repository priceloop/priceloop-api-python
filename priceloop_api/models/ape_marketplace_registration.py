import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.ape_marketplace import ApeMarketplace


T = TypeVar("T", bound="ApeMarketplaceRegistration")


@attr.s(auto_attribs=True)
class ApeMarketplaceRegistration:
    """
    Attributes:
        date (datetime.datetime):
        marketplace (ApeMarketplace):
    """

    date: datetime.datetime
    marketplace: "ApeMarketplace"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        marketplace = self.marketplace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "marketplace": marketplace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ape_marketplace import ApeMarketplace

        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        marketplace = ApeMarketplace.from_dict(d.pop("marketplace"))

        ape_marketplace_registration = cls(
            date=date,
            marketplace=marketplace,
        )

        ape_marketplace_registration.additional_properties = d
        return ape_marketplace_registration

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

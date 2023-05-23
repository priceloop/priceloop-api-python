from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ape_data_typeform import ApeDataTypeform
    from ..models.ape_marketplace import ApeMarketplace
    from ..models.map_ape_marketplace_registration import MapApeMarketplaceRegistration


T = TypeVar("T", bound="ApeData")


@attr.s(auto_attribs=True)
class ApeData:
    """
    Attributes:
        initial_marketplace (Union[Unset, ApeMarketplace]):
        registered_marketplaces (Union[Unset, MapApeMarketplaceRegistration]):
        typeform (Union[Unset, ApeDataTypeform]):
    """

    initial_marketplace: Union[Unset, "ApeMarketplace"] = UNSET
    registered_marketplaces: Union[Unset, "MapApeMarketplaceRegistration"] = UNSET
    typeform: Union[Unset, "ApeDataTypeform"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        initial_marketplace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initial_marketplace, Unset):
            initial_marketplace = self.initial_marketplace.to_dict()

        registered_marketplaces: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_marketplaces, Unset):
            registered_marketplaces = self.registered_marketplaces.to_dict()

        typeform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.typeform, Unset):
            typeform = self.typeform.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_marketplace is not UNSET:
            field_dict["initialMarketplace"] = initial_marketplace
        if registered_marketplaces is not UNSET:
            field_dict["registeredMarketplaces"] = registered_marketplaces
        if typeform is not UNSET:
            field_dict["typeform"] = typeform

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ape_data_typeform import ApeDataTypeform
        from ..models.ape_marketplace import ApeMarketplace
        from ..models.map_ape_marketplace_registration import MapApeMarketplaceRegistration

        d = src_dict.copy()
        _initial_marketplace = d.pop("initialMarketplace", UNSET)
        initial_marketplace: Union[Unset, ApeMarketplace]
        if isinstance(_initial_marketplace, Unset) or _initial_marketplace is None:
            initial_marketplace = UNSET
        else:
            initial_marketplace = ApeMarketplace.from_dict(_initial_marketplace)

        _registered_marketplaces = d.pop("registeredMarketplaces", UNSET)
        registered_marketplaces: Union[Unset, MapApeMarketplaceRegistration]
        if isinstance(_registered_marketplaces, Unset) or _registered_marketplaces is None:
            registered_marketplaces = UNSET
        else:
            registered_marketplaces = MapApeMarketplaceRegistration.from_dict(_registered_marketplaces)

        _typeform = d.pop("typeform", UNSET)
        typeform: Union[Unset, ApeDataTypeform]
        if isinstance(_typeform, Unset) or _typeform is None:
            typeform = UNSET
        else:
            typeform = ApeDataTypeform.from_dict(_typeform)

        ape_data = cls(
            initial_marketplace=initial_marketplace,
            registered_marketplaces=registered_marketplaces,
            typeform=typeform,
        )

        ape_data.additional_properties = d
        return ape_data

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

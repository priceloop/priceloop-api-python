from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate


T = TypeVar("T", bound="ApiColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiColumnAttributesUpdate:
    """
    Attributes:
        boolean_column_attributes (Union[Unset, ApiBooleanColumnAttributesUpdate]):
        description (Union[Unset, str]):
        is_gui_locked (Union[Unset, bool]):
        is_hidden (Union[Unset, bool]):
    """

    boolean_column_attributes: Union[Unset, "ApiBooleanColumnAttributesUpdate"] = UNSET
    description: Union[Unset, str] = UNSET
    is_gui_locked: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boolean_column_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boolean_column_attributes, Unset):
            boolean_column_attributes = self.boolean_column_attributes.to_dict()

        description = self.description
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boolean_column_attributes is not UNSET:
            field_dict["booleanColumnAttributes"] = boolean_column_attributes
        if description is not UNSET:
            field_dict["description"] = description
        if is_gui_locked is not UNSET:
            field_dict["isGuiLocked"] = is_gui_locked
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate

        d = src_dict.copy()
        _boolean_column_attributes = d.pop("booleanColumnAttributes", UNSET)
        boolean_column_attributes: Union[Unset, ApiBooleanColumnAttributesUpdate]
        if isinstance(_boolean_column_attributes, Unset):
            boolean_column_attributes = UNSET
        else:
            boolean_column_attributes = ApiBooleanColumnAttributesUpdate.from_dict(_boolean_column_attributes)

        description = d.pop("description", UNSET)

        is_gui_locked = d.pop("isGuiLocked", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        api_column_attributes_update = cls(
            boolean_column_attributes=boolean_column_attributes,
            description=description,
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
        )

        api_column_attributes_update.additional_properties = d
        return api_column_attributes_update

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

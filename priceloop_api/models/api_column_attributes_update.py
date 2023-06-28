from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_background_color import ColumnBackgroundColor
from ..models.column_computation_mode import ColumnComputationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate
    from ..models.api_string_column_attributes_update import ApiStringColumnAttributesUpdate


T = TypeVar("T", bound="ApiColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiColumnAttributesUpdate:
    """
    Attributes:
        background_color (Union[Unset, ColumnBackgroundColor]):
        boolean_column_attributes (Union[Unset, ApiBooleanColumnAttributesUpdate]):
        computation_mode (Union[Unset, ColumnComputationMode]):
        description (Union[Unset, None, str]):
        is_gui_locked (Union[Unset, None, bool]):
        is_hidden (Union[Unset, None, bool]):
        string_column_attributes (Union[Unset, ApiStringColumnAttributesUpdate]):
    """

    background_color: Union[Unset, ColumnBackgroundColor] = UNSET
    boolean_column_attributes: Union[Unset, "ApiBooleanColumnAttributesUpdate"] = UNSET
    computation_mode: Union[Unset, ColumnComputationMode] = UNSET
    description: Union[Unset, None, str] = UNSET
    is_gui_locked: Union[Unset, None, bool] = UNSET
    is_hidden: Union[Unset, None, bool] = UNSET
    string_column_attributes: Union[Unset, "ApiStringColumnAttributesUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        background_color: Union[Unset, str] = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.value

        boolean_column_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boolean_column_attributes, Unset):
            boolean_column_attributes = self.boolean_column_attributes.to_dict()

        computation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.computation_mode, Unset):
            computation_mode = self.computation_mode.value

        description = self.description
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        string_column_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.string_column_attributes, Unset):
            string_column_attributes = self.string_column_attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if boolean_column_attributes is not UNSET:
            field_dict["booleanColumnAttributes"] = boolean_column_attributes
        if computation_mode is not UNSET:
            field_dict["computationMode"] = computation_mode
        if description is not UNSET:
            field_dict["description"] = description
        if is_gui_locked is not UNSET:
            field_dict["isGuiLocked"] = is_gui_locked
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if string_column_attributes is not UNSET:
            field_dict["stringColumnAttributes"] = string_column_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate
        from ..models.api_string_column_attributes_update import ApiStringColumnAttributesUpdate

        d = src_dict.copy()
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: Union[Unset, ColumnBackgroundColor]
        if isinstance(_background_color, Unset) or _background_color is None:
            background_color = UNSET
        else:
            background_color = ColumnBackgroundColor(_background_color)

        _boolean_column_attributes = d.pop("booleanColumnAttributes", UNSET)
        boolean_column_attributes: Union[Unset, ApiBooleanColumnAttributesUpdate]
        if isinstance(_boolean_column_attributes, Unset) or _boolean_column_attributes is None:
            boolean_column_attributes = UNSET
        else:
            boolean_column_attributes = ApiBooleanColumnAttributesUpdate.from_dict(_boolean_column_attributes)

        _computation_mode = d.pop("computationMode", UNSET)
        computation_mode: Union[Unset, ColumnComputationMode]
        if isinstance(_computation_mode, Unset) or _computation_mode is None:
            computation_mode = UNSET
        else:
            computation_mode = ColumnComputationMode(_computation_mode)

        description = d.pop("description", UNSET)

        is_gui_locked = d.pop("isGuiLocked", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        _string_column_attributes = d.pop("stringColumnAttributes", UNSET)
        string_column_attributes: Union[Unset, ApiStringColumnAttributesUpdate]
        if isinstance(_string_column_attributes, Unset) or _string_column_attributes is None:
            string_column_attributes = UNSET
        else:
            string_column_attributes = ApiStringColumnAttributesUpdate.from_dict(_string_column_attributes)

        api_column_attributes_update = cls(
            background_color=background_color,
            boolean_column_attributes=boolean_column_attributes,
            computation_mode=computation_mode,
            description=description,
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            string_column_attributes=string_column_attributes,
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

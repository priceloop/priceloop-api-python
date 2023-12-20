from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_background_color import ColumnBackgroundColor
from ..models.column_group_color import ColumnGroupColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate
    from ..models.api_number_column_attributes_update import ApiNumberColumnAttributesUpdate
    from ..models.api_string_column_attributes_update import ApiStringColumnAttributesUpdate


T = TypeVar("T", bound="ApiColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiColumnAttributesUpdate:
    """
    Attributes:
        background_color (Union[Unset, None, ColumnBackgroundColor]):
        boolean_column_attributes (Union[Unset, None, ApiBooleanColumnAttributesUpdate]):
        choice_name (Union[Unset, None, str]):
        computation_mode (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        group_color (Union[Unset, None, ColumnGroupColor]):
        group_name (Union[Unset, None, str]):
        is_gui_locked (Union[Unset, None, bool]):
        is_hidden (Union[Unset, None, bool]):
        number_column_attributes (Union[Unset, None, ApiNumberColumnAttributesUpdate]):
        string_column_attributes (Union[Unset, None, ApiStringColumnAttributesUpdate]):
    """

    background_color: Union[Unset, None, ColumnBackgroundColor] = UNSET
    boolean_column_attributes: Union[Unset, None, "ApiBooleanColumnAttributesUpdate"] = UNSET
    choice_name: Union[Unset, None, str] = UNSET
    computation_mode: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    group_color: Union[Unset, None, ColumnGroupColor] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    is_gui_locked: Union[Unset, None, bool] = UNSET
    is_hidden: Union[Unset, None, bool] = UNSET
    number_column_attributes: Union[Unset, None, "ApiNumberColumnAttributesUpdate"] = UNSET
    string_column_attributes: Union[Unset, None, "ApiStringColumnAttributesUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        background_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.value if self.background_color else None

        boolean_column_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.boolean_column_attributes, Unset):
            boolean_column_attributes = (
                self.boolean_column_attributes.to_dict() if self.boolean_column_attributes else None
            )

        choice_name = self.choice_name
        computation_mode = self.computation_mode
        description = self.description
        group_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.group_color, Unset):
            group_color = self.group_color.value if self.group_color else None

        group_name = self.group_name
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        number_column_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.number_column_attributes, Unset):
            number_column_attributes = (
                self.number_column_attributes.to_dict() if self.number_column_attributes else None
            )

        string_column_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.string_column_attributes, Unset):
            string_column_attributes = (
                self.string_column_attributes.to_dict() if self.string_column_attributes else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if boolean_column_attributes is not UNSET:
            field_dict["booleanColumnAttributes"] = boolean_column_attributes
        if choice_name is not UNSET:
            field_dict["choiceName"] = choice_name
        if computation_mode is not UNSET:
            field_dict["computationMode"] = computation_mode
        if description is not UNSET:
            field_dict["description"] = description
        if group_color is not UNSET:
            field_dict["groupColor"] = group_color
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if is_gui_locked is not UNSET:
            field_dict["isGuiLocked"] = is_gui_locked
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if number_column_attributes is not UNSET:
            field_dict["numberColumnAttributes"] = number_column_attributes
        if string_column_attributes is not UNSET:
            field_dict["stringColumnAttributes"] = string_column_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_boolean_column_attributes_update import ApiBooleanColumnAttributesUpdate
        from ..models.api_number_column_attributes_update import ApiNumberColumnAttributesUpdate
        from ..models.api_string_column_attributes_update import ApiStringColumnAttributesUpdate

        d = src_dict.copy()
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: Union[Unset, None, ColumnBackgroundColor]
        if _background_color is None:
            background_color = None
        elif isinstance(_background_color, Unset) or _background_color is None:
            background_color = UNSET
        else:
            background_color = ColumnBackgroundColor(_background_color)

        _boolean_column_attributes = d.pop("booleanColumnAttributes", UNSET)
        boolean_column_attributes: Union[Unset, None, ApiBooleanColumnAttributesUpdate]
        if _boolean_column_attributes is None:
            boolean_column_attributes = None
        elif isinstance(_boolean_column_attributes, Unset) or _boolean_column_attributes is None:
            boolean_column_attributes = UNSET
        else:
            boolean_column_attributes = ApiBooleanColumnAttributesUpdate.from_dict(_boolean_column_attributes)

        choice_name = d.pop("choiceName", UNSET)

        computation_mode = d.pop("computationMode", UNSET)

        description = d.pop("description", UNSET)

        _group_color = d.pop("groupColor", UNSET)
        group_color: Union[Unset, None, ColumnGroupColor]
        if _group_color is None:
            group_color = None
        elif isinstance(_group_color, Unset) or _group_color is None:
            group_color = UNSET
        else:
            group_color = ColumnGroupColor(_group_color)

        group_name = d.pop("groupName", UNSET)

        is_gui_locked = d.pop("isGuiLocked", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        _number_column_attributes = d.pop("numberColumnAttributes", UNSET)
        number_column_attributes: Union[Unset, None, ApiNumberColumnAttributesUpdate]
        if _number_column_attributes is None:
            number_column_attributes = None
        elif isinstance(_number_column_attributes, Unset) or _number_column_attributes is None:
            number_column_attributes = UNSET
        else:
            number_column_attributes = ApiNumberColumnAttributesUpdate.from_dict(_number_column_attributes)

        _string_column_attributes = d.pop("stringColumnAttributes", UNSET)
        string_column_attributes: Union[Unset, None, ApiStringColumnAttributesUpdate]
        if _string_column_attributes is None:
            string_column_attributes = None
        elif isinstance(_string_column_attributes, Unset) or _string_column_attributes is None:
            string_column_attributes = UNSET
        else:
            string_column_attributes = ApiStringColumnAttributesUpdate.from_dict(_string_column_attributes)

        api_column_attributes_update = cls(
            background_color=background_color,
            boolean_column_attributes=boolean_column_attributes,
            choice_name=choice_name,
            computation_mode=computation_mode,
            description=description,
            group_color=group_color,
            group_name=group_name,
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            number_column_attributes=number_column_attributes,
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

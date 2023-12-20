from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_background_color import ColumnBackgroundColor
from ..models.column_group_color import ColumnGroupColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_boolean_column_attributes import ApiBooleanColumnAttributes
    from ..models.api_number_column_attributes import ApiNumberColumnAttributes
    from ..models.api_string_column_attributes import ApiStringColumnAttributes


T = TypeVar("T", bound="ApiColumnAttributes")


@attr.s(auto_attribs=True)
class ApiColumnAttributes:
    """
    Attributes:
        boolean_column_attributes (ApiBooleanColumnAttributes):
        computation_mode (str):
        is_gui_locked (bool):
        is_hidden (bool):
        number_column_attributes (ApiNumberColumnAttributes):
        string_column_attributes (ApiStringColumnAttributes):
        background_color (Union[Unset, None, ColumnBackgroundColor]):
        description (Union[Unset, None, str]):
        group_color (Union[Unset, None, ColumnGroupColor]):
        group_name (Union[Unset, None, str]):
    """

    boolean_column_attributes: "ApiBooleanColumnAttributes"
    computation_mode: str
    is_gui_locked: bool
    is_hidden: bool
    number_column_attributes: "ApiNumberColumnAttributes"
    string_column_attributes: "ApiStringColumnAttributes"
    background_color: Union[Unset, None, ColumnBackgroundColor] = UNSET
    description: Union[Unset, None, str] = UNSET
    group_color: Union[Unset, None, ColumnGroupColor] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boolean_column_attributes = self.boolean_column_attributes.to_dict()

        computation_mode = self.computation_mode
        is_gui_locked = self.is_gui_locked
        is_hidden = self.is_hidden
        number_column_attributes = self.number_column_attributes.to_dict()

        string_column_attributes = self.string_column_attributes.to_dict()

        background_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.value if self.background_color else None

        description = self.description
        group_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.group_color, Unset):
            group_color = self.group_color.value if self.group_color else None

        group_name = self.group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "booleanColumnAttributes": boolean_column_attributes,
                "computationMode": computation_mode,
                "isGuiLocked": is_gui_locked,
                "isHidden": is_hidden,
                "numberColumnAttributes": number_column_attributes,
                "stringColumnAttributes": string_column_attributes,
            }
        )
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if description is not UNSET:
            field_dict["description"] = description
        if group_color is not UNSET:
            field_dict["groupColor"] = group_color
        if group_name is not UNSET:
            field_dict["groupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_boolean_column_attributes import ApiBooleanColumnAttributes
        from ..models.api_number_column_attributes import ApiNumberColumnAttributes
        from ..models.api_string_column_attributes import ApiStringColumnAttributes

        d = src_dict.copy()
        boolean_column_attributes = ApiBooleanColumnAttributes.from_dict(d.pop("booleanColumnAttributes"))

        computation_mode = d.pop("computationMode")

        is_gui_locked = d.pop("isGuiLocked")

        is_hidden = d.pop("isHidden")

        number_column_attributes = ApiNumberColumnAttributes.from_dict(d.pop("numberColumnAttributes"))

        string_column_attributes = ApiStringColumnAttributes.from_dict(d.pop("stringColumnAttributes"))

        _background_color = d.pop("backgroundColor", UNSET)
        background_color: Union[Unset, None, ColumnBackgroundColor]
        if _background_color is None:
            background_color = None
        elif isinstance(_background_color, Unset) or _background_color is None:
            background_color = UNSET
        else:
            background_color = ColumnBackgroundColor(_background_color)

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

        api_column_attributes = cls(
            boolean_column_attributes=boolean_column_attributes,
            computation_mode=computation_mode,
            is_gui_locked=is_gui_locked,
            is_hidden=is_hidden,
            number_column_attributes=number_column_attributes,
            string_column_attributes=string_column_attributes,
            background_color=background_color,
            description=description,
            group_color=group_color,
            group_name=group_name,
        )

        api_column_attributes.additional_properties = d
        return api_column_attributes

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

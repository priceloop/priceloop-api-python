from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.number_display_style import NumberDisplayStyle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full import Full
    from ..models.truncated import Truncated


T = TypeVar("T", bound="ApiNumberColumnAttributesUpdate")


@attr.s(auto_attribs=True)
class ApiNumberColumnAttributesUpdate:
    """
    Attributes:
        display_style (Union[Unset, NumberDisplayStyle]):
        precision (Union['Full', 'Truncated', Unset]):
        unit (Union[Unset, None, str]):
    """

    display_style: Union[Unset, NumberDisplayStyle] = UNSET
    precision: Union["Full", "Truncated", Unset] = UNSET
    unit: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.full import Full

        display_style: Union[Unset, str] = UNSET
        if not isinstance(self.display_style, Unset):
            display_style = self.display_style.value

        precision: Union[Dict[str, Any], Unset]
        if isinstance(self.precision, Unset):
            precision = UNSET

        elif isinstance(self.precision, Full):
            precision = self.precision.to_dict()

        else:
            precision = self.precision.to_dict()

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_style is not UNSET:
            field_dict["displayStyle"] = display_style
        if precision is not UNSET:
            field_dict["precision"] = precision
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full import Full
        from ..models.truncated import Truncated

        d = src_dict.copy()
        _display_style = d.pop("displayStyle", UNSET)
        display_style: Union[Unset, NumberDisplayStyle]
        if isinstance(_display_style, Unset) or _display_style is None:
            display_style = UNSET
        else:
            display_style = NumberDisplayStyle(_display_style)

        def _parse_precision(data: object) -> Union["Full", "Truncated", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_number_precision_type_0 = Full.from_dict(data)

                return componentsschemas_number_precision_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_number_precision_type_1 = Truncated.from_dict(data)

            return componentsschemas_number_precision_type_1

        precision = _parse_precision(d.pop("precision", UNSET))

        unit = d.pop("unit", UNSET)

        api_number_column_attributes_update = cls(
            display_style=display_style,
            precision=precision,
            unit=unit,
        )

        api_number_column_attributes_update.additional_properties = d
        return api_number_column_attributes_update

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.number_display_style import NumberDisplayStyle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full import Full
    from ..models.truncated import Truncated


T = TypeVar("T", bound="ApiNumberColumnAttributes")


@attr.s(auto_attribs=True)
class ApiNumberColumnAttributes:
    """
    Attributes:
        display_style (NumberDisplayStyle):
        precision (Union['Full', 'Truncated']):
        unit (Union[Unset, None, str]):
    """

    display_style: NumberDisplayStyle
    precision: Union["Full", "Truncated"]
    unit: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.full import Full

        display_style = self.display_style.value

        precision: Dict[str, Any]

        if isinstance(self.precision, Full):
            precision = self.precision.to_dict()

        else:
            precision = self.precision.to_dict()

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayStyle": display_style,
                "precision": precision,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full import Full
        from ..models.truncated import Truncated

        d = src_dict.copy()
        display_style = NumberDisplayStyle(d.pop("displayStyle"))

        def _parse_precision(data: object) -> Union["Full", "Truncated"]:
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

        precision = _parse_precision(d.pop("precision"))

        unit = d.pop("unit", UNSET)

        api_number_column_attributes = cls(
            display_style=display_style,
            precision=precision,
            unit=unit,
        )

        api_number_column_attributes.additional_properties = d
        return api_number_column_attributes

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

from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiColumnWithNullableValues")


@attr.s(auto_attribs=True)
class ApiColumnWithNullableValues:
    """
    Attributes:
        name (str):
        values (Union[Unset, List[Optional[str]]]):
    """

    name: str
    values: Union[Unset, List[Optional[str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        values: Union[Unset, List[Optional[str]]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        values = cast(List[Optional[str]], d.pop("values", UNSET))

        api_column_with_nullable_values = cls(
            name=name,
            values=values,
        )

        api_column_with_nullable_values.additional_properties = d
        return api_column_with_nullable_values

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_definition import ChoiceDefinition


T = TypeVar("T", bound="Choice")


@attr.s(auto_attribs=True)
class Choice:
    """
    Attributes:
        name (str):
        values (Union[Unset, List['ChoiceDefinition']]):
    """

    name: str
    values: Union[Unset, List["ChoiceDefinition"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

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
        from ..models.choice_definition import ChoiceDefinition

        d = src_dict.copy()
        name = d.pop("name")

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = ChoiceDefinition.from_dict(values_item_data)

            values.append(values_item)

        choice = cls(
            name=name,
            values=values,
        )

        choice.additional_properties = d
        return choice

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

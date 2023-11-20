from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_on_conflict import ApiOnConflict
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column_with_nullable_values import ApiColumnWithNullableValues
    from ..models.api_column_with_values import ApiColumnWithValues


T = TypeVar("T", bound="Insert")


@attr.s(auto_attribs=True)
class Insert:
    """
    Attributes:
        on_conflict (ApiOnConflict):
        op (str):
        data_columns (Union[Unset, List['ApiColumnWithNullableValues']]):
        match_columns (Union[Unset, List['ApiColumnWithValues']]):
    """

    on_conflict: ApiOnConflict
    op: str
    data_columns: Union[Unset, List["ApiColumnWithNullableValues"]] = UNSET
    match_columns: Union[Unset, List["ApiColumnWithValues"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on_conflict = self.on_conflict.value

        op = self.op
        data_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_columns, Unset):
            data_columns = []
            for data_columns_item_data in self.data_columns:
                data_columns_item = data_columns_item_data.to_dict()

                data_columns.append(data_columns_item)

        match_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.match_columns, Unset):
            match_columns = []
            for match_columns_item_data in self.match_columns:
                match_columns_item = match_columns_item_data.to_dict()

                match_columns.append(match_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "onConflict": on_conflict,
                "op": op,
            }
        )
        if data_columns is not UNSET:
            field_dict["dataColumns"] = data_columns
        if match_columns is not UNSET:
            field_dict["matchColumns"] = match_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_column_with_nullable_values import ApiColumnWithNullableValues
        from ..models.api_column_with_values import ApiColumnWithValues

        d = src_dict.copy()
        on_conflict = ApiOnConflict(d.pop("onConflict"))

        op = d.pop("op")

        data_columns = []
        _data_columns = d.pop("dataColumns", UNSET)
        for data_columns_item_data in _data_columns or []:
            data_columns_item = ApiColumnWithNullableValues.from_dict(data_columns_item_data)

            data_columns.append(data_columns_item)

        match_columns = []
        _match_columns = d.pop("matchColumns", UNSET)
        for match_columns_item_data in _match_columns or []:
            match_columns_item = ApiColumnWithValues.from_dict(match_columns_item_data)

            match_columns.append(match_columns_item)

        insert = cls(
            on_conflict=on_conflict,
            op=op,
            data_columns=data_columns,
            match_columns=match_columns,
        )

        insert.additional_properties = d
        return insert

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

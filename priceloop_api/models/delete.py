from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_delete_mode import ApiDeleteMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_column_with_values import ApiColumnWithValues


T = TypeVar("T", bound="Delete")


@attr.s(auto_attribs=True)
class Delete:
    """
    Attributes:
        delete_mode (ApiDeleteMode):
        op (str):
        match_columns (Union[Unset, List['ApiColumnWithValues']]):
    """

    delete_mode: ApiDeleteMode
    op: str
    match_columns: Union[Unset, List["ApiColumnWithValues"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete_mode = self.delete_mode.value

        op = self.op
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
                "deleteMode": delete_mode,
                "op": op,
            }
        )
        if match_columns is not UNSET:
            field_dict["matchColumns"] = match_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_column_with_values import ApiColumnWithValues

        d = src_dict.copy()
        delete_mode = ApiDeleteMode(d.pop("deleteMode"))

        op = d.pop("op")

        match_columns = []
        _match_columns = d.pop("matchColumns", UNSET)
        for match_columns_item_data in _match_columns or []:
            match_columns_item = ApiColumnWithValues.from_dict(match_columns_item_data)

            match_columns.append(match_columns_item)

        delete = cls(
            delete_mode=delete_mode,
            op=op,
            match_columns=match_columns,
        )

        delete.additional_properties = d
        return delete

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

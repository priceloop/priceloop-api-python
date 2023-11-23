import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordChanged")


@attr.s(auto_attribs=True)
class RecordChanged:
    """
    Attributes:
        current_modification_timestamp (datetime.datetime):
        name (str):  Example: trigger-name.
        table_name (str):  Example: table-name.
        condition (Union[Unset, None, str]):  Example: {ColumnA} == "foo".
        watch_columns (Union[Unset, List[str]]):
    """

    current_modification_timestamp: datetime.datetime
    name: str
    table_name: str
    condition: Union[Unset, None, str] = UNSET
    watch_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_modification_timestamp = self.current_modification_timestamp.isoformat()

        name = self.name
        table_name = self.table_name
        condition = self.condition
        watch_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.watch_columns, Unset):
            watch_columns = self.watch_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentModificationTimestamp": current_modification_timestamp,
                "name": name,
                "tableName": table_name,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if watch_columns is not UNSET:
            field_dict["watchColumns"] = watch_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_modification_timestamp = isoparse(d.pop("currentModificationTimestamp"))

        name = d.pop("name")

        table_name = d.pop("tableName")

        condition = d.pop("condition", UNSET)

        watch_columns = cast(List[str], d.pop("watchColumns", UNSET))

        record_changed = cls(
            current_modification_timestamp=current_modification_timestamp,
            name=name,
            table_name=table_name,
            condition=condition,
            watch_columns=watch_columns,
        )

        record_changed.additional_properties = d
        return record_changed

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

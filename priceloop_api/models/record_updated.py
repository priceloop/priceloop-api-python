import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_watch_columns_type_0 import ApiWatchColumnsType0
    from ..models.api_watch_columns_type_1 import ApiWatchColumnsType1


T = TypeVar("T", bound="RecordUpdated")


@attr.s(auto_attribs=True)
class RecordUpdated:
    """
    Attributes:
        name (str):  Example: trigger-name.
        table_name (str):  Example: table-name.
        watch_columns (Union['ApiWatchColumnsType0', 'ApiWatchColumnsType1']):
        condition (Union[Unset, None, str]):  Example: {ColumnA} == "foo".
        current_modification_timestamp (Union[Unset, None, datetime.datetime]):
    """

    name: str
    table_name: str
    watch_columns: Union["ApiWatchColumnsType0", "ApiWatchColumnsType1"]
    condition: Union[Unset, None, str] = UNSET
    current_modification_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_watch_columns_type_0 import ApiWatchColumnsType0

        name = self.name
        table_name = self.table_name
        watch_columns: Dict[str, Any]

        if isinstance(self.watch_columns, ApiWatchColumnsType0):
            watch_columns = self.watch_columns.to_dict()

        else:
            watch_columns = self.watch_columns.to_dict()

        condition = self.condition
        current_modification_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.current_modification_timestamp, Unset):
            current_modification_timestamp = (
                self.current_modification_timestamp.isoformat() if self.current_modification_timestamp else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "tableName": table_name,
                "watchColumns": watch_columns,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if current_modification_timestamp is not UNSET:
            field_dict["currentModificationTimestamp"] = current_modification_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_watch_columns_type_0 import ApiWatchColumnsType0
        from ..models.api_watch_columns_type_1 import ApiWatchColumnsType1

        d = src_dict.copy()
        name = d.pop("name")

        table_name = d.pop("tableName")

        def _parse_watch_columns(data: object) -> Union["ApiWatchColumnsType0", "ApiWatchColumnsType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_watch_columns_type_0 = ApiWatchColumnsType0.from_dict(data)

                return componentsschemas_api_watch_columns_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_watch_columns_type_1 = ApiWatchColumnsType1.from_dict(data)

            return componentsschemas_api_watch_columns_type_1

        watch_columns = _parse_watch_columns(d.pop("watchColumns"))

        condition = d.pop("condition", UNSET)

        _current_modification_timestamp = d.pop("currentModificationTimestamp", UNSET)
        current_modification_timestamp: Union[Unset, None, datetime.datetime]
        if _current_modification_timestamp is None:
            current_modification_timestamp = None
        elif isinstance(_current_modification_timestamp, Unset) or _current_modification_timestamp is None:
            current_modification_timestamp = UNSET
        else:
            current_modification_timestamp = isoparse(_current_modification_timestamp)

        record_updated = cls(
            name=name,
            table_name=table_name,
            watch_columns=watch_columns,
            condition=condition,
            current_modification_timestamp=current_modification_timestamp,
        )

        record_updated.additional_properties = d
        return record_updated

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

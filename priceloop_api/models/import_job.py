import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.table_import_mode import TableImportMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_key import S3Key


T = TypeVar("T", bound="ImportJob")


@attr.s(auto_attribs=True)
class ImportJob:
    """
    Attributes:
        created_at (datetime.datetime):
        csv_separator (str):
        id (int):
        s_3_key (S3Key):
        table_import_mode (TableImportMode):  Default: TableImportMode.NEW.
        table_name (str):  Example: table-name.
        finished_at (Union[Unset, None, datetime.datetime]):
        is_successful (Union[Unset, None, bool]):
        message (Union[Unset, None, str]):
        started_at (Union[Unset, None, datetime.datetime]):
    """

    created_at: datetime.datetime
    csv_separator: str
    id: int
    s_3_key: "S3Key"
    table_name: str
    table_import_mode: TableImportMode = TableImportMode.NEW
    finished_at: Union[Unset, None, datetime.datetime] = UNSET
    is_successful: Union[Unset, None, bool] = UNSET
    message: Union[Unset, None, str] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        csv_separator = self.csv_separator
        id = self.id
        s_3_key = self.s_3_key.to_dict()

        table_import_mode = self.table_import_mode.value

        table_name = self.table_name
        finished_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat() if self.finished_at else None

        is_successful = self.is_successful
        message = self.message
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "csvSeparator": csv_separator,
                "id": id,
                "s3Key": s_3_key,
                "tableImportMode": table_import_mode,
                "tableName": table_name,
            }
        )
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if is_successful is not UNSET:
            field_dict["isSuccessful"] = is_successful
        if message is not UNSET:
            field_dict["message"] = message
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.s3_key import S3Key

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        csv_separator = d.pop("csvSeparator")

        id = d.pop("id")

        s_3_key = S3Key.from_dict(d.pop("s3Key"))

        table_import_mode = TableImportMode(d.pop("tableImportMode"))

        table_name = d.pop("tableName")

        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: Union[Unset, None, datetime.datetime]
        if _finished_at is None:
            finished_at = None
        elif isinstance(_finished_at, Unset) or _finished_at is None:
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        is_successful = d.pop("isSuccessful", UNSET)

        message = d.pop("message", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset) or _started_at is None:
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        import_job = cls(
            created_at=created_at,
            csv_separator=csv_separator,
            id=id,
            s_3_key=s_3_key,
            table_import_mode=table_import_mode,
            table_name=table_name,
            finished_at=finished_at,
            is_successful=is_successful,
            message=message,
            started_at=started_at,
        )

        import_job.additional_properties = d
        return import_job

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

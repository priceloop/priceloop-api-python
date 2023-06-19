import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.s3_key import S3Key


T = TypeVar("T", bound="ExportJob")


@attr.s(auto_attribs=True)
class ExportJob:
    """
    Attributes:
        available_until (datetime.datetime):
        created_at (datetime.datetime):
        id (int):
        s_3_key (S3Key):
        table_name (str):  Example: table-name.
    """

    available_until: datetime.datetime
    created_at: datetime.datetime
    id: int
    s_3_key: "S3Key"
    table_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_until = self.available_until.isoformat()

        created_at = self.created_at.isoformat()

        id = self.id
        s_3_key = self.s_3_key.to_dict()

        table_name = self.table_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableUntil": available_until,
                "createdAt": created_at,
                "id": id,
                "s3Key": s_3_key,
                "tableName": table_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.s3_key import S3Key

        d = src_dict.copy()
        available_until = isoparse(d.pop("availableUntil"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        s_3_key = S3Key.from_dict(d.pop("s3Key"))

        table_name = d.pop("tableName")

        export_job = cls(
            available_until=available_until,
            created_at=created_at,
            id=id,
            s_3_key=s_3_key,
            table_name=table_name,
        )

        export_job.additional_properties = d
        return export_job

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

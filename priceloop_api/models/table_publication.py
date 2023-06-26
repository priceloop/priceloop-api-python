import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="TablePublication")


@attr.s(auto_attribs=True)
class TablePublication:
    """
    Attributes:
        created_at (datetime.datetime):
        export_job_id (int):
        id (int):
    """

    created_at: datetime.datetime
    export_job_id: int
    id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        export_job_id = self.export_job_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "exportJobId": export_job_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        export_job_id = d.pop("exportJobId")

        id = d.pop("id")

        table_publication = cls(
            created_at=created_at,
            export_job_id=export_job_id,
            id=id,
        )

        table_publication.additional_properties = d
        return table_publication

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

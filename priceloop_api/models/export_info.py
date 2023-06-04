from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.export_job import ExportJob


T = TypeVar("T", bound="ExportInfo")


@attr.s(auto_attribs=True)
class ExportInfo:
    """
    Attributes:
        download_url (str):
        expires_in_seconds (int):
        export_job (ExportJob):
    """

    download_url: str
    expires_in_seconds: int
    export_job: "ExportJob"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        download_url = self.download_url
        expires_in_seconds = self.expires_in_seconds
        export_job = self.export_job.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downloadUrl": download_url,
                "expiresInSeconds": expires_in_seconds,
                "exportJob": export_job,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.export_job import ExportJob

        d = src_dict.copy()
        download_url = d.pop("downloadUrl")

        expires_in_seconds = d.pop("expiresInSeconds")

        export_job = ExportJob.from_dict(d.pop("exportJob"))

        export_info = cls(
            download_url=download_url,
            expires_in_seconds=expires_in_seconds,
            export_job=export_job,
        )

        export_info.additional_properties = d
        return export_info

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

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ImportJobResponse")


@attr.s(auto_attribs=True)
class ImportJobResponse:
    """
    Attributes:
        import_job_id (int):
        info_message (str):
        put_url (str):
    """

    import_job_id: int
    info_message: str
    put_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_job_id = self.import_job_id
        info_message = self.info_message
        put_url = self.put_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importJobId": import_job_id,
                "infoMessage": info_message,
                "putUrl": put_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        import_job_id = d.pop("importJobId")

        info_message = d.pop("infoMessage")

        put_url = d.pop("putUrl")

        import_job_response = cls(
            import_job_id=import_job_id,
            info_message=info_message,
            put_url=put_url,
        )

        import_job_response.additional_properties = d
        return import_job_response

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

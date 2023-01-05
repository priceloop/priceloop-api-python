from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PresignedUrl")


@attr.s(auto_attribs=True)
class PresignedUrl:
    """
    Attributes:
        description (str):
        put_url (str):
    """

    description: str
    put_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        put_url = self.put_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "putUrl": put_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        put_url = d.pop("putUrl")

        presigned_url = cls(
            description=description,
            put_url=put_url,
        )

        presigned_url.additional_properties = d
        return presigned_url

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

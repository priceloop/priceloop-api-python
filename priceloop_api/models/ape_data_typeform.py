from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApeDataTypeform")


@attr.s(auto_attribs=True)
class ApeDataTypeform:
    """
    Attributes:
        embed_id (str):
        form_id (str):
        response_id (str):
    """

    embed_id: str
    form_id: str
    response_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        embed_id = self.embed_id
        form_id = self.form_id
        response_id = self.response_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedId": embed_id,
                "formId": form_id,
                "responseId": response_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        embed_id = d.pop("embedId")

        form_id = d.pop("formId")

        response_id = d.pop("responseId")

        ape_data_typeform = cls(
            embed_id=embed_id,
            form_id=form_id,
            response_id=response_id,
        )

        ape_data_typeform.additional_properties = d
        return ape_data_typeform

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

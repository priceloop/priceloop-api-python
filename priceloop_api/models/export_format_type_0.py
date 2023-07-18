from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.csv import CSV


T = TypeVar("T", bound="ExportFormatType0")


@attr.s(auto_attribs=True)
class ExportFormatType0:
    """
    Attributes:
        csv (CSV):
    """

    csv: "CSV"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        csv = self.csv.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CSV": csv,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csv import CSV

        d = src_dict.copy()
        csv = CSV.from_dict(d.pop("CSV"))

        export_format_type_0 = cls(
            csv=csv,
        )

        export_format_type_0.additional_properties = d
        return export_format_type_0

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

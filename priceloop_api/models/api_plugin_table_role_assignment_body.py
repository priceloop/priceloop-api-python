from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiPluginTableRoleAssignmentBody")


@attr.s(auto_attribs=True)
class ApiPluginTableRoleAssignmentBody:
    """
    Attributes:
        table_name (str):  Example: table-name.
    """

    table_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        api_plugin_table_role_assignment_body = cls(
            table_name=table_name,
        )

        api_plugin_table_role_assignment_body.additional_properties = d
        return api_plugin_table_role_assignment_body

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

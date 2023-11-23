from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@attr.s(auto_attribs=True)
class Schedule:
    """
    Attributes:
        cron_expression (str):  Example: 0 8 * * *.
        name (str):  Example: trigger-name.
        table_name (str):  Example: table-name.
        condition (Union[Unset, None, str]):  Example: {ColumnA} == "foo".
    """

    cron_expression: str
    name: str
    table_name: str
    condition: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cron_expression = self.cron_expression
        name = self.name
        table_name = self.table_name
        condition = self.condition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cronExpression": cron_expression,
                "name": name,
                "tableName": table_name,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cron_expression = d.pop("cronExpression")

        name = d.pop("name")

        table_name = d.pop("tableName")

        condition = d.pop("condition", UNSET)

        schedule = cls(
            cron_expression=cron_expression,
            name=name,
            table_name=table_name,
            condition=condition,
        )

        schedule.additional_properties = d
        return schedule

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

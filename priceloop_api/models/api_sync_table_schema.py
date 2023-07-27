from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSyncTableSchema")


@attr.s(auto_attribs=True)
class ApiSyncTableSchema:
    """
    Attributes:
        new_table_name (str):  Example: table-name.
        origin_table_name (str):  Example: table-name.
        sync_column_names (Union[Unset, List[str]]):
    """

    new_table_name: str
    origin_table_name: str
    sync_column_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_table_name = self.new_table_name
        origin_table_name = self.origin_table_name
        sync_column_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sync_column_names, Unset):
            sync_column_names = self.sync_column_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newTableName": new_table_name,
                "originTableName": origin_table_name,
            }
        )
        if sync_column_names is not UNSET:
            field_dict["syncColumnNames"] = sync_column_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_table_name = d.pop("newTableName")

        origin_table_name = d.pop("originTableName")

        sync_column_names = cast(List[str], d.pop("syncColumnNames", UNSET))

        api_sync_table_schema = cls(
            new_table_name=new_table_name,
            origin_table_name=origin_table_name,
            sync_column_names=sync_column_names,
        )

        api_sync_table_schema.additional_properties = d
        return api_sync_table_schema

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

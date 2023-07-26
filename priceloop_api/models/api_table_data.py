from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_int import MapInt
    from ..models.table_row import TableRow


T = TypeVar("T", bound="ApiTableData")


@attr.s(auto_attribs=True)
class ApiTableData:
    """
    Attributes:
        scheduled_jobs (int):
        scheduled_jobs_per_function (MapInt):
        rows (Union[Unset, List['TableRow']]):
    """

    scheduled_jobs: int
    scheduled_jobs_per_function: "MapInt"
    rows: Union[Unset, List["TableRow"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_jobs = self.scheduled_jobs
        scheduled_jobs_per_function = self.scheduled_jobs_per_function.to_dict()

        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()

                rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledJobs": scheduled_jobs,
                "scheduledJobsPerFunction": scheduled_jobs_per_function,
            }
        )
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_int import MapInt
        from ..models.table_row import TableRow

        d = src_dict.copy()
        scheduled_jobs = d.pop("scheduledJobs")

        scheduled_jobs_per_function = MapInt.from_dict(d.pop("scheduledJobsPerFunction"))

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = TableRow.from_dict(rows_item_data)

            rows.append(rows_item)

        api_table_data = cls(
            scheduled_jobs=scheduled_jobs,
            scheduled_jobs_per_function=scheduled_jobs_per_function,
            rows=rows,
        )

        api_table_data.additional_properties = d
        return api_table_data

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

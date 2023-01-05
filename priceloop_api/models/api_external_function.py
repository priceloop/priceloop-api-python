from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiExternalFunction")


@attr.s(auto_attribs=True)
class ApiExternalFunction:
    """
    Attributes:
        function_name (str):
        return_type (str):
        parameter_types (Union[Unset, List[str]]):
    """

    function_name: str
    return_type: str
    parameter_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_name = self.function_name
        return_type = self.return_type
        parameter_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameter_types, Unset):
            parameter_types = self.parameter_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "functionName": function_name,
                "returnType": return_type,
            }
        )
        if parameter_types is not UNSET:
            field_dict["parameterTypes"] = parameter_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        function_name = d.pop("functionName")

        return_type = d.pop("returnType")

        parameter_types = cast(List[str], d.pop("parameterTypes", UNSET))

        api_external_function = cls(
            function_name=function_name,
            return_type=return_type,
            parameter_types=parameter_types,
        )

        api_external_function.additional_properties = d
        return api_external_function

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

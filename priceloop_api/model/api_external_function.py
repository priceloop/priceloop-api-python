# coding: utf-8

"""
    Priceloop API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from priceloop_api import schemas  # noqa: F401


class ApiExternalFunction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "parameterTypes",
            "functionName",
            "returnType",
        }
        
        class properties:
            functionName = schemas.StrSchema
            parameterTypes = schemas.StrSchema
            returnType = schemas.StrSchema
            __annotations__ = {
                "functionName": functionName,
                "parameterTypes": parameterTypes,
                "returnType": returnType,
            }
    
    parameterTypes: MetaOapg.properties.parameterTypes
    functionName: MetaOapg.properties.functionName
    returnType: MetaOapg.properties.returnType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionName"]) -> MetaOapg.properties.functionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameterTypes"]) -> MetaOapg.properties.parameterTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnType"]) -> MetaOapg.properties.returnType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["functionName", "parameterTypes", "returnType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionName"]) -> MetaOapg.properties.functionName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameterTypes"]) -> MetaOapg.properties.parameterTypes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnType"]) -> MetaOapg.properties.returnType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["functionName", "parameterTypes", "returnType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parameterTypes: typing.Union[MetaOapg.properties.parameterTypes, str, ],
        functionName: typing.Union[MetaOapg.properties.functionName, str, ],
        returnType: typing.Union[MetaOapg.properties.returnType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiExternalFunction':
        return super().__new__(
            cls,
            *args,
            parameterTypes=parameterTypes,
            functionName=functionName,
            returnType=returnType,
            _configuration=_configuration,
            **kwargs,
        )

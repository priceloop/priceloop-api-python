from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.color_1 import Color1
    from ..models.color_2 import Color2
    from ..models.color_3 import Color3
    from ..models.color_4 import Color4
    from ..models.color_5 import Color5
    from ..models.color_6 import Color6
    from ..models.color_7 import Color7
    from ..models.color_8 import Color8
    from ..models.color_9 import Color9
    from ..models.color_10 import Color10
    from ..models.color_11 import Color11
    from ..models.color_12 import Color12
    from ..models.color_13 import Color13
    from ..models.color_14 import Color14
    from ..models.color_15 import Color15
    from ..models.color_16 import Color16
    from ..models.color_17 import Color17
    from ..models.color_18 import Color18


T = TypeVar("T", bound="ChoiceDefinition")


@attr.s(auto_attribs=True)
class ChoiceDefinition:
    """
    Attributes:
        color (Union['Color1', 'Color10', 'Color11', 'Color12', 'Color13', 'Color14', 'Color15', 'Color16', 'Color17',
            'Color18', 'Color2', 'Color3', 'Color4', 'Color5', 'Color6', 'Color7', 'Color8', 'Color9']):
        value (str):
    """

    color: Union[
        "Color1",
        "Color10",
        "Color11",
        "Color12",
        "Color13",
        "Color14",
        "Color15",
        "Color16",
        "Color17",
        "Color18",
        "Color2",
        "Color3",
        "Color4",
        "Color5",
        "Color6",
        "Color7",
        "Color8",
        "Color9",
    ]
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.color_1 import Color1
        from ..models.color_2 import Color2
        from ..models.color_3 import Color3
        from ..models.color_4 import Color4
        from ..models.color_5 import Color5
        from ..models.color_6 import Color6
        from ..models.color_7 import Color7
        from ..models.color_8 import Color8
        from ..models.color_10 import Color10
        from ..models.color_11 import Color11
        from ..models.color_12 import Color12
        from ..models.color_13 import Color13
        from ..models.color_14 import Color14
        from ..models.color_15 import Color15
        from ..models.color_16 import Color16
        from ..models.color_17 import Color17
        from ..models.color_18 import Color18

        color: Dict[str, Any]

        if isinstance(self.color, Color1):
            color = self.color.to_dict()

        elif isinstance(self.color, Color10):
            color = self.color.to_dict()

        elif isinstance(self.color, Color11):
            color = self.color.to_dict()

        elif isinstance(self.color, Color12):
            color = self.color.to_dict()

        elif isinstance(self.color, Color13):
            color = self.color.to_dict()

        elif isinstance(self.color, Color14):
            color = self.color.to_dict()

        elif isinstance(self.color, Color15):
            color = self.color.to_dict()

        elif isinstance(self.color, Color16):
            color = self.color.to_dict()

        elif isinstance(self.color, Color17):
            color = self.color.to_dict()

        elif isinstance(self.color, Color18):
            color = self.color.to_dict()

        elif isinstance(self.color, Color2):
            color = self.color.to_dict()

        elif isinstance(self.color, Color3):
            color = self.color.to_dict()

        elif isinstance(self.color, Color4):
            color = self.color.to_dict()

        elif isinstance(self.color, Color5):
            color = self.color.to_dict()

        elif isinstance(self.color, Color6):
            color = self.color.to_dict()

        elif isinstance(self.color, Color7):
            color = self.color.to_dict()

        elif isinstance(self.color, Color8):
            color = self.color.to_dict()

        else:
            color = self.color.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.color_1 import Color1
        from ..models.color_2 import Color2
        from ..models.color_3 import Color3
        from ..models.color_4 import Color4
        from ..models.color_5 import Color5
        from ..models.color_6 import Color6
        from ..models.color_7 import Color7
        from ..models.color_8 import Color8
        from ..models.color_9 import Color9
        from ..models.color_10 import Color10
        from ..models.color_11 import Color11
        from ..models.color_12 import Color12
        from ..models.color_13 import Color13
        from ..models.color_14 import Color14
        from ..models.color_15 import Color15
        from ..models.color_16 import Color16
        from ..models.color_17 import Color17
        from ..models.color_18 import Color18

        d = src_dict.copy()

        def _parse_color(
            data: object,
        ) -> Union[
            "Color1",
            "Color10",
            "Color11",
            "Color12",
            "Color13",
            "Color14",
            "Color15",
            "Color16",
            "Color17",
            "Color18",
            "Color2",
            "Color3",
            "Color4",
            "Color5",
            "Color6",
            "Color7",
            "Color8",
            "Color9",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_0 = Color1.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_1 = Color10.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_2 = Color11.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_3 = Color12.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_4 = Color13.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_5 = Color14.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_6 = Color15.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_7 = Color16.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_8 = Color17.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_9 = Color18.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_10 = Color2.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_11 = Color3.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_12 = Color4.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_13 = Color5.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_14 = Color6.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_15 = Color7.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_choice_definition_badge_color_type_16 = Color8.from_dict(data)

                return componentsschemas_choice_definition_badge_color_type_16
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_choice_definition_badge_color_type_17 = Color9.from_dict(data)

            return componentsschemas_choice_definition_badge_color_type_17

        color = _parse_color(d.pop("color"))

        value = d.pop("value")

        choice_definition = cls(
            color=color,
            value=value,
        )

        choice_definition.additional_properties = d
        return choice_definition

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

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


def check_range(attrs: dict, from_name_value: str, to_name_value: str):
    """Проверка корреткности диапазна."""
    from_value = attrs.get(from_name_value)
    to_value = attrs.get(to_name_value)

    if from_value and to_value:
        if from_value > to_value:
            raise ValidationError(
                {
                    from_name_value:
                        [_('Значение от должны быть меньше, чем значение до')],
                },
            )
        # Показатели между собой могут различаться не более чем на 20 %
        if (from_value / to_value) < 0.75:
            raise ValidationError(
                {
                    from_name_value:
                        [
                            _(
                                'Граничный значения не должны различаться' +
                                ' друг от друга более, чем на 25%',
                            ),
                        ],
                },
            )

    if from_value and not to_value:
        attrs.update({to_name_value: attrs.get(from_name_value)})

    if to_value and not from_value:
        attrs.update({from_name_value: attrs.get(to_name_value)})

    return attrs

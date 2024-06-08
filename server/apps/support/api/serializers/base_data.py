from rest_framework import serializers

from server.apps.support.models import (
    Problem,
    ProblemSubcategory,
    ProblemTheme,
)


class BaseProblemSerializer(serializers.ModelSerializer):
    """Сериалайзер проблемы."""

    class Meta:
        model = Problem
        fields = (
            'id',
            'external_id',
            'name',
            'additional_info',
            'url',
        )


class BaseProblemThemeSerializer(serializers.ModelSerializer):
    """Сериалайзер подкатегории проблем."""

    problems = BaseProblemSerializer(many=True)

    class Meta:
        model = ProblemTheme
        fields = (
            'id',
            'problems',
            'external_id',
            'name',
        )


class BaseProblemSubcategorySerializer(serializers.ModelSerializer):
    """Сериалайзер подкатегории проблем."""

    problem_themes = BaseProblemThemeSerializer(many=True)

    class Meta:
        model = ProblemSubcategory
        fields = (
            'id',
            'problem_themes',
            'problem_category',
            'external_id',
            'name',
        )

from rest_framework import serializers


class EmptySerializer(serializers.Serializer):
    """Empty response body."""


class ErrorSerializer(serializers.Serializer):
    """Display errors to API users."""

    detail = serializers.CharField()

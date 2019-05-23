from rest_framework import serializers


class ReadOnlySerializer(serializers.Serializer):
    """Cannot be used to create or update instances."""

    def create(self, validated_data):
        """Invalid operation.

        Raises
        ------
        TypeError
            If the caller insists on creating an instance, raise a TypeError.

        """
        raise TypeError("ReadOnlySerializers cannot be used to create or update records.")

    def update(self, instance, validated_data):
        """Invalid operation.

        Raises
        ------
        TypeError
            If the caller insists on updating the instance, raise a TypeError.

        """
        raise TypeError("ReadOnlySerializers cannot be used to create or update records.")


class EmptySerializer(ReadOnlySerializer):
    """Empty response body."""


class ErrorSerializer(ReadOnlySerializer):
    """Display errors to API users."""

    detail = serializers.CharField()

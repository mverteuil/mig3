from unittest import mock

import pytest

from api import serializers


def test_read_only_serializer_create():
    """Should raise TypeError if create is attempted."""
    instance = mock.Mock(name="instance")
    with pytest.raises(TypeError):
        serializers.ReadOnlySerializer(instance).create({})


def test_read_only_serializer_update():
    """Should raise TypeError if update is attempted."""
    instance = mock.Mock(name="instance")
    with pytest.raises(TypeError):
        serializers.ReadOnlySerializer(instance).update(instance, {})

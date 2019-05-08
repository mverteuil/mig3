from unittest import mock

from ..api import serializers


def test_current_builder_account():
    """Should return request authenticated BuilderAccount."""
    expected_value = mock.Mock(name="BuilderAccount")
    request = mock.Mock(name="request", auth=expected_value)
    field = mock.Mock(name="serializer_field", context={"request": request})
    value_builder = serializers.CurrentBuilderAccount()
    value_builder.set_context(field)
    assert value_builder() == expected_value

from unittest import mock

from django.core.signing import BadSignature, SignatureExpired, TimestampSigner

from accounts.utils import URLSignature


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_signing_salt(patched_signer, settings):
    """Should apply salt from settings when signing values."""
    settings.SECRET_URL_SALT = "TEST"
    URLSignature.generate_signature()

    assert patched_signer.call_count == 1, patched_signer.call_args_list
    patched_signer.assert_called_once_with(salt=settings.SECRET_URL_SALT)


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_signed_value(patched_signer):
    """Should sign argument value."""
    URLSignature.generate_signature("EXPECTED")
    patched_signer().sign.assert_called_once_with("EXPECTED")


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_signed_result(patched_signer):
    """Should return signed value."""
    result = URLSignature.generate_signature()
    assert result is patched_signer().sign.return_value


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_validating_salt(patched_signer, settings):
    """Should apply salt from settings when validating values."""
    settings.SECRET_URL_SALT = "TEST"
    URLSignature.validate_signature(mock.Mock(name="secret"))
    patched_signer.assert_called_once_with(salt=settings.SECRET_URL_SALT)


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_valid_signature_match(patched_signer):
    """Should confirm match of unsigned value and expected value."""
    mock_secret = mock.Mock(name="secret")
    result = URLSignature.validate_signature(mock_secret, value=patched_signer().unsign.return_value)
    patched_signer().unsign.assert_called_once_with(mock_secret, max_age=None)
    assert result is True


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_bad_signature(patched_signer):
    """Should treat signature as invalid with a bad signature."""
    patched_signer().unsign.side_effect = [BadSignature]
    result = URLSignature.validate_signature("EXPECTED")
    patched_signer().unsign.assert_called_once_with("EXPECTED", max_age=None)
    assert result is False


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_max_age_check(patched_signer):
    """Should use max age if caller requests it."""
    mock_max_age = mock.MagicMock(name="max_age", autospec=int)
    URLSignature.validate_signature("EXPECTED", max_age=mock_max_age)
    patched_signer().unsign.assert_called_once_with("EXPECTED", max_age=mock_max_age)


@mock.patch("accounts.utils.signing.TimestampSigner", autospec=TimestampSigner)
def test_max_age_expired(patched_signer):
    """Should treat signature as invalid when expired."""
    mock_max_age = mock.MagicMock(name="max_age", autospec=int)
    patched_signer().unsign.side_effect = [SignatureExpired]
    result = URLSignature.validate_signature("EXPECTED", max_age=mock_max_age)
    patched_signer().unsign.assert_called_once_with("EXPECTED", max_age=mock_max_age)
    assert result is False

import pytest
from webpack_loader.loader import WebpackLoader


@pytest.fixture(autouse=True)
def monkeypatch_webpack(monkeypatch):
    """Replace webpack bundle calls with an empty list."""
    monkeypatch.setattr(WebpackLoader, "get_bundle", lambda loader, bundle_name: [])

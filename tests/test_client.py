"""Basic tests for TruthlockClient initialization."""

from truthlock import TruthlockClient, Algorithm, Verdict


def test_client_init():
    client = TruthlockClient(api_key="test-key", base_url="https://api.example.com")
    assert client._api_key == "test-key"
    assert client._base_url == "https://api.example.com"
    client.close()


def test_client_context_manager():
    with TruthlockClient(api_key="test") as client:
        assert client is not None


def test_enums():
    assert Algorithm.ED25519.value == "Ed25519"
    assert Verdict.VALID.value == "valid"

# Truthlock Python SDK

Official Python SDK for the [Truthlocks](https://truthlocks.com) cryptographic trust infrastructure.

## Installation

```bash
pip install truthlock
```

## Quick Start

```python
from truthlock import TruthlockClient

client = TruthlockClient(api_key="your-api-key")

# Mint an attestation
attestation = client.attestations.mint(
    content_hash="sha256:abc123...",
    metadata={"filename": "report.pdf", "content_type": "application/pdf"},
)

# Verify an attestation
result = client.verify.check(attestation_id=attestation.id)
print(result.verdict)  # "PASS"
```

## Documentation

Full documentation: [docs.truthlocks.com/sdk/python](https://docs.truthlocks.com/sdk/python)

## License

MIT

# Truthlocks Python SDK

Official Python SDK for [Truthlocks](https://truthlocks.com) cryptographic trust infrastructure.

## Install

```bash
pip install truthlock
```

## Quick Start (Free)

```python
from truthlock import TruthlockClient, Algorithm

# Register instantly - no website needed
result = await TruthlockClient.register("dev@example.com")
print(f"API Key: {result.api_key}")

# Protect content
client = TruthlockClient(api_key=result.api_key)
attestation = await client.attestations.mint(
    content_hash="sha256:abc123...",
    algorithm=Algorithm.ED25519,
)
```

## AI Framework Integrations

```bash
pip install truthlocks-openai truthlocks-anthropic truthlocks-langchain
pip install truthlocks-llamaindex truthlocks-crewai truthlocks-bedrock
```

## 10 Algorithms

Ed25519, ES256, ES384, ES512, RS256, RS384, RS512, PS256, PS384, PS512

## Free Tier

100 attestations/month, 1000 verifications. No credit card.

## Docs

- [API Reference](https://docs.truthlocks.com/sdk/python)
- [Quickstart](https://docs.truthlocks.com/quickstart)

## License

Apache 2.0

# LiteLLM

LiteLLM is a lightweight Python library and proxy server that provides a unified API for interacting with multiple Large Language Models (LLMs) like OpenAI, Anthropic, HuggingFace, Mistral, Cohere, and more. It simplifies development by enabling you to switch between different providers using a single codebase.

---

## Features

- ✅ Unified API for multiple LLMs
- ✅ Supports OpenAI, Azure, Anthropic, Mistral, Cohere, HuggingFace, Ollama, and more
- ✅ Easy model switching and fallback
- ✅ Local proxy server with OpenAI-compatible endpoints
- ✅ Cost and latency tracking
- ✅ Prompt templating and model-specific configs
- ✅ LangChain and FastAPI support

---

## Installation

```bash
pip install litellm
```

---

## Basic Usage

```python
from litellm import completion

response = completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response['choices'][0]['message']['content'])
```

---

## Proxy Server Mode

LiteLLM can run as a local proxy server exposing OpenAI-compatible API endpoints.

### Run with default settings:
```bash
litellm --port 4000
```

### Call the proxy:
```bash
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer fake-key" \
  -d '{
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hi"}]
      }'
```

---

## Configuration File (config.yaml)

```yaml
routes:
  - model_name: openai/gpt-3.5-turbo
    litellm_provider: openai
    api_key: OPENAI_API_KEY

  - model_name: anthropic/claude-3-haiku
    litellm_provider: anthropic
    api_key: ANTHROPIC_API_KEY

  - model_name: mistral/mixtral
    litellm_provider: mistral
    api_key: MISTRAL_API_KEY
```

### Run with config
```bash
litellm --config config.yaml --port 4000
```

---

## OpenRouter vs LiteLLM

| Feature              | LiteLLM (Python Library)                             | OpenRouter (Hosted Platform)                     |
|----------------------|------------------------------------------------------|--------------------------------------------------|
| Type                 | Python library + local proxy                         | Hosted API gateway platform                      |
| Unified API          | ✅ Yes                                                | ✅ Yes                                            |
| Access to 50+ models | ✅ Yes (via config and proxy)                         | ✅ Yes (via hosted API)                          |
| Local control        | ✅ Full local control, can self-host                  | ❌ Hosted externally                            |
| OpenAI-compatible    | ✅ Yes                                                | ✅ Yes                                            |
| Proxy functionality  | ✅ Yes (run your own server)                          | ❌ No                                             |
| Runtime routing      | ✅ Yes (custom fallback, routing rules)               | ❌ No                                             |
| Ideal for            | Developers building infrastructure, flexibility     | Quick LLM access without backend setup          |
| Use OpenRouter inside| ✅ Yes (OpenRouter as a provider in LiteLLM)          | ❌ Not applicable                                 |

### Key Difference (Paragraph Format)

**LiteLLM** is primarily a Python library and proxy server that gives developers the flexibility to route, switch, and control different LLMs locally or within their own infrastructure. It allows full customization of how models are called, adds fallback support, cost tracking, and provides OpenAI-compatible endpoints. In contrast, **OpenRouter** is a hosted API platform that simplifies access to over 50 LLMs without requiring any backend setup. While both provide a unified interface to many models, LiteLLM is developer-focused and infrastructure-ready, whereas OpenRouter is ideal for users who want instant API access with minimal configuration. Notably, you can also use OpenRouter as a provider inside LiteLLM, combining ease of access with full control.

---

## Advanced Capabilities

- **Fallback Models**: Define alternative models when the primary fails.
- **Streaming Support**: Real-time token streaming like OpenAI.
- **Cost Tracking**: Tracks price and token usage.
- **Latency Metrics**: Records API latency per request.
- **Prompt Templates**: Adjust prompts for each model.

---

## Integration

- ✅ Compatible with [LangChain](https://github.com/hwchase17/langchain)
- ✅ Plug-and-play with [FastAPI](https://fastapi.tiangolo.com/)
- ✅ Works with [OpenRouter](https://openrouter.ai) and other API providers

---

## Why Use LiteLLM?

- Avoid vendor lock-in
- Simplify code for multiple LLMs
- Centralize model management
- Build resilient systems with fallbacks
- Track and reduce cost in real-time

---

## License

LiteLLM is open-source under the MIT License.

---




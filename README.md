# Vanya

Personal assistant with a webhook-based architecture. Adapters for different input sources (Telegram, email, etc.) feed into a unified agent core.

## Architecture

```
webhooks/
  └── telegram.py    # Telegram adapter
  └── email.py       # (future) Email adapter
agent/
  └── core.py        # Agent logic (LLM, tools, etc.)
main.py              # FastAPI server
```

## Setup

```bash
pip install -r requirements.txt
```

## Running

```bash
export TELEGRAM_BOT_TOKEN="your-token"
python main.py
```

## Setting up Telegram Webhook

After deploying, set your webhook URL:

```bash
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook?url=https://your-domain.com/telegram/webhook"
```

## Adding New Adapters

1. Create a new file in `webhooks/` (e.g., `email.py`)
2. Define a FastAPI router that parses incoming requests
3. Convert to `Message` format and call `agent.process()`
4. Register the router in `main.py`

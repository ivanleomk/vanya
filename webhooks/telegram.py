import os
import httpx
from fastapi import APIRouter, Request

from agent import Agent
from agent.core import Message

router = APIRouter(prefix="/telegram", tags=["telegram"])

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

agent = Agent()


async def send_message(chat_id: int, text: str) -> None:
    """Send a message back to Telegram."""
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{TELEGRAM_API}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )


@router.post("/webhook")
async def telegram_webhook(request: Request):
    """Handle incoming Telegram webhook updates."""
    data = await request.json()

    # Extract message from update
    message_data = data.get("message")
    if not message_data:
        return {"ok": True}

    text = message_data.get("text", "")
    chat_id = message_data["chat"]["id"]
    user_id = str(message_data["from"]["id"])

    # Convert to universal message format
    message = Message(
        content=text,
        sender_id=user_id,
        metadata={"chat_id": chat_id, "raw": message_data}
    )

    # Process through agent
    response = await agent.process(message)

    # Send response back via Telegram
    await send_message(chat_id, response.content)

    return {"ok": True}

from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    """Universal message format across all adapters."""
    content: str
    sender_id: str
    metadata: dict[str, Any] | None = None


@dataclass
class Response:
    """Universal response format."""
    content: str
    metadata: dict[str, Any] | None = None


class Agent:
    """Core agent logic - adapter agnostic."""

    async def process(self, message: Message) -> Response:
        """Process an incoming message and return a response.

        This is where you plug in your LLM, tools, etc.
        """
        # TODO: Add actual agent logic (LLM calls, tool use, etc.)
        return Response(
            content=f"Received: {message.content}",
            metadata={"sender": message.sender_id}
        )

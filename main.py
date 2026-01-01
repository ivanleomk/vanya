import os
from fastapi import FastAPI

from webhooks import telegram_router

app = FastAPI(title="Vanya", description="Personal assistant with webhook adapters")

# Register webhook adapters
app.include_router(telegram_router)


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

from fastapi import FastAPI
from api.v1.endpoints import patents, chatbot, chats, users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(patents.router, prefix="/patents", tags=["patents"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])
app.include_router(chats.router, prefix="/chat", tags=["chat"])

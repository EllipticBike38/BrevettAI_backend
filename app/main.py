from fastapi import FastAPI
from api.v1.endpoints import patents, chatbot, chats, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(patents.router, prefix="/patents", tags=["patents"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])
app.include_router(chats.router, prefix="/chat", tags=["chat"])

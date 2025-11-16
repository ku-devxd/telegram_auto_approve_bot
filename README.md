Telegram Auto-Approve Bot (Aiogram 3)

A lightweight and reliable Telegram bot that automatically approves all join requests in a private channel or group.
Perfect for private communities, paid channels, online courses, or any closed Telegram space.

🚀 Features

Instantly approves all incoming join requests

Works in private channels and groups

Uses official Telegram Bot API (chat_join_request)

Clean and minimal code (Aiogram 3)

Easy to run locally or on any VPS

Secure — requires only one permission

🧩 Tech Stack

Python 3.10+

Aiogram 3.x

Telegram Bot API

📁 Project Structure
telegram-auto-approve-bot/
│
├── bot.py
├── requirements.txt
└── README.md

🧠 How It Works

When a user clicks your invite link and submits a join request,
Telegram sends a chat_join_request update →
the bot automatically calls approve_chat_join_request() →
the user is instantly approved.

🧾 Source Code
bot.py
import os
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_request(update: ChatJoinRequest):
    chat_id = update.chat.id
    user_id = update.from_user.id

    await bot.approve_chat_join_request(chat_id, user_id)
    print(f"[APPROVED] User {user_id} approved in chat {chat_id}")

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

📦 Installation
1. Install dependencies
pip install -r requirements.txt

2. Set your bot token

On macOS/Linux:

export BOT_TOKEN="YOUR_BOT_TOKEN"


On Windows (PowerShell):

setx BOT_TOKEN "YOUR_BOT_TOKEN"

3. Run the bot
python bot.py

🔧 Telegram Setup

Create a bot via @BotFather

Get your bot token

Add the bot to your private channel or group

Promote it to Administrator

Enable permission: Manage Join Requests

Done — the bot will automatically approve all requests

⭐ Highlights

Zero-delay approvals

Extremely lightweight

Perfect for automation & private channels

Beginner-friendly

Production-ready

📌 Possible Future Improvements

Welcome messages

Logging to file or database

Username filtering (whitelist/blacklist)

Admin dashboard

Webhook version

🎉 Done!

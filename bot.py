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

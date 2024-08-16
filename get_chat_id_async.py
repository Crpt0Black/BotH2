import asyncio
from telegram import Bot

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'

async def get_chat_id():
    bot = Bot(token=TOKEN)
    updates = await bot.get_updates()
    
    for update in updates:
        print(update.message.chat_id)

if __name__ == "__main__":
    asyncio.run(get_chat_id())

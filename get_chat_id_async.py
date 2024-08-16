import asyncio
from telegram import Bot

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'

async def get_chat_id():
    bot = Bot(token=TOKEN)
    updates = await bot.get_updates()
    
    if not updates:
        print("Tidak ada pembaruan yang ditemukan. Pastikan bot Anda sudah menerima pesan.")
        return

    for update in updates:
        if update.message:
            print(f"Chat ID: {update.message.chat_id}")
        else:
            print("Tidak ada pesan dalam pembaruan.")

if __name__ == "__main__":
    asyncio.run(get_chat_id())

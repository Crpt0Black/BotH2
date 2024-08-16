from telegram import Bot

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'

bot = Bot(token=TOKEN)
updates = bot.get_updates()

for update in updates:
    print(update.message.chat_id)

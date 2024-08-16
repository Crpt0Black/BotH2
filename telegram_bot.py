import telegram
from telegram.ext import Updater
import schedule
import time

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'
CHAT_ID = '5505900481'

bot = telegram.Bot(token=TOKEN)

def send_message():
    bot.send_message(chat_id=CHAT_ID, text="Waktunya Farming Tuan")

def job():
    schedule.every(2).hours.do(send_message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    job()

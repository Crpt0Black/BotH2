from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import uuid

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'

def start(update, context):
    update.message.reply_text('Bot ini aktif dalam mode inline!')

def inline_query(update, context):
    query = update.inline_query.query

    # Contoh hasil pencarian
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),  # ID unik untuk hasil
            title='Contoh Hasil',
            input_message_content=InputTextMessageContent(f'Anda mencari: {query}')
        )
    ]

    context.bot.answer_inline_query(update.inline_query.id, results)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(InlineQueryHandler(inline_query))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

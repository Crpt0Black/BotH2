from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Application, CommandHandler, InlineQueryHandler, ContextTypes
import uuid

# Ganti dengan token API dari BotFather
TOKEN = '7494808277:AAGfOvFKQM64DAZM9t0PrdeK_yfintW2XdA'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bot ini aktif dalam mode inline!')

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    # Contoh hasil pencarian
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),  # ID unik untuk hasil
            title='Contoh Hasil',
            input_message_content=InputTextMessageContent(f'Anda mencari: {query}')
        )
    ]

    await context.bot.answer_inline_query(update.inline_query.id, results)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(InlineQueryHandler(inline_query))

    application.run_polling()

if __name__ == '__main__':
    main()


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7657918931:AAEKtaMZwlZtPAR95FnrLfWL6Zkm8ODpiiA'
BOT_USERNAME = '@fedi4Bot'

id_counter = 0
user_ids = {}
history = []

def handle_response(text: str) -> str:
    text = text.lower()

    if "hi" in text:
        return "Hey there!"

    elif "how are you" in text:
        return "I am good."

    else:
        return "I do not understand what you wrote."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id})in {message_type}: "{text}"')

    response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    bot = Application.builder().token(TOKEN).build()


    from CrocoBot3.handler.start import start
    from CrocoBot3.handler.info import info
    from CrocoBot3.handler.tools import get_sticker_file_id, clear_history

    # Register command handlers
    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('info', info))
    bot.add_handler(CommandHandler('clear_history', clear_history))


    # Register message handler
    bot.add_handler(MessageHandler(filters.TEXT, handle_message))

    #other
    bot.add_handler(MessageHandler(filters.ALL, get_sticker_file_id))

    # Register error handler
    #bot.add_error_handler(error)

    print('Starting polling...')
    # Run the bot
    bot.run_polling(poll_interval=2)
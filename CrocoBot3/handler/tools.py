from telegram import Update
from telegram.ext import ContextTypes

from CrocoBot3 import history, user_ids

from CrocoBot3.handler.start import start

async def get_sticker_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('STICKER-FILE_ID: ' + update.message.sticker.file_id)

async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # history
    global id_counter
    user = update.message.from_user

    if user not in user_ids:
        await start(update, context)
    user_id = user_ids[user]

    history[user_id].append('info')
    # history


    history[user_id].clear()
    await update.message.reply_text('your history is empty!')
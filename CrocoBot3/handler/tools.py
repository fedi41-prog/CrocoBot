from telegram import Update
from telegram.ext import ContextTypes

from CrocoBot3 import history

async def get_sticker_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('STICKER-FILE_ID: ' + update.message.sticker.file_id)

async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    history[user].clear()
    await update.message.reply_text('your history is empty!')
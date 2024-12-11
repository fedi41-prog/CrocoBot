from telegram import Update
from telegram.ext import ContextTypes

from CrocoBot3 import history, user_ids, id_counter
from CrocoBot3.handler.start import start


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    #history
    global id_counter
    user = update.message.from_user

    if user not in user_ids:
        await start(update, context)

    user_id = user_ids[user]
    history[user_id].append('info')
    #history


    await update.message.reply_text('Bot username  -  @fedi4Bot')
    await update.message.reply_text('This bot is created by @Fedi4Karev. Just for FUN.')
    #contacts = ['LeetCode  -  https://leetcode.com/u/fedi41-prog/', 'Github  -  https://github.com/fedi41-prog']
    #for i in contacts:
    #    await update.message.reply_text(i)